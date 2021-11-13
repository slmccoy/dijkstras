import numpy as np

file = 'dijkstras_example.dat'

file_data = np.genfromtxt(file,dtype = [
    ('start','<U10'),
    ('end','<U10'),
    ('weight','<i8')
])

#Split file data into lists (rather than tuples) inside a list - for indexing
data = np.array([list(path) for path in file_data])

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

    network[start][end]=weight

print(network)
