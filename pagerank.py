import cmd
from pyspark.sql import SparkSession
from structs import Node


def pagerank(nodes, iter, dp):
    """
    Execute Page Rank algorithm on a collection of nodes
    :param nodes: list of interconnected nodes
    :param iter: number of iterations
    :param dp: damping factor
    :return:
    """
    n = nodes
    for _ in range(iter):
        neighbors = n.map(lambda node: (node.name, node.neighbors))
        contribs = n.flatMap(lambda node: list(node.neighbors.map(lambda ne: (ne, node.rank / len(node.neighbors)))))
        r = 1.0 - dp
        new_ranks = contribs.reduceByKey(lambda a, b: a + b).mapValues(lambda acc: r + dp * acc)
        n = new_ranks.join(neighbors).map(lambda node: Node(node[0], node[1][1], node[1][0]))
    n = n.map(lambda p: p[1]).collect()
    n.sort(key=lambda node: node.name)
    return n


# Read input file
args = cmd.read_args()
nodes = cmd.read_input(args.input)

# Init spark
spark = SparkSession.builder.appName("PageRank").getOrCreate()
nodes = spark.sparkContext.parallelize(nodes)

# Execute Page Rank
results = pagerank(nodes, args.iter, args.dp)

# Generate Output file
cmd.write_output(args.output, results)
