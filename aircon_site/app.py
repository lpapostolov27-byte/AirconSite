from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = "aircon-secret-2024"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name    = request.form.get("name")
        phone   = request.form.get("phone")
        email   = request.form.get("email")
        message = request.form.get("message")
        # TODO: Add email sending logic here
        flash("Благодарим! Ще се свържем с вас скоро.", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html")

if __name__ == "__main__":
    print("\n✅ AirCon Site started!")
    print("   http://localhost:5000\n")
    app.run(debug=False)
