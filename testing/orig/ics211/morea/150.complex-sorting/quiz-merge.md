---
morea_id: quiz-merge
morea_type: experience
title: "Q24: Merge two sorted arrays into a third array."
published: True
morea_summary: "Implement the merge method."
morea_sort_order: 4
morea_labels: 
  - "Quiz"
---

# Q24: Merge two sorted arrays into a third array.

Take out a piece of paper and put your name on the upper right corner.

* **Implement the merge(E[] left, E[] right, E[] result) method.** Use the Comparator&lt;E&gt; c to determine the order.

{% highlight java %}
public class Merge<E> {
  private Comparator<E> c;

  /**
   * Merges left and right, sorted arrays into result. Result is large enough
   * to hold both left and right.
   * @param left a sorted array.
   * @param right a sorted array.
   * @param result the sorted combination of left and right.
   */
  public void merge(E[] left, E[] right, E[] result) {
   // your code
  }

}
{% endhighlight %}

* Be sure to write JavaDoc comments for your code.

* Conduct a quick review of your code, before you are done.

* After the code, write an explanation the Big-O performance of the merge method.

* **Bonus point:** What is the difference between a binary search and a binary search tree?

* Hand in your code when you are done.

{% include quiz-timer2.html time="20" %}