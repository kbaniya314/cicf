import pytest
import subprocess
import glob
import re

def df(x):
    return 4*(x**3) - 6*(x**2) - 2*x + 2

def test_exercise_1():
    points = [(x, df(x)) for x in [-1.0, 0.0, 1.0, 2.0]]
    
    for (x,dx) in points:
        print(f"testing {x}")
        result = subprocess.run(["./exercise-1.py", str(x)], capture_output=True)

        assert(result.returncode == 0)
        output = result.stdout.decode() # translate from bytes to utf-8
        assert(float(output) == dx)


def test_exercise_2():
    goal = 2.173121521631591e-17
    result = subprocess.run("./exercise-2.py", capture_output=True)
    assert(result.returncode == 0)
    out = result.stdout.decode() # translate from bytes to utf-8
    result = float(out)
    assert(abs(goal - result) < 1e-18)


