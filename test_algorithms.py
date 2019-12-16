import pytest

from algorithms import GregTrowbridgeAlgorithm
from models import SolutionSet

def test_start():
    solution_set = SolutionSet(25, table_prefix="test_start")
    assert solution_set.count() == 0

class TestTrowbridge:

    table_prefix = 'trowbridge_test'
    
    def test_one(self):
        solution_set = SolutionSet(1, table_prefix=TestTrowbridge.table_prefix)
        GregTrowbridgeAlgorithm(solution_set)
        assert solution_set.count() == 1

    def test_two(self):
        solution_set = SolutionSet(2, table_prefix=TestTrowbridge.table_prefix)
        GregTrowbridgeAlgorithm(solution_set)
        assert solution_set.count() == 0

    def test_three(self):
        solution_set = SolutionSet(3, table_prefix=TestTrowbridge.table_prefix)
        GregTrowbridgeAlgorithm(solution_set)
        assert solution_set.count() == 0

    def test_four(self):
        solution_set = SolutionSet(4, table_prefix=TestTrowbridge.table_prefix)
        GregTrowbridgeAlgorithm(solution_set)
        assert solution_set.count() == 2

    def test_five(self):
        solution_set = SolutionSet(5, table_prefix=TestTrowbridge.table_prefix)
        GregTrowbridgeAlgorithm(solution_set)
        assert solution_set.count() == 10

    def test_six(self):
        solution_set = SolutionSet(6, table_prefix=TestTrowbridge.table_prefix)
        GregTrowbridgeAlgorithm(solution_set)
        assert solution_set.count() == 4

    def test_seven(self):
        solution_set = SolutionSet(7, table_prefix=TestTrowbridge.table_prefix)
        GregTrowbridgeAlgorithm(solution_set)
        assert solution_set.count() == 40

    def test_eight(self):
        solution_set = SolutionSet(8, table_prefix=TestTrowbridge.table_prefix)
        GregTrowbridgeAlgorithm(solution_set)
        assert solution_set.count() == 92

    def test_nine(self):
        solution_set = SolutionSet(9, table_prefix=TestTrowbridge.table_prefix)
        GregTrowbridgeAlgorithm(solution_set)
        assert solution_set.count() == 352

    def test_ten(self):
        solution_set = SolutionSet(10, table_prefix=TestTrowbridge.table_prefix)
        GregTrowbridgeAlgorithm(solution_set)
        assert solution_set.count() == 724

    def test_eleven(self):
        solution_set = SolutionSet(11, table_prefix=TestTrowbridge.table_prefix)
        GregTrowbridgeAlgorithm(solution_set)
        assert solution_set.count() == 2680
