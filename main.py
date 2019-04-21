from GraphOperations import GraphOperations
from Parser import Parser


if __name__ == '__main__':
    file = open('/home/stergios/Desktop/callgraph-out.txt', 'r')

    parser = Parser()
    graphOps = GraphOperations()

    vertexes_for_classes = parser.parse(file)

    graphOps.make_graph_classes(vertexes_for_classes)
    graphOps.betweenness_centrality()

    # TO DO
    # parser.graph_for_methods()
    # parser.graph_for_just_project()

