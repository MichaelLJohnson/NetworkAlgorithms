# Graph Class originally written by econchick
class Graph:

    # Constructor
    def __init__(self):
        self.nodes = list()
        self.edges = dict()
        self.distance = dict()

    # Add a node (Through it's label) to the graph
    def add_node(self, value):
        self.nodes.append(value)

    # Add a Bidirectional Edge to the Graph
    def add_edge(self, from_node, to_node, distance):

        # Connect the two nodes
        self.edges[from_node] = to_node
        self.edges[to_node] = from_node

        # Add the edge distance to distance dictionary
        self.distance[(from_node, to_node)] = distance
        self.distance[(to_node, from_node)] = distance


def dijkstra(graph, source):
    ## dijkstra: a function that runs dijkstra's algorithm for the given graph and source node
    # @graph: the graph to implement dijkstra's algorithm on
    # @source: the source node for dijkstra's algorithm


    ## Initialize variables

    # Solution List (Node, Distance to Source, Path)
    distToNode = [(source, 0, source)]
    
    # Nodes left to visit
    notVisited = list(graph.nodes)
    notVisited.remove(source)

    # Calculate Maximum Possible Distance for the graph
    MAX_DISTANCE = 0
    for arc in graph.distance:
        MAX_DISTANCE += graph.distance[arc]
    MAX_DISTANCE /= 2                           # This is as the arcs are bidirectional 


    # Run while there are nodes in notVisited
    while notVisited:

        # Initialize the table of nodes and distance to node
        table = dict()

        # Make dictionary of notVisted nodes and shortest path to source
        for prevNode, distance, path in distToNode:
            for node in notVisited:
                if (prevNode, node) in graph.distance:
                    if (node in table) and (table[node] != None) :
                        if distance + graph.distance[(prevNode, node)] > table[node][0]:
                            continue
                    table[node] = (distance + graph.distance[(prevNode, node)], path)
                elif node not in table:
                    table[node] = None

        # Initialize the minimum distance 
        min_distance = MAX_DISTANCE
        min_node = None

        # Find min distance to src
        for node in table:
            if (table[node] != None):
                if (table[node][0] < min_distance):
                    min_node = node
                    min_distance = table[min_node][0]

        # Add min distance / node to distanceTo Node dict
        distToNode.append((min_node, table[min_node][0], table[min_node][1]+min_node))

        # remove node from notVisted
        notVisited.remove(min_node)

        # Repeat while notVisted is not empty
      
    # Return the solution (list of tuples)
    return distToNode

