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

screenSize = screenHeight, screenWidth = 1280, 960
surface = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Pong")


rectColor = (255, 255, 255) #sets the rectangle color
rectSize = rectWidth, rectHeight = 70, 300 # sets size of the square to 100x100
rectPos = rectX, rectY = 0, 0 #sets the position of the square within the
# display

rectSpeed = 2 # I dont know what this means at all
# I found out its the speed that the square moves when the controls are pressed
# the lower the number the slower it goes and vice versa 

gameRect = pygame.Rect(rectX, rectY, rectWidth, rectHeight)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    gameRect.clamp_ip(surface.get_rect())

    pygame.draw.rect(surface, rectColor, gameRect)

    pygame.display.update()   
    
