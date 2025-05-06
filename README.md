Project Functionality:  
  The game has a screen with a button that, when pressed, starts the game. When the game starts, the play area will be drawn,
  dots will be drawn in valid spaces in the play area, and the player character will be drawn. The player character will move
  automatically based on the player's last input until it collides with a wall, at which point it will clear the last input and
  stop moving until the player gives a new input. If the player character collides with a dot, the player's score will increase
  by 10, and the dot will disappear. If all dots disappear, the game will end, and the player will be given the option to
  restart. Fruit will spawn in random spaces within the play area every so often, and when the player character collides with
  them, the player's score will increase by 50 and the fruit will disappear.  
  
Design Process:  
  I made most of these decisions based on the requirements of the final project. The movement could have been only when input
  is made and would still have satisfied the requirements, but I decided to be more accurate to the original Pacman. The play
  area was my attempt to recreate a simpler version of the maze from the original Pacman but without the cage for the ghosts.
  I chose the number of points awarded so that the score can easily reach triple digits while still being readable and with low
  likelyhood of a score that is too high to mean much.  
  
Requirements:  
  Board Size / Play Area:  
    • The game should be played on a window containing at least a 10-by-10 tile set.  
        Requirement met.  
    • Dots should be in all valid tiles for the Pac-man to be (no dots should be in walls or outside the boundaries).  
        Requirement met.  
  Pac-Man Movement:  
    • The Pac-man should move in one of four directions (up, down, left, right).  
        Requirement met.  
    • The player should control the direction using the arrow keys.  
        Requirement met, with the addition that WASD can be used as a substitute control scheme.  
    • There should be a path to the outside of the screen, and the Pac-man should be able to travel from one side to the other.  
        Requirement met.  
  Food Generation:  
    • Food should appear randomly on the game screen after some random number of seconds.  
        Requirement met.  
  Collision Detection:  
    • Pac-man's score increases when running into a dot or fruit  
        Requirement met  
    • The dot disappears.  
        Requirement met.  
    • The fruit disappears and the timer for the next fruit to spawn begins.  
        Requirement met.  
  Game Over and Score:  
    • Display a Game Over message when all dots are collected.  
        Requirement not met, but it does display a game over screen.  
    • Display the player's score, which is based on how much food and dots the Pac-man has collected.  
        Requirement met.  
  Restart Option:  
    • There should be an option to replay the game after a game over.  
        Requirement met.  
    
![FinalProjectFlowchart drawio](https://github.com/user-attachments/assets/dc6d4b21-5e8e-4462-b01a-9579b24df844)
