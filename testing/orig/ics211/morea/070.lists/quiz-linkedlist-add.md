---
morea_id: quiz-linkedlist-add
morea_type: experience
title: "Quiz 7: LinkedList add Quiz"
published: True
morea_summary: "Write the add method for the LinkedList class."
morea_sort_order: 4
morea_labels: 
  - "Quiz"
---
LinkedList *add* Quiz

* Take out a piece of paper and put your name on the upper right corner.

* **Write a Generic Java class LinkedList&lt;E&gt; that has one method:**

{% highlight java %}
public class LinkedList<E> implements List<E> {
  /** Holds the head of the list. */
  private LinkedNode<E> head;
  /** The size of the list. */
  private int size;

  public E add(E item) {
    // Your code goes here.
  }
}
{% endhighlight %}

  The method must add the item to the end of the list.

  * Be sure to write JavaDoc comments for your code.

* Conduct a quick review of your code, before you turn it in.

* After the code, write an explanation the Big-O performance of the *add* method.

* Hand in your code when you are done.

* Take a short break and be back in your seats at <span id="return_time"></span>


**Time remaining:**
<script src="{{ site.baseurl }}/js/countdown.js" type="text/javascript"></script>

<!-- =========================================================== -->
<script type="application/javascript">
var quizTime = 15;
var myCountdown2 = new Countdown({
									time: quizTime * 60,
									width:150,
									height:80,
									rangeHi:"minute"	// <- no comma on last item!
									});

var currentTime = new Date();
var h = currentTime.getHours();
var m = currentTime.getMinutes();
m = m + quizTime + 5;
if (m > 60) {
  h++;
  m = m % 60;
}
if (h > 12) {
  h = h - 12;
}
var returnTime = "" + h + ":";
if (m < 10){
  returnTime = returnTime + "0";
}
returnTime = returnTime + m;
$("#return_time").text(returnTime);
</script>

