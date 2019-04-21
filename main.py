from GraphOperations import GraphOperations
from Parser import Parser


if __name__ == '__main__':
    file = open('/home/stergios/Desktop/callgraph-out.txt', 'r')

    parser = Parser()
    graph_ops = GraphOperations()

    vertexes_for_classes = parser.parse(file)

    # Graph initialization
    graph_ops.make_graph(vertexes_for_classes)

    print("Betweenness Centrality: \n")
    graph_ops.betweenness_centrality()

    print('\n The 10 highest degree nodes are: \n')
    # prints 10 highest degree nodes
    graph_ops.vertexes_degree()

    print('\n Modularity of graph: \n')
    graph_ops.modularity()

    # TO DO
    # parser.graph_for_methods()
    # parser.graph_for_just_project()

