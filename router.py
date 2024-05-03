from flask import Flask, render_template, url_for, request
import random
import service, mapper

app = Flask("__name__")
app.config["SECRET_KEY"] = "secretkey"


@app.route("/", methods=["get", "post"])
def index():
    rows = mapper.view_expenses()
    return render_template("index.html", rows=rows)


@app.route("/create_db", methods=["get", "post"])
def create_db():
    status = mapper.create_database()
    return render_template("index.html", status=status)


@app.route("/settings", methods=["post", "get"])
def settings():
    return render_template("settings.html")


@app.route("/add_expenses", methods=["get", "post"])
def add_expenses():

    status = service.add_expenses()
    return render_template("add_expenses.html", status=status)


@app.route("/add_accounts", methods=["get", "post"])
def add_accounts():
    status = service.add_account()
    rows = mapper.view_account()
    return render_template("add_account_details.html", rows=rows)


@app.route("/delete_expenses", methods=["post", "get"])
def delete_expenses():
    service.delete_expenses()
    return render_template("delete.html")


@app.route("/delete_accounts", methods=["post", "get"])
def delete_accounts():
    service.delete_accounts()
    return render_template("delete.html")


if __name__ == "__main__":
    app.run("localhost", "5000", debug=True)
