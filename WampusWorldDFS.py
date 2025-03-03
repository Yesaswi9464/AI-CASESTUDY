class WumpusWorld:
    def __init__(self, grid):
        self.grid = grid
        self.n = len(grid)
        self.visited = set()
        self.path = []
        self.found_gold = False
    def is_safe(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.n and self.grid[x][y] != 'W' and self.grid[x][y] != 'P'
    def dfs(self, x, y):
        if (x, y) in self.visited or not self.is_safe(x, y) or self.found_gold:
            return
        self.visited.add((x, y))
        self.path.append((x, y))
        if self.grid[x][y] == 'G':  
            self.found_gold = True
            return
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            self.dfs(x + dx, y + dy)
            if self.found_gold:
                return
        self.path.pop() 
    def find_gold(self, start_x, start_y):
        self.dfs(start_x, start_y)
        return self.path if self.found_gold else "No path to gold found"
    def display_grid(self):
        print("\nWumpus World Grid:")
        print("-" * (self.n * 4))
        for row in self.grid:
            print(" | ".join(row))
            print("-" * (self.n * 4))
        print()
    def display_path(self):
        path_grid = [[self.grid[i][j] if (i, j) not in self.path else 'P' for j in range(self.n)] for i in range(self.n)]
        print("\nPath Taken by Agent:")
        print("-" * (self.n * 4))
        for row in path_grid:
            print(" | ".join(row))
            print("-" * (self.n * 4))
        print()
# Sample Wumpus World Grid (6x6)
# 'A' -> Agent Start Position
# 'G' -> Gold
# 'W' -> Wumpus
# 'P' -> Pit
# '.' -> Safe Path
grid = [
    ['A', '.', '.', 'P', '.', '.'],
    ['.', 'W', '.', '.', 'P', '.'],
    ['.', '.', 'P', '.', 'W', '.'],
    ['P', '.', '.', '.', '.', 'G'],
    ['.', 'W', 'P', '.', 'P', '.'],
    ['.', '.', '.', 'W', '.', '.']
]
start_x, start_y = 0, 0  
world = WumpusWorld(grid)
print("Initial Wumpus World Grid:")
world.display_grid()
path_to_gold = world.find_gold(start_x, start_y)
print("Path to Gold:", path_to_gold)
print("Final Path Taken:")
world.display_path()
