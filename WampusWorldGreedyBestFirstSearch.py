import heapq
import random

class WumpusWorld:
    def __init__(self, grid):
        self.grid = grid
        self.n = len(grid)
        self.visited = set()
        self.path = []
        self.found_gold = False

    def is_safe(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.n and self.grid[x][y] != 'W' and self.grid[x][y] != 'P'

    def heuristic(self, x, y, gold_x, gold_y):
        return abs(x - gold_x) + abs(y - gold_y) + random.uniform(0, 1)

    def greedy_best_first_search(self, start_x, start_y, gold_x, gold_y):
        priority_queue = []
        heapq.heappush(priority_queue, (0, start_x, start_y, []))
        self.visited.clear()
        
        while priority_queue:
            _, x, y, current_path = heapq.heappop(priority_queue)
            
            if (x, y) in self.visited:
                continue
            
            self.visited.add((x, y))
            new_path = current_path + [(x, y)]
            
            if (x, y) == (gold_x, gold_y):
                self.path = new_path
                return new_path
            
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            random.shuffle(directions)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if self.is_safe(nx, ny) and (nx, ny) not in self.visited:
                    priority = self.heuristic(nx, ny, gold_x, gold_y)
                    heapq.heappush(priority_queue, (priority, nx, ny, new_path))
        
        return "No path to gold found"

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

grid = [
    ['A', '.', '.', 'P', '.', '.'],
    ['.', 'W', '.', '.', 'P', '.'],
    ['.', '.', 'P', '.', 'W', '.'],
    ['P', '.', '.', '.', '.', 'G'],
    ['.', 'W', 'P', '.', 'P', '.'],
    ['.', '.', '.', 'W', '.', '.']
]

start_x, start_y = 0, 0
gold_x, gold_y = 3, 5

world = WumpusWorld(grid)
print("Initial Wumpus World Grid:")
world.display_grid()

path_to_gold = world.greedy_best_first_search(start_x, start_y, gold_x, gold_y)
print("Path to Gold:", path_to_gold)

print("Final Path Taken:")
world.display_path()
