import pytest
import subprocess
import glob
import re

def test_exercise_1():
    goal = [f"{n}" for n in range(1, 101) if (n % 3) == 0 or (n % 7) == 0]
    result = subprocess.run("./exercise-1.py", capture_output=True)

    assert(result.returncode == 0)
    output = result.stdout.decode() # translate from bytes to utf-8
    assert(output.splitlines() == goal)


def test_exercise_2():
    goal = [["setosa", 1.464], ["versicolor", 4.260], ["virginica", 5.552]]
    result = subprocess.run("./exercise-2.py", capture_output=True)
    assert(result.returncode == 0)
    out = result.stdout.decode() # translate from bytes to utf-8
    output = [line.split() for line in out]
    assert(output.splitlines() == goal)


