import random

MAX_TRIALS = 100

# Distance matrix
tsp = [[0, 400, 500, 300],
       [400, 0, 300, 500],
       [500, 300, 0, 400],
       [300, 500, 400, 0]]

cities = len(tsp)

# Value function: total distance of the route including return to start
def Value(state):
    total = 0
    for i in range(len(state) - 1):
        total += tsp[state[i]][state[i + 1]]
    # add return to start city
    total += tsp[state[-1]][state[0]]
    return total

# Generate neighbor by swapping two random cities (except keep city 0 fixed if required)
def get_neighbor(state):
    neighbor = state[:]
    i, j = random.sample(range(1, len(state)), 2)  # don’t swap the starting city 0
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
    return neighbor

# Hill climbing algorithm
def hill_climbing(state):
    current = state
    current_val = Value(current)
    for _ in range(MAX_TRIALS):
        neighbor = get_neighbor(current)
        neighbor_val = Value(neighbor)
        if neighbor_val < current_val:  # move if better
            current = neighbor
            current_val = neighbor_val
    return current

# Random-restart hill climbing
best_state = []
best_dist = float("inf")

for k in range(20):  # 20 restarts
    state = list(range(cities))
    random.shuffle(state[1:])  # fix city 0 at start, shuffle others
    state = hill_climbing(state)
    v = Value(state)
    if best_dist > v:
        best_dist = v
        best_state = state

print("Best route:", best_state, "with distance:", best_dist)
