import sys

sys.setrecursionlimit(10 ** 5)


def expand(actual, explorados, frontier, obstaculos, limit=45):
    spring = []
    x = actual[0]
    xmin = actual[0] - 1
    xplus = actual[0] + 1

    y = actual[1]
    ymin = actual[1] - 1
    yplus = actual[1] + 1

    if (xmin, y) not in explorados and (xmin, y) not in frontier and xmin >= 0 and (xmin, y) not in obstaculos:
        spring.append((xmin, y))

    if (xmin, yplus) not in explorados and (xmin, yplus) not in frontier and xmin >= 0 and yplus < limit and (xmin, yplus) not in obstaculos:
        spring.append((xmin, yplus))

    if (x, yplus) not in explorados and (x, yplus) not in frontier and yplus < limit and (x, yplus) not in obstaculos:
        spring.append((x, yplus))

    if (xplus, yplus) not in explorados and (xplus, yplus) not in frontier and xplus < limit and yplus < limit and (xplus, yplus) not in obstaculos:
        spring.append((xplus, yplus))

    if (xplus, y) not in explorados and (xplus, y) not in frontier and xplus < limit and (xplus, y) not in obstaculos:
        spring.append((xplus, y))

    if (xplus, ymin) not in explorados and (xplus, ymin) not in frontier and ymin >= 0 and xplus < limit and (xplus, ymin) not in obstaculos:
        spring.append((xplus, ymin))

    if (x, ymin) not in explorados and (x, ymin) not in frontier and ymin >= 0 and (x, ymin) not in obstaculos:
        spring.append((x, ymin))

    if (xmin, ymin) not in explorados and (xmin, ymin) not in frontier and xmin >= 0 and ymin >= 0 and (xmin, ymin) not in obstaculos:
        spring.append((xmin, ymin))

    return spring


def bfs(frontier, meta, explorados,obstaculos):
    if len(frontier) == 0:
        return []
    edo_actual = frontier[0]
    frontier.pop(0)
    explorados.append(edo_actual)

    if edo_actual == meta:
        return explorados
    else:
        off_spring = expand(edo_actual, explorados, frontier, obstaculos)

        frontier += off_spring

    return bfs(frontier, meta, explorados, obstaculos)


def dfs(frontier, meta, explorados, obstaculos):
    if len(frontier) == 0:
        return []
    edo_actual = frontier[0]
    frontier.pop(0)
    explorados.append(edo_actual)

    if edo_actual == meta:
        return explorados
    else:
        off_spring = expand(edo_actual, explorados, frontier, obstaculos)
        for elemento in reversed(off_spring):
            frontier.insert(0, elemento)

    return dfs(frontier, meta, explorados, obstaculos)


def gredy(par1, par2, par3):
    print('Es el metodo gredy')


def a_star(par1, par2, par3):
    print('Es el metodo A*')
