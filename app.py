
from flask import Flask, render_template, request
from model import analyze_plan
from tools import validate_plan, format_report

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    report = ""

    if request.method == "POST":
        plan = request.form.get("plan", "").strip()

        if validate_plan(plan):
            result = analyze_plan(plan)
            report = format_report(result)
        else:
            report = "Please enter a plan."

    return render_template("index.html", report=report)

if __name__ == "__main__":
    app.run(debug=True)
