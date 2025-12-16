import pygame
from life import GameOfLife
from pygame.locals import *
from ui import UI


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)
        self.cell_size = cell_size
        self.speed = speed
        self.width = self.life.cols * cell_size
        self.height = self.life.rows * cell_size
        self.cell_width = life.cols
        self.cell_height = life.rows
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.curr_generation = life.curr_generation

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(
                self.screen, pygame.Color("black"), (x, 0), (x, self.height)
            )
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(
                self.screen, pygame.Color("black"), (0, y), (self.width, y)
            )

    def draw_grid(self) -> None:
        surface = self.screen
        for x in range(self.cell_height):
            for y in range(self.cell_width):
                if self.life.curr_generation[x][y] == 1:
                    color = pygame.Color("green")
                else:
                    color = pygame.Color("white")

                rect = (
                    y * self.cell_size,
                    x * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                )
                pygame.draw.rect(surface, color, rect)

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")

        self.screen.fill(pygame.Color("white"))

        running = True
        paused = False

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        paused = not paused
                    elif event.key == K_r:
                        self.life.curr_generation = self.life.create_grid(
                            randomize=True
                        )

                        self.life.generations = 1
                elif event.type == MOUSEBUTTONDOWN and paused:
                    if event.button == 1:
                        mouse_x, mouse_y = event.pos
                        grid_x = mouse_y // self.cell_size
                        grid_y = mouse_x // self.cell_size
                        if (
                            0 <= grid_x < self.life.rows
                            and 0 <= grid_y < self.life.cols
                        ):
                            self.life.curr_generation[grid_x][grid_y] = (
                                1 - self.life.curr_generation[grid_x][grid_y]
                            )
            if not paused:
                self.life.step()

            self.screen.fill(pygame.Color("white"))

            self.draw_grid()
            self.draw_lines()

            pygame.display.flip()
            clock.tick(self.speed)

        pygame.quit()

    if __name__ == "__main__":
        game = GameOfLife((50, 50), True)
        gui = GUI(game, cell_size=15, speed=1)
        gui.run()
