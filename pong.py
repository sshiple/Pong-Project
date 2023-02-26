import pygame, sys, random # imports the required libraries

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

screenSize = screenWidth, screenHeight = 1280, 780
surface = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Pong")

#these are the colors
bg_color = pygame.Color('grey12')
wht_color = (255, 255, 255)

# HANDLE 1 CREATION = = = = = = = = = = = = = = = = = = = =

rectColor = wht_color #sets the rectangle color
rectSize = rectWidth, rectHeight = 30, 150 # sets size of the square to 100x100
rectPos = rectX, rectY = 0, (screenHeight / 2) - 75 #sets the position of the square within the
# display

rectSpeed = 1
# I found out its the speed that the square moves when the controls are pressed
# the lower the number the slower it goes and vice versa

player = pygame.Rect(rectX, rectY, rectWidth, rectHeight)

# HANDLE 2 CREATION = = = = = = = = = = = = = = = = = = = =

rect_twoPos = rect_twoX, rect_twoY = 1280, (screenHeight / 2) - 75
player_two = pygame.Rect(rect_twoX, rect_twoY, rectWidth, rectHeight)


#The Areas of the Game
borderTop = pygame.Rect(0, 0, screenWidth, 1)                 #Starts at the origin and stretches to the right side
borderBottom = pygame.Rect(0, screenHeight-1, screenWidth, 1) #Starts 1 pixel away from the bottom and stretches to the right side
board = pygame.Rect(0, 0, screenWidth, screenHeight)


# CREATION OF THE BALL
ballSize = ballHeight, ballWidth = 20, 20
ballPos = ballX, ballY = (screenWidth/2) - 10, (screenHeight/2) - 10
ball = pygame.Rect(ballX, ballY, ballWidth, ballHeight)
ballSpeedX = random.choice([-1, 1])
ballSpeedY = random.choice([-1, 1])
breakTime = 0;
#clock = pygame.time.Clock()


def move_ball(ball):
    #These have to be declared global. Otherwise, they'd be local, since they're in a function.
    global ballSpeedX, ballSpeedY, breakTime

    #This is to get a near constant framerate (might need this later)
    #dt = clock.tick(30)
    #ball.move_ip(ballSpeedX*dt, 0)
    #print(clock.get_fps())

    #How the ball bounces
    if ball.colliderect(player) or ball.colliderect(player_two):
        ballSpeedX *= -1
        ball.move_ip(ballSpeedX, ballSpeedY) #move_ip needs to be here too since the ball would be stuck otherwise
    elif ball.colliderect(borderTop) or ball.colliderect(borderBottom):
        ballSpeedY *= -1
        ball.move_ip(ballSpeedX, ballSpeedY) #move_ip needs to be here too since the ball would be stuck otherwise
    else:
        ball.move_ip(ballSpeedX, ballSpeedY) #The default state

    #How the ball respawns
    if not board.contains(ball):
        breakTime += 1 #Using pygame.time.wait or pygame.time.delay instead would not show the ball leaving the board.
        if breakTime == 300:
            ball.update(ballX, random.randrange(0, screenHeight, 1), ballWidth, ballHeight) #The y-value will be random along the line.
            ballSpeedY = random.choice([-1, 1]) #For ballSpeedX, the ball will always go to the player who didn't score.
            breakTime = 0


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


#Game Loop
#Using "while 1" instead of "while True" is more efficient
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #rectList = [ball, player, player_two, board]

    surface.fill(bg_color)

    move_rect(player)
    move_rectTwo(player_two)
    move_ball(ball)

    player.clamp_ip(surface.get_rect())
    player_two.clamp_ip(surface.get_rect())

    pygame.draw.ellipse(surface, wht_color, ball)
    pygame.draw.rect(surface, rectColor, player)
    pygame.draw.rect(surface, rectColor, player_two)
    pygame.draw.aaline(surface, wht_color, (screenWidth / 2, 0), (screenWidth / 2, screenHeight))

    # pygame.draw.rect(surface, rectColor, gameRect_2)

    #pygame.display.update(rectList) #Might need this later
    pygame.display.update()
