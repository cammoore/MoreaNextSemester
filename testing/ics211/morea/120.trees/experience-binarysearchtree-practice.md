---
morea_id: experience-binarysearchtree-practice
morea_type: experience
title: "BinarySearchTree Practice Quiz"
published: True
morea_summary: "Write the find() method for a BinarySearchTree."
morea_sort_order: 4
morea_labels: 
  - "Practice Quiz"
---
Binary Tree Traversal Practice Quiz

Practice Problem

* Take out a piece of paper and put your name on the upper right corner.

* **Write the find(E target) method for a BinarySearchTree.**

{% highlight java %}
public class BinarySearchTree<E> {
  private BinaryNode<E> root;
  private Comparator<E> comp;

  public E find(E item) {
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
* After the code, write an explanation the Big-O performance of the binarySearch method.

**Time Remaining:**

<script src="{{ site.baseurl }}/js/countdown.js" type="text/javascript"></script>
<!-- =========================================================== -->
<script type="application/javascript">
var myCountdown2 = new Countdown({
									time: 15 * 60,
									width:150,
									height:80,
									rangeHi:"minute"	// <- no comma on last item!
									});
</script>

You can restart the timer by reloading the page.

**Try to complete the problem in 15 minutes.**

If you cannot complete the program in 15 minutes, you can watch me solve the problem in a text editor.

{% include youtube.html id="n_DbGQTRjhw" %}