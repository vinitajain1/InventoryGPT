"""File discovery and LangChain loader adapters."""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path

from langchain_core.documents import Document

from inventorygpt.ingestion.config import FileIngestionConfig
from inventorygpt.ingestion.contracts import DocumentLoader, DocumentLoaderFactory
from inventorygpt.ingestion.errors import (
    DocumentLoadError,
    SourceNotFoundError,
    UnsupportedDocumentTypeError,
)

class FileDiscovery:
    """Discovers supported files without knowing how they are loaded."""

    def __init__(self, supported_extensions: Sequence[str]) -> None:
        self._supported_extensions = tuple(extension.lower() for extension in supported_extensions)

    def discover(
        self,
        source_path: Path,
        glob_patterns: Sequence[str]
    ) -> list[Path]:
        source_path = Path(source_path).expanduser()
        if not source_path.exists():
            raise SourceNotFoundError(f"Source path does not exist: {source_path}")

        if source_path.is_file():
            if not self._is_supported(source_path):
                raise UnsupportedDocumentTypeError(f"Unsupported document type: {source_path.suffix}")
            return [source_path]

        discovered: set[Path] = set()
        for pattern in glob_patterns:
            discovered.update(path for path in source_path.glob(pattern) if path.is_file())

        return sorted(
            path
            for path in discovered
            if self._is_supported(path) and (include_hidden or not self._is_hidden(path))
        )

    def _is_supported(self, path: Path) -> bool:
        return path.suffix.lower() in self._supported_extensions

    @staticmethod
    def _is_hidden(path: Path) -> bool:
        return any(part.startswith(".") for part in path.parts)


class LangChainLoaderFactory:
    """Creates concrete loaders for supported document types."""

    # Responsibility:
    # - Select the correct loader for a file type.
    # - Hide LangChain loader details from document sources.

    def __init__(self) -> None:
        """Initialize the loader factory."""
        pass

    def create(self, path):
        """Create a loader for the supplied path."""
        pass


class DirectoryDocumentSource:
    """Loads documents from a file or directory using injected discovery and loader policies."""

    def __init__(
        self,
        config: FileIngestionConfig,
        discovery: FileDiscovery | None = None,
        loader_factory: DocumentLoaderFactory | None = None,
    ) -> None:
        self._config = config
        self._discovery = discovery or FileDiscovery(config.supported_extensions)
        self._loader_factory = loader_factory or LangChainLoaderFactory(
            encoding=config.encoding,
            autodetect_encoding=config.autodetect_encoding,
        )

    def load(self) -> list[Document]:
        documents: list[Document] = []
        paths = self._discovery.discover(
            source_path=self._config.source_path,
            glob_patterns=self._config.glob_patterns
        )

        for path in paths:
            try:
                loaded_documents = self._loader_factory.create(path).load()
            except Exception as exc:
                raise DocumentLoadError(f"Failed to load document: {path}") from exc

            documents.extend(self._with_file_metadata(document, path) for document in loaded_documents)

        return documents

    def _with_file_metadata(document: Document, path: Path) -> Document:
        metadata = dict(document.metadata)
        metadata.setdefault("source", str(path))
        metadata["file_name"] = path.name
        metadata["file_extension"] = path.suffix.lower()
        return Document(page_content=document.page_content, metadata=metadata)
