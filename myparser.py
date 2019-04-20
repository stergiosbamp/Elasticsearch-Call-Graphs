import networkx as nx
import matplotlib.pyplot as plt


class GraphOperations:

    def __init__(self):
        self.graph = nx.Graph()

    def connect_edges(self, u, v):
        self.graph.add_edge(u, v)

    def draw_graph(self):
        nx.draw(self.graph)
        plt.show()

    def betweenness_centrality(self):
        print(nx.betweenness_centrality(self.graph))

    def make_graph_classes(self, vertex_list):
        for pair in vertex_list:
            self.connect_edges(pair[0], pair[1])


class Parser:
    def __init__(self):
        self.connected_edges = []

    def parse(self, file):
        for line in file:
            if line[0] == 'C':
                print(line[2:]) # skip first 2 char which are "C:" and take the remaining
                vertex_one, vertex_two = line[2:].strip().split(' ')
                self.connected_edges.append((vertex_one, vertex_two))

        return self.connected_edges


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

