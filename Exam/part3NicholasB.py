# INSTRUCTIONS:
#  - Make sure you have Flask installed
#  - Run the python file
#  - Click the link in the terminal to open in your browser

# Comments from me:
# In the instructions it said assume that html files would be in templates folder,
# I asked our teacher and he said that we didnt need to create actual html files and to just assume
# So i just wrote html in the return of the view function

# PS. The instuctions for most questions are quite vauage, and specific requirements could be added on each question for clarity
# They do not explain how to do it just what you want done for that question.

from flask import Flask

app = Flask(__name__)


@app.route("/form")
def form():
    return "<h1>Form Page</h1><br><form action='submit'><input type='submit'></form>"


@app.route("/submit")
def submit():
    return "<h1>Form Submitted</h1>"


if __name__ == "__main__":
    app.run(debug=True)
