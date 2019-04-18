# -*- coding: utf-8 -*-
"""
MTH 3300 JMWA HW #7: class Polynomial

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

def DictionaryHasPolynomialForm(dictionary):
    """ Returns True if dictionary's keys are all nonnegative ints, 
        and values are all floats. False otherwise. """
    if type(dictionary) is not dict:
        return False
    for k,v in dictionary.items():
        if type(k) is not int or k < 0 or type(v) not in (int, float):
            return False
    return True

def OneTerm(coeff, degree):
    """ Returns string of one term in a Polynomial. """
    assert type(coeff) in (int, float) and type(degree) is int, \
        "Polynomial term cannot have non-float coefficient or non-int degree."
    if degree == 0:
        xStr = ""  # don't print x if x^0
    elif degree == 1:
        xStr = "x" # don't print a power on x if x^1
    else:
        xStr = "x^" + str(degree)  # any other power should look like x^n
        
    if coeff == 0.0:
        return "0"  # don't print anything else if coeff = 0
    elif coeff == 1.0 and xStr != "":
        return xStr # don't print coeff if coeff in {1,-1} and x shows up
    elif coeff == -1.0 and xStr != "":
        return "-" + xStr # don't print coeff if coeff in {1,-1} and x shows up
    else:
        return str(coeff) + xStr  # usual look: a_n x^n


class Polynomial(object):
    def __init__(self, poly_dict):
        """ poly_dict is a dictionary whose (key, val) pairs are 
        (power, coefficient). """
        assert DictionaryHasPolynomialForm(poly_dict), \
            "Polynomial initializing dictionary not of right form."
        self.coeffs = poly_dict
            
    def __str__(self):
        polyStr = ""
        firstTerm = True
        f = self.clean() # don't print any 0 coefficients
        # Sort the powers from greatest to least.
        largestPowerFirst = sorted(f.coeffs.keys(),reverse=True)
        if len(largestPowerFirst) == 0:
            return "0"  # need to deal with 'empty' Polynomial
        for k in largestPowerFirst:
            thisTerm = OneTerm(f.coeffs[k], k)
            if not firstTerm and thisTerm != "":
                thisTerm = " + " + thisTerm
            polyStr += thisTerm   # add term
            if firstTerm:
                firstTerm = False  # find a better way to deal with firstTerm!
        return polyStr

    def clean(self):
        """ Removes the coefficient-zero terms in self. """
        cleanPoly = {}
        for k in self.coeffs:
            if self.coeffs[k] != 0.0:
                cleanPoly[k] = self.coeffs[k]
        return Polynomial(cleanPoly)

    def __eq__(self, other):
        """ Compares Polynomials for mathematical equality. """
        return self.clean().coeffs == other.clean().coeffs

    def __neg__(self):
        """ Returns the negative Polynomial of self. """
        negself = {}
        for k in self.coeffs:
            negself[k] = -self.coeffs[k]
        return Polynomial(negself)

    def __add__(self, other):
        """ Returns the Polynomial self + other."""
        sumPoly   = {}
        selfCopy  = self.coeffs.copy()
        otherCopy = other.coeffs.copy()
        
        for k,v in self.coeffs.items():
            for l,w in other.coeffs.items():
                # first, combine all the common-powered terms.
                if k == l:
                    sumPoly[k] = v + w
                    del selfCopy[k]
                    del otherCopy[l]
        # then, add in all the terms only in one Polynomial.
        for k,v in selfCopy.items():
            sumPoly[k] = v
        for k,v in otherCopy.items():
            sumPoly[k] = v
        return Polynomial(sumPoly).clean()

    def __sub__(self, other):
        return self + -other
    
    def __mul__(self, other):
        prodPoly = {}
        for k,v in self.coeffs.items():
            for l,w in other.coeffs.items():
                if k+l in prodPoly:
                    prodPoly[k+l] += v*w
                else:
                    prodPoly[k+l] = v*w
        return Polynomial(prodPoly).clean()
        
    def evaluate(self, x):
        assert type(x) in (int, float), "Polynomial cannot be evaluated at non-float."
        y = 0.0
        for k in self.coeffs:
            y += self.coeffs[k] * (x ** k)
        return y
        
    def derivative(self):
        """ Returns the derivative of the Polynomial self. """
        ddxPoly = {}
        for k in self.coeffs:
            ddxPoly[k-1] = k * self.coeffs[k]  # d(cx^k)/dx = kcx^(k-1)
        # drop the constant term from the derivative, if it exists
        try:
            del ddxPoly[-1]  # this entry doesn't belong.
        except KeyError:
            pass
        return Polynomial(ddxPoly)
    
    def integral(self, C = 0.0):
        """ Returns the indefinite integral of the Polynomial self, 
            with constant of integration C, i.e.
            \int self(x) dx = F(x) + C. """
        assert type(C) in (int, float), "Constant of integration must be float."
        intPoly = {}
        for k in self.coeffs:
            intPoly[k+1] = self.coeffs[k] / (k+1)  # int (cx^k)dx = cx^(k+1)/(k+1)
        if C != 0.0:
            intPoly[0] = C
        return Polynomial(intPoly)

    def definite_integral(self, a, b):
        """ Returns \int_a^b self(x) dx. """
        assert type(a) in (int, float), "Lower limit of integration must be float."
        assert type(b) in (int, float), "Upper limit of integration must be float."
        intSelf = self.integral()
        return intSelf.evaluate(b) - intSelf.evaluate(a)

# ----------------------------------
#  FUNCTION DEFINITIONS END HERE
# ----------------------------------
# ----------------------------------
#  MAIN CODE STARTS HERE
# ----------------------------------

if __name__ == "__main__":

    pass
    
# ----------------------------------
#  MAIN CODE ENDS HERE
# ----------------------------------
