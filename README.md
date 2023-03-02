# Pong Project

![pong game img](https://user-images.githubusercontent.com/102317619/222326890-bdeb57b2-23ed-4258-90ce-1b14a930799b.png)

## Program Versions
  Mac OS Big Sur + Windows 11
  Python 3.10.10
  Pygame 2.1.2
  
## Motivation:
    We chose this game because we wanted a chance to showcase all of the concepts
    that we learned so far in class, while priming ourselves to create more complex 
    game systems. We grabbed references of the old school pong games to inspire us.
 
## Reasoning:
    We decided to structure the code the way we did to have everything organized and easy 
    to find what we need. We placed all the variables up at the top and labeled the section 
    accordingly. We had our controller functions right underneath, these include the ball and both 
    of the handles. Then the game loop was last.

## Image:
![IMG_0521](https://user-images.githubusercontent.com/102317619/222335830-6115ac3f-2c0a-41df-a0c6-d43a22eaac7c.PNG)

 
## Future Work:
### Enhancements:
        The game contollers could handle a bit smoother. It kind of jumps, the motion is not fluid. Upgrading the 
        physics on that would be a plus. An extra feature would be sound a sound that is made each time a player
        scores or when the game is over.
        There's currently a glitch in the game that would need to be patched up in the future. It happens when
        the handle/paddle slides over the ball when the ball is next to it. The ball then goes through the handle
        from one end to another. I already tried to fix it, by displacing the ball onto the side of the handle,
        but this would cause problems for the score tracking.
 
### Generalization: 
     The games has all the usual components of most games. A game loops that runs until the player wants to quit, 
     handles that the player can control and a main objective for the player to obtain.

## Instructions:
Run the program with "python3 pong.py". This is a 2 player game, so Player 1 will control the left handle with 'w' and 's', and Player 2 will control the right side with the up and down arrow keys.
 
    
