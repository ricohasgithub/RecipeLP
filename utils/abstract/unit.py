'''
    This class represents a fundamental unit
    Parent class for:
        data_unit, logic_unit
'''

class Unit():
    def __init__(self, data, operation):
        self.data = data
        self.operation = operation