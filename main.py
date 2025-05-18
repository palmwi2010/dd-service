from dotenv import load_dotenv
from services.run_dd import run_dd
from services.report_manager import save_dd_report
import sys

def main():
    # Load environment variables
    load_dotenv()
    
    # Get company name from user
    print("\n=== Commercial Due Diligence Initial Analysis ===")
    company_name = input("\nEnter the name of the company to analyze: ").strip()
    
    if not company_name:
        print("Error: Company name cannot be empty.")
        sys.exit(1)
    
    print(f"\nAnalyzing {company_name}...")
    print("\n" + "="*50 + "\n")
    
    # Get and display company information
    analysis = run_dd(company_name)
    print(analysis)
    print("\n" + "="*50)
    
    # Save the report
    file_path = save_dd_report(company_name, analysis)
    print(f"\nReport saved to: {file_path}")

if __name__ == "__main__":
    main()

