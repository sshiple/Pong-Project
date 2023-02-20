import pygame, sys # imports the required libraries

#what the game should have
    #game loop
    #model
        #state of game
    #view
        #updating screen
    #controller
        #inputs
        #Event queue
    #entities (character/things)
        #player character
    #main game script

    
pygame.init()

# this is the creation of the screen

screenSize = screenHeight, screenWidth = 1280, 780
surface = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Pong")


bg_color = pygame.Color('grey12')
wht_color = (255, 255, 255)

rectColor = wht_color #sets the rectangle color
rectSize = rectWidth, rectHeight = 70, 200 # sets size of the square to 100x100
rectPos = rectX, rectY = 0, 100 #sets the position of the square within the
# display

rectSpeed = 1 # I dont know what this means at all
# I found out its the speed that the square moves when the controls are pressed
# the lower the number the slower it goes and vice versa 

gameRect = pygame.Rect(rectX, rectY, rectWidth, rectHeight)



def move_rect(gameRect):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        gameRect.move_ip(0, -rectSpeed)
    if keys[pygame.K_DOWN]:
        gameRect.move_ip(0, rectSpeed)



        
#game loop
        
        
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    move_rect(gameRect)

    surface.fill(bg_color)

    gameRect.clamp_ip(surface.get_rect())

    pygame.draw.rect(surface, rectColor, gameRect)

    pygame.display.update()   
    
