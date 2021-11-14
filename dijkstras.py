import numpy as np
import sys

def extract_data(file):
    '''
    Extract data from .dat file and create dictionary
    '''

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
        path_start = path[0]
        path_end = path[1]
        weight = path[2]

        network[path_start][path_end]=int(weight)

    return network, total_weight

def dijkstras(network, total_weight, start, end):

    # recreated here to simplify function requirement
    nodes = network.keys()
    size = len(nodes)

    unvisited = dict(zip(nodes,[total_weight]*size))
    unvisited[start] = 0

    solution = unvisited.copy()

    previous = dict(zip(nodes,['']*size))

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
                previous[next] = current

        del unvisited[current]

    path = []

    # by using range iteration it limited iteration to number of visited nodes
    # current will start with end of iteration - should be end node
    for create_path in range(iteration):
        path.append(current)
        if current == start:
            break
        current = previous[current]
        if current == '':
            print('No Path Exists')
            exit()

    path.reverse()
    return path

if __name__ == '__main__':

    name, file, start, end = sys.argv
    network, total_weight = extract_data(file)
    path = dijkstras(network, total_weight ,start,end)
    for node in path:
        print(node)
