import argparse
from structs import Node


def read_args():
    """
    Reads the arguments from command line
    :return: Parsed arguments
    """
    parser = argparse.ArgumentParser(description='Execute Page Rank on input file.')
    parser.add_argument('--input', help='Name of the input file', default='input')
    parser.add_argument('--output', help='Name of the output file', default='output')
    parser.add_argument('--dp', help='Damping factor', default=0.75, type=float)
    parser.add_argument('--iter', help='Max Iterations', default=1, type=int)
    return parser.parse_args()


def read_input(filename):
    """
    Reads the input file and parse it to internal structs
    :param filename: Name of the input file
    :return: Nodes for the page rank algorithm
    """
    first_line = True
    num_of_nodes = 0
    counter = 0
    nodes = []
    with open(filename) as file:
        for line in file:
            if first_line:
                num_of_nodes = int(line)
                for i in range(num_of_nodes):
                    nodes.append(Node(str(i)))
                first_line = False
                continue
            elif num_of_nodes == counter:
                break
            else :
                neighbors = map(lambda x: int(x)-1, line.split())
                nodes[counter].add_neighbors(neighbors)
                counter += 1
    for node in nodes:
        print(f"{node.name}, neig: {node.neighbors}\n")
    return nodes


def write_output(filename, results):
    """
    Writes the output file
    :param filename: Name of the output file
    :param results: pagerank results
    """
    with open(filename, 'w+') as output:
        for r in results:
            output.write(str(r.rank) + '\n')
        output.close()
