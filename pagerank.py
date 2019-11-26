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
    curr = iter
    r = 1.0 - dp
    neighbors = n.map(lambda node: (str(node.name), node.neighbors))
    while curr > 0:
        print('ITERATION: ' + str(iter - curr))
        contribs = n.flatMap(lambda node: list(map(lambda ne: (str(ne), node.rank / len(node.neighbors)), node.neighbors)))
        new_ranks = contribs.reduceByKey(lambda a, b: a + b).mapValues(lambda acc: r + dp * acc)
        n = new_ranks.fullOuterJoin(neighbors).map(lambda node: Node(int(node[0]), node[1][1], node[1][0] if node[1][0] else r))
        curr -= 1
    n = n.collect()
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
