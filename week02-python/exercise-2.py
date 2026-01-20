#!/usr/bin/env python

# CICF Week 2 Exercise 2
#
# Reading a CSV the hard way
#
# Copy the iris.csv file from week 1 into this directory.
#  (cp ../week01-command-line/iris.csv .)
# Then read the CSV file and calculate the average petal length
# for each species in the file.

import csv
import numpy as np


# The hard part is reading the CSV file

species = {}

with open('iris.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        sname = row['species']
        lengths = species.get(sname, [])
        lengths.append(float(row['petal_length']))
        species[sname] = lengths

# change this to print the average for each species
# hint: use numpy
for k,v in species.items():
    print(f"{k} {v:0.3f}")



