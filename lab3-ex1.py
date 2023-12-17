# Suppose we have a sequence of occurrences. We assume that the time between occurrences is exponentially distributed with on average there is one occurrence every 10 minutes. You come upon this system at time 100, and wait until the next occurrence. How long, on average, will you have to wait? Test your answer with a simulation. 

import numpy as np
import matplotlib.pyplot as plt

# Parameters
average_time_between_occurrences = 10  # minutes
num_simulations = 100000

# Generate exponentially distributed random variables
wait_times = np.random.exponential(scale=average_time_between_occurrences, size=num_simulations)

# Plot histogram
plt.hist(wait_times, bins=50, density=True, alpha=0.75, color='blue', edgecolor='black')

# Add a vertical line at the average wait time
plt.axvline(np.mean(wait_times), color='red', linestyle='dashed', linewidth=2, label=f'Average Wait Time: {np.mean(wait_times):.9f} minutes')
print(wait_times)
# Add labels and title
plt.xlabel('Wait Time (minutes)')
plt.ylabel('Frequency')
plt.title('Distribution of Wait Times')
plt.legend()

# Show the plot
plt.show()
