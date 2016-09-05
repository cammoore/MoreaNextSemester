---
morea_id: experience-heap-practice
morea_type: experience
title: "Heap Practice Quiz"
published: True
morea_summary: "Write the reheap method."
morea_sort_order: 4
morea_labels: 
  - "Practice Quiz"
---

Heap Practice Quiz

Practice Problem

* Take out a piece of paper and put your name on the upper right corner.

* **Write a reHeap() method for the following Max Heap.**

{% highlight java %}
public class MaxHeap<E> {
  private E[] heap;
  private Comparator<E> c;
  private int size;

  /**
   * Re-heap the heap so that the largest value is on top of 
   * the heap. Assume the new item is at size - 1.
   */
  private void reHeap() {
   // your code
  }
  
}
{% endhighlight %}

* You can use a helper method.
* Be sure to write JavaDoc comments for your code.
* After the code, write an explanation the Big-O performance of the reHeap method.

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

{% include youtube.html id="_to7mdMIFMI" %}
