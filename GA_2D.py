"""

Implementation of Genetic Algorithm in 2D Search Space
by: Bryce Buchanan

"""
import numpy as np
import random
import matplotlib.pyplot as plt

"""
Initializes the chromosome using a uniform distribution between -5.0 and 5.0
"""
def initialize():
    chromosome = []
    for i in range(6):
        gene = random.uniform(-5.0, 5.0)
        chromosome.append(gene)
    return chromosome

"""
Implements fitness using the provided function to maximize the score

Returns: proportionate representation of the fitness scores
"""
def fitness(chromosome):
    fit_score = []
    for gene in chromosome:
        fit = pow(gene, 4) - 22 * pow(gene, 2)
        fit_score.append(fit)
    fit_sum = sum(fit_score)
    return fit_score
    
"""
Finds the index of the gene we want to select

Returns: an index for the selected gene
"""
def find_selector(sort):
    ind = random.uniform(0.0, 1.0)
    val = 0
    if (ind <= sort.get(0)):
        val = 0
    if (ind >= sort.get(0) and ind <= sort.get(1)): 
        val = 1
    if (ind >= sort.get(1) and ind <= sort.get(2)):
        val = 2
    if (ind >= sort.get(2) and ind <= sort.get(3)):
        val = 3
    if (ind >= sort.get(3) and ind <= sort.get(4)):
        val = 4
    if (ind >= sort.get(4)):
        val = 5
    return val

"""
Implements crossover using the random number in range crossover operator

Returns: the offspring of the two parents
"""
def crossover(parent_one, parent_two):
    offspring = []
    if random.random() <= 0.5:
        #print("CROSSOVER OCCURED!")
        if parent_one > parent_two:
            temp = parent_one
            parent_one = parent_two
            parent_two = temp
        offspring.append(random.uniform(parent_one, parent_two))
        offspring.append(random.uniform(parent_one, parent_two))
    else:
        offspring.append(parent_one)
        offspring.append(parent_two)
    return offspring

"""
Implements mutation using the additive operator, with a 0.01% chance of mutation

Returns: Either 0 (if no mutatation) or a random number between [-5.0, 5.0] (if mutation occuers)
"""
def mutate(chromosome):
    if random.random() <= 0.01:
        #print("MUTATION OCCURED!")
        return random.uniform(-5.0, 5.0)
    else:
        return 0

"""
Implements selection using the roulette wheel operator
"""
def select(chromosome):
    selector = fitness(chromosome)
    for element in selector:
        selector[selector.index(element)] = element/sum(selector)
    # Sorts the dictionary to compare values
    sort = sorted(selector)
    sort_dict = dict(zip(range(0,5),sort))
    selected = []
    for item in range(len(chromosome)):
        selected.append(chromosome[find_selector(sort_dict)])
    return selected