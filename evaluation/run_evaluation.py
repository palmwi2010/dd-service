from typing import Optional, List
from statistics import median
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from .types import DDEvaluation
from .prompts import SYSTEM_PROMPT, RUBRIC_PROMPT, EVALUATION_TEMPLATE

def create_evaluation_chain():
    """Create a LangChain chain for evaluating DD reports."""
    # Create the chat prompt template
    prompt = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(SYSTEM_PROMPT),
        SystemMessagePromptTemplate.from_template(RUBRIC_PROMPT),
        HumanMessagePromptTemplate.from_template(EVALUATION_TEMPLATE)
    ])
    
    # Create the LLM with structured output
    llm = ChatOpenAI(
        model="gpt-4.1",
        temperature=0.2  # Low temperature for more consistent scoring
    ).with_structured_output(DDEvaluation)
    
    return prompt | llm

def evaluate_report(report: str, ensemble_count: int = 1) -> DDEvaluation:
    """
    Evaluate a DD report using the LLM judge.
    
    Args:
        report: The DD report content to evaluate
        ensemble_count: Number of parallel evaluations to run (default=1)
        
    Returns:
        DDEvaluation: The evaluation results
    """
    chain = create_evaluation_chain()
    
    # Run evaluations in parallel using Langchain's batch operation
    inputs = [{"report": report} for _ in range(ensemble_count)]
    results = chain.batch(inputs)
    
    # Take median scores for each dimension
    return DDEvaluation(
        factual_accuracy=int(median(r.factual_accuracy for r in results)),
        narrative_coherence=int(median(r.narrative_coherence for r in results)),
        analytical_depth=int(median(r.analytical_depth for r in results)),
        numerical_reasoning=int(median(r.numerical_reasoning for r in results)),
        overall_quality=int(median(r.overall_quality for r in results)),
        # Use the comments from the first result
        comments=results[0].comments
    )

def print_evaluation(result: DDEvaluation) -> None:
    """Pretty print the evaluation results."""
    print("\n=== DD Report Evaluation ===\n")
    
    # Print scores
    print("Scores (out of 10):")
    print(f"  Factual Accuracy:      {result.factual_accuracy}")
    print(f"  Narrative Coherence:   {result.narrative_coherence}")
    print(f"  Analytical Depth:      {result.analytical_depth}")
    print(f"  Numerical Reasoning:   {result.numerical_reasoning}")
    print(f"  Overall Quality:       {result.overall_quality}")
    
    # Print comments
    print("\nDetailed Comments:")
    print(result.comments)
    print("\n" + "="*25) 