import sys
sys.path.append("..")
from nologic.base import state_selector

def even_divide():

    def _divide(n):
        return (n // 2)

    _state = 0

    return (_state, _divide)


def odd_divide():
    
    def _divide(n):
        return ((n-1) // 2)
    
    _state = 1
    
    return (_state, _divide)


def divide(n):

    _state = n % 2
    f = state_selector(_state, [even_divide, odd_divide])
    return f(n)

    
    
if __name__ == '__main__':

    print(divide(101))
    