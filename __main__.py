from argparse import ArgumentParser

from algorithms import GregTrowbridgeAlgorithm, JoyceLiuAlgorithm
from models import SolutionSet

def main():

    parser = ArgumentParser(description='N-Queens Solver')
    parser.add_argument('ns', metavar='n', type=int, nargs='+', help='One or more n-values to find Queen placement solutions on n-by-n sized chess boards')
    parser.add_argument('--algorithm', default='liu', choices=['liu', 'trowbridge'], metavar='algorithm', type=str, nargs='?', help='Either "liu" for Joyce Liu\'s algorithm or "trowbridge" for Greg Trowbridge\'s algorithm') 
    args = parser.parse_args()

    if args.algorithm == 'liu':
       [JoyceLiuAlgorithm(SolutionSet(n)) for n in args.ns]
    else:
       [GregTrowbridgeAlgorithm(SolutionSet(n)) for n in args.ns]
if __name__ == "__main__":
    main()
