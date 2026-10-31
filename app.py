from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "rrce-ieee-demo-key"

events = [
    {"date": "NOV 12, 2026", "title": "AI & Innovation Summit", "type": "Conference",
     "description": "Explore practical applications of artificial intelligence, machine learning and emerging technologies."},
    {"date": "NOV 20, 2026", "title": "CodeSprint 2026", "type": "Hackathon",
     "description": "A collaborative coding challenge for students who enjoy solving real-world problems."},
    {"date": "DEC 05, 2026", "title": "Future Tech Talks", "type": "Workshop",
     "description": "Learn from technical speakers and discover new directions in engineering and computing."}
]

@app.route("/")
def home():
    return render_template("index.html", events=events)

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    interest = request.form.get("interest", "").strip()
    if not name or not email:
        flash("Please enter your name and email address.", "error")
    else:
        # Demo only: registrations are not stored or emailed.
        flash(f"Thank you, {name}! Your demo registration has been received.", "success")
    return redirect(url_for("home") + "#join")

if __name__ == "__main__":
    app.run(debug=True)
