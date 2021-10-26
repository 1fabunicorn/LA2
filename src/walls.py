import pygame


class Walls:
    def __init__(self, fgcolor, width, height, wall_width, screen):
        self.fgcolor = fgcolor
        self.width = width
        self.height = height
        self.wall_width = wall_width
        self.screen = screen
        
    def show(self):
        pygame.draw.rect( self.screen, self.fgcolor, pygame.Rect(0, 0, self.width, self.wall_width) )
        pygame.draw.rect(self.screen, self.fgcolor, pygame.Rect((0, 0), (self.wall_width, self.height)))
        pygame.draw.rect(self.screen, self.fgcolor, pygame.Rect((0, self.height - self.wall_width), (self.width, self.wall_width)))