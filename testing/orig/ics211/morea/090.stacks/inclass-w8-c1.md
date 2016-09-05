---
morea_id: inclass-w8-c1
morea_type: experience
title: "Practice: Stacks"
published: True
morea_summary: ""
morea_labels:
morea_sort_order:
morea_start_date: "2016-10-10T10:30:00"
---

# Practice: Array Stacks

**Take out a piece of paper. We'll be programming on paper.**

Write Java code for the following problem.

### Problem 1

**Implement the ArrayStack class:**

{% highlight java %}
public interface Stack211<E> {
  boolean empty();
  E peek();
  E pop();
  E push(E item);
}

public class ArrayStack<E> implements Stack211<E> {
  private E[] data;
  private int top;

  // your code here.

}
{% endhighlight %}

### Problem 2

**Answer the following questions:**

* What value should top be initialized to in the ArrayStack constructor? Why?

* When do we need to resize the **data** array?

## Show me your code before you leave
