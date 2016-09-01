---
morea_id: experience-H07
morea_type: experience
title: "H07: Two-Dice Pig Game"
published: True
morea_start_date: "2016-10-21T23:55:00"
morea_summary: "Write a program that allows players to play Two-Dice Pig."
morea_labels: 
  - "Homework Assignment"
---

# ICS 111 Homework Assignment H07: Two-Dice Pig Game


1) Write a program that allows players to play the game Two-Dice Pig. 

The rules of Two-Dice Pig are:

Each turn, a player repeatedly rolls two dice until a 1 is rolled or the player decides to "hold":

 * If a single 1 is rolled, the player scores nothing and the turn ends.
 
 * If two 1s are rolled, the player’s entire score is lost, and the turn ends.
 
 * If the player rolls any other number, it is added to their turn total and the player's turn continues.
 
 * If a double is rolled, the point total is added to the turn total as with any roll but the player is obligated to roll again.
 
 * If a player chooses to "hold", their turn total is added to their score, and it becomes the next player's turn.

The first player to 100 or more points wins.

The program should ask for the number of players, then create an array of *Player*s.  The *Player* class should have a name instance variable and a score instance variable. Once the players are initialized the program should start playing the game by giving each player a turn.  

The program should have a function named *playerTurn* that allows the player to decide when to "hold". The function must return the score for the player's turn.

The program should use an instance of the class *PairOfDice* to do the rolling of the dice. (See the text for examples of the class.)

## Turning in the Assignment

The assignment is due on Friday, October 21st at 11:55pm. You may turn it in early. 

1. Conduct a personal review of your code before turning it in. Does your code follow the [Java Coding Standard](../references/reading-java-coding-standard.html)?

   Is it clear and well commented?

2. Test your code.

    * Does it produce the correct output? 

3. Sign into Laulima, then navigate to the ICS111 site. In the left hand side of the site, there is an Assignments tab/link.  Click on it and view all of the posted assignments. Select the assignment that you want to turn in and attach your files and accept the honor pledge to submit the assignment.
  
