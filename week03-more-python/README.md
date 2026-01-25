# CICF Week 3

There are many things with Python that are left to go over, so the tutorial will look at Jupyter notebooks and the Pandas library.

The goals for this tutorial are:

1. Download data from LIGO and know what an HDF5 file is.
2. Use the NumPy and Pandas packages.


## Tutorial

You can run Jupyter notebooks in the Codespace.
Open the [first notebook](./1-introduction.ipynb) in a tab (either click on the file in the left-side file browser, or use the `code` command at the command line).
When the notebook opens, there should be a button at the top left to "Select kernel".
Click it and then choose the second option, the installed python version.
And this point you can execute the code cells in the notebook by putting the curser in the cell and typing Ctrl-Return.


## Pandas

There is an extremely useful tool for working with CSV data called Pandas.
Open and work through the [second notebook](./2-pandas.ipynb).


## LIGO

Finally, lets look at some scientific data from a major facility.
This is in the [third notebook](./3-plot-ligo-data.ipynb)



# Resources

* [Advanced HDF5 with h5py Tutorial](https://github.com/HDFGroup/hdf5-tutorial/blob/main/04-Python-Bliss.ipynb)
* [HDF5 Field Guide](https://support.hdfgroup.org/documentation/hdf5/latest/)
* [Basics of Pandas](https://www.geeksforgeeks.org/machine-learning/python-basics-of-pandas-using-iris-dataset/)
* [Gravational Wave Open Science Center](https://gwosc.org/)


** Scientific Computing **

* HPC Carpentry [Introduction to High-Performance Computing](https://carpentries-incubator.github.io/hpc-intro/)
* News article on design of a new HPC system at TACC: [With Vista, TACC now has three paths to its future horizon superomputer (2024)](https://www.nextplatform.com/2024/01/29/with-vista-tacc-now-has-three-paths-to-its-future-horizon-supercomputer/)
* [BOINC](https://boinc.berkeley.edu/) distributed scientific computing
* [SETI@Home](https://setiathome.berkeley.edu/) is the original distributed computing project. No longer distributing tasks, though.
* TACC's [Frontera User Guide](https://docs.tacc.utexas.edu/hpc/frontera/)


**Networking Performance Links**

* [Latency and IP](https://www.potaroo.net/ispcolumn/2000-09-latency.html) by Geoff Huston, September 2000.
* High latency, but high throughput (i.e. putting data on a disk drive and ship it) examples are Amazon Snowball and [Snowmobile](https://aws.amazon.com/snowmobile/). Quote: "This secure data truck stores up to 100 PB of data and can help you to move exabytes to AWS in a matter of weeks."
* One can use non-TCP and non-IP protocols like [Internet2](https://internet2.edu/), [ESnet (DOE)](https://www.es.net/), [NSF FABRIC Testbed](https://fabric-testbed.net/), or custom (e.g. [Facebook](https://engineering.fb.com/category/networking-traffic/)
* Popular press article: [Connecting the South Pole](https://www.datacenterdynamics.com/en/analysis/connecting-the-south-pole/)

