from flask import Flask
import data
from flask import render_template

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/education")
def education():
    kwargs = data.education
    return render_template("education.html", kwargs=kwargs)

@app.get("/skills")
def skills():
    skill_list = data.skills
    return render_template("skills.html", kwargs=skill_list)

@app.get("/experience")
def experience():
    exp_list = data.experience
    return render_template("experience.html", kwargs=exp_list)

@app.get("/portfolio")
def portfolio():
    port_list = data.portfolio
    return render_template("portfolio.html", kwargs=port_list)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)