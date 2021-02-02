'''
    This class represents a fundamental unit/token
    Parent class for:
        data_unit, logic_unit
'''

class Token():

    def __init__(self):
        pass

    def __init__(self, data):
        self.data = data
        self.dimensions = len(data)

    def compare(self, other):
        pass

    def get_combination_dimension(self):
        # By the handshake combination problem, the number of interactions will be equal to [n*(n-1)]/2
        return (((self.dimension - 1) * self.dimension) / 2)

    def token_compare(self):
        pass

    def __str__(self):
        return ("Token of dimension: " + self.dimension + "; " + self.data)