---
morea_id: experience-linkedstack-practice
morea_type: experience
title: "LinkedStack Practice Quiz"
published: True
morea_summary: "Write the LinkedStack implementation of the Stack interface."
morea_sort_order: 4
morea_labels: 
  - "Practice Quiz"
---

LinkedStack Practice Quiz

Practice Problem

* Take out a piece of paper and put your name on the upper right corner.

* **Write the following method for the LinkedStack class:**

{% highlight java %}
public interface Stack211<E> {
  boolean empty();
  E peek();
  E pop();
  E push(E item);
}

public class LinkedStack<E> implements Stack211<E> {
  private LinkedNode<E> topOfStack;
  ...
  public E push(E item) {
    // your code here.
  }
  ...
}
{% endhighlight %}

  * Be sure to write JavaDoc comments for your code.

* Conduct a quick review of your code, before you are done.

* After the code, write an explanation the Big-O performance of the push method.

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

{% include youtube.html id="J_ZPxEZxJ0g" %}