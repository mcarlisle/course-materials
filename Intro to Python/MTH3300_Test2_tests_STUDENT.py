# -*- coding: utf-8 -*-
"""
Test #2 Test Suite

Nov 10, 2017

@mcarlisle

This file supplies test cases for Problem 1 through Problem 4 for Test #2,
along with sample output in print statements, to compare.

"""

# ----------------------------------
#  IMPORT STATEMENTS START HERE
# ----------------------------------
import Unit_Testing as UT
from MTH3300_Test2_sample_code import \
    PoissonCounts, DictionaryAverage, MCPoissonMeanEstimation, errorPct
    # THIS FILE WILL NOT RUN unless you replace 
    # "MTH3300_Test2_sample_code" with your test file's name.
# ----------------------------------
#  IMPORT STATEMENTS END HERE
# ----------------------------------
# ----------------------------------
#  GLOBAL VARIABLES START HERE
# ----------------------------------
# Test #2 function aliases, for ease of typing tests
REST = UT.RaisedErrorSimpleTest
GDT = UT.GoodDataTest
BUT = UT.BatchUnitTest
P1 = PoissonCounts
P2 = DictionaryAverage
P3 = MCPoissonMeanEstimation
P4 = errorPct
AE = AssertionError

ep = 0.1  # basic threshold for error estimation LLN tests
# a single test could still be somewhat off, probabilistically, 
# but 10% in is definitely the right ballpark
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

if __name__ == "__main__":

    def P1GDT(dictionary, length):
        """Checking Problem 1: is the output a dictionary with fewer 
        entries than the number of samples made? Good enough for now.
        """
        return (type(dictionary) == dict and len(dictionary) <= length)
    
    def P3GDT(n,x,M):
        """Checking Problem 3: is the output sample average within ep (as a %)
        of 
        """
        y = P3(n,x,M)
#        print("y = {0} vs x = {1}".format(y,x))
#        print("type(y) = {0} and type(x) = {1}".format(type(y), type(x)))
        # TODO mention in class the issue with float vs numpy.float64
        err = P4(y,x)
#        print(err)
        return (err < ep)

    test_dictionary = {
            # Problem 1: P1(n=samples, x=mean)
            "Problem 1 Assertion test 1a ('x pos float')": {
                "test_type": "REST", "func": P1, "args": (10, -2.4), "error": AE},
            "Problem 1 Assertion test 1b ('x pos float')": {
                "test_type": "REST", "func": P1, "args": (10, -2), "error": AE},
            "Problem 1 Assertion test 1c ('x pos float')": {
                "test_type": "REST", "func": P1, "args": (10, "string!"), "error": AE},
            "Problem 1 Assertion test 2a ('n pos int')": {
                "test_type": "REST", "func": P1, "args": (-2, 2.4), "error": AE},
            "Problem 1 Assertion test 2b ('n pos int')": {
                "test_type": "REST", "func": P1, "args": (1.6, 2.4), "error": AE},
            "Problem 1 Assertion test 2c ('n pos int')": {
                "test_type": "REST", "func": P1, "args": ("string!", 2.4), "error": AE},
            "Problem 1 good data test 1": {
                "test_type": "GDT", "func": P1GDT, "args": (P1(100,4),100), 
                "correct_answer": True},
            "Problem 1 good data test 2": {
                "test_type": "GDT", "func": P1GDT, "args": (P1(50,5.6),50), 
                "correct_answer": True},
            # Problem 2: P2(dict)
            "Problem 2 Assertion test 1 ('nonempty dict')": {
                "test_type": "REST", "func": P2, "args": ({},), "error": AE},
            "Problem 2 Assertion test 2a ('key-value pair non-numeric')": {
                "test_type": "REST", "func": P2, "args": ({4:5,5:"hello",3:8},), 
                "error": TypeError},
            "Problem 2 Assertion test 2b ('key-value pair non-numeric')": {
                "test_type": "REST", "func": P2, "args": ({4:5,"hello":5,3:8},), 
                "error": TypeError},
            "Problem 2 Assertion test 2c ('key-value pair non-numeric')": {
                "test_type": "REST", "func": P2, "args": ({4:5,"hello":"world",3:8},), 
                "error": TypeError},
            "Problem 2 good data test 1": {
                "test_type": "GDT", "func": P2, "args": ({3:4, 8:1, 0:5, 2:6},), 
                "correct_answer": 2.0},
            # Problem 3: P3(n=samples per run, x=mean, M=runs)
            "Problem 3 Assertion test 1a ('x pos float')": {
                "test_type": "REST", "func": P3, "args": (200,-2.4,100), "error": AE},
            "Problem 3 Assertion test 1b ('x pos float')": {
                "test_type": "REST", "func": P3, "args": (200,-2,100), "error": AE},
            "Problem 3 Assertion test 1c ('x pos float')": {
                "test_type": "REST", "func": P3, "args": (20,"string!",10), "error": AE},
            "Problem 3 Assertion test 2a ('n pos int')": {
                "test_type": "REST", "func": P3, "args": (-2,2.4,100), "error": AE},
            "Problem 3 Assertion test 2b ('n pos int')": {
                "test_type": "REST", "func": P3, "args": (1.6,2.4,100), "error": AE},
            "Problem 3 Assertion test 2c ('n pos int')": {
                "test_type": "REST", "func": P3, "args": ("string!",2.4,100), "error": AE},
            "Problem 3 Assertion test 3a ('M pos int')": {
                "test_type": "REST", "func": P3, "args": (200,2.4,-100), "error": AE},
            "Problem 3 Assertion test 3b ('M pos int')": {
                "test_type": "REST", "func": P3, "args": (200,2.4,100.2), "error": AE},
            "Problem 3 Assertion test 3c ('M pos int')": {
                "test_type": "REST", "func": P3, "args": (200,2.4,"string!"), "error": AE},
            # Problem 4: P4(P3(n,x,M)=sample mean, x=mean)
            # BEFORE Problem 3 good data tests
            "Problem 4 Assertion test 1a ('est, actual int or float')": {
                "test_type": "REST", "func": P4, "args": ([],100.3), "error": AE},
            "Problem 4 Assertion test 1b ('est, actual int or float')": {
                "test_type": "REST", "func": P4, "args": (200.5,(6,5)), "error": AE},
            "Problem 4 Assertion test 1c ('est, actual int or float')": {
                "test_type": "REST", "func": P4, "args": ("nope",[]), "error": AE},
            "Problem 4 good data test 1a": {
                "test_type": "GDT", "func": P4, "args": (200.5,100.25), 
                "correct_answer": 1.0},
            "Problem 4 good data test 1b": {
                "test_type": "GDT", "func": P4, "args": (100.25,200.5), 
                "correct_answer": 0.5},
            "Problem 4 good data test 1c": {
                "test_type": "GDT", "func": P4, "args": (3,0), 
                "correct_answer": 1.0},
            "Problem 4 good data test 1d": {
                "test_type": "GDT", "func": P4, "args": (0,3), 
                "correct_answer": 1.0},
            "Problem 4 good data test 1e": {
                "test_type": "GDT", "func": P4, "args": (0,0), 
                "correct_answer": 0.0},
            # Now we can do Problem 3 good data tests... with enough runs.
            "Problem 3 good data test 1": {
                "test_type": "GDT", "func": P3GDT, "args": (200,2.4,500), 
                "correct_answer": True},
            "Problem 3 good data test 2": {
                "test_type": "GDT", "func": P3GDT, "args": (500,3.64,1000), 
                "correct_answer": True},
            }
    totals = BUT(test_dictionary)
    print("END OF TESTS: ", end="")
    print("{0} FAILURES OUT OF {1} TESTS.".format(totals[0], totals[1]))

# ----------------------------------
#  MAIN CODE ENDS HERE
# ----------------------------------
