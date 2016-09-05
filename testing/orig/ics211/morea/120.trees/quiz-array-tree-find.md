---
morea_id: quiz-array-tree-find
morea_type: experience
title: "Q19: Binary Search Tree find() method"
published: True
morea_summary: "Write the find(E e) method for an Array based Binary Search Tree."
morea_sort_order: 4
morea_labels: 
  - "Quiz"
---

## Q19: Binary Search Tree find() method

Take out a piece of paper and put your name on the upper right corner.

* **Implement the find(E item) method for a Binary Search Tree.** Use the Comparator&lt;E&gt; c to determine the order.

{% highlight java %}
public class BinarySearchTree<E> {
  private E[] treeData;
  private Comparator<E> c;

  public E find(E item) {
   // your code
  }

}
{% endhighlight %}

**Hint:** Left child index = 2 x parentIndex + 1. Right child index = 2 x parentIndex + 2. ParentIndex = (childIndex -1)/2

* You can use a helper method.

* Be sure to write JavaDoc comments for your code.

* Conduct a quick review of your code, before you are done.

* After the code, write an explanation the Big-O performance of the method(s).

* Hand in your code when you are done.

{% include quiz-timer2.html time="15" %}