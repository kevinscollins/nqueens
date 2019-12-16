from argparse import ArgumentParser
from multiprocessing import Process

from algorithms import GregTrowbridgeAlgorithm, JoyceLiuAlgorithm
from models import SolutionSet

def worker_in_new_process(Algorithm, n, starting_configuration):
    print('worker_in_new_process() called!')
    solution_set = SolutionSet(n, reset_schema=False)
    algorithm = Algorithm(solution_set, run_now=False)
    algorithm.find_solutions_from_top_row(
        starting_configuration['columns_in_row_order'],
        starting_configuration['left_diagonal_mask'],
        starting_configuration['column_mask'],
        starting_configuration['right_diagonal_mask'])
    solution_set.commit()
    
def main():

    parser = ArgumentParser(description='N-Queens Solver')
    parser.add_argument('ns', metavar='n', type=int, nargs='+', help='One or more n-values to find Queen placement solutions on n-by-n sized chess boards')
    parser.add_argument('--algorithm', default='liu', choices=['liu', 'trowbridge'], metavar='algorithm', type=str, nargs='?', help='Either "liu" for Joyce Liu\'s algorithm or "trowbridge" for Greg Trowbridge\'s algorithm') 
    args = parser.parse_args()

    # Playing with multiprocessing but the answers are not coming out correctly :)
    n = 6
    solution_set = SolutionSet(n)
    algo = JoyceLiuAlgorithm(solution_set, run_now=False)

    print(str(algo.get_first_row_starting_configurations()))

    workers = []
    for starting_configuration in algo.get_first_row_starting_configurations():
        worker = Process(target=worker_in_new_process, args=(JoyceLiuAlgorithm, n, starting_configuration))
        workers.append(worker)
        worker.start()

    for worker in workers:
        worker.join()

    print ("Found {} solutions for n = {}".format(solution_set.count(), n))

if __name__ == "__main__":
    main()
