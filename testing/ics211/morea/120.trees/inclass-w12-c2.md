---
morea_id: inclass-w12-c2
morea_type: experience
title: "Practice: Binary Trees"
published: True
morea_summary: "Working with Binary Trees"
morea_labels:
morea_sort_order:
morea_start_date: "2016-11-09T10:30:00"
---

# Practice: Binary Search Trees

**Take out a piece of paper. We'll be programming on paper.**

### Problem 1

* **Implement the find(E e) method for a Binary Search Tree.** Use the Comparator&lt;E&gt; c to determine the order.

{% highlight java %}
public class BinarySearchTree<E> {
  private BinaryNode<E> root;
  private Comparator<E> c;

  public E find(E e) {
   // your code
  }

  private class BinaryNode<E> {
    private E data;
    private BinaryNode<E> left;
    private BinaryNode<E> right;
  }
}
{% endhighlight %}

* You should use a recursive helper method.

## Show me your code before you leave
