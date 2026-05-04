"""Configuration objects for ingestion components."""

from dataclasses import dataclass
from pathlib import Path

@dataclass
class FileIngestionConfig:
    """Configuration options to read file"""
    source_path:Path
    glob_patterns:tuple[str,...] = ("**/*.pdf")
    supported_extensions: tuple[str, ...] = (".pdf", ".txt", ".md")
    encoding: str = "utf-8"


@dataclass
class ChunkingConfig:
    """Options for splitting documents into retrievable chunks."""

    chunk_size: int = 1000
    chunk_overlap: int = 150
    separators: tuple[str, ...] = ("\n\n", "\n", " ", "")
