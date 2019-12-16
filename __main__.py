from argparse import ArgumentParser

from algorithms import GregTrowbridgeAlgorithm
from models import SolutionSet

def main():

    parser = ArgumentParser(description='N-Queens Solver')
    parser.add_argument('ns', metavar='n', type=int, nargs='+', help='One or more n-values to find Queen placement solutions on n-by-n sized chess boards') 
    args = parser.parse_args()

    [GregTrowbridgeAlgorithm(SolutionSet(n)) for n in args.ns]

if __name__ == "__main__":
    main()
