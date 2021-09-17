# import "packages" from flask
from flask import Flask, render_template, request

# create a Flask instance
app = Flask(__name__)

#this adds the greet code-------------------------------

def greet(link, file, defaultsubmission):
    if request.form:                                                    # if the user submits a name
        submission = request.form.get("input")                          # store what the user submits
        if len("input") != 0:                                        # and if there is text in the submission box
            return render_template(file, input=submission, link=link)   # give html file the stored name
    return render_template(file, input=defaultsubmission, link=link)    # if no submitted text, use "defaultsubmission"

@app.route('/')
def index():
    return render_template("index.html")

# about us pages -------------------------------------

@app.route('/avinh/', methods=['GET', 'POST'])
def avinh():
    return greet('/avinh/', "/about/avinh.html", "World")

@app.route('/akhil/', methods=['GET', 'POST'])
def akhil():
    return greet('/akhil/', "/about/akhil.html", "World")

@app.route('/calissa/', methods=['GET', 'POST'])
def calissa():
    return greet('/calissa/', "/about/calissa.html", "World")

@app.route('/valen/', methods=['GET', 'POST'])
def valen():
    return greet('/valen/', "/about/valen.html", "World")

# mini-labs ------------------------------------------

@app.route('/greet/', methods=['GET', 'POST'])
def greetminilab():
    return greet('/greet/', "/minilabs/greet.html", "World")

@app.route('/videojournal/')
def videojournal():
    return render_template("/minilabs/videojournal.html")

@app.route('/binaryhackathon/', methods=['GET', 'POST'])
def binaryhackathon():
    return greet('/greet/', "/minilabs/binaryhackathon.html", "8")

# How-Its-Made ---------------------------------------

@app.route('/test-prep-tuesday/')
def PairShareJournal():
    return render_template("/HowItsMade/TPT.html")

@app.route('/brainwrites/')
def brainwrites():
    return render_template("/HowItsMade/brainwrites.html")

@app.route('/wireframes/')
def wireframes():
    return render_template("/HowItsMade/wireframes.html")

# theme ---------------------------------------------

@app.route('/food/')
def food():
    return render_template("food.html")

@app.route('/shop/')
def shop():
    return render_template("shop.html")

@app.route('/customization/')
def customization():
    return render_template("customization.html")

@app.route('/minigames/', methods=['GET', 'POST'])
def minigames():
    return render_template("minigames.html")

if __name__ == "__main__":
    app.run()

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
