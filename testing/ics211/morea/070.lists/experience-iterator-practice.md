---
morea_id: experience-iterator-practice
morea_type: experience
title: "Iterator Practice Quiz"
published: True
morea_summary: "Write next method for the LinkedListIterator class."
morea_sort_order: 4
morea_labels: 
  - "Practice Quiz"
---

Iterator Practice Quiz

Practice Problem

* Take out a piece of paper and put your name on the upper right corner.

* **Write the following method for the LinkedListIterator class:**

{% highlight java %}
public class LinkedList<E> implements List<E> {
  private LinkedNode<E> head;
  private int size;

   ...

  private class LinkedListIterator<E> implements Iterator<E> {
    private LinkedNode<E> next;
    ...
    public E next() {
      // your code here.
    }
    ...
  }
}
{% endhighlight %}

  * Be sure to write JavaDoc comments for your code.

* Conduct a quick review of your code, before you are done.

* After the code, write an explanation the Big-O performance of the next method.

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

{% include youtube.html id="BdbCi3GPfSU" %}

