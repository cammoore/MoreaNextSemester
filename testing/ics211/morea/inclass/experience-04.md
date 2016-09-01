---
morea_id: experience-04
morea_type: experience
title: "IC04: Lists Practice"
published: True
morea_summary: "Write the LinkedList remove method."
morea_sort_order: 4
morea_labels: 
  - "In class"
  - "2/9"
---

# IC04: LinkedList remove method


**Step 1** 30 minutes.

* Form teams of two.
* Introduce yourself to your partner.
* Take out a piece of paper, put put both your names on the top right of the paper.

* **Implement the LinkedList remove method that removes the item at the given index.**

{% highlight java %}
public class LinkedList<E> {
  private LinkedNode<E> head;
  private int size;

  public E remove(int index) {
    // your code
  }

  private class LinkedNode<E> {
    private E data;
    private LinkedNode<E> next;
  }
}
{% endhighlight %}

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

