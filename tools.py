
def validate_plan(user_plan):
    """Check whether the user has entered a plan."""

    if not user_plan:
        return False

    return True


def format_report(ai_response):
    """Format the AI response as a readable report."""

    report = """
===================================
       PLAN GUARD AI REPORT
===================================

"""

    report += ai_response

    report += "\n\n==================================="

    return report
