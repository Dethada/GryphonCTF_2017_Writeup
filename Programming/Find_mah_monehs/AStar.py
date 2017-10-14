#!/usr/bin/python
#from Node import *
from Node import *
from pwn import *
import time, os

c = remote("prog.chal.gryphonctf.com", 17454)
reply = c.recv(timeout=11)
c.send('y\n\r')
chars = set(['-', '+', '@', '$'])
roundz = 1
while roundz < 101:
    print "round: {}".format(roundz)
    openset = []
    closedset = []
    blocked = []
    start = None
    end = None
    try:
        reply = c.recvuntil('>', timeout=11)
    except Exception:
        reply = c.recv()
        print reply
        break
    lines = reply.splitlines()
    route = []
    for i,line in enumerate(lines):
        z = []
        for j,char in enumerate(line):
            if char in chars:
                z.append(char)
        if z and len(z) != 1:
            route.append(z)
    mapLength = len(route)
    # store start and end
    for i in range(mapLength):
        for j in range(mapLength):
            if route[i][j] == "@":
                start = Node(cords=[i,j])
                closedset.append(start)
            elif route[i][j] == "$":
                end = Node(cords=[i,j])
    # route[row][column]
    prevNodeCords = start.cords
    addNeighbors(start, mapLength-1, closedset, openset, end, route)
    currentNode = None
    while openset:
        currentNode = nextMove(openset, closedset)
        addNeighbors(currentNode, mapLength-1, closedset, openset, end, route)
        #print str(currentNode.cords) #+ " " + getDirection(prevNodeCords, currentNode.cords)
        if currentNode.cords == end.cords:
            break
        for i in openset:
            if i.cords == currentNode.cords:
                openset.remove(i)
                break
        closedset.append(currentNode)

    answer = getPath(currentNode, end)
    c.send(answer)
    roundz+=1

reply = c.recvuntil("}", timeout=11)
print reply
print "Exited gracefully"
c.close()
