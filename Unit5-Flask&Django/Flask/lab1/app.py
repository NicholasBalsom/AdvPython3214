from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/hello/<name>")
def hello(name):
    return render_template("hello.html", name=name)


@app.route("/number/<int:n>")
def number(n):
    return f"<h1>{str(n)}</h1>"


@app.route("/greet")
def greet():
    # example querry request would be "/greet?name=Bob"
    # querrys for a name in the url if none provided name will equal 'Guest'
    name = request.args.get("name", "Guest")
    return render_template("greet.html", name=name)


@app.route("/farewell/<name>")
def farewell(name):
    return render_template("farewell.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
