---
morea_id: inclass-w3-c1
morea_type: experience
title: "Practice: Sorting"
published: True
morea_summary: ""
morea_labels:
morea_sort_order:
#morea_start_date: "2016-01-12"
#morea_end_date: "2016-01-13"
---


# Practice: Sorting

**Take out a piece of paper. We'll be programming on paper.**

### Problem 1

In your teams write a generic Java class ArraySorter&lt;E&gt; that has one method:

{% highlight java %}
public void bubbleSort(E[] data, Comparator<E> c);
{% endhighlight %}
Remember *Comparator* is the following interface.
{% highlight java %}
public interface Comparator<E> {
  int compare(E o1, E o2);
}
{% endhighlight %}

The **bubbleSort** method must use the bubble sort algorithm to sort the **data** array.

### Problem 2

Answer the following questions:

  * Should **bubbleSort** method be static? 
  * Why or why not?


## Show me your code before you leave
