import csv

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

def dijkstra2(graph, initial):
    distToNode = [(initial, 0, initial)]

    notVisited = list(graph.nodes)
    notVisited.remove(initial)

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
        min_value = 99999999
        min_node = None
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

myGraph = Graph()

# Add Nodes
myGraph.add_node("t")
myGraph.add_node("u")
myGraph.add_node("v")
myGraph.add_node("w")
myGraph.add_node("x")
myGraph.add_node("y")
myGraph.add_node("z")

# Add Edges
myGraph.add_edge("z", "x", 8)
myGraph.add_edge("z", "y", 12)
myGraph.add_edge("x", "y", 6)
myGraph.add_edge("y", "t", 7)
myGraph.add_edge("y", "v", 8)
myGraph.add_edge("v", "t", 4)
myGraph.add_edge("x", "w", 6)
myGraph.add_edge("w", "v", 4)
myGraph.add_edge("w", "u", 3)
myGraph.add_edge("v", "u", 3)
myGraph.add_edge("u", "t", 2)

outFile = open("dijkstra solutions.csv", "w")
output = csv.writer(outFile)

# Print Column headings 
print("\t", end="")
colHeading = [""]
for node in myGraph.nodes:
    print("%s\t" % node, end="")
    colHeading.append(node)

output.writerow(colHeading)
print()

pathDict = dict()

# print lines
for srcNode in myGraph.nodes:
    print("%s\t" % srcNode, end="")
    myLine = [srcNode]
    solution = dijkstra2(myGraph, srcNode)
    for node in solution:
        pathDict[node[2][-1]] = node[1]
    for destNode in myGraph.nodes:
        print("%d\t" % pathDict[destNode], end="")
        myLine.append(pathDict[destNode])

    output.writerow(myLine)
    print()

outFile.close()