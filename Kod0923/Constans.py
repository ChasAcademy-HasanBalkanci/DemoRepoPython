from typing import Final

# Constant variable

PI:Final = 3.14

PI = 3.1415926

print(PI) 

# Notera att Final inte är nödvändigt, men det är "best practice" att använda för konstanter för att göra koden mer lättläst och lättare att förstå.

class Constants:
    PI: Final = 22/7
    MAX_LENGTH = 33
    MIN_LENGTH = 10

def __init__(self, min_lenght=Constants.MIN_LENGTH, max_lenght=Constants.MAX_LENGTH):
    self.min_lenght = min_lenght
    self.max_lenght = max_length

def area(self, a, b) -> float:
    return Constants.PI * (self.min_lenght + self.max_lenght) / 2
x = area(7, 9)
print(x)