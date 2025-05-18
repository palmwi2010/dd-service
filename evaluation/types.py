from pydantic import BaseModel, Field

class DDEvaluation(BaseModel):
    """Pydantic model for DD report evaluation scores and comments."""
    factual_accuracy: int = Field(
        ..., 
        description="Does the report state verifiable facts correctly and cite sources or evidence? (integer score 1-100)"
    )
    narrative_coherence: int = Field(
        ..., 
        description="Is the storyline logical, well-structured, and easy to follow? (integer score 1-100)"
    )
    analytical_depth: int = Field(
        ..., 
        description="Are arguments supported by sound logic, segmentation, or framework-based thinking? (integer score 1-100)"
    )
    numerical_reasoning: int = Field(
        ..., 
        description="Are market-sizing, growth rates, and finance calculations internally consistent and plausible? (integer score 1-100)"
    )
    overall_quality: int = Field(
        ..., 
        description="Holistic impression relative to Tier-1 consultancy standards (integer score 1-100)"
    )
    comments: str = Field(
        ..., 
        description="Concise comments on the report justifying the scores given."
    ) 