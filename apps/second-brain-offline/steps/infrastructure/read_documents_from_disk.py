from pathlib import Path

from loguru import logger
from typing_extensions import Annotated
from zenml.steps import get_step_context, step

from src.second_brain_offline.domain.document import Document

