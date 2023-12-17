# Write a program to carry out the following experiment. A coin is tossed 100 times and the number of heads that turn up is recorded. This experiment is then repeated 1000 times. Have your program plot a bar graph for the proportion of the 1000 experiments in which the number of heads is n, for each n in the interval [35, 65]. Does the bar graph look as though it can be fit with a normal curve?

import random
import matplotlib.pyplot as plt

def coin_toss_experiment(num_tosses, num_experiments):
    results = []
    for _ in range(num_experiments):
        # Perform a coin toss experiment
        heads_count = sum(random.choice([0, 1]) for _ in range(num_tosses))
        results.append(heads_count)
    return results

def plot_bar_graph(results):
    plt.hist(results, bins=range(35, 66), density=True, alpha=0.75, edgecolor='black')
    plt.title('Coin Toss Experiment Results')
    plt.xlabel('Number of Heads')
    plt.ylabel('Proportion')
    plt.show()

# Parameters
num_tosses = 100
num_experiments = 1000

# Run the experiment
experiment_results = coin_toss_experiment(num_tosses, num_experiments)

# Plot the bar graph
plot_bar_graph(experiment_results)
