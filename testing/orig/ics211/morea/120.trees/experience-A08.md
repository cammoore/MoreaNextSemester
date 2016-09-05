---
morea_id: experience-A08
morea_type: experience
title: "A08: Sort by using a Binary Search Tree"
published: True
morea_summary: "Implement a BinarySearchTree and use it to sort Contacts."
morea_start_date: "2016-11-18T23:55:00"
morea_sort_order: 32
morea_labels: 
  - "Homework Assignment"
---


# ICS 211 Homework A08: Binary Search Tree

In this assignment you will implement a BinarySearchTree class, Contact class, ContactComparator, and use them to sort the Contacts.

A `Contact` has a first name, last name, contact number.

The `ContactComparator` must implement the `Comparator` interface. It should sort by last name then first name.

The `BinarySearchTree` must:

  * implement the SearchTree interface,
  * use a Comparator to decide order,
  * and have a method `inorderString` that prints out the contacts in sorted order.

{% highlight java %}
public interface SearchTree<E> {
  /**
   * Inserts item into where it belongs in the tree.
   * @return true if item is inserted, false if item is already in tree.
   */
  boolean add(E item);
  /**
   * @return true if item is in the tree, false otherwise.
   */
  boolean contains(E item);
  /**
   * @return a reference to the target if found, null if target isn't in the tree.
   */
  E find(E target);
  /**
   * Removes target from the tree.
   * @return a reference to the target if found, null if target isn't in the tree.
   */
  E delete(E target);
  /**
   * Removes target from the tree.
   * @return true if target was in the tree, false otherwise.
   */
  boolean remove(E target);
}

public class BinarySearchTree<E> implements SearchTree<E> {
  private Comparator<E> comp;

  /**
   * Creates a new BinarySearchTree.
   * @param c the comparator to use for determining order.
   */
  public BinarySearchTree(Comparator<E> c) {
    ...
  }

  /**
   * @return the contacts in order as a string.
   */
  public String inorderString() {
    ...
  }
  // implement this class.
}
{% endhighlight %}

You need another class with a `main` method that creates the BinarySearchTree, adds several `Contacts` then prints them out in order.


## Algorithm Analysis

Write up a runtime analysis of each of the use of a Binary Search Tree to sort, giving the big-O for sorting, and explaining how you got your results. Send your analysis to the TA together with your code. This part counts for 25% of the grade on this assignment. Even if your code doesn't work, you should do this part to the best of your ability.


## Testing

You must also build your own test code to make sure that your implementation works.

Please thoroughly test your code and briefly discuss your testing strategy. Turn in all test code.

## Turning in the Assignment

The assignment is due on Friday at 11:55pm. You may turn it in early.

1. Conduct a personal review of your code before turning it in. Does your code follow the [Java Coding Standard](../010.introduction/reading-java-coding-standard.html)?
   Is it clear and well commented?
2. Test your code. Does your solution work on the Sudoku puzzles in the newspaper?
3. Sign into Laulima, then navigate to the ICS211 site. In the left hand side of the site, there is an Assignments tab/link.  Click on it and view all of the posted assignments. Select the assignment that you want to turn in and attach your files and accept the honor pledge to submit the assignment.
 
