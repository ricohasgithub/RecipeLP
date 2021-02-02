
from utils.abstract.unit import Token

class Operation_Token(Token):

    def __init__(self, operation):
        super().__init__()
        self.operation = operation

