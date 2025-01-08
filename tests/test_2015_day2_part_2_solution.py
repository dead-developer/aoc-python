import pytest
from _2015.day_2.part_2_solution import solution

collect_solution=3812909

def test_part2_solution():
    assert solution() == collect_solution, "Solution should return " + str(collect_solution)
