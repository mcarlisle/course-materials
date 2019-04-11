# -*- coding: utf-8 -*-
"""
MTH 3300 JMWA Test #2

Nov 8, 2017

@mcarlisle

"""
# ----------------------------------
#  OPENING DESCRIPTION ENDS HERE
# ----------------------------------
# ----------------------------------
#  IMPORT STATEMENTS START HERE
# ----------------------------------
from numpy.random import poisson
from numpy import average
from numpy import float64 as nfl64
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

"""
Multiple Choice 
"""

def PartI():
    
    # Problem 1: scope
    print("#1:")
    x = 5
    y = -1
    def f(x,y):
        x = x + 3
        y = y + 2
        return x * y
    print("{0} + {1} = {2}... that can't be right.".format(y,x,f(x,y)))
#    print("{0} + {2} = {1}... that can't be right.".format(x,y,f(x,y)))
#    print("{0} + {1} = {2}... that can't be right.".format(y,x,f(y,x)))
#    print("{1} + {2} = {0}... that can't be right.".format(x,y,f(y,x)))
    
    '''
5 + 8 = -1... that can't be right.
-1 + 5 = 8... that can't be right. ***
-1 + 5 = 14... that can't be right.
-1 + 14 = 5... that can't be right.
    '''
    
    
    # Problem 2: list, range
    print("#2:")
    x = [1,2,4,5]
    y = x
    z = y[1:3]
    print("I like the number {k}".format(k=z[1]))
    '''
    I like the number 1
    I like the number 2
    I like the number 4 ***
    I like the number 5
    '''
    
    # Problem 3: recursion
    print("#3:")
    def onandon(n):
        if n == 1:
            return 0
        else:
            return n + onandon(n-1) * 2
        
    x = 3 + onandon(3)
    print(2 * x)
    '''
    24
    20 ***
    18
    14
    6
    0
    '''
    
    # Problem 4: assertions
    print("#4:")
    def buggy(x):
        assert x > 2, "buggy: x is too large"
        assert x < 4, "buggy: x is too small"
        return x + 0.01
    print(buggy(3.2))
#    print(buggy(5.2))
### RUN THIS ONE    print(buggy(-1.3))
    print("AssertionError: buggy: x is too large")
    '''
    3.21
    AssertionError: buggy: x is too small 
    
    3.21
    AssertionError: buggy: x is too small
    AssertionError: buggy: x is too large

    3.21
    AssertionError: buggy: x is too large
    AssertionError: buggy: x is too small
    
    3.21
    AssertionError: buggy: x is too large ***
    '''

    # Problem 5: try/except
    print("#5:")
    def alsobuggy(x,y):
        try:
            z = x + y
            return z
        except TypeError:
            print("alsobuggy: cannot add different types")
    a = 5
    b = 4.6
    c = "i am a string"
    d = "i am also a string WHAT ARE YOU DOING"
    print(alsobuggy(a,d))
    print(alsobuggy(b,a))
    print(alsobuggy(c,d))
    '''
    alsobuggy: cannot add different types
    9.6
    i am a stringi am also a string WHAT ARE YOU DOING    

    alsobuggy: cannot add different types
    
    TypeError: alsobuggy: cannot add different types

    alsobuggy: cannot add different types ***
    None
    9.6
    i am a stringi am also a string WHAT ARE YOU DOING        
    '''

# ----------------------------------
#  PART II: ALGORITHMS / CODING
# ----------------------------------

""" 
1. Define a function that takes as input a positive integer and a positive float:
    - n = number of Poisson random variable samples to generate
    - x = mean (average) parameter of the random variable
and outputs a dictionary that contains how many times each positive integer 
was returned as a Poisson with parameter x.

Assert that n is a positive integer and x is a positive float.

2. Define a function that takes as input a dictionary whose (key,value) pairs 
are both numbers. Return the average of the products of those pairs, i.e.
for every entry in the dictionary, sum up key*value, and divide the sum by the
sum of the counts in the dictionary (i.e. the number of samples).

Assert that the input is a non-empty dictionary, and raise a TypeError if 
any (key, value) pair are not both numbers.

This function will yield the average of the samples counted in #1.

3. Estimate the mean of a Poisson random variable via Monte Carlo simulation:

    Generate a dictionary from Problem 1 M times, each time computing its 
    average with Problem 2. Store these averages in a list.
    When complete, average this list. Return the result.
    
4. Get the error percentage between the result of Problem 3 and the "true" mean.

"""

def errorPct(est, actual):
    """Returns the error % between est and actual (with actual being baseline).
    """
    assert type(est) in (nfl64, float, int), "errorPct: arg1 non-numeric"
    assert type(actual) in (nfl64, float, int), "errorPct: arg2 non-numeric"
    
    if actual != 0.0:
        return round(abs((est - actual)/actual),6)  # to avoid binary issues
    elif est != 0.0:
        return round(abs((est - actual)/est),6)  # ... this always returns 1!
    else:
        return 0.0 # no error if both values are 0!


def PoissonCounts(n, x, printSamples=False):  # Problem 1
#    print("Entering PoissonCounts")    
    assert type(n) == int and n > 0, "PoissonCounts: # samples not pos int"
    assert (type(x) == float or type(x) == int) and x > 0, \
        "PoissonCounts: parameter not pos float"
    
    samples = poisson(x,n)
    if printSamples:
        print("Inside Problem 1: this is the list of Poisson samples generated:")
        print(samples)
    poisson_dictionary = {}
    for i in range(n):
        if samples[i] in poisson_dictionary:
            poisson_dictionary[samples[i]] += 1
        else:
            poisson_dictionary[samples[i]] = 1
            
#    print(samples)
#    print(poisson_dictionary)
#    print("Exiting PoissonCounts")    
    return poisson_dictionary


def DictionaryAverage(nums):  # Problem 2
#    print("Entering DictionaryAverage")
    assert nums == dict(nums), "DictionaryAverage: input not a dict"
    nums_len = len(nums)
    assert nums_len > 0, "DictionaryAverage: empty dictionary"
    try:
        total = 0.0
        num_samples = 0
        for k in nums:
#            print("k,v = {0},{1}".format(k,nums[k]))
            total += k * nums[k]
            num_samples += nums[k]
#        print("Exiting DictionaryAverage")
        return total / num_samples
    except:
        raise TypeError("DictionaryAverage: non-numerical (key, value) pair")


def MCPoissonMeanEstimation(n, x, M):  # Problem 3
#    print("Entering MCPoissonMeanEstimation")
    assert type(n) == int and n > 0, "MCMeanEstimation: # samples/run not pos int"
    assert (type(x) == float or type(x) == int) and x > 0, \
        "MCMeanEstimation: parameter not positive"
    assert type(M) == int and M > 0, "MCMeanEstimation: # runs not pos int"
    averages = []
#    print("\nBeginning runs: ")
    for i in range(M):
        averages.append(DictionaryAverage(PoissonCounts(n, x, False)))
#        if i % 100 == 0:
#            print("{0}... ".format(i), end="")
#    print("\nComplete.\n")
#    print("Exiting MCPoissonMeanEstimation")

#    return sum(averages)/len(averages)  # float
    return average(averages)  # numpy.float64


# ----------------------------------
#  FUNCTION DEFINITIONS END HERE
# ----------------------------------
# ----------------------------------
#  MAIN CODE STARTS HERE
# ----------------------------------

if __name__ == "__main__":

    PartI()
    
    # --- PROBLEM 1 ---
    print("\n\nSample output for Problem 1: ")
    print("a dictionary that contains how many times each nonnegative integer")
    print("was returned as a Poisson sample.")
    
    mean = 2.3
    ''' this is x in Problem 1 -- assert positive float'''
    samples = 10  
    ''' this is n in Problem 1 -- assert positive integer'''
    
    problem1out = PoissonCounts(samples, mean)  #, True)
    print("mean: {0}".format(mean))
    print("number of samples: {0}".format(samples))
    print(problem1out)
    
    #--- PROBLEM 2 ---
    print("\n\nSample output for Problem 2:")
    print("take something that looks like Problem 1's output as input; ")
    print("returns the average of the products of (key,value) pairs")
    print("BECAUSE value ARE COUNTS OF HOW MANY TIMES key APPEARED AS A SAMPLE")
    
    print(DictionaryAverage(problem1out))
    
    #--- PROBLEMS 3-4 ---
    samples, mean, runs = 2000, 5.78, 500  # this is n, x, M in Problems 3-4
    
    print("\n\nSample output for Problem 3:")
    print("Inputs for Poisson mean estimation:")
    print("'True' mean: {0}".format(mean))
    print("Samples per run: {0}".format(samples))
    print("Simulation runs: {0}\n".format(runs))
    
    sample_mean = MCPoissonMeanEstimation(samples, mean, runs)
    err = errorPct(sample_mean, mean) * 100
    print("Results:")
    print("Sample mean (Problem 3): {0}".format(sample_mean))
    print("'True' mean: {0}".format(mean))
    print("Error (Problem 4): {0}%".format(err))


    
# ----------------------------------
#  MAIN CODE ENDS HERE
# ----------------------------------
















