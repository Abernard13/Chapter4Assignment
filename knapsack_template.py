import random
from math import exp

MAX_TRIALS = 100   # iterations per run
INIT_TEMP = 100    # initial temperature
COOLING = 0.95     # cooling rate

Objects = {
    'A': (10, 2),  # (weight, value)
    'B': (6, 3),
    'C': (4, 8),
    'D': (8, 5),
    'E': (9, 5),
    'F': (7, 6)
}

C = 15  # capacity of the bag
Items = list(Objects.keys())
nObjects = len(Objects)

# Value function: return -1 if overweight, else return total value
def Value(state):
    total_weight = 0
    total_value = 0
    for i in range(nObjects):
        if state[i] == 1:  # item is taken
            w, v = Objects[Items[i]]
            total_weight += w
            total_value += v
    if total_weight > C:
        return -1  # illegal state
    return total_value

# Get neighbor: flip one random bit
def get_neighbor(state):
    neighbor = state[:]
    i = random.randrange(nObjects)
    neighbor[i] = 1 - neighbor[i]
    return neighbor

# Simulated Annealing
def simulated_annealing(state):
    current = state
    current_val = Value(current)
    T = INIT_TEMP

    while T > 0.1:  # stop when temperature is low
        for _ in range(MAX_TRIALS):
            neighbor = get_neighbor(current)
            neighbor_val = Value(neighbor)

            if neighbor_val == -1:  # skip illegal states
                continue

            # If better, accept immediately
            if neighbor_val > current_val:
                current = neighbor
                current_val = neighbor_val
            else:
                # Accept worse solution with some probability
                delta = neighbor_val - current_val
                if random.random() < exp(delta / T):
                    current = neighbor
                    current_val = neighbor_val

        # decrease temperature
        T *= COOLING

    return current

# Main random restarts
bestValue = -1
bestState = []
for k in range(40):  # 40 restarts
    state = [random.randrange(2) for _ in range(nObjects)]
    state = simulated_annealing(state)
    v = Value(state)

    if v > bestValue:
        bestValue = v
        bestState = state

print('Best state found:', bestState, 'with total value:', bestValue)
