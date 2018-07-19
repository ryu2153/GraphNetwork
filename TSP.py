import numpy as np
import itertools
import time
from Graph import Graph


class TSP:

    @staticmethod
    def executeCompleteEnumeration(graph:Graph, repeat = 3) -> float :
        arr = np.arange(graph.N)
        permutation = list((itertools.permutations(arr)))  # 順列

        perSize = len(permutation) #列挙数
        checkSize = int(perSize / graph.N) #走査数
        print("N = " + str(graph.N))
        print("列挙数:" + str(perSize))
        print("走査数:" + str(checkSize))

        minPathCost = 10000
        minPathIndex = 0

        starttime = time.time()
        for r in range(repeat):
            for index in range(checkSize):
                pathCost = graph.getCost(permutation[index])

                if (minPathCost > pathCost):
                    minPathCost = pathCost
                    minPathIndex = index

        aveTime = (time.time() - starttime) / repeat

        print("～完全列挙法～")
        print("最小コスト:" + str(minPathCost))
        print("最小経路:" + str(permutation[minPathIndex]))
        print("N=" + str(graph.N) + " repeat=" + str(repeat))
        print("平均処理時間:" + str(aveTime))

        return aveTime

    @staticmethod
    def executeNearestAddition(graph:Graph, repeat = 3) -> float:
        print("～Nearest Addition法～")

        calcTime = 0.0
        partialPath = []
        partialPath.append(0) #部分閉路

        yetTown = list(range(graph.N))
        for pa in partialPath:
            yetTown.remove(pa)

        while(len(partialPath) < graph.N):
            print("partialPath " + str(partialPath))
            print("yetTown " + str(yetTown))

            minDistance = 10000
            townJ = 0
            townK = 0
            for j in partialPath:
                for k in yetTown:
                    if(minDistance > graph.weight[j][k]):
                        minDistance = graph.weight[j][k]
                        townJ = j
                        townK = k
            print("townJ:" + str(townJ) + " townK:" + str(townK))
            if( townJ == 0 ):
                partialPath.append(townK)
            else:
                partialPath.insert(partialPath.index(townJ)-1,townK)
            yetTown.remove(townK)

            print("Cost:{} newPath:{} \n".format(graph.getCost(partialPath), partialPath))

        return calcTime
        

