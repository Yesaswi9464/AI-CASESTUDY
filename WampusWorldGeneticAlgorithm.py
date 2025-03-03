import random
import numpy as np
class WumpusWorldGA:
    def __init__(self, grid, population_size=10, generations=50, mutation_rate=0.1):
        self.grid = grid
        self.n = len(grid)
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.start_x, self.start_y = self.find_position('A')
        self.gold_x, self.gold_y = self.find_position('G')
    def find_position(self, item):
        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j] == item:
                    return i, j
        return None, None
    def is_safe(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.n and self.grid[x][y] not in ('W', 'P')
    def fitness(self, path):
        x, y = self.start_x, self.start_y
        for dx, dy in path:
            x, y = x + dx, y + dy
            if not self.is_safe(x, y):
                return float('inf')
            if (x, y) == (self.gold_x, self.gold_y):
                return len(path)
        return float('inf')
    def generate_population(self):
        return [[random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)]) for _ in range(self.n * 2)] for _ in range(self.population_size)]
    def mutate(self, path):
        if random.random() < self.mutation_rate:
            idx = random.randint(0, len(path) - 1)
            path[idx] = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
        return path
    def crossover(self, parent1, parent2):
        split = random.randint(0, len(parent1) - 1)
        return parent1[:split] + parent2[split:]
    def genetic_algorithm(self):
        population = self.generate_population()
        for _ in range(self.generations):
            population = sorted(population, key=self.fitness)
            if self.fitness(population[0]) != float('inf'):
                return population[0]
            new_population = population[:self.population_size // 2]
            while len(new_population) < self.population_size:
                p1, p2 = random.sample(new_population, 2)
                child = self.mutate(self.crossover(p1, p2))
                new_population.append(child)
            population = new_population
        return population[0]
    def display_grid(self):
        print("\nWumpus World Grid:")
        print("-" * (self.n * 4))
        for row in self.grid:
            print(" | ".join(row))
            print("-" * (self.n * 4))
        print()
    def display_path(self, path):
        x, y = self.start_x, self.start_y
        path_grid = [[self.grid[i][j] for j in range(self.n)] for i in range(self.n)]
        for dx, dy in path:
            x, y = x + dx, y + dy
            if (x, y) == (self.gold_x, self.gold_y):
                break
            path_grid[x][y] = 'P'
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
world = WumpusWorldGA(grid)
print("Initial Wumpus World Grid:")
world.display_grid()
best_path = world.genetic_algorithm()
print("Path to Gold:", best_path)
print("Final Path Taken:")
world.display_path(best_path)
