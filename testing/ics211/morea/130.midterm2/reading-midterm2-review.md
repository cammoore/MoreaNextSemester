---
morea_id: reading-midterm2-review
morea_type: reading
title: "Midterm 2 Review"
published: True
morea_summary: "Review for Midterm #2."
morea_start_date: "2016-10-31"
morea_labels: 
  - "Lecture"
---

# Outline

* Stacks
* Prefix, Infix, Postfix Notation
* Queues
* Recursion

## Format

* Similar to Midterm 1. Closed book, notes, neighbor, computer, phone, etc.
* Material from screencasts, quizzes, lectures, book, assignments.
* All the material in Chapters 3.1-3.4, 4-4.5, 5-5.6


## Stacks

 * Last-In First-Out (LIFO) Data structure
 * Stack Interface
    * Empty
    * Peek
    * Pop
    * Push

 * Two implementations
    * Array
    * Linked
    * Big O
    
 * Uses

## Prefix, Infix, Postfix Notation

  * Prefix: operator before operands
  * Infix: operator between operands, needs precedence and parentheses
  * Postfix: operator after operands
  * Implementing Prefix and Infix require two stacks
  * Implementing Postfix only requires one

## Queues

 * First-In First-Out (FIFO) Data structure
 * Queue Interface
    * boolean add(E item)
    * boolean offer(E item)
    * E element()
    * E peek()
    * E poll()
    * E remove()
    * int size()
    
  * Two implementations
      * Array
      * Linked
      * Big O
      
  * Uses

## Recursion

  * Useful problem solving technique
    * Problem has a simple base case
    * Can reduce the problem by solving a smaller problem closer to the base case
  
  * In Java recursion is at the Method level
    * Use the Activation Stack to remember
    * Parameters of the method encode the problem
    
  * Useful in describing some data structures
    * Linked List
    * Binary Tree
    * Binary Search Tree
    
  * Useful in manipulating recursive data structures
