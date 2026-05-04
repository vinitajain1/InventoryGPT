"""Configuration boilerplate for ingestion components."""


class FileIngestionConfig:
    """Configuration placeholder for file-based document ingestion."""

    # Expected fields:
    # - source_path
    # - glob_patterns
    # - supported_extensions
    # - encoding

    def __init__(self) -> None:
        """Initialize file ingestion configuration."""
        pass


class ChunkingConfig:
    """Configuration placeholder for document chunking."""

    # Expected fields:
    # - chunk_size
    # - chunk_overlap
    # - separators

    def __init__(self) -> None:
        """Initialize chunking configuration."""
        pass
