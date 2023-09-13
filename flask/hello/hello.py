from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return "<p>Hello, World<p>"

@app.route("/<name>")
def hello_name(name):
    return render_template("home.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
