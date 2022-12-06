class NegativeSumError(Exception):
    def __init__(self):
        self.message = 'This sum is negative'
        super().__init__(self.message)
def sum_with_exceptions(a, b):
    c = a + b
    if c < 0:
        raise NegativeSumError()
    
    return c
