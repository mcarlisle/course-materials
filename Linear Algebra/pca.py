#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 2019
Updated on Wed Mar 27 2019

@author: mcarlisle

PCA example
"""

from math import sqrt
import numpy as np
import pandas as pd

# First, read in the data.
A = pd.read_excel("pca_scores.xls")

# Next, subtract off the means for each column.
A_centered = A - A.mean()

# Next, construct the covariance matrix.
A_centered_mtx = np.array(A_centered)
S = np.matmul(A_centered_mtx, A_centered_mtx.transpose()) / (A.shape[0]-1)
# If there are m = len(A.shape[0]) samples of n = len(A.shape[1]) parameters,
# then S is m x m. We expect that m is much larger than n.
d = min(A.shape[0], A.shape[1])  # max dimension possible for eigenspace

# Get the eigendecomposition (diagonalization) of the covariance matrix.
S_eig = np.linalg.eig(S) 

# The total variance is the sum of the eigenvalues of S.
total_var = sum(S_eig[0].real)

# The eigenpairs of S need to be put in descending order by eigenvalue.
S_eigidx  = list(S_eig[0].argsort())
S_eigidx.reverse()  # We want the eigenpairs in descending order.
# Really, we only care about the nonzero-eigenvalue eigenpairs.
S_eigvals = S_eig[0][S_eigidx][0:d]
S_eigvect = S_eig[1].transpose()[S_eigidx] #[0:min(A.shape[0], A.shape[1])]

# For large dimension reduction, we will manage the eigenpairs at this point
# to make managing NumPy's "strange zeros", and complex values, from appearing.
S_eigvals = S_eigvals.round(8).real
S_eigvect = S_eigvect.round(8).real

# Now that we have the eigendecomposition sorted descending, report.
S_eigweights = list(map(lambda x: round(100 * x / total_var, 8), S_eigvals))
S_eigweights = np.array(S_eigweights).round(8).real
report_str   = "component {}: {} accounts for {}% of total variance"
#for i in range(2):
#    print(report_str.format(i+1, str(S_eigvect[i]), S_eigweights[i]))

# What do these principal components tell us about the data? 
# They give "new directions" to compress the data down significantly, 
# with minimal loss of information.

# We would like to reconstuct A (as much as possible) from the PCA.
A_eigvals = [sqrt((A.shape[0]-1) * S_eigvals[i]) for i in range(d)]

# We must build the opposite side of the SVD, but must divide by the SAME number.
R = np.matmul(A_centered_mtx.transpose(), A_centered_mtx) / (A.shape[0]-1)
R_eig = np.linalg.eig(R) # the nonzeros should match S_eig
R_eigidx  = list(R_eig[0].argsort())
R_eigidx.reverse()  # We want the eigenpairs in descending order.
R_eigvals = R_eig[0][R_eigidx][0:d]
R_eigvect = R_eig[1].transpose()[R_eigidx] 
R_eigvals = R_eigvals.round(8).real
R_eigvect = R_eigvect.round(8).real

# Approximate the original centered matrix A via the first few terms of its SVD.
A_approx = sum([A_eigvals[i] * np.outer(S_eigvect[i],R_eigvect[i]) for i in range(d)])

# ---------

# Or, just do the entire thing in two lines.

A_svd = np.linalg.svd(A_centered_mtx)
V2 = A_svd[2][0:2]

PCA_plot = np.matmul(A_centered_mtx, V2.transpose())
PCA_plot_letters = ['C','A','B','C','B','A','F','A','A','A','F','F',
                    'A','A','A','A','B','C','A','C','F','C','A','B',
                    'C','C','A','B','B','A','B']
grade_to_color = { 'A': '#00FF00', 'B': '#77FFFF', 'C': '#CCCC77', 
                   'D': '#FF77FF', 'F': '#FF0000' }
PCA_plot_colors = [grade_to_color[i] for i in PCA_plot_letters]

import matplotlib.pyplot as plt
plt.xlabel("PC1")
plt.ylabel("PC2")
# build plot, one color at a time
for grade in sorted(list(set(PCA_plot_letters))):
    xc = [p for (i,p) in enumerate(list(PCA_plot[:,0])) if PCA_plot_letters[i] == grade]
    yc = [p for (i,p) in enumerate(list(PCA_plot[:,1])) if PCA_plot_letters[i] == grade]
    cc = grade_to_color[grade]   
    mc = '$' + grade + '$'  # use LaTeX for letter grades on plot itself
    plt.scatter(x = xc, y = yc, c = cc, marker = mc, label = grade)
    
plt.legend(loc=4)
plt.show()  # and we've reproduced the graph in the lecture notes.

