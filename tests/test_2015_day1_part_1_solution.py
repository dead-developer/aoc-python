import pytest
from _2015.day_1.part_1_solution import solution

collect_solution=232

def test_part1_solution():
    assert solution() == collect_solution, "Solution should return " + str(collect_solution)
