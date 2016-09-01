---
morea_id: experience-A07
morea_type: experience
title: "A07: Recursive Hexadecimal Sudoku Solver"
published: True
morea_summary: "Implement a recursive method to solve a given Hexadecimal Sudoku problem."
morea_start_date: "2016-10-28T23:55:00"
morea_labels: 
  - "Homework Assignment"
---

# ICS 211 Homework A07: Recursive Sudoku Solver

In this assignment, you implement a recursive method to find a solution to a given Hexadecimal Sudoku problem.

A Sudoku is a 16x16 grid of integers, each with values 0..F.

A Sudoku is valid when each of the 16 rows, each of the 16 columns, and each of the 16 4x4 boxes in the grid has exactly one each of the possible values 0..F, without any duplicates.

A Sudoku problem is a Sudoku grid with some of the grid cells already filled. The solution fills the remaining cells to give a valid Sudoku.

A recursive strategy for finding a solution to a Sudoku problem is as follows:

1. If all cells are filled, see if this Sudoku is valid. If it is, we  have found a solution. If not, this Sudoku is not a solution.

2. If at least one cell is not filled, see what values are legal in this cell:

  * If no values are legal, then this Sudoku is not a solution.

  * If one or more values are legal, place each legal values in the cell in turn, one at a time. For each, recursively attempt to find a solution that fills the remaining empty cells.

    If a solution is found for at least one legal value, set the Sudoku to reflect this solution, and return that a solution was found.

    If no solution is found for any legal value, reset this cell to the value it had when this method was called, and report that this Sudoku does not have a solution.

    Every time the code recursively attempts to find a solution, it will fill cells in the Sudoku grid. If the attempt is not successful, returning, your code must restore the Sudoku grid to the values had before the call.


This algorithm is an example of **backtracking**: at any point in the search, try any one of the available options. If that option doesn't work, return to that point, and try a different option, until all the available options have been tried.

Most of the code you will need has been provided at [HexadecimalSudoku.java](hexadecimalSudoku.java.html) and [HexadecimalSudokuTest.java](hexadecimalSudokuTest.java.html). In particular, the method *checkSudoku* returns true if a Sudoku is valid, and false otherwise (it can also print where a Sudoku is invalid). The method *toString* will convert a Sudoku to a printable form, again with an option to check the validity of the Sudoku and provide more information.

[HexadecimalSudokuTest.java](hexadecimalSudokuTest.java.html) also provides some test Sudoku with solutions.

All this code assumes that a Sudoku is represented as a 16-element array of rows, where each row is a 16-element array of ints. Each of the ints must have a value in 0..F. The value -1 represents an empty cell.

You must implement the at least two methods:

1. **public static boolean solveSudoku (int [] [] sudoku)** This method recursively fills all the empty Sudoku cells with values in 0..F. Your method should return true if a solution exists, and return false otherwise. If the method returns true, it must fill in the Sudoku with a valid solution. If it returns false, it must leave the Sudoku unchanged.

1. **private static ArrayList&lt;Integer&gt; legalValues(int [] [] sudoku, int row, int column)** This method should return an ArrayList of all the legal values for the given cell. If the cell is not empty the method should return *null*. You must use this method in your recursive solution. If there are no valid values then the ArrayList should be empty.

Your solution must be recursive. You may want to write a recursive helper method rather than making the *solveSudoku* method recursive, but this choice is up to you.

Your *solveSudoku* code must use a for loop to test each of the legal values for one cell. The values must come from the **levalValues** method. Your solution must use recursion to try to find values for all the other empty cells.

**Note** that *checkSudoku* doesn't verify that all cells are filled  -- it just verifies that none of the Sudoku rules are broken.

Also note that people do not generally use backtracking to solve Sudoku. There are Sudoku problems that are difficult for humans to solve, but easy for recursive algorithms to solve. 

## Testing

You must also build your own test code to make sure that your implementation works. Turn in your test code together with the Sudoku class with the implemented **solveSudoku** and **legalValues** methods.

Please thoroughly test your code and briefly discuss your testing strategy. Turn in all test code.

## Discussion

When your algorithm attempts to solve **example3** and **example4** you might notice some issues.  Please write a short discussion of what the issues are with solving these examples (2 - 3 paragraphs).  Turn in your discussion with your code.

## Turning in the Assignment

The assignment is due on Friday at 11:55pm. You may turn it in early. 

1. Conduct a personal review of your code before turning it in. Does you code follow the [Java Coding Standard](../010.introduction/reading-java-coding-standard.html)? Is it clear and well commented?
2. Test your code. Do you get the same answer as the solution?
3. Sign into Laulima, then navigate to the ICS211 site. In the left hand side of the site, there is an Assignments tab/link.  Click on it and view all of the posted assignments. Select the assignment that you want to turn in and attach your files and accept the honor pledge to submit the assignment. 
  
