from pydantic import BaseModel
from typing import List, Optional


class ImageInput(BaseModel):
    filename: str
    caption: Optional[str] = None


class DocumentInput(BaseModel):
    filename: str
    extracted_text: Optional[str] = None


class RefineRequest(BaseModel):
    text: Optional[str] = None
    images: Optional[List[ImageInput]] = []
    documents: Optional[List[DocumentInput]] = []


class Intent(BaseModel):
    summary: str
    domain: str
    target_users: str


class Meta(BaseModel):
    source_types: List[str]
    confidence_score: float
    missing_fields: List[str]
    rejected: bool = False
    rejection_reason: Optional[str] = None


class RefinedPrompt(BaseModel):
    meta: Meta
    intent: Intent
    functional_requirements: List[str]
    technical_constraints: List[str]
    non_functional_requirements: List[str]
    expected_outputs: List[str]
    assumptions: List[str]
    open_questions: List[str]
