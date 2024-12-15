import pytest
from .part_1_solution import solution

collect_solution=1598415

def test_part1_solution():
    assert solution() == collect_solution, "Solution should return " + str(collect_solution)
