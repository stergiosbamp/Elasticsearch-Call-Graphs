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
