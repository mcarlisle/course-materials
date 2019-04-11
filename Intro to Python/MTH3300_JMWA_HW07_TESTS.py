# -*- coding: utf-8 -*-
"""
HW #7: class Polynomial

Nov 20, 2017

@mcarlisle

HW #7: Write a class for polynomial functions, i.e. mathematical functions 
of the form
y = a_0 x^0 + a_1 x^1 + a_2 x^2 + ... + a_n x^n,
where n is a whole number, and a_0, a_1, ... a_n are real numbers (floats).

The class needs to initialize the function with whatever coefficients and 
exponents you give it (question: what's a good data structure for these 
coefficients and powers?), and needs to be able to:
- print the function in a 'nice' readable way
- compute the value of the function at a certain value of x
- add, subtract, and multiply two functions
- give the derivative of the function
- return the indefinite integral of the function (ignoring the constant of 
integration)
- compute the definite integral of the function over an interval

Remember your calculus! Calculus on polynomials is easy - just application 
of the power rule on each term.

Bonus if the class has functions to:
- find all roots of the function in a given interval (within a given tolerance)
- find all critical points of the function in a given interval
- find the maximum and minimum of the function in a given interval

You cannot use an existing Python package that does these things; you need 
to write your class using only standard Python.

Here are four test cases (note: you'll need more):
1. The derivative of the function
y = 5x^4 + -3.2x^2 + 12
is the function
y = 20x^3 + -6.4x^1.
2. The sum of 
20x^3 + -6.4x and 8.1x^9 + -2x 
is 
8.1x^9 + 20x^3 + -8.4x.
3. The product of the functions
y = 7x^4 + 0.5x^3 and y = 8.1x^9 + -2x^1
is the function
y = 56.7x^13 + 4.05x^12 + -14x^5 + -1x^4.
4. The integral of the function y = 5.3x^2 + -1
is the function
y = 1.7666667x^3 + -1x^1.
5. The integral of the function y = 5.3x^2 + -1
over the interval [2.1, 3.5]
is the number
57.9847.

Assigned Mon, Nov 20.
Due Mon, Dec 4.

"""
# ----------------------------------
#  OPENING DESCRIPTION ENDS HERE
# ----------------------------------
# ----------------------------------
#  IMPORT STATEMENTS START HERE
# ----------------------------------
from MTH3300_JMWA_HW07 import Polynomial
# ----------------------------------
#  IMPORT STATEMENTS END HERE
# ----------------------------------
# ----------------------------------
#  GLOBAL VARIABLES START HERE
# ----------------------------------
# ----------------------------------
#  GLOBAL VARIABLES END HERE
# ----------------------------------
# ----------------------------------
#  FUNCTION DEFINITIONS START HERE
# ----------------------------------
# ----------------------------------
#  FUNCTION DEFINITIONS END HERE
# ----------------------------------
# ----------------------------------
#  MAIN CODE STARTS HERE
# ----------------------------------

# CHANGE THE INITS BELOW TO YOUR DATA STRUCTURE

if __name__ == "__main__":

    print("BEGIN POLYNOMIAL TESTS\n")

    test1 =  Polynomial({4:5, 2:-3.2, 0:12})
    test1ddx = "The derivative of {0} is {1}."
    print(test1ddx.format(test1, test1.derivative()))

    test2a = Polynomial({3:20, 1:-6.4})
    test2b = Polynomial({9:8.1, 1:-2})
    test2sum = "The sum of {0} and {1} is {2}."
    test2prod = "The product of {0} and {1} is {2}."
    print(test2sum.format(test2a, test2b, test2a + test2b))
    print(test2prod.format(test2a, test2b, test2a * test2b))
    c = -2.1
    test2eval = "The polynomial f(x) = {0} evaluated at c = {1} is f({1}) = {2}."
    print(test2eval.format(test2a, c, test2a.evaluate(c)))
    
    test3 =  Polynomial({2:5.3, 0:-1})
    a, b = 2.1, 3.5
    test3indef = "The indefinite integral of {0} is {1}."
    test3def   = "The definite integral of {0} on the interval [{1}, {2}] is {3}."
    print(test3indef.format(test3, test3.integral()))
    print(test3def.format(test3, a, b, test3.definite_integral(a,b)))
    
    print("\nEND POLYNOMIAL TESTS")
    
# ----------------------------------
#  MAIN CODE ENDS HERE
# ----------------------------------
