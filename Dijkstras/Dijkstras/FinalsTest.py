import csv
from Dijkstras import dijkstra

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

# 
outFile = open("solutions.csv", "w")
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

# Print Lines to Console
for srcNode in myGraph.nodes:

    # Print Matrix Headers
    print("%s\t" % srcNode, end="")

    # Create a new list for the line, starting with the source node
    myLine = [srcNode]

    # Run Dijkstra's Algorithm for the source node 
    solution = dijkstra(myGraph, srcNode)

    # Add each solution to the path dictionary
    for node in solution:
        pathDict[node[2][-1]] = node[1]

    # 
    for destNode in myGraph.nodes:
        print("%d\t" % pathDict[destNode], end="")
        myLine.append(pathDict[destNode])

    output.writerow(myLine)
    print()

outFile.close()
