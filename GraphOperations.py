import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.community import greedy_modularity_communities


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

    def make_graph(self, vertex_list):
        for pair in vertex_list:
            self.connect_edges(pair[0], pair[1])

    def vertexes_degree(self):
        node_dict = {node: degree for (node, degree) in self.graph.degree}
        print(sorted(node_dict.items(), key=lambda p: p[1], reverse=True)[0:10])

    def modularity(self):

        print('\n There are ' + len(greedy_modularity_communities(self.graph)).__str__() + ' communities \n')

        for community in greedy_modularity_communities(self.graph):
            print(set(community))

    def write_gexf(self, vertex_tuple):
        self.make_graph(vertex_tuple)
        return nx.write_gexf(self.graph, "/home/stergios/Desktop/MyGephiData.gexf")

    def info_for_graph(self, vertex_tuple):

        # Construct the graph from the given list
        self.make_graph(vertex_tuple)

        print("Betweenness Centrality: \n")
        self.betweenness_centrality()

        print('\n The 10 highest degree nodes are: \n')
        # prints 10 highest degree nodes
        self.vertexes_degree()

        print('\n Modularity of graph: \n')
        self.modularity()
