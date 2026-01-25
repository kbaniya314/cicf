#!/usr/bin/env python

# CICF Week 3 Exercise 1
#
# A dual number is a number in the form a + b𝜀 where a and b are real numbers
# and 𝜀 has the property that 𝜀^2 = 0. So one can add and multiply dual numbers
# as:
#   (a + b𝜀) + (c + d𝜀) = (a+b) + (c+d)𝜀
#   (a + b𝜀) * (c + d𝜀) = (ac) + (ad + bc)𝜀
#
# They are useful for computing derivatives since if we start with the dual
# number a + 𝜀 then computing f(a + 𝜀) = c + d𝜀 gives us c = f(a) and d = f'(a).
# where f' is the derivative of f.
#
# The dual numbers can be represented as a 2x2 matrix where
#
#   a + b𝜀 <-- corresponds to -->  [ a  b ]
#                                  [ 0  a ]
#
#
# Given a real number x as a command line argument, print the derivative of the
# following function at the point x.
#
#   f(x) = x * (x^2 - 1) * (x - 2)
#

import numpy as np
import sys


x = float(sys.argv[1])

# do something to compute derivative.
a = np.array([[x, 1], [0, x]])
one = np.array([[1, 0], [0, 1]])


# change this to print the derivative of f at x
print(x)


