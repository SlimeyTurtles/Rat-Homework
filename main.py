# import "packages" from flask
from flask import Flask, render_template, request
from images import image_data
from pathlib import Path  # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f

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

#-------------------------- ABOUT US PAGES -----------------------------------#

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

#-------------------------- OUR WORK PAGES -----------------------------------#

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

@app.route('/addition/')
def addition():
    return render_template("/OurWork/addition.html")

#-------------------------- THEME PAGES-----------------------------------#

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


# money calculations ------------------------------------------------------------------------------------------------------------

class CoinBank:
    num_coins = 100
# This is a dictionary with key value pairs
    dict = {'Premium Mouse Color': 10, 'Larger Mouse Size': 15, 'Rename Mouse': 20, 'Elite Mouse Skin': 10, 'Heightened Smell': 20}

    def getCoins(self):
        return self.num_coins

    def removeCoins(self, coins):
        # if removing coins (coins are negative) and we can afford it
        if self.num_coins >= coins:
            self.num_coins = self.num_coins - coins
            return self.num_coins
        else:
            raise ValueError("You do not have that many coins")

# add any number of coins
    def AddCoins(self, coins):
        self.num_coins = self.num_coins + coins

    def costOfMouseUpgrade(key):
        return dict[key]

    def buyMouseUpgrade(self, key):
        try:
            cost = dict[key]
            print ("cost of " + key + " is ", cost)
            return self.removeCoins(cost)
        except KeyError:
            # Raise a KeyError because the key passed to us does not match anything in our dictionary
            raise KeyError("No mouse upgrade avaiable for " + key)

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)