"""
Project 2
Using Genetic Algorithms for Function Approximation

Language: Python

By: Bryce Buchanan
ID: 113318419
"""
from GA_1D import *

def main():
    # Chromosome initialization
    chromosome = initialize()

    # Selection
    chromosome = select(chromosome)

   # Crossover
    cross = chromosome.copy()

    # Mutation
    for gene in chromosome:
        gene += gene + mutate(chromosome)
    return 0

if __name__ == "__main__":
    main()