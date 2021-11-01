
dict = {'Premium Mouse Color': 10, 'Larger Mouse Size': 15, 'Rename Mouse': 20, 'Elite Mouse Skin': 10, 'Heightened Smell': 20}

class CoinBank:
    num_coins = 100

    def setCoins(self, coins):
        self.num_coins = coins

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
