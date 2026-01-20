# CICF Week 2

The goals for the week 2 lab are:

1. Be able to work with Python from the command line.
2. Use NumPy

## Python

Python is a programming language that is ubiquitous in scientific computing.
It is easy to learn, and can be extended easily using packages.
Python can be used as scripts, or interactively at the command line.
There are also things called _notebooks_ or _Jupyter notebooks_ which provide a visual envrionment for exploring data and doing analysis.
We will discuss Jupyter notebooks more in week 3.

## The REPL

Python is already installed in the codespace.
Start it with the `python` command.

```
@dbrower ➜ /workspaces/cicf (main) $ python
Python 3.13.11 (main, Dec  9 2025, 02:02:02) [GCC 14.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL
>>>
```

The `>>>` is the Python prompt, analogous to the shell prompt `$`.
Python will wait for you to type a line and then it will run it.
This interactive session is sometimes called a  REPL for "Read-Eval-Print Loop": the interpreter will read a line that you type, evaluate it, print the result, and then repeat the process.
(Not forever, though. You can exit back to the shell by typing either `Ctrl-D` or the command `exit`.)

Unlike the shell, Python expects you to enter a Python _expression_ at the prompt.

For starters, we can use the prompt as a fancy calculator.

```
>>> 2+2
4
>>> 2**80
1208925819614629174706176
>>> import math
>>> math.log2(300)
8.228818690495881
```

We can assign and use variables:

```
>>> x = 2**10
>>> x
1024
>>> y = 5
>>> x+y
1029
>>> y = y + 1
>>> x+y
1030
>>> [k**2 for k in range(y)]
[0, 1, 4, 9, 16, 25]
>>> a=_
>>> a
[0, 1, 4, 9, 16, 25]
```

The above makes a variable `x` and sets it equal to 2 to the 10th power.
It then sets variable `y` equal to 5.
We can make expressions with `x` and `y`.
The values for `x` and `y` don't change unless we set them.
We can make a list using a _list comprehension_.
The underscore `_` variable is a special one when we are using the interactive prompt.
It holds the value of the the previous prompt.
Lists can be indexed to get values out of them:

```
>>> a[3]
9
>>> a.append('apple')
>>> a
[0, 1, 4, 9, 16, 25, 'apple']
```

The `append()` method will change the list variable it is attached to.
Also, lists can contain values of any type.
In this case we added a string to the list of integers.

```
>>> [type(t) for t in a]
[<class 'int'>, <class 'int'>, <class 'int'>, <class 'int'>, <class 'int'>, <class 'str'>]
```

We can define functions at the interactive prompt:

```
>>> def fact(n):
...        if n <= 1: return 1
...        return n*fact(n-1)
...
>>> fact(5)
120
>>> fact(30)
265252859812191058636308480000000
>>> fact(30.0)
2.6525285981219103e+32
```

Here we define a function, the factorial function, and then use it in the interactive session.
Why do you think there is there a difference between `fact(30)` and `fact(30.0)`?

We have a more in-depth [introduction to Python](./python.md).
There are also good tutorials listed in the [resources](#resources) section.


## NumPy

The `math` module is part of the Python standard library.  It
implements a routine to calculate few standard functions and some
basic probability distributions.

However, since Python's built-in support for numerical calculations is
limited in efficiency and performance, people often reach for the
famous [NumPy] package.

[NumPy]: https://numpy.org/

NumPy makes numerically-intensive programming easier and makes code
run faster. It brings it's own datatype to the game: an actual array!
Numpy's arrays are quite fast -- substantially faster than Python's
regular way of representing arrays as "lists of lists" (or in three
dimensions, "lists of lists of lists" and so forth.

The critical NumPy data type is the array.  NumPy arrays are faster
and more compact than Python lists. A NumPy array consumes less memory
and is convenient to use.  You can find an excellent
[introduction][numpy-intro] to NumPy in the project's website.

[numpy-intro]: https://numpy.org/doc/stable/user/absolute_beginners.html

In this notebook, let us work through some NumPy examples.  First,
let's tell Python we want to use numpy:

```{python}
import numpy as np
```

The `as np` part lets us specify a _namespace_, in this case a nice,
short name so we don't have to type out `numpy` _every single time_.

The one caveat with NumPy arrays is that all the elements inside an
array need to have the same data type (e.g. integer, float, double).

Now we can create an array or two:

```{python}
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(a)
```

The `array()` function will turn nested lists into an array.
You can also make new arrays by asking for an array of zeros of a given size

```{python}
z = np.zeros(3)
print(z)
```

or ones:

```{python}
m = np.ones((3,3))
print(m)
```

(note that the dimensions are given as a _tuple_).

You can also element-wise add, subtract, or multiply:

```{python}
z + 3
```

Or

```{python}
a % 2
```

Comparisons are element wise

```{python}
a > 5
```

You can get the dimensions of an array by querying its `.shape`
property:

```{python}
print(a.shape)
print(m.shape)
print(z.shape)
```

The `shape` property returns us a _tuple_ that tells us how many
elements there are in each dimension.  The number of elements in the
tuple tells us how many dimensions the array has.

### NumPy Linear Algebra

Let's do a little bit of linear algebra. NumPy has routines to do
basic linear algebra, such as finding a matrix inverse, or solving a
linear system.

We will need to bring in the [linalg] ("linear algebra") part of
NumPy, which would be the `numpy.linalg` module.  We will use the name
`nl` as a shorthand for `numpy.linalg`.

[linalg]: https://numpy.org/doc/stable/reference/routines.linalg.html

```{python}
import numpy.linalg as nl

k = np.array([[1,1,1], [1,1,0], [1,0,0]])

kinv = nl.inv(k)
kinv
```

To do matrix multiplication use the operator `@`.

```{python}
k @ kinv
```

For a complete list of operators, see: [Mapping Operators to
Functions][op-table].

[op-table]: http://docs.python.org/library/operator.html#mapping-operators-to-functions

The array multiplication `*` and matrix multiplication `@` are very different.
Here is an example with a square array.

```
>>> x = np.array([[0,-1],[1,0]])
>>> x*x
array([[0, 1],
       [1, 0]])
>>> x@x
array([[-1,  0],
       [ 0, -1]])
```

(as an aside, this suggests the array `x` behaves as a square root of -1 with respect to matrix multiplcation).

You can get an array of equally spaced points using `np.linspace()`.
It takes a starting point, an endpoint and the total number of points desired.

```
>>> w = np.linspace(-2*np.pi, 2*np.pi, 100)
>>> w.shape
(100,)
>>> w
array([-6.28318531, -6.15625227, -6.02931923, -5.9023862 , -5.77545316,
       -5.64852012, -5.52158709, -5.39465405, -5.26772102, -5.14078798,
       -5.01385494, -4.88692191, -4.75998887, -4.63305583, -4.5061228 ,
       -4.37918976, -4.25225672, -4.12532369, -3.99839065, -3.87145761,
       -3.74452458, -3.61759154, -3.4906585 , -3.36372547, -3.23679243,
       -3.10985939, -2.98292636, -2.85599332, -2.72906028, -2.60212725,
       -2.47519421, -2.34826118, -2.22132814, -2.0943951 , -1.96746207,
       -1.84052903, -1.71359599, -1.58666296, -1.45972992, -1.33279688,
       -1.20586385, -1.07893081, -0.95199777, -0.82506474, -0.6981317 ,
       -0.57119866, -0.44426563, -0.31733259, -0.19039955, -0.06346652,
        0.06346652,  0.19039955,  0.31733259,  0.44426563,  0.57119866,
        0.6981317 ,  0.82506474,  0.95199777,  1.07893081,  1.20586385,
        1.33279688,  1.45972992,  1.58666296,  1.71359599,  1.84052903,
        1.96746207,  2.0943951 ,  2.22132814,  2.34826118,  2.47519421,
        2.60212725,  2.72906028,  2.85599332,  2.98292636,  3.10985939,
        3.23679243,  3.36372547,  3.4906585 ,  3.61759154,  3.74452458,
        3.87145761,  3.99839065,  4.12532369,  4.25225672,  4.37918976,
        4.5061228 ,  4.63305583,  4.75998887,  4.88692191,  5.01385494,
        5.14078798,  5.26772102,  5.39465405,  5.52158709,  5.64852012,
        5.77545316,  5.9023862 ,  6.02931923,  6.15625227,  6.28318531])
```


1. tutorials for python
  a) exercise: compute square root? https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf
2. numpy for science
  a) arrays, creating, operations, linear regression
  b) homogenious
3. read CSV file, do something (regression for each type?)
  a) do pandas at this step? or first use CSV library.
  b) exercise: read CSV with csv library. convert into np array.
  c) exercise: read CSV file with pandas?
4. random arrays




## Resources

Parts of this tutorial were taken from the [LIGO data tutorial](https://gwosc.org/tutorial02/).

- [Programming with Python](https://swcarpentry.github.io/python-novice-inflammation/) is a introduction to Python, part of the always nice Software Carpentry workshops.
- [An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html)
- [Python Reference](https://docs.python.org/3/) for the most recent version of Python.
- [NumPy for Absolute Beginners](https://numpy.org/doc/stable/user/absolute_beginners.html)
- Literate Programming is a specific instance of the idea that code
  and documentation should be more mixed together. Here is a [Knuth
  paper](http://www.literateprogramming.com/knuthweb.pdf) and an
  [amazing website](http://www.literateprogramming.com/articles.html)
  (not Knuth's) with more information that you ever thought existed on
  program documentation.
- [Markdown Cheat Sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

- [Jupyter Manual](https://docs.jupyter.org/en/latest/)
- [MatPlotLib](https://matplotlib.org/)
- [HDF5](https://docs.hdfgroup.org/hdf5/v1_14/_intro_h_d_f5.html) is a
  file format that supports efficient storage and transfer of numeric
  data.
- All of the [released LIGO data](https://gwosc.org/data/)
