from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


def fibonacci(n):
    if n in {0, 1}:  # Base case
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello/<name>")
def hello(name):
    return render_template("hello.html", name=name)


@app.route("/new_hello/<name>")
def new_hello(name):
    return render_template("new_hello.html", name=name)


@app.route("/about")
def about():
    return "<h1>About Page</h1>"


@app.route("/capitalize/<word>")
def capitalize(word):
    return "<h1>{}</h1>".format(escape(word.capitalize()))


@app.route("/add/<int:num1>/<int:num2>")
def add(num1, num2):
    return "<h1>{}</h1>".format(num1 + num2)


@app.route("/fib/<int:n>")
def fib(n):
    result = fibonacci(n)
    return f"The fibonacci number at position {n} is {result}"


if __name__ == "__main__":
    app.run(debug=True)  # add port and (host=0.0.0.0 for example) for network server
