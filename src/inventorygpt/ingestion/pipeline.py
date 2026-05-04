from inventorygpt.ingestion.contracts import DocumentSource, DocumentTransformer, DocumentSink
from __future__ import annotations
from dataclasses import dataclass, field
from langchain_core.documents import Document

@dataclass
class IngestionResult:

    loaded_document_count: int
    output_document_count: int
    persisted_document_count: int
    documents: tuple[Document, ...] = field(repr=False)


class DataIngestionPipeline:
    """Coordinates source, transformer, and sink abstractions."""

    # Responsibility:
    # - Orchestrate the ingestion workflow.
    # - Depend on abstractions instead of concrete implementations.

    def __init__(self, source:DocumentSource, 
                 transformers:DocumentTransformer, 
                 sink:DocumentSink) -> None:
        """Initialize the ingestion pipeline."""
        self._source = source
        self._transformers = DocumentTransformer
        self._sink = sink

    def run(self):
        """Run the ingestion pipeline."""
        loaded_documents = self._source.load()
        output_documents = self._transformers.transform(loaded_documents)
        persisted_count = 0
        if self._sink is not None:
            self._sink.persist(output_documents)
            persisted_count = len(output_documents)

        return IngestionResult(
            loaded_document_count=len(loaded_documents),
            output_document_count=len(output_documents),
            persisted_document_count=persisted_count,
            documents=tuple(output_documents),
        )