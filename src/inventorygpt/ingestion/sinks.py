"""Sink boilerplate for persisting transformed documents."""


class InMemoryDocumentSink:
    """Stores documents in memory for tests and dry runs."""

    # Responsibility:
    # - Keep an in-memory copy of documents.
    # - Avoid knowing how documents were loaded or transformed.

    def __init__(self) -> None:
        """Initialize the in-memory sink."""
        pass

    def persist(self, documents):
        """Persist documents in memory."""
        pass


class ChromaVectorStoreSink:
    """Persists documents into a Chroma vector store."""

    # Responsibility:
    # - Store transformed documents in Chroma.
    # - Receive embeddings through dependency injection.

    def __init__(self, persist_directory=None, embedding_function=None) -> None:
        """Initialize the Chroma sink."""
        pass

    def persist(self, documents):
        """Persist documents into Chroma."""
        pass
