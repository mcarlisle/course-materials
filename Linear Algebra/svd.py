#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 2019
Updated on Wed Mar 27 2019

@author: mcarlisle

Singular Value Decomposition example

Linear Algebra

"""

import numpy as np
import math

A = np.array([[-5,2,0],[1,-1,-4],[-3,9,6],[18,0,-12]])

# Here's the punchline in one line. We'll do the work to compare to this result.
A_SVD = np.linalg.svd(A)

#-----------------------------------------------------------------------------
# Now, here's all the mathematical work. 
#-----------------------------------------------------------------------------

# First, generate the symmetric A A^t and A^t A.
AAt = np.matmul(A, A.transpose())
AtA = np.matmul(A.transpose(), A)

# Then, get their eigenvalues and eigenvectors.
AAt_eig = np.linalg.eig(AAt)
AtA_eig = np.linalg.eig(AtA)
# NOTE: Columns are eigenvectors: AAt_eig[0][i] has eigenvector AAt_eig[1][:,i].

# Convert these eigenvector matrices into their transposes
# so we can rearrange the eigenpairs easily.
AAt_eig_col = (AAt_eig[0], AAt_eig[1].transpose())
AtA_eig_col = (AtA_eig[0], AtA_eig[1].transpose())


# l is a list of values to round, n is the rounding precision
def roundlist(l, n):
    return list(map(lambda x: round(x,n), l))

# a is the (e-val, e-vect) pair, n is the rounding precision
def rounded_eigenpair(a, n):
    return (round(a[0],n), roundlist(a[1],n))

# Sort the eigenvalues, and their associated eigenvectors, in descending order.
AAt_eig_sort = sorted(zip(list(AAt_eig_col[0]), list(AAt_eig_col[1])), reverse=True)
AtA_eig_sort = sorted(zip(list(AtA_eig_col[0]), list(AtA_eig_col[1])), reverse=True)

# Round everything for cleaner numbers.
r = 8
AAt_eig_sort = list(map(lambda a: rounded_eigenpair(a, r), AAt_eig_sort))
AtA_eig_sort = list(map(lambda a: rounded_eigenpair(a, r), AtA_eig_sort))

# The singular values of A are the square roots of the shared eigenvalues.
eig_check1 = set(map(lambda x: x[0], AAt_eig_sort))
eig_check2 = set(map(lambda x: x[0], AtA_eig_sort))
# NOTE: Casting to set here to use intersection eliminates duplicates!
eig_shared = eig_check1.intersection(eig_check2)
eig_shared = sorted(list(eig_shared), reverse=True)

# Make Sigma the right shape for multiplication
Sigma = np.zeros(A.shape)
# Then, fill in the diagonal of Sigma with the square roots of eig_shared. 
for i in range(min(A.shape)):
    Sigma[i][i] = math.sqrt(eig_shared[i])
# ... so what if it's not Pythonic? It's nice!

# Construct U and V out of the eigenvectors - transpose to get rows.
U = np.array(list(map(lambda x: x[1], AAt_eig_sort))).transpose()
Vt = np.array(list(map(lambda x: x[1], AtA_eig_sort)))

# You'll note that some of these eigenvectors might be the negatives 
# of the ones computed by the SVD method above.

