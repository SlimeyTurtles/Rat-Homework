# import "packages" from flask
from flask import Flask, render_template, request

# create a Flask instance
app = Flask(__name__)

#this adds the greet code
def greet(link, file):
    if request.form:                                                        # if the user submits a name
        name = request.form.get("name")                                     # store what the user submits
        if len(name) != 0:                                                  # and if there is text in the submission box
            return render_template(file, greetInput=name, htmlLink=link)    # give html file the stored name
    return render_template(file, greetInput="World", htmlLink=link)         # if no submitted text, default to "Greetings, World"

@app.route('/')
def index():
    return render_template("index.html")

# about us pages

@app.route('/avinh/', methods=['GET', 'POST'])
def avinh():
    return greet('/avinh/', "avinh.html")

@app.route('/akhil/')
def akhil():
    return render_template("akhil.html")

@app.route('/calissa/')
def calissa():
    return render_template("calissa.html")

@app.route('/valen/')
def valen():
    return render_template("valen.html")

# mini-labs

@app.route('/greet/', methods=['GET', 'POST'])
def greetminilab():
    return greet('/greet/', "greet.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
