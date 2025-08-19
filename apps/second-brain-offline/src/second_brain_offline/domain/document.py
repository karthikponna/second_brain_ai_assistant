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
    
