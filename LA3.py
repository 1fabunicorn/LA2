from src.ball import Ball
from src.walls import Walls
import random
import pygame
# define a main function
def main():
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
     
    # create a surface on screen that has the size of 240 x 180
    WIDTH = 800
    HEIGHT = 400
    WALL_WIDTH = 20
    VELOCITY = 5
    FPS = 30

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
     
    # define a variable to control the main loop
    running = True
    clock = pygame.time.Clock()

    #add a solid background as r,g,b:
    fgcolor = pygame.Color("white")
    bgcolor = pygame.Color("black")
    screen.fill(bgcolor)
    wall = Walls(fgcolor, WIDTH, HEIGHT, WALL_WIDTH, screen)
    wall.show()
    x0 = WIDTH - Ball.RADIUS
    y0 = HEIGHT // 2
    vx0 = -VELOCITY
    #vy0 = 0
    vy0 = random.choice([-VELOCITY, VELOCITY])
    b0 = Ball(x0, y0,vx0, vy0, fgcolor, bgcolor, WALL_WIDTH, screen)

    pygame.display.update()

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            pygame.display.update()
            clock.tick(FPS)

            b0.update()
            wall.show()
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()