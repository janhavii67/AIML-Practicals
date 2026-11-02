import heapq

# Maze representation
maze = [
    ['S', 0, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 'G']
]

start = (0, 0)
goal = (3, 3)

# Heuristic function
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* Algorithm
def astar(start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))

    g = {start: 0}
    parent = {}

    while open_list:
        f, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1]

        r, c = current

        # Four possible movements
        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            nr, nc = r + dr, c + dc

            if (0 <= nr < 4 and 0 <= nc < 4
                and maze[nr][nc] != 1):

                neighbour = (nr, nc)
                new_g = g[current] + 1

                if new_g < g.get(neighbour, float('inf')):
                    g[neighbour] = new_g
                    f = new_g + heuristic(neighbour, goal)

                    heapq.heappush(open_list, (f, neighbour))
                    parent[neighbour] = current

    return None


# Find and display path
path = astar(start, goal)

if path:
    print("Path found:")
    for position in path:
        print(position)

    for r, c in path:
        if maze[r][c] == 0:
            maze[r][c] = '*'

    print("\nMaze:")
    for row in maze:
        print(*row)

else:
    print("No path found!")


