import sys

sys.setrecursionlimit(10 ** 5)


def expand(actual, explorados, frontier, obstaculos, dic, limit=45):
    spring = []
    x = actual[0]
    xmin = actual[0] - 1
    xplus = actual[0] + 1

    y = actual[1]
    ymin = actual[1] - 1
    yplus = actual[1] + 1

    if (xmin, y) not in explorados and (xmin, y) not in frontier and xmin >= 0 and (xmin, y) not in obstaculos:
        spring.append((xmin, y))
        dic[(xmin, y)] = actual

    if (xmin, yplus) not in explorados and (xmin, yplus) not in frontier and xmin >= 0 and yplus < limit and (xmin, yplus) not in obstaculos:
        spring.append((xmin, yplus))
        dic[(xmin, yplus)] = actual

    if (x, yplus) not in explorados and (x, yplus) not in frontier and yplus < limit and (x, yplus) not in obstaculos:
        spring.append((x, yplus))
        dic[(x, yplus)] = actual

    if (xplus, yplus) not in explorados and (xplus, yplus) not in frontier and xplus < limit and yplus < limit and (xplus, yplus) not in obstaculos:
        spring.append((xplus, yplus))
        dic[(xplus, yplus)] = actual

    if (xplus, y) not in explorados and (xplus, y) not in frontier and xplus < limit and (xplus, y) not in obstaculos:
        spring.append((xplus, y))
        dic[(xplus, y)] = actual

    if (xplus, ymin) not in explorados and (xplus, ymin) not in frontier and ymin >= 0 and xplus < limit and (xplus, ymin) not in obstaculos:
        spring.append((xplus, ymin))
        dic[(xplus, ymin)] = actual

    if (x, ymin) not in explorados and (x, ymin) not in frontier and ymin >= 0 and (x, ymin) not in obstaculos:
        spring.append((x, ymin))
        dic[(x, ymin)] = actual

    if (xmin, ymin) not in explorados and (xmin, ymin) not in frontier and xmin >= 0 and ymin >= 0 and (xmin, ymin) not in obstaculos:
        spring.append((xmin, ymin))
        dic[(xmin, ymin)] = actual

    return spring


def expand2(actual, explorados, frontier, obstaculos, dic, limit=45):
    spring = []
    x = actual.x
    xmin = actual.x - 1
    xplus = actual.x + 1

    y = actual.y
    ymin = actual.y - 1
    yplus = actual.y + 1

    if Nodo(xmin, y) not in explorados and Nodo(xmin, y) not in frontier and xmin >= 0 and Nodo(xmin, y) not in obstaculos:
        spring.append(Nodo(xmin, y))
        dic[Nodo(xmin, y).convertir_a_tupla()] = actual

    if Nodo(xmin, yplus) not in explorados and Nodo(xmin, yplus) not in frontier and xmin >= 0 and yplus < limit and Nodo(xmin, yplus) not in obstaculos:
        spring.append(Nodo(xmin, yplus))
        dic[Nodo(xmin, yplus).convertir_a_tupla()] = actual

    if Nodo(x, yplus) not in explorados and Nodo(x, yplus) not in frontier and yplus < limit and Nodo(x, yplus) not in obstaculos:
        spring.append(Nodo(x, yplus))
        dic[Nodo(x, yplus).convertir_a_tupla()] = actual

    if Nodo(xplus, yplus) not in explorados and Nodo(xplus, yplus) not in frontier and xplus < limit and yplus < limit and Nodo(xplus, yplus) not in obstaculos:
        spring.append(Nodo(xplus, yplus))
        dic[Nodo(xplus, yplus).convertir_a_tupla()] = actual

    if Nodo(xplus, y) not in explorados and Nodo(xplus, y) not in frontier and xplus < limit and Nodo(xplus, y) not in obstaculos:
        spring.append(Nodo(xplus, y))
        dic[Nodo(xplus, y).convertir_a_tupla()] = actual

    if Nodo(xplus, ymin) not in explorados and Nodo(xplus, ymin) not in frontier and ymin >= 0 and xplus < limit and Nodo(xplus, ymin) not in obstaculos:
        spring.append(Nodo(xplus, ymin))
        dic[Nodo(xplus, ymin).convertir_a_tupla()] = actual

    if Nodo(x, ymin) not in explorados and Nodo(x, ymin) not in frontier and ymin >= 0 and Nodo(x, ymin) not in obstaculos:
        spring.append(Nodo(x, ymin))
        dic[Nodo(x, ymin).convertir_a_tupla()] = actual

    if Nodo(xmin, ymin) not in explorados and Nodo(xmin, ymin) not in frontier and xmin >= 0 and ymin >= 0 and Nodo(xmin, ymin) not in obstaculos:
        spring.append(Nodo(xmin, ymin))
        dic[Nodo(xmin, ymin).convertir_a_tupla()] = actual

    return spring


def bfs(frontier, meta, explorados,obstaculos, dic):
    if len(frontier) == 0:
        return []
    edo_actual = frontier[0]
    frontier.pop(0)
    explorados.append(edo_actual)

    if edo_actual == meta:
        return explorados
    else:
        off_spring = expand(edo_actual, explorados, frontier, obstaculos, dic)

        frontier += off_spring

    return bfs(frontier, meta, explorados, obstaculos, dic)


def dfs(frontier, meta, explorados, obstaculos, dic):
    if len(frontier) == 0:
        return []
    edo_actual = frontier[0]
    frontier.pop(0)
    explorados.append(edo_actual)

    if edo_actual == meta:
        return explorados
    else:
        off_spring = expand(edo_actual, explorados, frontier, obstaculos, dic)
        for elemento in reversed(off_spring):
            frontier.insert(0, elemento)

    return dfs(frontier, meta, explorados, obstaculos, dic)


def calc_distancia(celda, meta):
    return round(((celda[0]-meta[0])**2+(celda[1]-meta[1])**2)**0.5, 2)


def eval(off, meta):
    result = []
    for element in off:
        result.append([calc_distancia(element, meta), element])
    return result


def greedy(frontier, explorados, meta, obstaculos, dic):
    if len(frontier) == 0:
        return []
    edo_actual = frontier[0]
    frontier.pop(0)
    explorados.append(edo_actual)

    if edo_actual == meta:
        return explorados
    else:
        off = expand(edo_actual, explorados, frontier, obstaculos, dic)
        off = eval(off, meta)
        off = sorted(off)
        if len(off) > 0:
            frontier.append(off[0][1])

    return greedy(frontier, explorados, meta, obstaculos, dic)


def calc_distancia_diagonal(actual, meta):
    return max(abs(actual[0]-meta[0]), abs(actual[1]-meta[1]))


def heuristics(a, b):
    return ((a.x - b.x)**2 + abs(a.y - b.y)**2)**0.5


def a_star(openSet, closeSet, meta, obstaculos, dic):
    explorados = []
    current = []
    while True:
        if len(openSet) == 0:
            return []
        if len(openSet) > 0:
            winner = 0
            for i in range(len(openSet)):
                if openSet[i].f < openSet[winner].f:
                    winner = i

            current = openSet[winner]

            if current == meta:
                temp = current
                while temp.prev:
                    explorados.append(temp.prev)
                    temp = temp.prev
                return explorados

            openSet.remove(current)
            closeSet.append(current)

            for neighbor in expand2(current, explorados, openSet, obstaculos, dic):
                tempG = current.g + 1

                newPath = False
                if neighbor in openSet:
                    if tempG < neighbor.g:
                        neighbor.g = tempG
                        newPath = True
                else:
                    neighbor.g = tempG
                    newPath = True
                    openSet.append(neighbor)

                if newPath:
                    neighbor.h = heuristics(neighbor, meta)
                    neighbor.f = neighbor.g + neighbor.h
                    neighbor.prev = current


class Nodo:
    def __init__(self, i, j):
        self.x, self.y = i, j
        self.f, self.g, self.h = 0, 0, 0
        self.prev = None

    def __eq__(self, nodo):
        return self.x == nodo.x and self.y == nodo.y

    def convertir_a_tupla(self):
        return (self.x, self.y)
