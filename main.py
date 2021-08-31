# import "packages" from flask
from flask import Flask, render_template

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/avinh/')
def avinh():
    return render_template("avinh.html")

@app.route('/akhil/')
def akhil():
    return render_template("akhil.html")

@app.route('/calissa/')
def calissa():
    return render_template("calissa.html")

@app.route('/valen/')
def valen():
    return render_template("valen.html")

@app.route('/stub/')
def stub():
    return render_template("stub.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
