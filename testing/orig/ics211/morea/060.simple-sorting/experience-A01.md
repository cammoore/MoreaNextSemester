---
morea_id: experience-A01
morea_type: experience
title: "A01: Sorting Java Arrays"
published: True
morea_summary: "Write a Generic Java Class that supports sorting Arrays."
morea_sort_order: 8
morea_start_date: "2016-09-09T23:55:00"
morea_labels: 
  - "Homework Assignment"
---

# ICS 211 Homework A01: Sorting Arrays

* Create a Generic Java class named ArraySort that has three methods:

{% highlight java %}

public void insertionSort(E[] data, Comparator<? super E> compare);
public void bubbleSort(E[] data, Comparator<? super E> compare);
public void selectionSort(E[] data, Comparator<? super E> compare);

{% endhighlight %}

Each method should implement the named simple sort algorithm on the array data.  Use the [Comparator&lt;E&gt;](http://docs.oracle.com/javase/7/docs/api/java/util/Comparator.html) to determine the order of the items in the array. Sort the arrays in ascending order.  The 'smallest' element should be in position 0, 'largest' in array.length - 1.

The methods should keep track of the number of comparisons, number of swaps and the amount of time it took to sort the array. To record the time taken, your code should call [System.nanoTime](http://docs.oracle.com/javase/7/docs/api/java/lang/System.html#nanoTime()) at the beginning of each of the methods and save the value as the start time. It should then call [System.nanoTime](http://docs.oracle.com/javase/7/docs/api/java/lang/System.html#nanoTime()) again at the end, and print the difference between the two times.  The difference may be zero if your system clock does not update the time quickly enough, but otherwise should accurately report how many nanoseconds (billionths of a second) it took to execute your code. When the sort methods complete they should report the number of comparison, swaps, and the execution time in nanoseconds.

Be sure to thoroughly test your code. Turn in your test code along with your Class.

## Algorithm Analysis

Write up a runtime analysis of each of the sorting methods, giving the big-O of each, and explaining how you got your results. Send your analysis to the TA together with your code. This part counts for 25% of the grade on this assignment. Even if your code doesn't work, you should do this part to the best of your ability.


## Turning in the Assignment

The assignment is due on Friday at 11:55pm. You may turn it in early. 

1. Conduct a personal review of your code before turning it in. Does your code follow the
   [Java Coding Standard](morea/010.introduction/reading-java-coding-standard.html)?
   Is it clear and well commented?
2. Test your code.
    * What happens if the data array has nulls in it?
3. Sign into Laulima, then navigate to the ICS211 site. In the left hand side of the site, there is an Assignments tab/link.  Click on it and view all of the posted assignments. Select the assignment that you want to turn in and attach your files and accept the honor pledge to submit the assignment.
  
