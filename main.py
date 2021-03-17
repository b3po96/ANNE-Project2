"""
Project 2
Using Genetic Algorithms for Function Approximation

Language: Python

By: Bryce Buchanan
ID: 113318419
"""
#from deap import base, creator, tools

from GA_1D import *

def main():
    chromosome = initialize()
    print(chromosome)
    chromosome = select(chromosome)
    for gene in chromosome:
        gene += gene + mutate(chromosome)
    return 0

if __name__ == "__main__":
    main()