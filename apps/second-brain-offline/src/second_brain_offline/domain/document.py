import json
from pathlib import Path

from pydantic import BaseModel, Field

from second_brain_offline import utils


class DocumentMetadata(BaseModel):
    id: str
    url: str
    title: str
    properties: dict

    def obfuscate(self) -> "DocumentMetadata":
        """Create an obfuscated version of this metadata by modifying in place.

        Returns:
            DocumentMetadata: Self, with ID and URL obfuscated.
        """

        original_id = self.id.replace("-", "")
        fake_id = utils.generate_random_hex(len(original_id))

        self.id = fake_id
        self.url = self.url.replace(original_id, fake_id)

        return self
    
class Document(BaseModel):
    id: str = Field(default_factory=lambda: utils.generate_random_hex(length=32))
    metadata: DocumentMetadata
    parent_metadata: DocumentMetadata | None = None
    content: str
    content_quality_score: float | None = None
    summary: str | None = None
    child_urls: list[str] = Field(default_factory=list)


    @classmethod
    def from_file(cls, file_path:Path) -> "Document":
        """Read a Document object from a JSON file.

        Args:
            file_path: Path to the JSON file containing document data.

        Returns:
            Document: A new Document instance constructed from the file data.

        Raises:
            FileNotFoundError: If the specified file doesn't exist.
            ValidationError: If the JSON data doesn't match the expected model structure.
        """

        json_data = file_path.read_text(encoding="utf-8")

        return cls.model_validate_json(json_data)