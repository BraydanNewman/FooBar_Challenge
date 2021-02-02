import numpy as np


class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def solution(map):
    final_map = []





    for i in range(len(map)):
        map[i].insert(0, 1)
        map[i].insert(len(map[i]), 1)

    l = ["1"] * len(map[0])
    print(l)

    map.insert(0, l)
    map.insert(len(map)+1, l)

    print(np.array(_map))


    start = (1, 1)
    end = (len(map)-2, len(map[0])-2)

    path = astar(map, start, end)
    print(path)

def astar(maze, start, end):
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    open_list = [ ]
    closed_list = [ ]

    open_list.append(start_node)

    while len(open_list) > 0:
        print(len(open_list))
        print(str(len(closed_list)) + "\n")
        current_node = open_list[ 0 ]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node == end_node:
            path = [ ]
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[ ::-1 ]

        children = [ ]
        for new_position in [ (0, -1), (0, 1), (-1, 0), (1, 0)]:

            node_position = (
            current_node.position[ 0 ] + new_position[ 0 ], current_node.position[ 1 ] + new_position[ 1 ])

            if node_position[ 0 ] > (len(maze) - 1) or node_position[ 0 ] < 0 or node_position[ 1 ] > (
                    len(maze[ len(maze) - 1 ]) - 1) or node_position[ 1 ] < 0:
                continue

            if maze[ node_position[ 0 ] ][ node_position[ 1 ] ] != 0:
                continue

            new_node = Node(current_node, node_position)

            children.append(new_node)

        for child in children:
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            child.g = current_node.g + 1
            child.h = ((child.position[ 0 ] - end_node.position[ 0 ]) ** 2) + (
                        (child.position[ 1 ] - end_node.position[ 1 ]) ** 2)
            child.f = child.g + child.h

            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            open_list.append(child)



if __name__ == '__main__':
    _map = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]

    solution(_map)