# import "packages" from flask
from flask import Flask, render_template, request

# create a Flask instance
app = Flask(__name__)

#this adds the greet code-------------------------------

def greet(link, file, default):
    if request.form:                                                # if the user submits a name
        input = request.form.get("input")                           # store what the user submits
        if len("input") != 0:                                       # and if there is text in the number box
            return render_template(file, input=input, link=link)    # give html file the stored name
    return render_template(file, input=default, link=link)          # if there is nothing submitted, use "default"

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
    if request.form:
        number = request.form.get("input")
        if len(number) != 0:
            return render_template("/minilabs/binaryhackathon.html", BITS=int(number), link="/binaryhackathon/")
    return render_template("/minilabs/binaryhackathon.html", BITS=8, link="/binaryhackathon/")

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

@app.route('/minigames/')
def minigames():
    return render_template("minigames.html")

# money calculations

class CoinBank:
    num_coins = 10

    def getCoins(self):
        return self.num_coins

    def addCoins(self, coins):
        self.num_coins = self.num_coins + coins
        return self.num_coins

    def removeCoins(self, coins):
        # only remove coins if we have enough! We do not let you spend more than you have
        if self.num_coins >= coins:
            self.num_coins = self.num_coins - coins
            return self.num_coins
        else:
            raise ValueError("You do not have that many coins")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
