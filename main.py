# Example file showing a basic pygame "game loop"
import pygame

xMax = 64
yMax = 36
scale = 20
frame_rate = 60
# pygame setup
pygame.init()
screen = pygame.display.set_mode((xMax * scale, yMax * scale))
clock = pygame.time.Clock()
running = True

grid = [
    [ False for i in range(xMax)] for j in range(yMax)
]
flipped_grid = [
    [ False for i in range(xMax)] for j in range(yMax)
]

def flipornot(i, j):
    total = 0
    for xDiff in [-1,0,1]:
        for yDiff in [-1,0,1]:
            checkX = i - xDiff
            checkY = j - yDiff
            if checkX<0 or checkY<0 or checkX >= xMax or checkY >= yMax or (xDiff == 0 and yDiff == 0):
                continue
            else:
                # print(checkY, checkX)
                total += grid[checkY][checkX]
    if grid[j][i]:
        # print((j,i), 'alive', 'total=', total)
        #alive
        if total >= 4:
            #print((j,i), 'will be ded')
            return True # ded
        elif 2 <= total <=3:
            #print((j,i), 'will stay alive')

            return False # stay alive
        elif total < 2:
            #print((j,i), 'will be ded')
            return True

    else:
        # dead
        if total == 3:
            # make cell alive
            return True
        else:
            # cell remains dead
            return False





def flip_grid():
    global grid
    global flipped_grid

    for i in range(1, xMax):
        for j in range(1, yMax):
            to_flip_or_not_to_flip = flipornot(i,j)
            if to_flip_or_not_to_flip:
                #print('flipping', (j,i), grid[j][i], flipped_grid[j][i])
                flipped_grid[j][i] = not grid[j][i]
                #print('flipped', (j,i), grid[j][i], flipped_grid[j][i])
            else:
                flipped_grid[j][i] = grid[j][i]

    temp = flipped_grid
    flipped_grid = grid
    grid = temp
                
playmode = False
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            # print(x,y)
            grid[y//scale][x//scale] = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                playmode = not playmode



    # fill the screen with a color to wipe away anything from last frame

    for i in range(0, xMax*scale, scale):
        for j in range(0, yMax * scale, scale):
            color = (255,255,255) if grid[j//scale][i//scale] else (0,0,0)
            pygame.draw.rect(screen, color, pygame.Rect(i, j, scale, scale))



    # RENDER YOUR GAME HERE
    if playmode:
        flip_grid()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(frame_rate)  # limits FPS to 60

pygame.quit()
