from GraphOperations import GraphOperations


class Parser:

    def __init__(self, f):
        self.file = f

        # Those list initializing again when calling children classes
        # and are empty although in begging they are ok

        self.connected_edges_classes = []
        self.connected_edges_methods = []

        # self.connected_edges_project = []

        self.graph_ops = GraphOperations()

    # Having the edges of each category as an attribute
    # it doesn't need to iterate through the whole list again
    # at children classes. I have the lists ready by iterating once.

    def parse(self):
        for line in self.file:
            if line[0] == 'C':
                vertex_one, vertex_two = line[2:].strip().split(' ') # skip first 2 char which are "C:" and take the remaining which is clean
                self.connected_edges_classes.append((vertex_one, vertex_two))
            if line[0] == 'M':
                # example of line:
                # M:javassist.bytecode.analysis.MultiArrayType:isAssignableTo(javassist.bytecode.analysis.Type) (M)javassist.bytecode.analysis.Type:getCtClass()

                dirty_vertex_one, dirty_vertex_two = line.strip().split(' ')
                clean_vertex_one = dirty_vertex_one[2:]
                clean_vertex_two = dirty_vertex_two[3:]
                self.connected_edges_methods.append((clean_vertex_one, clean_vertex_two))

    def reducted_parse(self):
        for line in self.file:
            if line[0] == 'C':
                vertex_one, vertex_two = line[2:].strip().split(' ')  # skip first 2 char which are "C:" and take the remaining which is clean
                if self.is_in_project(vertex_one, vertex_two):
                    self.connected_edges_classes.append((vertex_one, vertex_two))

            if line[0] == 'M':
                dirty_vertex_one, dirty_vertex_two = line.strip().split(' ')

                # Line example:

                # M:org.elasticsearch.rest.action.cat.RestIndicesAction:buildTable(org.elasticsearch.rest.RestRequest,org.elasticsearch.index.Index[],org.elasticsearch.action.admin.cluster.health.ClusterHealthResponse,org.elasticsearch.action.admin.indices.stats.IndicesStatsResponse,org.elasticsearch.cluster.metadata.MetaData) (M)org.elasticsearch.action.admin.indices.stats.CommonStats:getSearch()

                clean_vertex_one = dirty_vertex_one[2:]
                clean_vertex_two = dirty_vertex_two[3:]
                if self.is_in_project(clean_vertex_one, clean_vertex_two):
                    self.connected_edges_methods.append((clean_vertex_one, clean_vertex_two))

    def get_classes_vertices(self):
        return self.connected_edges_classes

    def get_methods_vertices(self):
        return self.connected_edges_methods

    def is_in_project(self, v_one, v_two):
        if "org.elasticsearch" in v_one and "org.elasticsearch" in v_two:
            return True

    def make_gephi_data(self):
        self.graph_ops.write_gexf(self.connected_edges_classes)

    def show_data_for_classes(self):
        self.graph_ops.info_for_graph(self.connected_edges_classes)

    def show_data_for_methods(self):
        self.graph_ops.info_for_graph(self.connected_edges_methods)