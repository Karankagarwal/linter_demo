import json

class AppDemo:

    def __init__(self, a):
        self.a = a

    def Typechecking_and_naming_convention(self, vara: str, varb) -> None:
        return vara + varb

    def docstring_google(self, varx: str) -> None:
        """ Docstring not matching google style  """
        return None

    def unused_variable(self, varc: str):
        print(f'a={self.a}')
        return None



    def code_refactoring(self, vara: int) -> int  :
        if vara == 1:
            return vara
        else:
            return 'string'



