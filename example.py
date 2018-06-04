from fcoin import Fcoin

fcoin = Fcoin()

print fcoin.get_symbols()

print fcoin.get_currencies()


fcoin.auth('you_key', 'you_secret')

fcoin.get_balance()

fcoin.buy('fteth', 0.0001, 10)
fcoin.sell('fteth', 0.0002, 5)

