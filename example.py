from fcoin import Fcoin
#if python3 use fcoin3
#from fcoin3 import Fcoin


fcoin = Fcoin()

print(fcoin.get_symbols())

print(fcoin.get_currencies())

fcoin.auth('you-key', 'you-secret') 

print(fcoin.get_balance())

print(fcoin.buy('fteth', 0.0001, 10))
#print(fcoin.sell('fteth', 0.002, 5))
#print(fcoin.cancel_order('6TfBZ-eORp4_2nO5ar6zhg0gLLvuWzTTmL1OzOy9OYg='))
#print(fcoin.get_candle('M1','fteth'))
