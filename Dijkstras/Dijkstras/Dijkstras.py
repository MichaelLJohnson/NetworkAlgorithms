# Graph Class written by econchick
class Graph:
  def __init__(self):
    self.nodes = list()
    self.edges = dict()
    self.distance = {}

  def add_node(self, value):
    self.nodes.append(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node] = to_node
    self.edges[to_node] = from_node
    self.distance[(from_node, to_node)] = distance
    self.distance[(to_node, from_node)] = distance


def dijkstra(graph, initial):
    distToNode = [(initial, 0, initial)]

    notVisited = list(graph.nodes)
    notVisited.remove(initial)
    min_value = 0
    min_node = None

    for arc in graph.distance:
        min_value += graph.distance[arc]

    while notVisited:
        table = dict()

        # Make dictionary of notVisted nodes and shortest path to src
        for prevNode, distance, path in distToNode:
            for node in notVisited:
                if (prevNode, node) in graph.distance:
                    if (node in table) and (table[node] != None) :
                        if distance + graph.distance[(prevNode, node)] > table[node][0]:
                            continue
                    table[node] = (distance + graph.distance[(prevNode, node)], path)
                elif node not in table:
                    table[node] = None

        # Find min distance to src
        for node in table:
            if (table[node] != None):
                if (table[node][0] < min_value):
                    min_node = node
                    min_value = table[min_node][0]

        # Add min distance / node to distanceTo Node dict
        distToNode.append((min_node, table[min_node][0], table[min_node][1]+min_node))

        # remove node from notVisted
        notVisited.remove(min_node)

        # Repeat while notVisted is not empty
      
    # Return the list of tuples 
    return distToNode

