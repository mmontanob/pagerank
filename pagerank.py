import cmd
from pyspark.sql import SparkSession


def pagerank(nodes, iter, dp):
    """
    Execute Page Rank algorithm on a collection of nodes
    :param nodes: list of interconected nodes
    :param iter: number of iterations
    :param dp: damping factor
    :return:
    """
    pass


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
