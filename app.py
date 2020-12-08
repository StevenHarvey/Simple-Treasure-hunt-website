from flask import Flask, redirect, url_for, render_template
from flask_restful import Api
from resources.todo import Todo
import requests
app = Flask(__name__)
api = Api(app)


def apikey():
    headers = {
        'accept': '*/*',
        'X-Api-Key': 'b4b234dff51b43b498d693f30ea5f54b',
    }


    params = (
        ('length', '16'),
        ('hasDigits', 'true'),
        ('hasUppercase', 'false'),
        ('hasSpecial', 'false'),
    )

    response = requests.get(
        'https://randommer.io/api/Text/Password', headers=headers, params=params)
    global finalkey
    finalkey = (response.json())


api.add_resource(Todo, "/api/<int:id>")
@app.route("/")
def home():
    return render_template("htmlss.html", content="Testing", x=4)
@app.route("/api/")
def hiddenss():
    return render_template("apihome.html", content="testing", x=4)

@app.route("/backend")
def backend():
    return render_template("htmlss2.html", content="Testing", x=4)


@app.route("/api/5a61f8e3e63b7e93777f.js")
def hidden():
    apikey()
    return render_template("apigrab.html", content="testing", x=4, variable=str(finalkey))
if __name__ == "__main__":
    app.run(debug=True)
