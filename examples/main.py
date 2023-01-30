import matplotlib.pyplot as plt
from random import randint
from tqdm import tqdm
import ga as ga
from math import sin, cos

VISUALIZE = True
NUM_EPOCHS = 10000

if VISUALIZE:
    from display import Display

def initialize_points(
    num_points: int,
    xlim: tuple[int, int] = (0, 800),
    ylim: tuple[int, int] = (0, 600)
) -> list[ga.Point]:
    """
    Function used to initialize nodes for the graph structure
    Generates points within a specific window size given by xlim and ylim
    """
    point_coords = []
    for _ in range(num_points):
        x = randint(xlim[0], xlim[1])
        y = randint(ylim[0], ylim[1])
        point_coords.append(ga.Point(x=x, y=y))
    return point_coords

def initialize_points_cirlce(
    num_points: int,
    radius: int
) -> list[ga.Point]:
    point_coords = []
    step_size = 2 * 3.1415 / num_points
    for i in range(num_points):
        x = radius * cos(step_size * i)
        y = radius * sin(step_size * i)
        point_coords.append(ga.Point(x=x, y=y))
    return point_coords

if __name__ == '__main__':
    # Initialize nodes, solver, and display
    # node_coords = [Point(0, 0), Point(0, 1), Point(1, 1), Point(1, 0)]
    # node_coords = initialize_points_cirlce(60, radius=700)
    node_coords = initialize_points(100)
    fitness = ga.fitness.TSP(
        ga.metrics.EuclideanDistance(),
        node_coords
    )

    solver = ga.models.GeneticAlgorithm(
        selection = ga.selection.RouletteWheel(),
        crossover = ga.crossover.TwoPoint(crossover_size=None),
        mutation = ga.mutation.CutInsert(cut_size=None),
        fitness = fitness,
        generation_size = 50,
        sequence_length = len(node_coords)-2,
        crossover_rate = 0.7,
        mutation_rate = 0.2,
    )

    if VISUALIZE:
        screen = Display(node_coords)
        screen.fit(node_coords)
    
    # Run the simulation
    best_list = []
    current_list = []
    for _ in tqdm(range(NUM_EPOCHS)):
        err = ''
        solver.step()
        current_list.append(1/fitness.evaluate_state(solver.current_state))
        best_list.append(1/fitness.evaluate_state(solver.best_state))

        if VISUALIZE:
            current_state = [node_coords[0]] + [node_coords[i+1] for i in solver.current_state] + [node_coords[-1]]
            best_state = [node_coords[0]] + [node_coords[i+1] for i in solver.best_state] + [node_coords[-1]]
            err = screen.update(current_state, best_state)
        if err or solver.finished:
            print(err)
            break

    # if solver.finished:
    #     screen.idle()
    
    # Plot the solution metrics over time
    plt.plot(current_list, label='current')
    plt.plot(best_list, label='best')
    plt.title('Performance over time')
    plt.ylabel('Metric')
    plt.xlabel('Epochs')
    plt.legend()
    plt.savefig('examples/result.png')

