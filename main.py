"""
Project 2
Using Genetic Algorithms for Function Approximation

Language: Python

By: Bryce Buchanan
ID: 113318419
"""
from random import uniform

from GA_2D import *
from HC_2D import *
from HC_3D import *

#TODO Complete
def GA_first(chromosome):
    for i in range(1000):
        # Selection
        chromosome = select(chromosome)
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
    return(chromosome)

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
def plot_2D(point):
    fx = pow(np.linspace(-5,5,100), 4) - 22*pow(np.linspace(-5,5,100), 2)
    guess = pow(point, 4) - 22*pow(point, 2)
    plt.figure()
    plt.scatter(np.linspace(-5,5,100), fx, color='r', label='f(x)')
    plt.annotate('Max Estimate', (point, guess), xytext=(point + 1, guess + 1), 
                    arrowprops=dict(arrowstyle='->', connectionstyle='arc3'))
    plt.title('Original Function')
    plt.ylabel('f(x)')
    plt.xlabel('x')
    plt.show()

"""
Helper Function for plotting in 3D
"""
def plot_3D(coords):
    dx, dy = np.meshgrid(np.linspace(-5,5,500), np.linspace(-5,5,500))
    fz = -22*dx**2 + dx**4 - 22*dy**2 + dy**4
    guess = -22*coords[0]**2 + coords[0]**4 - 22*coords[1]**2 + coords[1]**4
    plt.figure()
    ax = plt.axes(projection = '3d')
    ax.plot_surface(dx,dy,fz, cmap = 'viridis')
    ax.set_title('Original Function')
    ax.set_zlabel("f(x,y)")
    ax.set_ylabel('y')
    ax.set_xlabel('x')
    plt.show()

def main():
    # Chromosome initialization
    chromosome = initialize()
    chromosome = GA_first(chromosome)
    print(chromosome)

    #hill_x = HC_first()
    #hill_xy = HC_second()

    #plot_2D(hill_x)
    #plot_3D(hill_xy)
    
if __name__ == "__main__":
    main()