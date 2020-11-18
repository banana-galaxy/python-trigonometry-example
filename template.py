import pygame, math, pyautogui

# initiate pygame 
pygame.init()
# initiate timer to limit fps
clock = pygame.time.Clock()

# get screen size
size = pyautogui.size()
# adjust size for window dimensions
size = [size[0]//4, size[1]//2]

# set window size and caption
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("eye like thingy")

# colors
white = (205, 205, 205)
black = (30, 30, 30)
 
# main code
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # -- logic --

    # seting diameters
    if size[1] < size[0]:
        ellipse_diameter = size[1]//3
        ball_diameter = size[1]//20
    else:
        ellipse_diameter = size[0]//3
        ball_diameter = size[0]//20

    # eye boundary
    ellipse_x = size[0]//2-ellipse_diameter//2
    ellipse_y = size[1]//2-ellipse_diameter//2

    # eyeball moving code!

    # eyeball initial position
    ball_x = size[0]//2-ball_diameter//2
    ball_y = size[1]//2-ball_diameter//2

    # get mouse position
    mouse = pygame.mouse.get_pos()
    
    # screen center to mouse distance
    delta_x = mouse[0] - size[0]//2
    delta_y = mouse[1] - size[1]//2
    distance = math.sqrt(delta_x**2 + delta_y**2)

    # determine if mouse is inside or outside eye boundary
    if distance >= ellipse_diameter//2-ball_diameter//2:
        # mouse is outside boundary
        
        # get relative angle screen center to mouse
        angle = math.atan2(delta_y, delta_x)

        # convert angle to coordinates for the eyeball
        ball_x = size[0]//2 + math.cos(angle)*(ellipse_diameter//2 - ball_diameter//2) - ball_diameter//2
        ball_y = size[1]//2 + math.sin(angle)*(ellipse_diameter//2 - ball_diameter//2) - ball_diameter//2
    else:
        # mouse is inside boudary

        # set ball coordinates to mouse
        ball_x = mouse[0] - ball_diameter//2
        ball_y = mouse[1] - ball_diameter//2


    # -- graphics --

    # clear screen 
    screen.fill(black)

    # eye boundary
    pygame.draw.ellipse(screen, white, [ellipse_x, ellipse_y, ellipse_diameter, ellipse_diameter], 2)

    # eyeball
    pygame.draw.ellipse(screen, white, [ball_x, ball_y, ball_diameter, ball_diameter])


    # -- screen update --

    # update
    pygame.display.flip()
 
    # 60 fps
    clock.tick(60)
 

pygame.quit()
