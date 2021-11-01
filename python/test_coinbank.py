import pytest as pytest

from coin_bank import CoinBank, costofmouseupgrade


def test_startingCoinsEqual100():
    assert CoinBank().getCoins() == 100


def test_addOneCoin():
    assert CoinBank().addCoins(1) == 101


def test_removeOneCoin():
    assert CoinBank().removeCoins(1) == 99


def test_removeAllCoins():
    assert CoinBank().removeCoins(10) == 90


def test_removeTooManyCoinsValueError():
    with pytest.raises(ValueError):
        # sorry hacker you do not have that many coins
        CoinBank().removeCoins(100000)
        assert False


def test_unsupportedMouseUpgradeRaisesError():
    with pytest.raises(KeyError):
        remaining_coins = CoinBank().buyMouseUpgrade('Flying Mouse')
        assert True;


def test_costofmouseupgrade():
    assert 20 == costofmouseupgrade('Rename Mouse')


def test_renameMouse():
    coinBank = CoinBank()
    starting_coins = coinBank.getCoins()
    remaining_coins = coinBank.buyMouseUpgrade('Rename Mouse')
    spent_coins = starting_coins - remaining_coins
    assert spent_coins == 20
    assert remaining_coins == 80
