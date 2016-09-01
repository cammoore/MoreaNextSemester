---
morea_id: inclass-w9-c2
morea_type: experience
title: "Practice: Classes"
published: True
morea_summary: "Playing the Pig game."
morea_labels:
  - In class
morea_sort_order:
morea_start_date: "2016-10-20T00:00:00"
---

# Practice: Classes

**Take out a piece of paper. We'll be programming on paper.**

### Problem 1

Write a subroutine that takes a *Player* parameter.  The subroutine should play a single turn of the Two-Dice Pig Game.

You can assume that the *PairOfDice* class exists and it has a method *roll()* and accessor methods *getDie1()* and *getDie2()*.

Each turn in the Two-Dice Pig Game, a player repeatedly rolls two dice until a 1 is rolled or the player decides to "hold":

 * If a single 1 is rolled, the player scores nothing and the turn ends.
 
 * If two 1s are rolled, the player’s entire score is lost, and the turn ends.
 
 * If the player rolls any other number, it is added to their turn total and the player's turn continues.
 
 * If a double is rolled, the point total is added to the turn total as with any roll but the player is obligated to roll again.
 
 * If a player chooses to "hold", their turn total is added to their score, and it becomes the next player's turn.
 
The subroutine should update the *Player*'s score after the end of the turn.


## Show me your code before you leave
