from loguru import logger
from typing_extensions import Annotated
from zenml import get_step_context, step

from src.second_brain_offline.application.agents.quality import (
    HeuristicQualityAgent,
    QualityScoreAgent,
)
from src.second_brain_offline.domain import Document


@step
def add_quality_score(
    documents: list[Document],
    model_id: str = "gpt-4o-mini",
    mock: bool = False,
    max_workers: int = 10,
) -> Annotated[list[Document], "scored_documents"]:
    """Adds quality scores to documents using heuristic and model-based scoring agents.

    This function processes documents in two stages:
    1. Applies heuristic-based quality scoring
    2. Uses a model-based quality agent for documents that weren't scored by heuristics

    Args:
        documents: List of documents to evaluate for quality
        model_id: Identifier for the model to use in quality assessment.
            Defaults to "gpt-4o-mini"
        mock: If True, uses mock responses instead of real model calls.
            Defaults to False
        max_workers: Maximum number of concurrent quality check operations.
            Defaults to 10

    Returns:
        list[Document]: Documents enhanced with quality scores, annotated as
            "scored_documents" for pipeline metadata tracking

    Note:
        The function adds metadata to the step context including the total number
        of documents and how many received quality scores.
    """