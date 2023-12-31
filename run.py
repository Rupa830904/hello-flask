import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/teachers.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", teachers=data)

@app.route("/about/<teacher_name>")
def about_teacher(teacher_name):
    teacher = {}
    with open("data/teachers.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == teacher_name:
                teacher = obj
    return render_template("teacher.html", teacher=teacher)
    #return "<h1>" + member["name"] + "</h1>"


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
        flash("We will contact you at".format(request.form.get("email")))
    return render_template("contact.html", page_title="Contact" )

@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Contact")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)