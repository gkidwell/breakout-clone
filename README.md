breakout-clone
==============

Python version of Breakout, written using pygame

project4.py
Bridgewater State University
COMP 399 Fall 09 - Project 4
Author: Glen Kidwell
Assignment:
Create a simple Breakout clone.


How to start
============

To start the game, open extract the files from the .zip into a folder. Open project4.py with Python 2.7. Pygame MUST be installed.


How to play
===========

You control a grey paddle, and must bounce a white ball around the screen, which breaks the bricks upon contact. You must attempt to not lose any balls. You begin with three balls.

If you break all the bricks on the screen, you progress to the next level. If you beat the three levels, you win the game.

Upon breaking a break, it may drop one of three different bonuses (or nothing). If you catch the bonus with your paddle, you will be rewarded.
 - Blue Gem: Adds 1000 points to your score.
 - Red F Circle: Adds 200 points to your score, and sets your ball on Fire. The ball will be red. This allows it to temporarily pass through bricks when breaking them, rather than bouncing back. After passing through 5 bricks, this bonus wears off. The ball will become white again.
 - Green S Circle: Adds 200 points to your score, and makes your paddle temporarily Sticky. The paddle will be green. This allows the ball to stick to your paddle, rather than immediately bouncing back. After the ball has stuck to your paddle 3 times, this bonus will wear off. The paddle becomes grey again.


Controls
========

 - Left arrow key: Moves your paddle to the left.
 - Right arrow key: Moves your paddle to the left.
 - Space bar: Releases the paddle from your paddle. This is used at the start of play, or when the paddle is Sticky.
 - R key: When viewing the End Game screen, as it instructs, the R key can be used to Restart the game.


How I implemented
=================

I implemented the game in the most straightforward manner that occurred to me.

All sprites are created at the beginning. A list allBricks is created for my 22 brick sprites. The levelSprites sprite group is initially emtpy. The allSprites sprite group contains all sprites.

During the main loop of the game, it checks for key events and takes appropriate action.

At the beginning of a given level, it resets appropriate sprites, and reads the appropriate text file for the layout of the bricks. The characters in the text file dictate the color of the brick, but other than that, they are all identical. The bricks for the level are added to the levelSprites group.

The main loop of the game also checks for when the ball is lost, when the paddle collides with bonuses, when the ball collides with the paddle or a brick, and appropriate actions are taken.

Upon the destruction of a brick, there is a 3 in 10 chance of a bonus dropping, with each type of bonus having a 1 in 10 chance.

When a brick is destroyed, its sprite is removed from the levelSprites group. When the group is empty, the next level begins. At the start of a new level, this is repopulated when the level's text file is read, and old brick sprites are recycled.

When the player runs out of balls, or wins, an End Game screen is displayed with an appropriate message.

With the previously described bonuses, I decided to implement counters for how many time they were used, rather than a counter for how many seconds it had been in effect, because it was simpler.


References to other code
========================

The bonusitem.py and scorebar.py files are reused and slightly edited from Glen Kidwell's Project 2 in COMP 399, the sidescrolling shoot-'em-up. The endgame.py file is reused from Glen Kidwell's Project 3 in COMP 399, the tower defense. Nearly identical functionality was required or desired in this project.


Possible problem
================

When a ball collides with a break, it reverses its y direction. Thus, if it was going down, it now goes up; if it was going up, it now goes down. This leads to a minor problem:

Suppose there is one brick immediately above another. The ball is going, for the sake of description, northeast, and it hits the left side of the top brick. It reverses y direction, and is now going southeast. It immediately hits the bottom brick, and reverses y direction again, and goes northeast again and continues. Because of how quickly this is processed, it appears as though it passes right through both. However, it is acting as I programmed it to.

This was discussed with Professor Santore, and he said it would be fine, but to mention it in the readme.
