---
morea_id: experience-binary-search-practice
morea_type: experience
title: "Recursive Search Practice Quiz"
published: True
morea_summary: "Implement a recursive binary search method on a sorted array of ints."
morea_sort_order: 4
morea_labels: 
  - "Practice Quiz"
---
Recursive Search Practice Quiz

Practice Problem

* Take out a piece of paper and put your name on the upper right corner.

* **Write a recursive method to search a sorted array:**

{% highlight java %}
/**
 * @return the index of value in the sorted array data, or -1 if value is not in the array.
 */
public static int binarySearch(int[] data, int value) { // the data array is sorted.
  // your code here.
  // you can use a recursive helper method
}
{% endhighlight %}

The binary search algorithm decides which half of the array the value is in by comparing the value to the middle of the array then searching the correct half.

* Be sure to write JavaDoc comments for your code.

* Conduct a quick review of your code, before you are done.

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

{% include youtube.html id="f7xLcSiVdL4" %}