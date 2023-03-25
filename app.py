import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        url = request.form["url"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(url),
            temperature=0.9,
            max_tokens=2500
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result", "")

    return render_template("index.html", result=result.split("\n"))


def generate_prompt(url):
    return """Summarize the content of this URL in bullet points, and summarize any numbers: {}""".format(
        url.capitalize()
    )
