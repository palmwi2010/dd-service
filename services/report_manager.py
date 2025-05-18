from pathlib import Path
import re

def save_dd_report(company_name: str, content: str) -> str:
    """Save a DD report to a file with automatic naming.
    
    Args:
        company_name (str): Name of the company (will be sanitized for filename)
        content (str): The markdown content to save
        
    Returns:
        str: The path where the file was saved
    """
    # Create reports directory if it doesn't exist
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)
    
    # Sanitize company name for filename
    safe_name = re.sub(r'[^\w\s-]', '', company_name).strip().lower()
    safe_name = re.sub(r'[-\s]+', '-', safe_name)
    
    # Find an available filename
    base_path = reports_dir / f"{safe_name}_dd.md"
    final_path = base_path
    counter = 1
    
    while final_path.exists():
        final_path = reports_dir / f"{safe_name}_dd({counter}).md"
        counter += 1
    
    # Save the report
    with open(final_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return str(final_path) 