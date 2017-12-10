import pygame
import world

class Bird:

    _x = 0
    _y = 0
    _r = 0
    _vx = 0
    _vy = 0
    _color = (100, 200, 0)

    def __init__(self, x, y, r):
        self._x = x
        self._y = y
        self._r = r

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_r(self):
        return self._r

    def get_color(self):
        return self._color

    def get_vx(self):
        return self._vx

    def set_vx(self, vx):
        self._vx = vx

    def get_vy(self):
        return self._vy

    def set_vy(self, vy):
        self._vy = vy

    def draw(self, surf):
        pygame.draw.circle(surf, self._color, (int(self._x), int(self._y)), self._r)

    def move(self):
        self.gravity()
        self._x += self._vx
        self._y += self._vy

    def gravity(self):
        self._vy += 0.3
        y = self._y + self._r
        if y > world.groundLine:
            self._vy = 0

    def jump(self):
        self._vy = -3