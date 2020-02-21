class Calculator:
    def __init__(self):
        pass
    
    def add(self,*args):
        sum = 0
        for value in args:
            number = int(value)
            sum += number
        return sum
