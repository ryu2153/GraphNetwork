from Graph import Graph
from TSP import TSP

N = 10
repeat = 10

allGraph = Graph("graph100.txt")
townGraph = allGraph.pickAdjacent(range(N))
townGraph.printWeight()
# TSP.executeCompleteEnumeration(townGraph, repeat)
TSP.executeNearestAddition(townGraph)
