# import "packages" from flask
from flask import Flask, render_template, request

# create a Flask instance
app = Flask(__name__)

#this adds the greet code
def greet(link, file):
    if request.form:                                               # if the user submits a name
        name = request.form.get("name")                            # store what the user submits
        if len(name) != 0:                                         # and if there is text in the submission box
            return render_template(file, input=name, link=link)    # give html file the stored name
    return render_template(file, input="World", link=link)         # if no submitted text, default to "Greetings, World"

@app.route('/')
def index():
    return render_template("index.html")

# about us pages

@app.route('/avinh/', methods=['GET', 'POST'])
def avinh():
    return greet('/avinh/', "avinh.html")

@app.route('/akhil/', methods=['GET', 'POST'])
def akhil():
    return greet('/akhil/', "akhil.html")

@app.route('/calissa/', methods=['GET', 'POST'])
def calissa():
    return greet('/calissa/', "calissa.html")

@app.route('/valen/', methods=['GET', 'POST'])
def valen():
    return greet('/valen/', "valen.html")

# mini-labs

@app.route('/greet/', methods=['GET', 'POST'])
def greetminilab():
    return greet('/greet/', "greet.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
