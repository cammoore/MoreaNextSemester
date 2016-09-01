---
morea_id: inclass-w10-c1
morea_type: experience
title: "Practice: Binary Search"
published: True
morea_summary: "Recursive Binary Search"
morea_labels:
morea_sort_order:
morea_start_date: "2016-10-24T10:30:00"
---


# Practice: Recursive Binary Search

**Take out a piece of paper. We'll be programming on paper.**

* **Write a recursive method to search a sorted array:**

{% highlight java %}
/**
 * @return the index of value in the sorted array data, or -1 if value is not in the array.
 */
public static int binarySearch(E[] data, E value, Comparator<E> c) { // the data array is sorted.
  // your code here.
  // you can use a recursive helper method
}
{% endhighlight %}

The binary search algorithm decides which half of the array the value is in by comparing the value to the middle of the array then searching the correct half.


## Show me your code before you leave
