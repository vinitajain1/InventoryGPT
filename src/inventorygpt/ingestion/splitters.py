"""Transformer boilerplate for preparing documents for retrieval."""


class NoOpDocumentTransformer:
    """Passes documents through unchanged."""

    def transform(self, documents):
        """Return documents without transformation."""
        pass


class RecursiveTextChunker:
    """Splits documents into retrieval-sized chunks."""

    # Responsibility:
    # - Chunk document text.
    # - Avoid knowing where documents are loaded from or persisted.

    def __init__(self, config=None) -> None:
        """Initialize the chunker."""
        pass

    def transform(self, documents):
        """Transform documents into chunks."""
        pass
