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

# this is the creation of the screen that the game is 

screenSize = screenHeight, screenWidth = 1280, 780
surface = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Pong")

#these are the colors
bg_color = pygame.Color('grey12')
wht_color = (255, 255, 255)

# HANDLE 1 CREATION = = = = = = = = = = = = = = = = = = = =

rectColor = wht_color #sets the rectangle color
rectSize = rectWidth, rectHeight = 30, 150 # sets size of the square to 100x100
rectPos = rectX, rectY = 0, 100 #sets the position of the square within the
# display

rectSpeed = 1 # I dont know what this means at all
# I found out its the speed that the square moves when the controls are pressed
# the lower the number the slower it goes and vice versa 

player = pygame.Rect(rectX, rectY, rectWidth, rectHeight)

# HANDLE 2 CREATION = = = = = = = = = = = = = = = = = = = = 

rect_twoPos = rect_twoX, rect_twoY = 1280, 0

player_two = pygame.Rect(rect_twoX, rect_twoY, rectWidth, rectHeight)

# MOVEMENT FOR PLAYER ONE 
def move_rect(player):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_two.move_ip(0, -rectSpeed)
    if keys[pygame.K_DOWN]:
        player_two.move_ip(0, rectSpeed)


# MOVEMENT FOR PLAYER TWO
def move_rectTwo(player_two):
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        player.move_ip(0, -rectSpeed)
    if key[pygame.K_s]:
        player.move_ip(-0, rectSpeed)

        
#game loop
        
        
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    move_rect(player)
    move_rectTwo(player_two)

    surface.fill(bg_color)

    player.clamp_ip(surface.get_rect())
    player_two.clamp_ip(surface.get_rect())

    pygame.draw.rect(surface, rectColor, player)
    pygame.draw.rect(surface, rectColor, player_two)

    pygame.draw.aaline(surface, wht_color, (screenHeight / 2, 0), (screenHeight / 2, screenWidth))

    # pygame.draw.rect(surface, rectColor, gameRect_2)

    pygame.display.update()   
    
