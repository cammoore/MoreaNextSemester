---
morea_id: inclass-w3-c2
morea_type: experience
title: "Practice: Reading Code"
published: True
morea_summary: "Find the errors in the code."
morea_labels:
morea_sort_order:
morea_start_date: "2016-09-07T10:30:00"
---

# Practice: Reading Code

* Take out a sheet of paper.

* Form teams of two.

### Problem 1

* Write down the bugs in the following code.

{% highlight java %}
01   public void 3Sorts(E[] data, Comparator<E> c) {
02     for (int i = 0; i <= data.length; i++) {
03       for (int j = i; j < data.length; j++) 
04         int temp = data[j];
05         if (data[j] > data[j + 1]) {
06           swap(data[j], data[j + 1];
07         }
08       }
09     }
10   }
11
12
13   private E getMinimum(E[] data, Comparator<E> c)
14     int min = data[0];
15     for (int i = 0; i < data.length; i += 2) {
16       if (c.compare(min, data[i]) < 0) {
17         min = data[i];
18       }
19     }
20     return min;
21   }
{% endhighlight %}

### Problem 2

In your teams write a generic Java class ArraySorter&lt;E&gt; that has one method:

{% highlight java %}
public void insertionSort(E[] data, Comparator<E> c);
{% endhighlight %}
Remember *Comparator* is the following interface.
{% highlight java %}
public interface Comparator<E> {
  int compare(E o1, E o2);
}
{% endhighlight %}

The **insertionSort** method must use the insertion sort algorithm to sort the **data** array.

### Problem 3

In your teams add the **selectionSort** method to your generic Java class ArraySorter&lt;E&gt;.

{% highlight java %}
public void selectionSort(E[] data, Comparator<E> c);
{% endhighlight %}
Remember *Comparator* is the following interface.
{% highlight java %}
public interface Comparator<E> {
  int compare(E o1, E o2);
}
{% endhighlight %}

The **selectionSort** method must use the selection sort algorithm to sort the **data** array.


## Show me your code before you leave

