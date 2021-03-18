"""
Project 2
Using Genetic Algorithms for Function Approximation

Language: Python

By: Bryce Buchanan
ID: 113318419
"""
from random import uniform

from GA_1D import *
from HC_1D import *

#TODO Complete
def GA_first():
    # Chromosome initialization
    chromosome = initialize()

    for i in range(100):
        # Selection
        chromosome = select(chromosome)
        print(chromosome)
        # Crossover
        cross = chromosome.copy()
        random.shuffle(cross)
        chromosome.clear()
        for i in range(0, 3):
            parent_one = cross.pop()
            parent_two = cross.pop()
            offspring = crossover(parent_one, parent_two)
            chromosome.append(offspring[0])
            chromosome.append(offspring[1])
        # Mutation
        for gene in chromosome:
            gene += gene + mutate(chromosome)


def main():
   # GA_first()
    hill_results = []
    for i in range(1000):
        hill_results.append(hill_climb(uniform(-5,5)))
    print(sum(hill_results)/len(hill_results))
    
if __name__ == "__main__":
    main()