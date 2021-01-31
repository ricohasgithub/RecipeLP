'''
    This class represents a fundamental unit
    Parent class for:
        data_unit, logic_unit
'''

class Unit():

    def __init__(self):
        pass

    def __init__(self, dimension, data, operation, relations):
        self.dimension = dimension
        self.data = data
        self.operation = operation
        self.relations = relations