from .init_class import Building
from engine import t, cst
import pygame

class Wall(Building):
    def __init__(self, x, y):
        super().__init__("Wall", (1, 1), [x, y], 1, 400, "defense")
        self.t = [0, 0, 0, 0]
        self.load()

    def load(self):
        """
        charge l'image du bâtiment
        """
        if sum(self.t) != 2:
            name = self.name + str(sum(self.t))
        else:
            if self.t[0] == self.t[2] and self.t[1] == self.t[3]:
                name = self.name + "2_0"
            else:
                name = self.name + "2_1"
        self.img = t.load_img(f"buildings/{self.name}/{name}.png", int(cst("SIZE_CASE")) * self.size[0] - 1,
                              int(cst("SIZE_CASE")) * self.size[1] - 1)
        self.img = pygame.transform.rotate(self.img, self.angle)

    def update_type(self):
        pass