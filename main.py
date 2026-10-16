

from model import analyze_plan
from tools import format_report, validate_plan


def main():
    print("===================================")
    print("       PLAN GUARD AI")
    print(" Intelligent Plan Analysis System")
    print("===================================")

    user_plan = input("\nDescribe your plan: ").strip()

    if not validate_plan(user_plan):
        print("Error: Please enter a plan.")
        return

    print("\nAnalyzing your plan... Please wait.\n")

    ai_response = analyze_plan(user_plan)
    report = format_report(ai_response)

    print(report)


if __name__ == "__main__":
    main()
