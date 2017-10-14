from math import sqrt

class Node:
    def __init__(self, cords, parent=None):
        self.parent=parent
        self.cords=cords
        self.f=0

    def __eq__(self, other):
        return self.cords == other.cords

    def addNs(self, int length, blocked):
        neighbors = []
        if self.cords[0] < length:
            if blocked[self.cords[0]+1][self.cords[1]] != '-':
                neighbors.append(Node([self.cords[0]+1, self.cords[1]], parent=self))
        if self.cords[0] > 0:
            if blocked[self.cords[0]-1][self.cords[1]] != '-':
                neighbors.append(Node([self.cords[0]-1, self.cords[1]], parent=self))
        if self.cords[1] < length:
            if blocked[self.cords[0]][self.cords[1]+1] != '-':
                neighbors.append(Node([self.cords[0], self.cords[1]+1], parent=self))
        if self.cords[1] > 0:
            if blocked[self.cords[0]][self.cords[1]-1] != '-':
                neighbors.append(Node([self.cords[0], self.cords[1]-1], parent=self))
        return neighbors

    def setF(self, f):
        self.f = f

def getHeuristic(cC, eC):
    a = (abs(cC[0] - eC[0]) + 1) ** 2
    b = (abs(cC[1] - eC[1]) + 1) ** 2
    return 10 * sqrt(a + b)

def addNeighbors(node, mapLength, closedset, openset, end, route):
    potentialNeighours = node.addNs(mapLength, route)
    for i in potentialNeighours:
        if isClosedset(i, closedset, openset):
            potentialNeighours.remove(i)
    if potentialNeighours:
        openset.extend(potentialNeighours)
    # get total score
    for i in openset:
        i.setF(getHeuristic(i.cords, end.cords))

cdef isClosedset(node, closedset, openset):
    for i in closedset:
        if i == node:
            return True
    for i in openset:
        if i == node:
            return True
    return False

def nextMove(openset, closedset):
    cdef int lowestF = 9999999999
    lowestNode = None
    for node in openset:
        if node not in closedset:
            tmp = node.f
            if tmp < lowestF:
                lowestF = tmp
                lowestNode = node
    return lowestNode

def getDirection(prev, next):
    for i in range(2):
        if prev[i] != next[i]:
            if i == 0:
                if prev[i] > next[i]:
                    return "w"
                else:
                    return "s"
            else:
                if prev[i] > next[i]:
                    return "a"
                else:
                    return "d"

def getPath(node, end):
    fk = node
    path = []
    answer = ""
    while fk.parent != None:
        path.append(fk.parent.cords)
        fk = fk.parent
    path.reverse()
    path.append(end.cords)
    for i in range(len(path)-1):
        answer += getDirection(path[i], path[i+1])
    return answer