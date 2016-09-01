---
morea_id: quiz-binary-search-tree
morea_type: experience
title: "Q18: Binary Search Tree insert() method"
published: True
morea_summary: "Write the insert(E e) method for a Binary Search Tree."
morea_sort_order: 4
morea_labels: 
  - "Quiz"
---

## Q18: Binary Search Tree insert() method.

Take out a piece of paper and put your name on the upper right corner.

* **Implement the insert(E e) method for a Binary Search Tree.** Use the Comparator&lt;E&gt; c to determine the order.

{% highlight java %}
public class BinarySearchTree<E> {
  private BinaryNode<E> root;
  private Comparator<E> c;

  public void insert(E e) {
   // your code
  }

  private class BinaryNode<E> {
    private E data;
    private BinaryNode<E> left;
    private BinaryNode<E> right;
  }
}
{% endhighlight %}

* You can use a helper method.
* Be sure to write JavaDoc comments for your code.
  * Be sure to write JavaDoc comments for your code.

* Conduct a quick review of your code, before you are done.

* After the code, write an explanation the Big-O performance.

* Hand in your code when you are done.

{% include quiz-timer2.html time="15" %}