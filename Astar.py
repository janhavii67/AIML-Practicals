
from pyamaze import maze, agent
from queue import PriorityQueue


def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1 - x2) + abs(y1 - y2)


def astar(m):
    start = (m.rows, m.cols)
    goal = (1, 1)

    g_score = {cell: float('inf') for cell in m.grid}
    g_score[start] = 0

    f_score = {cell: float('inf') for cell in m.grid}
    f_score[start] = h(start, goal)

    apath = {}
    open_list = PriorityQueue()
    open_list.put((f_score[start], h(start, goal), start))

    while not open_list.empty():
        current_cell = open_list.get()[2]

        if current_cell == goal:
            break

        for d in "EWNS":
            if m.maze_map[current_cell][d]:

                if d == 'E':
                    childcell = (current_cell[0], current_cell[1] + 1)
                elif d == 'W':
                    childcell = (current_cell[0], current_cell[1] - 1)
                elif d == 'S':
                    childcell = (current_cell[0] + 1, current_cell[1])
                elif d == 'N':
                    childcell = (current_cell[0] - 1, current_cell[1])

                temp_g_score = g_score[current_cell] + 1

                if temp_g_score < g_score[childcell]:
                    g_score[childcell] = temp_g_score
                    f_score[childcell] = (
                        temp_g_score + h(childcell, goal)
                    )

                    apath[childcell] = current_cell


                    open_list.put((
                        f_score[childcell],
                        h(childcell, goal),
                        childcell
                    ))

    # Check whether the goal was reached
    if goal != start and goal not in apath:
        print("No path found!")
        return {}

    # Convert parent mapping into forward path
    fwdPath = {}
    cell = goal

    while cell != start:
        parent = apath[cell]
        fwdPath[parent] = cell
        cell = parent

    return fwdPath


# Create maze``
m = maze(5, 5)
m.CreateMaze()

# Find path using A*
path = astar(m)

if path:
    a = agent(m, footprints=True, color='yellow')
    m.tracePath({a: path}, delay=200)
else:
    print("Path is empty. Agent cannot move.")

m.run()
