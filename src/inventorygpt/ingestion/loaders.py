"""Loader boilerplate for file discovery and document loading."""


class FileDiscovery:
    """Discovers supported source files."""

    # Responsibility:
    # - Find candidate files.
    # - Avoid knowing how files are parsed.

    def __init__(self) -> None:
        """Initialize file discovery."""
        pass

    def discover(self, source_path, glob_patterns, include_hidden=False):
        """Return source file paths that should be ingested."""
        pass


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
    """Loads raw documents from a file or directory."""

    # Responsibility:
    # - Coordinate discovery and loading.
    # - Avoid knowing how documents are chunked or persisted.

    def __init__(self, config, discovery=None, loader_factory=None) -> None:
        """Initialize a directory document source."""
        pass

    def load(self):
        """Load documents from the configured source."""
        pass
