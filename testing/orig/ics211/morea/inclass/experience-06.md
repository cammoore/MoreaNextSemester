---
morea_id: experience-06
morea_type: experience
title: "IC06: Queues Practice"
published: True
morea_summary: "Write the ArrayQueue add and offer methods."
morea_sort_order: 4
morea_labels: 
  - "In class"
  - "3/9"
---

# IC06: Write the ArrayQueue add and offer methods.


**Step 1** 30 minutes.

* Form teams of two.
* Introduce yourself to your partner.
* Take out a piece of paper, put put both your names on the top right of the paper.

* **Write the ArrayQueue add and offer methods.**

{% highlight java %}
public class ArrayQueue<E> {
  private E[] data;
  int front;
  int rear;
  int size;

  public boolean add(E item) { /* your code */ }
  public boolean offer(E item) { /* your code */ }
}
{% endhighlight %}

* Your methods should be O(1).
* Be sure to write JavaDoc comments for your code.

<script src="countdown.js" type="text/javascript"></script>

<!-- =========================================================== -->
<script type="application/javascript">
var myCountdown2 = new Countdown({
									time: 25 * 60,
									width:150,
									height:80,
									rangeHi:"minute"	// <- no comma on last item!
									});

</script>

**Step 2**

Introduce yourself to your neighbor team, then switch papers. You will review your neighbor team's program. Put your names underneath the other team's names. Below the program note any errors in the code and at least one good thing about the code.

