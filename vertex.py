# Define the vertex for the graph
class Vertex:
    """
    Define the vertex for the graph, eg:
    id = "V0"
    adj = {V1 : 5, V5 : 2}
    """

    def __init__(self, key):
        self.id = key
        self.connectTo = {}

    def add_neighbor(self, nbr, weight=0):
        self.connectTo[nbr] = weight

    def get_connections(self):
        return self.connectTo.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connectTo[nbr]

    def __str__(self):
        return str(self.id) + ' connectTo: ' + str([x.id for x in self.connectTo])
