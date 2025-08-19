from pathlib import Path

from loguru import logger
from zenml import Pipeline

from steps.infrastructure import (
    read_documents_from_disk,
)