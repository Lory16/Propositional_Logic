"""
START: 09/03/21
FORMALISM
---type_logic
    CON: connective (in CONNECTIVES)
    VAR: variable
"""
CONNECTIVES = ('and', 'or', 'imp', 'co', 'not')

class Node(object):
    "Represents a node. Each node has: id, name ('and', 'A'...), type_logic"
    def __init__(self, id, name):
        """
        initalize the node with:
        -id, int
        -name, str
        -type_logic: CON or VAR
        """
        self.id = id
        # TODO: for now it accept only A-Z as variable
        assert name in CONNECTIVES or (ord('A') <= ord(name) <= ord('Z'))
        self.name = name
        if name in CONNECTIVES:
            # it's a connective
            self.type_logic = 'CON'
        else:
            # it's a variable
            self.type_logic = 'VAR'

    def __str__(self):
        return '(' + str(self.id) + ', ' + str(self.name) + ', ' + str(self.type_logic) + ')'

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_type_logic(self):
        return self.type_logic
    
    def __eq__(self, other):
        return (self.name == other.name and self.type_logic == other.type_logic)
    
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return self.id.__hash__()


class Edge(object):
    """Represents an edge from a node to another, with a certain weight"""
    def __init__(self, src, dest, weight = 1):
        """
        they are the ids of src and dest:
        -src, int
        -dest, int
        """
        assert src.get_type_logic() != dest.get_type_logic() or dest.get_name() == 'not'
        self.src = src
        self.dest = dest
        self.weight = weight

    def get_src(self):
        return self.src

    def get_dest(self):
        return self.dest

    def get_weight(self):
        return self.weight
    
    def set_weight(self, value):
        self.weight = value

    def __str__(self):
        return '{} -> {}'.format(self.get_src(), self.get_dest())

class Digraph(object):
    """Represents a directed graph of Node and Edge objects"""
    def __init__(self):
        # set made of all nodes of the digraph
        self.nodes = set([])
        # dictionary with the shape: Node -> [list of edges]
        self.edges = {}

    def __str__(self):
        output = '____________________\nDIGRAPH:\n'
        for node in self.edges.keys():
            output += 'NODE '+'('+str(node.get_id())+', '+node.get_name()+', '+node.get_type_logic()+')''\n'
            for edge in self.edges[node]:
                dest = edge.get_dest()
                output += str(node)+' -> '+str(dest)+'\n'
            output += '\n'
        output += '____________________'
        return output

    def add_node(self, node):
        """Adds a Node object to the Digraph. Raises a ValueError if it is
        already in the graph."""
        if node in self.nodes:
            raise ValueError('Node already in the Digraph')
        # the set of nodes is a set, so I use add
        self.nodes.add(node)
        # creating a void list associated to the node (for the future,
        # when I'll have edges to add)
        self.edges[node] = []
    
    def add_edge(self, edge):
        """Adds an Edge instance to the Digraph. Raises a
        ValueError if either of the nodes associated with the edge is not
        in the  graph."""
        # NOTE you need to have both nodes before adding their edge
        if edge.get_src() not in self.nodes or edge.get_dest() not in self.nodes:
            raise ValueError('No node in the digraph matches this edge')
        self.edges[edge.get_src()].append(edge)

# testing Node class
example1 = Node(1, 'and')
example2 = Node(2, 'A')
print(example1)
print(example2)
print(example1 == example2)
# testing Edge class
edge12 = Edge(example1, example2)
print(edge12)
# testing Digraph class
test_digraph = Digraph()
test_digraph.add_node(example1)
test_digraph.add_node(example2)
test_digraph.add_edge(edge12)
print(test_digraph)