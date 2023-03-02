import pygame, sys, random #Imports the required libraries

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

#Screen Creation
screenSize = screenWidth, screenHeight = 1280, 780
surface = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Pong")

#Colors
bg_color = pygame.Color('grey12')
wht_color = (255, 255, 255)

#Handle Creation
rectColor = wht_color #Sets the rectangle color
rectSize = rectWidth, rectHeight = 30, 150 #Sets size of the rectangle
rectSpeed = 1 #The speed that the rectangle moves when the controls are pressed
              #(the lower the number the slower it goes and vice versa).
rect1Pos = rect1X, rect1Y = 0, (screenHeight / 2) - 75 #Sets the position of the rectangle within the display
player1 = pygame.Rect(rect1X, rect1Y, rectWidth, rectHeight)
rect2Pos = rect2X, rect2Y = 1280, (screenHeight / 2) - 75
player2 = pygame.Rect(rect2X, rect2Y, rectWidth, rectHeight)

#Ball Creation
ballSize = ballHeight, ballWidth = 20, 20
ballPos = ballX, ballY = (screenWidth/2)-10, (screenHeight/2)-10
ball = pygame.Rect(ballX, ballY, ballWidth, ballHeight)
ballSpeedX = random.choice([-1, 1])
ballSpeedY = random.choice([-1, 1])
breakTime = 0;

#The Areas of the Game
borderTop = pygame.Rect(0, 0, screenWidth, 1)                 #Starts at the origin and stretches to the right side
borderBottom = pygame.Rect(0, screenHeight-1, screenWidth, 1) #Starts 1 pixel away from the bottom and stretches to the right side
board = pygame.Rect(0, 0, screenWidth, screenHeight)

#Text Variables
scorePlayer1 = 0
scorePlayer2 = 0
gameFont = pygame.font.Font("Jura.ttf", 42)


#Movement for Player One
def move_rect1(player1):
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        player1.move_ip(0, -rectSpeed)
    if key[pygame.K_s]:
        player1.move_ip(0, rectSpeed)


#Movement for Player Two
def move_rect2(player2):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player2.move_ip(0, -rectSpeed)
    if keys[pygame.K_DOWN]:
        player2.move_ip(0, rectSpeed)


#Movement of the Ball
def move_ball(ball):
    #These have to be declared global. Otherwise, they'd be local, since they're in a function.
    global ballSpeedX, ballSpeedY, breakTime, scorePlayer1, scorePlayer2, ballX

    #How the ball bounces
    if ball.colliderect(player1) or ball.colliderect(player2):
        ballSpeedX *= -1
        ballX += ballSpeedX #Only ballX needs to be tracked for scores.
        ball.move_ip(ballSpeedX, ballSpeedY) #move_ip needs to be here too since the ball would be stuck otherwise
    elif ball.colliderect(borderTop) or ball.colliderect(borderBottom):
        ballSpeedY *= -1
        ballX += ballSpeedX
        ball.move_ip(ballSpeedX, ballSpeedY) #move_ip needs to be here too since the ball would be stuck otherwise
    else:
        ballX += ballSpeedX
        ball.move_ip(ballSpeedX, ballSpeedY) #The default state

    #How the ball respawns
    if not board.contains(ball):
        breakTime += 1 #Using pygame.time.wait or pygame.time.delay instead would not show the ball leaving the board.
        if breakTime == 150:
            if ballX < 0:
                scorePlayer1 += 1
            else:
                scorePlayer2 += 1
            ballX = (screenWidth/2)-10 #Resetting ballX
            ball.update(ballX, random.randrange(0, screenHeight, 1), ballWidth, ballHeight) #The y-value will be random along the line.
            ballSpeedY = random.choice([-1, 1]) #For ballSpeedX, the ball will always go to the player who didn't score.
            breakTime = 0


#Game Loop
#Using "while 1" instead of "while True" is more efficient
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill((36, 36, 36)) #Dark gray background

    move_rect1(player1)
    move_rect2(player2)
    move_ball(ball)

    player1.clamp_ip(surface.get_rect())
    player2.clamp_ip(surface.get_rect())

    pygame.draw.ellipse(surface, (255, 255, 255), ball)
    pygame.draw.rect(surface, (255, 255, 255), player1)
    pygame.draw.rect(surface, (255, 255, 255), player2)
    pygame.draw.aaline(surface, (255, 255, 255), (screenWidth / 2, 0), (screenWidth / 2, screenHeight))

    player1Text = gameFont.render(f"{scorePlayer1}", True, (255, 255, 255))
    surface.blit(player1Text, (800,75))

    player2Text = gameFont.render(f"{scorePlayer2}", True, (255, 255, 255))
    surface.blit(player2Text, (450,75))

    pygame.display.update(board)
