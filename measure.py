import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import numpy as np

from kosaraju import kosaraju_algorithm


def generate_input(n, m):
    edges = []
    for i in range(m):
        a = random.randint(0, n - 1)
        b = random.randint(0, n - 1)
        edges.append((a, b))
    return edges


if __name__ == '__main__':
    n_values = range(10, 1000, 10)
    m_values = range(10, 100, 10)
    times = [[] for _ in n_values]
    for i, n in enumerate(n_values):
        for m in m_values:
            edges = generate_input(n, m)
            start = timer()
            kosaraju_algorithm(n, edges)
            end = timer()
            times[i].append(end - start)

    # Calculate average times
    avg_times = [np.mean(t) for t in times]

    # Convert lists to numpy arrays for easier manipulation
    n_values = np.array(n_values)
    avg_times = np.array(avg_times)

    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(n_values, avg_times, label='Average Execution Time')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Time (s)')
    plt.title('Performance of Kosaraju Algorithm')
    plt.legend()
    plt.grid(True)
    plt.show()