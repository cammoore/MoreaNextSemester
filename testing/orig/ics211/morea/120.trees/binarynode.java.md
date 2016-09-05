---
morea_id: binarynode-java
morea_type: reading
title: "BinaryNode.java"
published: True
morea_summary: "Base code for assignment 9."
morea_sort_order: 36
morea_labels: 
  - "Homework Assignment"
---

{% highlight java %}
/** 
  * A node in a binary tree 
  * @author         Edo Biagioni
  * @lecture        ICS 211 Mar 15 or later
  * @date           March 14, 2011
  * @bugs           private class: include this code within a larger class
  */

private static class BinaryNode<T> {
  private T item;
  private BinaryNode<T> left;
  private BinaryNode<T> right;


/** 
  * Constructor to build a node with no subtrees
  * @param the value to be stored by this node
  */
  private BinaryNode(T value) {
    item = value;
    left = null;
    right = null;
  }


/** 
  * Constructor to build a node with a specified (perhaps null) subtrees
  * @param the value to be stored by this node
  * @param the left subtree for this node
  * @param the right subtree for this node
  */
  private BinaryNode(T value, BinaryNode<T> l, BinaryNode<T> r) {
    item = value;
    left = l;
    right = r;
  }
}
{% endhighlight %}
