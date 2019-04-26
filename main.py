from GraphOperations import GraphOperations
from ElasticSearchParser import ElasticSearchParser

if __name__ == '__main__':
    file = open('/home/stergios/Desktop/calls-elasticsearch.txt', 'r')

    es_parser = ElasticSearchParser(file)
    es_parser.reducted_parse()

    graph_operations = GraphOperations()

    classes_edges_tuple = es_parser.get_classes_vertices()
    methods_edges_tuple = es_parser.get_methods_vertices()

    graph_operations.write_gexf(classes_edges_tuple, "/home/stergios/Desktop/class_graph.gexf")
    graph_operations.write_gexf(methods_edges_tuple, "/home/stergios/Desktop/methods_graph.gexf")