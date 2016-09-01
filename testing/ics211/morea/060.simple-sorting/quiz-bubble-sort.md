---
morea_id: quiz-bubble-sort
morea_type: experience
title: "Q05: Bubble Sort"
published: True
morea_summary: "Write a simple Java Class that has a bubbleSort method."
morea_labels:
  - Quiz
morea_sort_order: 
#morea_start_date: "2016-01-12"
#morea_end_date: "2016-01-13"
---

## Q05: Simple Sorting Quiz

* Take out a piece of paper and put your name on the upper right corner.

* **Write a Generic Java class ArraySorter&lt;E&gt; that has one method:**

{% highlight java %}
public void bubbleSort(E[] data, Comparator<E> c);
{% endhighlight %}
Remember *Comparator* is the following interface.
{% highlight java %}
public interface Comparator<E> {
  int compare(E o1, E o2);
}
{% endhighlight %}


The method must use the Bubble Sort algorithm to sort the data array.

* Be sure to write JavaDoc comments for your code.

* Conduct a quick review of your code, before you turn it in.

* After the code, write an explanation the Big-O performance of the insertionSort method.

* Hand in your code when you are done.

{% include quiz-timer2.html time="15" %}
