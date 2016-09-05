---
morea_id: quiz-binarytree-tostring-pre
morea_type: experience
title: "Q17: Binary Tree Pre-order toString()"
published: True
morea_summary: "Write a pre-order toString() method for a Binary Tree."
morea_sort_order: 4
morea_labels: 
  - "Quiz"
---

Take out a piece of paper and put your name on the upper right corner.

* **Implement a pre-order toString() method for a Binary Tree.** Use a pre-order traversal of the tree, printing out the node data.

{% highlight java %}
public class BinaryTree<E> {
  private BinaryNode<E> root;

  public String toString() {
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

* What is the BigO for the *toString()* method?

* Hand in your code when you are done.

{% include quiz-timer2.html time="15" %}