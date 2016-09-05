---
morea_id: inclass-w6-c1
morea_type: experience
title: "Practice: Array Iterators"
published: True
morea_summary: "Implementing Iterators."
morea_labels:
morea_sort_order:
morea_start_date: "2016-09-26T10:30:00"
---

# Practice: ArrayList Iterators

**Take out a piece of paper. We'll be programming on paper.**

### Problem 1

* **Write a Generic Java class ArrayListIterator&lt;E&gt;.**

{% highlight java %}
public interface Iterator211<E> {
  /** @return true if the iteration has more elements. */
  boolean hasNext();
  /** @return The next element in the iteration. */
  E next();
}

public class ArrayList<E> implements List211<E> {
  /** Holds the items in the list. */
  private E[] data;
  /** The size of the list. */
  private int size;
  
  private class ArrayListIterator<E> implements Iterator<E> {

    // your code goes here.

  }
}
{% endhighlight %}

### Problem 2

* **Answer the following questions:**

  * What is the Big-O of the **next** method?
  
  * How do we keep track of of the itteration?


## Show me your code before you leave


