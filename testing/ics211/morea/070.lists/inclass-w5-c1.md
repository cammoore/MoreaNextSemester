---
morea_id: inclass-w5-c1
morea_type: experience
title: "Practice: LinkedList add"
published: True
morea_summary: "Practice implementing the LinkedList."
morea_labels:
morea_sort_order:
morea_start_date: "2016-09-19T10:30:00"
---

# Practice: LinkedList

**Take out a piece of paper. We'll be programming on paper.**

### Problem 1

* **Write a Generic Java class LinkedList&lt;E&gt;:**

{% highlight java %}
public class LinkedList<E> implements List211<E> {
  /** Holds the head of the list. */
  private LinkedNode<E> head;
  /** The size of the list. */
  private int size;

  // Your code goes here.

}
{% endhighlight %}

* Be sure to write JavaDoc comments for your code.

### Problem 2

* **Answer the following questions:**

  * What is the Big-O of the **get** method?
  
  * Why do we keep track of **size**?

  * How can we make the **add(E item)** method more efficient?

## Show me your code before you leave
