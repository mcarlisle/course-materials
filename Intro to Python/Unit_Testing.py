# -*- coding: utf-8 -*-
"""
MTH 3300 Unit Testing Functions

Nov 8, 2017

@mcarlisle
"""
# ----------------------------------
#  OPENING DESCRIPTION ENDS HERE
# ----------------------------------
# ----------------------------------
#  IMPORT STATEMENTS START HERE
# ----------------------------------
from inspect import getfullargspec  # CheckArguments
from sys import exc_info # RaisedErrorSimpleTest, GoodDataTest
# ----------------------------------
#  IMPORT STATEMENTS END HERE
# ----------------------------------
# ----------------------------------
#  GLOBAL VARIABLES START HERE
# ----------------------------------
passed = "... passed"
failed = " FAILED " # a space makes it more obvious in the report
other_error = ": raised other Error"
otherError = other_error
# ----------------------------------
#  GLOBAL VARIABLES END HERE
# ----------------------------------
# ----------------------------------
#  FUNCTION DEFINITIONS START HERE
# ----------------------------------

def CheckArguments(testname, func, args):
    """ Checks if the tuple args contains a valid number of arguments for the
        function func. 
        Returns True if so, and raises an error if not.
    """
    raise_error = "CheckArguments: {0}: bad args for {1}".format(testname, func)

    funcargs = getfullargspec(func)
    #  min, max # of args = "args" - "defaults", "args"
    if funcargs[3] != None:
        minargs, maxargs = len(funcargs[0])-len(funcargs[3]), len(funcargs[0])
    elif funcargs[0] != None:
        minargs, maxargs = 0, len(funcargs[0])
    else:
        minargs, maxargs = 0, 0
    assert isinstance(args, tuple) and minargs <= len(args) <= maxargs, raise_error
    return True


def RaisedErrorSimpleTest(testname, func, args, error):
    """ Runs a one-line test of func to determine if func(*args) raises error.
        Returns 0 for passed test, 1 for failed test (for counting failures).
    """
    # First, test the args for func, so we know the test is valid.
    CheckArguments(testname, func, args)  # throws AssertionError
    # Then, we'll do the test we're here for.
    try:
        func(*args) 
        # don't care about what func returns; just checking if it runs at all
    except error:  # error is the *EXPECTED* error raised in this test
        print(testname + passed)
        return 0   # remember, 0 is a PASS (we count failures)
    except:
        # mention in the failure that a different error was raised
        print(failed + testname + failed)
        print(" Unexpected error: " + str(exc_info()[0]))
        print(" " + str(exc_info()[1]))
        return 1   # and count the failure
    else:
        print(failed + testname + failed)
        return 1   # count the failure


def GoodDataTest(testname, func, args, correct_answer):
    """ Runs a one-line test of func to determine if func(*args) returns 
        correctAnswer. 
        ASSUMES that args has the right kinds of arguments!
        Returns 0 for passed test, 1 for failed test (for counting).
    """
    # First, test the args for func, so we know the test is valid.
    CheckArguments(testname, func, args)  # throws AssertionError
    # Then, we'll do the test we're here for.
    try:
        if func(*args) == correct_answer:
            print(testname + passed)
            return 0
        else:
            print(failed + testname + failed)
            return 1
    except:
        print(failed + testname + failed)
        print(" Unexpected error: " + str(exc_info()[0]))
        print(" " + str(exc_info()[1]))
        return 1
    
# abbreviations for BatchUnitTest and anyone else that wants them
REST = RaisedErrorSimpleTest
GDT = GoodDataTest

def BatchUnitTest(testDict):
    """ Runs a batch of unit tests, with parameters in testDict.
    
        STRUCTURE OF testDict ENTRY:
        testname: {func, args, test_type, error, correct_answer}
        key: testname: str
        value: dict:
            func: function name
            args: tuple of arguments for func
            test_type: REST or GDT   #... or future types?
            error: used in REST
            correct_answer: used in GDT

        Returns a tuple (fail_count, test_count) of nonnegative ints.
    """
    fail_count, test_count = 0, 0
    # built this way in case new test types are created
    for testname, test in testDict.items():
        test_count += 1
        if test["test_type"] == "REST":
            fail_count += REST(testname, test["func"], test["args"], test["error"])
        elif test["test_type"] == "GDT":
            fail_count += GDT(testname, test["func"], test["args"], test["correct_answer"])

    return fail_count, test_count
    
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