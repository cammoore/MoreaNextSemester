---
morea_id: inclass-w5-c2
morea_type: experience
title: "Practice: DoubleLinkedLists"
published: True
morea_summary: "More LinkedLists"
morea_labels:
morea_sort_order:
morea_start_date: "2016-09-21T10:30:00"
---

# Practice: DoubleLinkedList

**Take out a piece of paper. We'll be programming on paper.**

### Problem 1

* **Write a Generic Java class DLinkedList&lt;E&gt;:**

{% highlight java %}
public class DLinkedList<E> implements List211<E> {
  /** Holds the head of the list. */
  private DLinkedNode<E> head;
  /** The size of the list. */
  private int size;

  // Your code goes here.

  /** Doubly linked node. */
  private class DLinkedNode<E> {
    E data;
    DLinkedNode<E> next;
    DLinkedNode<E> prev;
  }
}
{% endhighlight %}

* Be sure to write JavaDoc comments for your code.

### Problem 2

* **Answer the following questions:**

  * What is the Big-O of the **add(E item)** method? Why?
  
  * What is the Big-O of the **remove(int index)** method? Why?


## Show me your code before you leave

