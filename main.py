# import "packages" from flask
from flask import Flask, render_template, request, jsonify
from images import image_data
from pathlib import Path  # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f

import requests

# create a Flask instance
app = Flask(__name__)

# Greet Function

def greet(link, file, default):
    if request.form:                                                # if the user submits a name
        input = request.form.get("input")                           # store what the user submits
        if len("input") != 0:                                       # and if there is text in the number box
            return render_template(file, input=input, link=link)    # give html file the stored name
    return render_template(file, input=default, link=link)          # if there is nothing submitted, use "default"

@app.route('/')
def index():
    access_token = "2573~5LIOVMh7P3sMuGrZQS4lWrXp6k96wZf7zBy8efDat22Y1sTAcLYLoMyKP0AanUQR"
    homework_list_url = "https://poway.instructure.com/api/v1/courses/108206/assignments?access_token=" + access_token
    response = requests.get(homework_list_url)
    homework_list = []
    for assignment in response.json():
        homework_list.append(assignment["name"])
    return render_template("index.html", homework_list=homework_list)

# About us

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

# Our work

@app.route('/greet/', methods=['GET', 'POST'])
def greetminilab():
    return greet('/greet/', "/OurWork/greet.html", "World")

@app.route('/videojournal/')
def videojournal():
    return render_template("/OurWork/videojournal.html")

@app.route('/binaryhackathon/', methods=['GET', 'POST'])
def binaryhackathon():
    if request.form:
        number = request.form.get("input")
        if len(number) != 0:
            return render_template("/OurWork/binaryhackathon.html", BITS=int(number), link="/binaryhackathon/")
    return render_template("/OurWork/binaryhackathon.html", BITS=8, link="/binaryhackathon/")

@app.route('/rgb/', methods=['GET', 'POST'])
def rgb():
    path = Path(app.root_path) / "static" / "img"
    return render_template('OurWork/rgb.html', images=image_data(path))

@app.route('/test-prep-tuesday/')
def PairShareJournal():
    return render_template("/OurWork/TPT.html")

@app.route('/brainwrites/')
def brainwrites():
    return render_template("/OurWork/brainwrites.html")

@app.route('/wireframes/')
def wireframes():
    return render_template("/OurWork/wireframes.html")

@app.route('/logic-lab/')
def logiclab():
    return render_template("/OurWork/logiclab.html")

@app.route('/color-code/')
def colorcode():
    return render_template("/OurWork/colorcode-temp.html")

@app.route('/addition/')
def addition():
    return render_template("/OurWork/addition.html")

# PBL

@app.route('/food/')
def food():
    return render_template("food.html")

@app.route('/shop/')
def shop():
    return render_template("shop.html")

@app.route('/customization/')
def customization():
    return render_template("customization.html")

@app.route('/minigames/minigames/')
def minigames():
    return render_template("/minigames/minigames.html")

@app.route('/minigames/Snake/')
def Snake():
    return render_template("/minigames/Snake.html")

@app.route('/minigames/game/')
def Game():
    return render_template("/minigames/game.html")

@app.route('/minigames/game/mousespeed')
def UpgradeMouseSpeed():
    return jsonify("true")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)