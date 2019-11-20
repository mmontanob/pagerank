import argparse


def read_args():
    """
    Reads the arguments from command line
    :return: Input filename, Output filename
    """
    parser = argparse.ArgumentParser(description='Execute Page Rank on input file.')
    parser.add_argument('--input', help='Name of the input file', default='input')
    parser.add_argument('--output', help='Name of the output file', default='output')
    args = parser.parse_args()
    return args.input, args.output


def read_input(filename):
    """
    Reads the input file and parse it to internal structs
    :param filename: Name of the input file
    :return: Nodes for the page rank algorithm
    """
    pass


def write_output(filename):
    """
    Writes the output file
    :param filename: Name of the output file
    """
    pass
