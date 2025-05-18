from dotenv import load_dotenv
from services.run_dd import run_dd
from services.report_manager import save_dd_report
from evaluation import evaluate_report, print_evaluation
import sys
import argparse

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Generate a due diligence report for a company')
    parser.add_argument('company_name', help='Name of the company to analyze')
    parser.add_argument('-e', '--evaluate', action='store_true', 
                       help='Evaluate the generated report using LLM judge')
    parser.add_argument('--ensemble', type=int, default=1,
                       help='Number of parallel evaluations to run (default: 1)')
    args = parser.parse_args()

    # Load environment variables
    load_dotenv()
    
    print(f"\nAnalyzing {args.company_name}...")
    print("\n" + "="*50 + "\n")
    
    # Generate and display DD report
    analysis = run_dd(args.company_name)
    print(analysis)
    print("\n" + "="*50)
    
    # Save the report
    file_path = save_dd_report(args.company_name, analysis)
    print(f"\nReport saved to: {file_path}")

    # Evaluate the report if requested
    if args.evaluate:
        print("\nEvaluating report...")
        evaluation = evaluate_report(analysis, ensemble_count=args.ensemble)
        print_evaluation(evaluation)

if __name__ == "__main__":
    main()

