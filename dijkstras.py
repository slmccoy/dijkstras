import numpy as np

file = 'dijkstras_example.dat'

file_data = np.genfromtxt(file,dtype = [
    ('start','<U10'),
    ('end','<U10'),
    ('weight','<i8')
])

#Split file data into lists (rather than tuples) inside a list - for indexing
data = np.array([list(path) for path in file_data])

total_weight = sum([int(weight) for weight in data[:,2]])

nodes = set() # as we do not want duplicates
nodes.update(data[:,0],data[:,1])
size = len(nodes)

# create nested dictionary
network = dict(zip(nodes,[{} for _ in range(size)]))

# populate nested dictionary with weights
for path in data:
    start = path[0]
    end = path[1]
    weight = path[2]

    network[start][end]=int(weight)

'''
Dijkstras
'''

start = 'A'
end = 'F'

unvisited = dict(zip(nodes,[total_weight]*size))
unvisited[start] = 0

solution = unvisited.copy()

# max iterations is one per node
for iteration in range(size):

    # get minimum distance of unvisited to select next node
    current = min(unvisited, key = unvisited.get)

    # to avoid unnecessary loops
    if current == end:
        break

    current_distance = solution[current]

    # create list of connected nodes
    connected = network[current]

    for next in connected.keys():
        if next not in unvisited.keys():
            continue

        weight = connected[next]

        proposed_distance = current_distance + weight
        # if the new distance is less than previous - update distance
        if proposed_distance < solution[next]:
            solution[next] = proposed_distance
            unvisited[next] = proposed_distance

    del unvisited[current]

print(solution)
