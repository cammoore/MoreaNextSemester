---
morea_id: inclass-w6-c2
morea_type: experience
title: "Practice: Iterators"
published: True
morea_summary: "More Iterators"
morea_labels:
morea_sort_order:
morea_start_date: "2016-09-28T10:30:00"
---

# Practice: LinkedList Iterators

**Take out a piece of paper. We'll be programming on paper.**

### Problem 1

* **Write a Generic Java class LinkedListIterator&lt;E&gt;.**

{% highlight java %}
public interface Iterator211<E> {
  /** @return true if the iteration has more elements. */
  boolean hasNext();
  /** @return The next element in the iteration. */
  E next();
}

public class LinkedList<E> implements List211<E> {
  /** Holds the items in the list. */
  private LinkedNode<E> head;
  /** The size of the list. */
  private int size;
  
  private class LinkedListIterator<E> implements Iterator<E> {

    // your code goes here.

  }
}
{% endhighlight %}

### Problem 2

* **Answer the following questions:**

  * What is the Big-O of the **hasNext** method?
  
  * How do we keep track of of the iteration?

## Show me your code before you leave

