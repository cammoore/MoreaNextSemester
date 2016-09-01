---
morea_id: quiz-heapsort-person
morea_type: experience
title: "Quiz 12: HeapSort"
published: True
morea_summary: "Write a Heapsort of an array of Persons."
morea_sort_order: 4
morea_labels: 
  - "Quiz"
  - "4/22"
---

# Quiz 12: Write a Heapsort of an array of Persons.


**30 minutes.**

Take out a piece of paper and put your name on the upper right corner.

* **Implement a Heapsort of an array of Persons.**

{% highlight java %}
public static void heapSort(Person[] array) {
   // your code
}
{% endhighlight %}

* The Person class implements Comparable
{% highlight java %}
public interface Caparable<E> {
  /**
   * Compares this object to o. Returns a negative integer, zero, or a positive integer
   * as this object is less than, equal to, or greater than the specified object.
   */
  int compareTo(E o);
}
{% endhighlight %}

* Be sure to write JavaDoc comments for your code.

###Conduct a quick review of your code, before you turn it in.

# Hand in your code when you are done.

<script src="countdown.js" type="text/javascript"></script>

<!-- =========================================================== -->
<script type="application/javascript">
var myCountdown2 = new Countdown({
									time: 30 * 60,
									width:150,
									height:80,
									rangeHi:"minute"	// <- no comma on last item!
									});

</script>
