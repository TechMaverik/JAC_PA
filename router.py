from flask import Flask, render_template, url_for

app = Flask("__name__")
app.config["SECRET_KEY"] = "secretkey"


@app.route("/", methods=["get", "post"])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run("localhost", "5000", debug=True)
