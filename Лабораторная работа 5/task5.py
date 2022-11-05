from random import sample

symbols = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz0123456789'
n = 8

def get_random_password() -> str:
    return ''.join(sample(symbols, n))

print(get_random_password())
