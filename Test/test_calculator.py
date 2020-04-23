

import unittest
#from Calculator import Calculator

from Simple_calculator.calculator import *

class CalculatorTest(unittest.TestCase):
    calculator = Calculator()
    def test_add_two_numbers(self):
        self.assertEqual(-2, self.calculator.add(-1,-1))
        self.assertEqual(3, self.calculator.add(1,2))

    def test_add_many_numbers(self):
        self.assertEqual(10 , self.calculator.add(1,2,3,4))  
        self.assertEqual(15 , self.calculator.add(1,2,3,4,5)) 
        

    def test_multiply_two_numbers(self):
        self.assertEqual(3, self.calculator.multiply(1,3))
        self.assertEqual(-3, self.calculator.multiply(-1,3))

    def test_multiply_many_numbers(self):
        self.assertEqual(120, self.calculator.multiply(1,2,3,4,5))

    

if __name__ == "__main__":
    unittest.main() 