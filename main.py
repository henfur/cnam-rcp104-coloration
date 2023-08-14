import numpy as np

def readGraph(path) -> list:
    print("Reading graph...")
    rowCount = 0
    columnCount = 0
    edges = []
    with open(path) as matrixFile:
        for line in matrixFile:
            splittedLine = line.split()
            if(splittedLine[0] == "c"):
                continue
            elif(splittedLine[0] == "p"):
                rowCount = int(splittedLine[2])
                columnCount = int(splittedLine[3])
            else:

                edges.append([splittedLine[1], splittedLine[2]])
    
    graph = np.zeros((rowCount, columnCount))
    for e in edges:
        graph[int(e[0]) - 1][int(e[1]) - 1] = 1
        graph[int(e[1]) - 1][int(e[0]) - 1] = 1

    return graph

def getOrder(graph) -> dict:
    print("Getting order...")
    rowCount = len(graph)
    columnCount = len(graph[0])

    order = {}

    for i in range(rowCount):
        neighbourCount = 0
        for j in range(columnCount):
            if graph[i][j] == 1:
                neighbourCount += 1
        order[str(i)] = neighbourCount
    
    return(list(dict(sorted(order.items(), key=lambda item: item[1], reverse=True)).keys()))


def getNeighbours(graph, vertex):
    neighbours = []
    for index in range(len(graph[vertex])):
        if graph[vertex][index] == 1:
            neighbours.append(index)
    return neighbours

# def dSaturColoration(graph) -> list:
#     affectedColors = [0] * len(graph)

#     order = getOrder(graph)

#     for vertex in order:
#         if affectedColors[int(vertex)] == 0:
#             if affectedColors.count(1) == 0:
#                 affectedColors[int(vertex)] = 1
#             else:
#                 neighbours = getNeighbours(graph, int(vertex))
#                 if len(neighbours) == 0:
#                     affectedColors[int(vertex)] = 1
#                 else:
#                     minColor = len(graph[0]) + 1
#                     maxColor = -1
#                     for neighbour in neighbours:
#                         if affectedColors[neighbour] != 0 and affectedColors[neighbour] < minColor:
#                             minColor = affectedColors[neighbour]
#                         if affectedColors[neighbour] > maxColor:
#                             maxColor = affectedColors[neighbour]
#                     if minColor > 1:
#                         print("VERTEX : ", vertex)
#                         print(minColor - 1)
#                         affectedColors[int(vertex)] = minColor - 1
#                     else:
#                         affectedColors[int(vertex)] = maxColor + 1
#     return affectedColors

def dSaturColoration(graph) -> list:
    totalColors = list(range(1,len(graph)))
    affectedColors = [0] * len(graph)

    order = getOrder(graph)

    for vertex in order:
        if affectedColors[int(vertex)] == 0:
            if affectedColors.count(1) == 0:
                affectedColors[int(vertex)] = 1
            else:
                neighbours = getNeighbours(graph, int(vertex))
                if len(neighbours) == 0:
                    affectedColors[int(vertex)] = 1
                else:
                    neighbourColors = []
                    for neighbour in neighbours:
                        if affectedColors[neighbour] != 0:
                            neighbourColors.append(affectedColors[neighbour])
                    for color in totalColors:
                        if neighbourColors.count(color) == 0:
                            affectedColors[int(vertex)] = color
                            break
    return affectedColors

def __main__():
    # Reading graphs
    g1 = readGraph("./files/g1.txt")
    g2 = readGraph("./files/g2.txt")
    graphGL = readGraph("./files/inithx.i.1.col")
    graphQuenn = readGraph("./files/mat.tepper.cmu.edu_COLOR_instances_queen11_11.col.txt")

    # Results
    print("===== G1 =====")
    g1Colors = dSaturColoration(g1)
    print("Colors : ", max(g1Colors))
    print(g1Colors)

    print("===== G2 =====")
    g2Colors = dSaturColoration(g2)
    print("Colors : ", max(g2Colors))
    print(g2Colors)

    print("===== GraphGL =====")
    graphGLColors = dSaturColoration(graphGL)
    print("Colors : ", max(graphGLColors))

    print("===== GraphQueen =====")
    graphQueenColors = dSaturColoration(graphQuenn)
    print("Colors : ", max(graphQueenColors))
__main__()