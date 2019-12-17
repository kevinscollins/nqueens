# Exploration of the [N-Queens Problem](https://en.wikipedia.org/wiki/Eight_queens_puzzle) in Python

## Instructions 

> These are the different aspect of the project you can work on (in order):
> 1. determine all possible solutions for a given N where N ≥ 8 (within 10 mins on a laptop). Bonus points for a higher N where N is the size of the board / number of queens
> 2. iterate over N and store the solutions in postgres using SQLAlchemy
> 3. write basic tests that at least verify the number of solutions for a given N match what's online. I recommend using pytest
> 4. Docker-ize the solution, so that I can run the code and tests without any assumption of my local setup (including running a postgres instance in docker-compose)
> 5. setup Travis CI (or similar) for your public GitHub repo to run the tests automatically
>
> You don't need to go through all of the steps, but there should be instructions on how I can run the code. I mainly want to see how you approach a problem and your coding style. There are multiple steps so you have the option to show me different skills. It's up to you.
>
> Please commit everything in a public GitHub repo and use python3.
>
> You can borrow from an existing solution—except for Google's. If you borrow from someone else's code, please cite where you got the code and be ready to explain how the code works.

## Run it!

The [master branch](https://github.com/kevinscollins/nqueens) has all 5 of these implemented and can be cloned and then should be runnable
with a recent/compatible Docker installation.

### Installation

`git clone https://github.com/kevinscollins/nqueens && cd nqueens`

### Build Docker containers and Start Database

`docker-compose up -d`

### Classic 8-Queens Computation

`docker-compose run app python nqueens 8`

### Run Tests

`docker-compose run app pytest nqueens`

## Algorithmic Exploration

I implemented Greg Trowbridge's ["A Bitwise Solution to the N Queens Problem in JavaScript"](http://gregtrowbridge.com/a-bitwise-solution-to-the-n-queens-problem-in-javascript/)
in python, and upgraded it with Joyce Liu's ["Using Symmetry to Optimize an N-Queens Counting Algorithm"](http://liujoycec.github.io/2015/09/20/n_queens_symmetry/). 

I believe both of these approaches are parallizable, by separating out each column of the first row into separate recursive processes, 
but did not get this successfully working in a short period of time, see [wip_multiprocessing](https://github.com/kevinscollins/nqueens/tree/wip_multiprocessing).

## Performance

On my 2016 Macbook Pro, I can run N = 14 in 48 seconds of "wall clock" time, including container startup and overhead, etc. For N = 15, it takes right around 10 minutes.
For comparison, Joyce Liu's JavaScript algorithm completes N = 16 in about 8 seconds 😳 - althought it doesn't save, or even store, the solutions.

I profiled it with cProfile and the majority of the time is getting used with bitwise operations. There are other functions that could be improved for incremental speedup.

I did not realize how slow python's bitwise operations are and might have approached this problem differently if I had. Short of implementing the recursive logic natively, 
I did not find a good way to get native-esque bit operation performance in python.


