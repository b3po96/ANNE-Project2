"""
Project 2
Using Genetic Algorithms for Function Approximation

Language: Python

By: Bryce Buchanan
ID: 113318419
"""
from random import uniform

from GA_2D import initialize2D, select2D, crossover2D, mutate2D
from GA_3D import initialize3D, select3D, crossover3D, mutate3D
from HC_2D import *
from HC_3D import *

def GA_first(chromosome):
    avg_chromosome = []
    for i in range(100):
        for i in range(1000):
            # Selection
            chromosome = select2D(chromosome)
            # Crossover
            cross = chromosome.copy()
            random.shuffle(cross)
            chromosome.clear()
            for i in range(0, 3):
                parent_one = cross.pop()
                parent_two = cross.pop()
                offspring = crossover2D(parent_one, parent_two)
                chromosome.append(offspring[0])
                chromosome.append(offspring[1])
            # Mutation
            for gene in chromosome:
                gene += mutate2D(chromosome)
        avg_chromosome.append(sum(chromosome)/len(chromosome))
    return sum(avg_chromosome)/len(avg_chromosome)


def GA_second(chromosome):
    avg_chromosome = []
    for i in range(100):
        for i in range(1000):
            # Selection
            chromosome = select3D(chromosome)
            # Crossover
            cross = chromosome.copy()
            random.shuffle(cross)
            chromosome.clear()
            for i in range(0, 3):
                parent_one = cross.pop()
                parent_two = cross.pop()
                offspring = crossover3D(parent_one, parent_two)
                chromosome.append(offspring[0])
                chromosome.append(offspring[1])
            # Mutation
            for gene in chromosome:
                mutant = mutate3D(chromosome)
                gene = [mutant[0], mutant[1]]
        x = sum([element[0] for element in chromosome])/len(chromosome)
        y = sum([element[1] for element in chromosome])/len(chromosome)
        avg_chromosome.append([x, y])
    avg_x = sum([element[0] for element in avg_chromosome])/len(avg_chromosome)
    avg_y = sum([element[1] for element in avg_chromosome])/len(avg_chromosome)
    return [avg_x, avg_y] 
"""
Implements Hill Climbing in 2D API
"""
def HC_first():
    hill_results_2D = []
    for i in range(1000):
        hill_results_2D.append(hill_climb_2D(uniform(-5,5)))
    return sum(hill_results_2D)/len(hill_results_2D)

"""
Implements Hill Climbing in 3D API
"""
def HC_second():
    hill_results_3D = []
    for i in range(100):
        coords = (random.uniform(-5, 5), random.uniform(-5,5))
        hill_results_3D.append(list(hill_climb_3D(coords)))
    return [sum(hill_results_3D[0])/len(hill_results_3D), sum(hill_results_3D[1])/len(hill_results_3D)]

"""
Helper Function for plotting in 2D
"""
def plot_2D(point, title):
    fx = pow(np.linspace(-5,5,100), 4) - 22*pow(np.linspace(-5,5,100), 2)
    guess = pow(point, 4) - 22*pow(point, 2)
    plt.figure()
    plt.scatter(np.linspace(-5,5,100), fx, color='r', label='f(x)')
    plt.annotate('Max Estimate', (point, guess), xytext=(point + 1, guess + 1), 
                    arrowprops=dict(arrowstyle='->', connectionstyle='arc3'))
    plt.title(title)
    plt.ylabel('f(x)')
    plt.xlabel('x')
    plt.show()

"""
Helper Function for plotting in 3D
"""
def plot_3D(coords, title):
    estimate = "Max Estimate: " + str(coords)
    dx, dy = np.meshgrid(np.linspace(-5,5,500), np.linspace(-5,5,500))
    fz = -22*dx**2 + dx**4 - 22*dy**2 + dy**4
    guess = -22*coords[0]**2 + coords[0]**4 - 22*coords[1]**2 + coords[1]**4
    plt.figure()
    ax = plt.axes(projection = '3d')
    ax.plot_surface(dx,dy,fz, cmap = 'viridis')
    ax.set_title(title)
    ax.set_zlabel("f(x,y)")
    ax.set_ylabel('y')
    ax.set_xlabel('x')
    ax.text(-10, -10, 300, estimate)
    plt.show()

def main():
    # Chromosome initialization - 2D
    chromosome2D = initialize2D()
    chromosome2D = GA_first(chromosome2D)
    
    # Chromosome initialization - 3D
    chromosome3D = initialize3D()
    chromosome3D = GA_second(chromosome3D)

    plot_2D(chromosome2D, "Genetic Algorithm - 2D")
    plot_3D(chromosome3D, "Genetic Algorithm - 3D")

    # Hill Climbing
    hill_x = HC_first()
    hill_xy = HC_second()

    plot_2D(hill_x, 'Hill Climbing - 2D')
    plot_3D(hill_xy, 'Hill Climbing - 3D')
    
if __name__ == "__main__":
    main()