import pygame


class Ball:
    RADIUS = 10
    def __init__(self, x, y, vx, vy, fgcolor, bgcolor, wall_width, screen):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.height, self.width = screen.get_size()
        self.fgcolor = fgcolor
        self.bgcolor = bgcolor
        self.wall_width = wall_width
        self.screen = screen
    
    def show(self, color):
        pygame.draw.circle(self.screen, color, (self.x, self.y), self.RADIUS)

    def update(self):
        self.bounce()
        self.show(self.bgcolor)
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.show(self.fgcolor)

    def bounce(self):
        if (self.x == self.wall_width):
            self.vx *= -1

        if (self.y <= self.wall_width) or (self.y >= (self.width - self.wall_width)):
            
            self.vy *= -1