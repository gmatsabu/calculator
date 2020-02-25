class Calculator:
    def __init__(self):
        pass
    
    def add(self,*args):
        sum = 0
        for value in args:
            number = int(value)
            sum += number
        return sum
    
    
def multiply(*numbers):
    product = 1

    for number in numbers:
        product = product * number
    return product

print(multiply(1,3))

print(multiply(1,2,3,4,5))
        
