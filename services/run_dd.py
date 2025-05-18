from langchain_openai import ChatOpenAI

def run_dd(company_name: str) -> str:
    """Run DD on a company and return response in markdown format."""
    llm = ChatOpenAI(
        model="gpt-4o-mini",
    )

    prompt = f"""Provide a brief initial due diligence analysis for {company_name}. Include:
    1. Company Overview
    2. Main Products/Services
    3. Key Market Position
    4. Major Competitors
    5. Potential Risk Factors
    
    Format the response in a clear, structured way. Return the response in markdown format."""
    
    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        return f"Error getting company information: {str(e)}"