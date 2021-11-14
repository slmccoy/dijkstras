import unittest
from dijkstras import extract_data, dijkstras

class TestDijkstras(unittest.TestCase):

    file = 'exmouth-links.dat'
    network = {}
    total_weight = 0

    def test_extract_data(self):
        network, total_weight = extract_data(self.file)

        # check if main outputs are of the correct form
        self.assertIsInstance(network, dict)
        self.assertIsInstance(total_weight, int)

        # check it is a nested dictionary and weights are stored as integers
        for path_start in network.keys():
            connections = network[path_start]
            self.assertIsInstance(connections, dict)

            if len(connections) == 0:
                continue

            for path_end in connections.keys():

                weight = network[path_start][path_end]

                self.assertIsInstance(weight, int)

        self.network = network
        self.total_weight = total_weight

    def test_dijkstras(self):
        network = self.network
        total_weight = self.total_weight

        nodes = network.keys()

        # check it is able to produce a path list for any combination of nodes
        for start in nodes:
            for end in nodes:

                path = dijkstras(network, total_weight ,start,end)
                self.assertIsInstance(path, list)

if __name__ == '__main__':
    unittest.main()
