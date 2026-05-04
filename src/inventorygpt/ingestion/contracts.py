"""Protocol contracts for dependency-inverted ingestion components."""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path
from typing import Protocol

from langchain_core.documents import Document


class DocumentLoader(Protocol):
    """Loads LangChain documents from one concrete source."""

    def load(self) -> list[Document]:
        """Return documents extracted from the source."""


class DocumentLoaderFactory(Protocol):
    """Creates a loader for a source file."""

    def create(self, path: Path) -> DocumentLoader:
        """Return a loader capable of reading the path."""


class DocumentSource(Protocol):
    """Reads documents from an external source."""

    def load(self) -> list[Document]:
        """Return source documents ready for transformation."""


class DocumentTransformer(Protocol):
    """Transforms documents without knowing where they came from or will go."""

    def transform(self, documents: Sequence[Document]) -> list[Document]:
        """Return transformed documents."""


class DocumentSink(Protocol):
    """Persists transformed documents into a downstream store."""

    def persist(self, documents: Sequence[Document]) -> None:
        """Persist documents into the target storage backend."""