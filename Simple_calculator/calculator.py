
class Calculator:

    def __init__(self):
        pass


    def add(self, *args):
        sum = 0
        for number in args:
            total = int(number)
            sum += total
        return sum

    def multiply(self, *args):
        product = 1
        for number in args:
            total = int(number)
            product *= total
        return product