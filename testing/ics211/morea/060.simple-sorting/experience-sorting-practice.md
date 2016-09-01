---
morea_id: experience-sorting-practice1
morea_type: experience
title: "Simple Sorting Practice Quiz"
published: True
morea_summary: "Write a simple Java Class that has a bubbleSort method."
morea_sort_order: 4
morea_labels: 
  - "Practice Quiz"
---

Simple Sorting Practice Quiz

Practice Problem

* Take out a piece of paper and put your name on the upper right corner.

* **Write a simple Java class that has one static method:**

{% highlight java %}
public static <E> void bubbleSort(E[] data, Comparator<E> compare);
{% endhighlight %}

  The method must use the Bubble Sort algorithm to sort the data array.

  Remember the Comparator&lt;E&gt; interface defines the following method:
{% highlight java %}
int compare(E o1, E o2); // Returns negative if o1 < o2, 0 if equal, positive if o1 > o2
{% endhighlight %}

  * Be sure to write JavaDoc comments for your code.

* Conduct a quick review of your code, before you are done.

* After the code, write an explanation the Big-O performance of the bubbleSort method.

{% include quiz-timer2.html time="25" %}

**Try to complete the problem in 25 minutes.**

If you cannot complete the program in 25 minutes, you can watch me solve the problem in a text editor.

{% include youtube.html id="plShqNpeQK8" %}
