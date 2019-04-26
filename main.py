# from ClassesParser import ClassesParser
# from GraphOperations import GraphOperations
# from MethodsParser import MethodsParser
# from Parser import Parser

from DadParser import DadParser

if __name__ == '__main__':
    file = open('/home/stergios/Desktop/callgraph-out.txt', 'r')

    # parser = Parser()
    # graph_ops = GraphOperations()
    #
    # vertexes_for_classes = parser.parse(file)
    # graph_ops.info_for_graph(vertexes_for_classes)


    ## TESTING

    dad = DadParser(file)
    dad.parse()

    # class_parser = ClassesParser(file)
    # methods_parser = MethodsParser(file)
    # class_parser.show_data()
    # methods_parser.show_data()

    # dad.show_data_for_classes()

    dad.make_gephi_data()

    print("\n ****************** Methods Graph **************** \n")



    # Takes much time
    # dad.show_data_for_methods()




