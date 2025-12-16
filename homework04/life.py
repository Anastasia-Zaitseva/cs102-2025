import pathlib
import random
import typing as tp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        if randomize:
            return [[random.randint(0, 1) for _ in range(self.cols)] for _ in range(self.rows)]
        return [[0] * self.cols for _ in range(self.rows)]

    def get_neighbours(self, cell: Cell) -> Cells:
        x, y = cell
        neighbours = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (x, y) != (x + i, y + j):
                    new_x, new_y = x + i, y + j
                    if 0 <= new_x < self.rows and 0 <= new_y < self.cols:
                        neighbours.append(self.curr_generation[new_x][new_y])
        return neighbours

    def get_next_generation(self) -> Grid:
        new_grid = self.create_grid(randomize=False)
        for x in range(self.rows):
            for y in range(self.cols):
                neighbours = self.get_neighbours((x, y))
                if self.curr_generation[x][y] == 1:
                    if sum(neighbours) == 2 or sum(neighbours) == 3:
                        new_grid[x][y] = 1
                else:
                    if sum(neighbours) == 3:
                        new_grid[x][y] = 1
        return new_grid

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.prev_generation = [row[:] for row in self.curr_generation]
        self.curr_generation = self.get_next_generation()
        self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        return self.max_generations is not None and self.generations >= self.max_generations

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        return self.curr_generation != self.prev_generation

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        with open(filename) as f:
            lines = f.readlines()
            game = GameOfLife((len(lines), len(lines[0].strip())), False)
            for x, row in enumerate(lines):
                for y, cell in enumerate(row.strip()):
                    if cell == "1":
                        game.curr_generation[x][y] = 1
                    else:
                        game.curr_generation[x][y] = 0
        return game

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        with open(filename, "w") as f:
            for row in self.curr_generation:
                string = "".join("1" if cell == 1 else "0" for cell in row) + "\n"
                f.write(string)
