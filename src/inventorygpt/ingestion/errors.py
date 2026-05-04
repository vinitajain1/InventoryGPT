"""Exception boilerplate for ingestion failures."""


class IngestionError(Exception):
    """Base placeholder exception for ingestion errors."""
    pass


class SourceNotFoundError(IngestionError):
    """Placeholder exception for missing source paths."""
    pass


class UnsupportedDocumentTypeError(IngestionError):
    """Placeholder exception for unsupported document types."""
    pass


class DocumentLoadError(IngestionError):
    """Placeholder exception for document loading failures."""
    pass


class VectorStoreDependencyError(IngestionError):
    """Placeholder exception for vector-store dependency failures."""
    pass
