---
morea_id: experience-linked-queue-practice
morea_type: experience
title: "LinkedQueue Practice Quiz"
published: True
morea_summary: "Write the LinkedQueue implementation of the Queue interface."
morea_sort_order: 4
morea_labels: 
  - "Practice Quiz"
---

LinkedQueue Practice Quiz

Practice Problem

* Take out a piece of paper and put your name on the upper right corner.

* **Write the following method for the LinkedQueue class:**

{% highlight java %}
public interface Queue211<E> {
  boolean add(E e); // add e to the end of the queue. May throw an IllegalStateException
  E element(); // returns the front of the queue w/o removing
  boolean offer(E e); // inserts e to into the queue.
  E peek(); // returns the front of the queue or null.
  E poll(); // removes and returns the front of the queue or null.
  E remove(); // removes and returns the front of the queue, may throw an IllegalStateException.
}

public class LinkedQueue<E> implements Queue211<E> {
  private LinkedNode<E> front;
  private LinkedNode<E> rear;
  private int size;
  ...
  public E poll() {
    // your code here.
  }
  ...
}
{% endhighlight %}

  * Be sure to write JavaDoc comments for your code.

* Conduct a quick review of your code, before you are done.

* After the code, write an explanation the Big-O performance of the poll method.

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

{% include youtube.html id="sgmZ6ZFl_78" %}