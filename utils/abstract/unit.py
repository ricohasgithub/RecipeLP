'''
    This class represents a fundamental unit/token
    Parent class for:
        data_unit, logic_unit
'''

class Token():

    def __init__(self):
        pass

    def __init__(self, dimension, data, operation, relations):
        self.dimension = dimension
        self.data = data
        self.operation = operation
        self.relations = relations

    def compare(self, other):
        pass

    def get_combination_dimension(self):
        # By the handshake combination problem, the number of interactions will be equal to [n*(n-1)]/2
        return (((self.dimension - 1) * self.dimension) / 2)

    def token_compare(self):
        pass