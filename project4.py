""" project4.py
    COMP 399 Fall 09 Project 4
    Author: Glen Kidwell
    Assignment:
    Create a simple Breakout clone.

    Controls:
    Left arrow key: Moves your paddle to the left.
    Right arrow key: Moves your paddle to the left.
    Space bar: Releases the paddle from your paddle. This is used at the start of play, or when the paddle is Sticky.
    R key: When viewing the End Game screen, as it instructs, the R key can be used to Restart the game."""

import pygame, random, os
# Import other classes
import paddle, ball, brick, scorebar, endgame, bonusItem

def main():
    """ This is the main method of the game.
        Much of the game is intialized and controlled here.
    """
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("COMP 399 Project 4 - Glen Kidwell")

    # Create necessary instances of all classes.
    playerPaddle = paddle.Paddle(screen)
    gameBall = ball.Ball(screen)
    gameScore = scorebar.Scorebar(screen)
    # 22 Brick sprites are created.
    # The third level has 22 bricks, and due to reuse of the sprites, this is as many as will be needed.
    brick0 = brick.Brick(screen)
    brick1 = brick.Brick(screen)
    brick2 = brick.Brick(screen)
    brick3 = brick.Brick(screen)
    brick4 = brick.Brick(screen)
    brick5 = brick.Brick(screen)
    brick6 = brick.Brick(screen)
    brick7 = brick.Brick(screen)
    brick8 = brick.Brick(screen)
    brick9 = brick.Brick(screen)
    brick10 = brick.Brick(screen)
    brick11 = brick.Brick(screen)
    brick12 = brick.Brick(screen)
    brick13 = brick.Brick(screen)
    brick14 = brick.Brick(screen)
    brick15 = brick.Brick(screen)
    brick16 = brick.Brick(screen)
    brick17 = brick.Brick(screen)
    brick18 = brick.Brick(screen)
    brick19 = brick.Brick(screen)
    brick20 = brick.Brick(screen)
    brick21 = brick.Brick(screen)
    pointBonus = bonusItem.BonusItem(screen,0)
    fireBonus = bonusItem.BonusItem(screen,1)
    stickyBonus = bonusItem.BonusItem(screen,2)

    # List of all bricks
    allBricks = [brick0, brick1, brick2, brick3, brick4,
                 brick5, brick6, brick7, brick8, brick9,
                 brick10, brick11, brick12, brick13, brick14,
                 brick15, brick16, brick17, brick18, brick19,
                 brick20, brick21]
    # levelSprites will be used to contain the bricks in a given level.
    # It is populated in the levelBegin if block.
    levelSprites = pygame.sprite.Group()
    allSprites = pygame.sprite.Group(playerPaddle, gameBall, levelSprites, allBricks, gameScore, pointBonus, fireBonus, stickyBonus)

    # Sound effects for various events.
    brickdestroy = pygame.mixer.Sound(os.path.join("sounds", "brickdestroy.ogg"))
    fireballbonus = pygame.mixer.Sound(os.path.join("sounds", "fireballbonus.ogg"))
    lostball = pygame.mixer.Sound(os.path.join("sounds", "lostball.ogg"))
    pointsbonus = pygame.mixer.Sound(os.path.join("sounds", "pointsbonus.ogg"))
    stickybonus = pygame.mixer.Sound(os.path.join("sounds", "stickybonus.ogg"))
    paddlebounce = pygame.mixer.Sound(os.path.join("sounds", "paddlebounce.ogg"))
    youwin = pygame.mixer.Sound(os.path.join("sounds", "youwin.ogg"))

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((100,100,100))
    screen.blit(background, (0,0))

    clock = pygame.time.Clock()
    # Booleans
    keepGoing = True
    gameOver = False
    levelBegin = True
    playerLost = False
    # Counter variables
    q = 0
    level = 1
    stickyuse = 0
    fireuse = 0 

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    # Move paddle left
                    playerPaddle.leftKey = True
                elif event.key == pygame.K_RIGHT:
                    # Move paddle right
                    playerPaddle.rightKey = True
                elif event.key == pygame.K_SPACE:
                    # Release ball, if applicable
                    if gameBall.moving == False:
                        gameBall.moving = True
            elif event.type == pygame.KEYUP:
                # Cease moving if necessary
                if playerPaddle.leftKey == True:
                    playerPaddle.leftKey = False
                elif playerPaddle.rightKey == True:
                    playerPaddle.rightKey = False

        # This loop is entered at the start of each level.
        if levelBegin == True:
            # A new background image is loaded.
            background = pygame.image.load(os.path.join("backgrounds", "background%d.jpg" % level))
            background = background.convert()
            screen.blit(background, (0,0))
            # There are three levels.
            if level != 4:
                # Reset various sprites and counters, and empty the levelSprites group.
                gameBall.reset()
                playerPaddle.reset()
                pointBonus.reset()
                fireBonus.reset()
                stickyBonus.reset()
                levelSprites.empty()
                stickyuse = 0
                fireuse = 0
                q = 0
                # Open and read the appropriate text file for the level.
                file = open(os.path.join("layouts", "level%d.txt" % level))
                linesList = file.readlines()
                for i in range(len(linesList)):
                    linesList[i] = linesList[i].strip()
                    for j in range(len(linesList[i])):
                        # 'N' indicates no brick.
                        if linesList[i][j] != 'N':
                            # The brick will be moved to the appropriate location.
                            # (100*j) is the x value; the width of each brick is 100.
                            # (100+20*i) is the y value; the heigh of each brick is 20, and the top row is offset from the top of the screen by 100.
                            allBricks[q].changePos(100*j,100+20*i)
                            # The brick is added to levelSprites.
                            levelSprites.add(allBricks[q])
                            # 'B' indicates a blue brick
                            if linesList[i][j] == 'B':
                                allBricks[q].image = pygame.image.load(os.path.join("images", "bluebrick.png"))
                            # 'G' indicates a green brick
                            elif linesList[i][j] == 'G':
                                allBricks[q].image = pygame.image.load(os.path.join("images", "greenbrick.png"))
                            # 'R' indicates a red brick
                            elif linesList[i][j] == 'R':
                                allBricks[q].image = pygame.image.load(os.path.join("images", "redbrick.png"))
                            # 'Y' indicates a yellow brick
                            elif linesList[i][j] == 'Y':
                                allBricks[q].image = pygame.image.load(os.path.join("images", "yellowbrick.png"))
                            q = q + 1
                # End the if block, and increase level.
                levelBegin = False
                level = level + 1
            else:
            # If level >= 4, the game should end.
                keepGoing = False
                playerLost = False
                gameOver = True

        if gameBall.lost == True:
            # This will be true when the ball has passed beneath the screen.
            lostball.play()
            # Decrease amount of balls.
            gameScore.balls = gameScore.balls - 1
            # If the player is out of balls, end the game.
            if gameScore.balls < 1:
                keepGoing = False
                playerLost = True
                gameOver = True
            # Reset gameBall.lost, sprites, and counter variables.
            gameBall.lost = False
            gameBall.reset()
            playerPaddle.reset()
            pointBonus.reset()
            fireBonus.reset()
            stickyBonus.reset()
            stickyuse = 0
            fireuse = 0
        if playerPaddle.rect.colliderect(pointBonus.rect):
            # If the player gets the pointsBonus (gem), add 1000 points.
            gameScore.score += 1000
            pointBonus.reset()
            pointsbonus.play()
        if playerPaddle.rect.colliderect(fireBonus.rect):
            # If the player gets the fireBonus (red f circle), add 200 points, make gameBall.fire True, and change the image.
            gameScore.score += 200
            fireBonus.reset()
            gameBall.fire = True
            gameBall.image = pygame.image.load(os.path.join("images", "fireball.png"))
            fireballbonus.play()
        if playerPaddle.rect.colliderect(stickyBonus.rect):
            # If the player gets the fireBonus (red f circle), add 200 points, make gameBall.sticky True, and change the paddle's image.
            gameScore.score += 200
            stickyBonus.reset()
            gameBall.sticky =  True
            playerPaddle.image = pygame.image.load(os.path.join("images", "stickypaddle.png"))
            stickybonus.play()
        if gameBall.rect.colliderect(playerPaddle):
            # If the ball hits the paddle, it should go up.
            paddlebounce.play()
            gameBall.ydirection = gameBall.up
            if gameBall.sticky == False:
                # If the ball is not sticky, let the ball continue, changing its dx depending on where its center hit the paddle's 100 pixel length.
                if (gameBall.rect.centerx > playerPaddle.rect.centerx - 10) and (gameBall.rect.centerx < playerPaddle.rect.centerx + 10):
                    # If it hits the center (pixels 40 through 60 on the paddle)
                    gameBall.dx = 0
                elif (gameBall.rect.centerx > playerPaddle.rect.left) and (gameBall.rect.centerx < playerPaddle.rect.left + 20):
                    # If it hits the left edge of the paddle (pixels 0 through 20 on the paddle)
                    gameBall.dx = 20
                elif (gameBall.rect.centerx < playerPaddle.rect.right) and (gameBall.rect.centerx > playerPaddle.rect.right - 20):
                    # If it hits the right edge of the paddle (pixels 80 through 100 on the paddle)
                    gameBall.dx = 20
                else:
                    # Otherwise (pixels 20 through 40 and 60 through 80 on the paddle)
                    gameBall.dx = 10
            else:
                # If the ball is sticky, have it stick to the paddle until the spacebar is pressed.
                gameBall.rect.bottom = playerPaddle.rect.top
                gameBall.moving = False
                stickyuse += 1
                if stickyuse == 3:
                    # When 'sticky' has been utilized 3 times, it wears off.
                    gameBall.sticky = False
                    stickyuse = 0
                    playerPaddle.image = pygame.image.load(os.path.join("images", "paddle.png"))
        for z in range(len(allBricks)):
            # Check all elements of allBricks.
            if gameBall.rect.colliderect(allBricks[z]):
                # If the ball hits a given brick
                if gameBall.fire == False:
                    # If the ball is not on fire, reverse y direction of ball.
                    if gameBall.ydirection == gameBall.up:
                        gameBall.ydirection = gameBall.down
                    elif gameBall.ydirection == gameBall.down:
                        gameBall.ydirection = gameBall.up
                else:
                    # If the ball is on fire, it will go pass through the brick.
                    fireuse += 1
                    if fireuse == 5:
                        # When 'fire' has been utilized 5 times (gone through 5 bricks), it wears off.
                        gameBall.fire = False
                        gameBall.image = pygame.image.load(os.path.join("images", "ball.png"))
                        fireuse = 0
                randomnumber = random.randrange(1,10)
                # Each of the 3 bonuses has a 1 in 10 chance of appearing upon destruction of a brick.
                # If the bonus already exists on screen (<bonus>.moving == True),
                # or if the player is currently utilizing that bonus type (gameBall.<bonus> == True),
                # then the bonus will not spawn.
                # If a bonus spawns, it centers itself where the destroyed brick was, and moves downward.
                if randomnumber == 1:
                    if pointBonus.moving == False:
                        pointBonus.rect.centerx = allBricks[z].rect.centerx
                        pointBonus.rect.centery = allBricks[z].rect.centery
                        pointBonus.moving = True
                elif randomnumber == 2:
                    if fireBonus.moving == False and gameBall.fire == False:
                        fireBonus.rect.centerx = allBricks[z].rect.centerx
                        fireBonus.rect.centery = allBricks[z].rect.centery
                        fireBonus.moving = True
                elif randomnumber == 3:
                    if stickyBonus.moving == False and gameBall.sticky == False:
                        stickyBonus.rect.centerx = allBricks[z].rect.centerx
                        stickyBonus.rect.centery = allBricks[z].rect.centery
                        stickyBonus.moving = True
                brickdestroy.play()
                # Remove the brick from the levelSprites group, and reset it.
                allBricks[z].remove(levelSprites)
                allBricks[z].reset()
                # Increase score.
                gameScore.score = gameScore.score + 100
                # If the levelSprites group is empty, begin the next level.
                if levelSprites.sprites() == []:
                    levelBegin = True

        allSprites.clear(screen,background)
        allSprites.update()
        # At the beginning of a level, or if the paddle is Sticky,
        # this allows the ball to mimic the x movement of the paddle, centered just above it.
        # The awkward placement in the program was necessary for it the ball to properly follow the paddle.
        if gameBall.moving == False:
            if playerPaddle.leftKey == True or playerPaddle.rightKey == True:
                gameBall.rect.centerx = playerPaddle.rect.centerx
        allSprites.draw(screen)
        pygame.display.flip()
                
    # Depending on whether the player lost or won, draw an endscreen to the screen with the appropriate parameter.
    allSprites.clear(screen,background)
    if playerLost == True:
        endscreen = endgame.EndGame(screen,0)
    else:
        youwin.play()
        endscreen = endgame.EndGame(screen,1)
    endSprites = pygame.sprite.Group(endscreen)
    # Allow the user to quit, or press the R key to restart.
    while gameOver == True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()
        endSprites.clear(screen, background)
        endSprites.update()
        endSprites.draw(screen)
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
