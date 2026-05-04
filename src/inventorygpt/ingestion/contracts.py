"""Interface boilerplate for ingestion components."""


class DocumentLoader:
    """Interface placeholder for loading documents from one source."""

    def load(self):
        """Load documents from the source."""
        pass


class DocumentLoaderFactory:
    """Interface placeholder for creating document loaders."""

    def create(self, path):
        """Create a loader for the supplied path."""
        pass


class DocumentSource:
    """Interface placeholder for a source of raw documents."""

    def load(self):
        """Load documents from the source."""
        pass


class DocumentTransformer:
    """Interface placeholder for transforming documents."""

    def transform(self, documents):
        """Transform documents for downstream retrieval."""
        pass


class DocumentSink:
    """Interface placeholder for persisting transformed documents."""

    def persist(self, documents):
        """Persist documents into a target store."""
        pass
