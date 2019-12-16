from math import pow

class GregTrowbridgeAlgorithm:
    """
    Pythonication of Greg Trowbridge's "A Bitwise Solution to the N Queens Problem in Javascript" [0]
    based on Martin Richards "Backtracking Algorithms in MCPL using Bit Patterns and Recursion" [1]

    [0] http://gregtrowbridge.com/a-bitwise-solution-to-the-n-queens-problem-in-javascript/
    [1] http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.51.7113&rep=rep1&type=pdf
    """

    def mask_to_str(self, mask):
        format_string = '{' + '0:0{}b'.format(self.n) + '}'
        return format_string.format(mask)

    def print_mask(self, name, mask):
        print('{} = {}'.format(name, self.mask_to_str(mask)))

    def convert_to_boolean_string(self, columns_in_row_order):
        return ''.join([str(self.mask_to_str(x)) for x in columns_in_row_order])
    
    def find_remaining_solutions(self, columns_in_row_order, left_diagonal_mask, column_mask, right_diagonal_mask):
        if column_mask == self.max_ones:
            self.solution_set.add(self.convert_to_boolean_string(columns_in_row_order))
            self.count += 1
            return

        possible_column_mask = ~ ( left_diagonal_mask | column_mask | right_diagonal_mask)

        while possible_column_mask & self.max_ones:
            bit = (possible_column_mask & - possible_column_mask) & self.max_ones
            possible_column_mask = (possible_column_mask - bit) & self.max_ones
            self.find_remaining_solutions(
                columns_in_row_order.copy() + [bit],
                ((left_diagonal_mask | bit) >> 1),
                (column_mask | bit),
                ((right_diagonal_mask | bit) << 1))
            
    def __init__(self, solution_set):
        self.solution_set = solution_set
        self.n = self.solution_set.n
        self.max_ones = int(pow(2, self.solution_set.n) - 1)
        self.count = 0
        self.find_remaining_solutions(list(), 0, 0, 0)
        print ("Found {} solutions for n = {}".format(self.count, self.n))
