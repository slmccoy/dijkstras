import time
from dijkstras import extract_data, dijkstras

file_path = 'exmouth-links.dat'

'''
Check run time for 'extract_data'
'''

start_time = time.time()
network, total_weight = extract_data(file_path)
import_time = time.time() - start_time

print(f'Time for data extract file: {import_time} seconds')


'''
Check runtime for 'dijkstras'
'''

nodes = network.keys()
max_time = 0
max_nodes = []

# checking every combination of start and end node
for start in nodes:
    for end in nodes:

        start_time = time.time()
        path = dijkstras(network, total_weight ,start,end)
        run_time = time.time() - start_time

        if run_time > max_time:
            max_time = run_time
            max_nodes = [start, end]

print(f'Max time for Dijkstras: {max_time} seconds')


'''
Check full runtime including printing
'''
# use max combination only
start = max_nodes[0]
end = max_nodes[1]

start_time = time.time()
path = dijkstras(network, total_weight ,start,end)
for node in path:
    print(node)

full_runtime = import_time + time.time() - start_time

print(f'Total time including printing path: {full_runtime} seconds')
