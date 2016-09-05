---
morea_id: quiz-linkedlist-set
morea_type: experience
title: "Q08: LinkedList set Quiz"
published: True
morea_summary: "Write the set method for the LinkedList class."
morea_sort_order: 4
morea_labels: 
  - "Quiz"
---
LinkedList *set* Quiz

* Take out a piece of paper and put your name on the upper right corner.

* **Write a Generic Java class LinkedList&lt;E&gt; that has one method:**

{% highlight java %}
public class LinkedList<E> implements List<E> {
  /** Holds the head of the list. */
  private LinkedNode<E> head;
  /** The size of the list. */
  private int size;

  public E set(int index, E item) {
    // Your code goes here.
  }
}
{% endhighlight %}

  The method must set the item at the given index.

  * Be sure to write JavaDoc comments for your code.

* Conduct a quick review of your code, before you turn it in.

* After the code, write an explanation the Big-O performance of the *set* method.

* Hand in your code when you are done.


{% include quiz-timer2.html time="15" %}
