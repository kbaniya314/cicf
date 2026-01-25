#!/usr/bin/env python

# CICF Week 3 Exercise 2
#
# Look at the LIGO time series and output the largest absolute difference between
# two different samples.
#

import h5py

data = h5py.File('H-H2_LOSC_4_V1-815235072-4096.hdf5', 'r')
strain = data['strain/Strain']

dmax = 0

for x,y in zip(strain[:-1],strain[1:]):
    pass


print(dmax)



