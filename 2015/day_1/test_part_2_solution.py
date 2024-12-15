import pytest
from .part_2_solution import solution

collect_solution=1783

def test_part2_solution():
    assert solution() == collect_solution, "Solution should return " + str(collect_solution)
