import sys
import numpy as np

class Graph:
    edgeList = []
    adjacent = None
    weight = None
    degree = None
    N = 0 # 点の数
    M = 0 # 辺の数
    vertexConnectivity = 0  # 点連結度 κ(G)
    edgeConnectivity = 0    # 辺連結度 λ(G)

    def __init__(self, fileName):
        if type(fileName) == str:
            graphData = open(fileName, "r").readlines()
            self.N = int(graphData[0])
            # print("GraphSize={}".format(self.size))

            #辺の読み込み
            for line in graphData[1:]:
                edge = line[:-1].split(" ")
                edge = list(map(int, edge))  # intに変換
                self.edgeList.append(edge)
            self.M = len(self.edgeList)
            # print(self.edgeList)

            # 隣接行列の作成
            self.adjacent = np.zeros([self.N, self.N], dtype=int)
            self.weight = np.zeros([self.N, self.N], dtype=int)

            for i in range(len(self.edgeList)):
                self.adjacent[self.edgeList[i][0]][self.edgeList[i][1]] += 1
                self.adjacent[self.edgeList[i][1]][self.edgeList[i][0]] += 1
                self.weight[self.edgeList[i][0]][self.edgeList[i][1]] = self.edgeList[i][2]
                self.weight[self.edgeList[i][1]][self.edgeList[i][0]] = self.edgeList[i][2]

        else:
            self.adjacent = fileName
            self.N = len(self.adjacent)
            self.weight = np.zeros([self.N, self.N], dtype=int)


        # 次数の計算
        self.degree = np.sum(self.adjacent, axis=0)
        # print(self.degree)

    # オイラーグラフかどうか
    def isEuler(self):
        for d in self.degree:
            if d % 2 != 0:
                return False
        return True

    #隣接行列の表示
    def printAdjacent(self):
        print("-Adjacent-")
        for r in range(self.N):
            sys.stdout.write("│")
            for c in range(self.N):
                if (c != 0): sys.stdout.write(" ")
                sys.stdout.write(str(self.adjacent[r][c]))
            print("│")

    # 距離行列の表示
    def printWeight(self):
        print("-Weight-")
        for r in range(self.N):
            sys.stdout.write("│")
            for c in range(self.N):
                if (c != 0): sys.stdout.write(" ")
                sys.stdout.write(str("{0:2d}".format(self.weight[r][c])))
            print("│")

    #次数配列の表示
    def printDegree(self):
        print("-Degree-")
        print(self.degree)

    def __calcVertexConnectivity(self):
        print("mu")

    def visit(self, v, yet):
        yet[v] = 0
        for w in range(len(self.adjacent)):
            if self.adjacent[v][w] == 1 and yet[w] == 1:
                self.visit(w, yet)

    # この関数はグラフの連結成分数を返す。
    # すなわち、連結グラフのときには1が、非連結のときには 2以上が返される。
    def connectCheck(self):
        yetToVisit = []
        count = 0
        for i in range(len(self.adjacent)):
            yetToVisit.append(1)

        for i in range(len(self.adjacent)):
            if yetToVisit[i] == 1:
                count += 1
            self.visit( i, yetToVisit)
        return count

    #引数配列の要素のみを取り出す
    def pickAdjacent(self, pickArray):
        pickSize = len(pickArray)
        if self.adjacent.shape[0] < pickSize:
            return None

        pickAdjacent = np.identity(pickSize, dtype=int) #pickの大きさと同じ零行列を作成

        for i in range(pickSize):
            for j in range(pickSize):
                pickAdjacent[i][j] = self.adjacent[pickArray[i]][pickArray[j]]

        pickedGraph = Graph(pickAdjacent)

        for i in range(pickSize):
            for j in range(pickSize):
                pickedGraph.weight[i][j] = self.weight[pickArray[i]][pickArray[j]]

        return pickedGraph

    def getSize(self):
        return self.N

    def getCost(self, routeArray)->int:
        cost = 0
        size = len(routeArray)
        for i in range(size - 1):
            cost += self.weight[routeArray[i]][routeArray[i + 1]]

        #最後の要素から始端まで戻るコスト
        cost += self.weight[routeArray[size - 1]][routeArray[0]]
        return cost

