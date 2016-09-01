---
morea_id: experience-A10
morea_type: experience
title: "A09: Sorting Performance"
published: True
morea_summary: "Implement Heapsort, Quicksort, Mergesort."
morea_start_date: "2016-12-02T23:55:00"
morea_sort_order: 40
morea_labels: 
  - "Homework Assignment"
---

# ICS 211 Homework A10: Sorting Performance

In this assignment your are going to modify your ArraySort program from Assignment 01 to add the following sorting methods:

{% highlight java %}

public void heapSort(E[] data, Comparator<? super E> compare);
public void mergeSort(E[] data, Comparator<? super E> compare);
public void quickSort(E[] data, Comparator<? super E> compare);

{% endhighlight %}


The methods should keep track of the number of comparisons, number of swaps and the amount of time it took to sort the array. To record the time taken, your code should call [System.nanoTime](http://docs.oracle.com/javase/7/docs/api/java/lang/System.html#nanoTime()) at the beginning of each of the methods and save the value as the start time. It should then call [System.nanoTime](http://docs.oracle.com/javase/7/docs/api/java/lang/System.html#nanoTime()) again at the end, and print the difference between the two times.  The difference may be zero if your system clock does not update the time quickly enough, but otherwise should accurately report how many nanoseconds (billionths of a second) it took to execute your code. When the sort methods complete they should report the number of comparison, swaps, and the execution time in nanoseconds.

## Algorithm Analysis

Use the following three files, [A10-1000-words.txt](A10-1000-words.txt), [A10-5000-words.txt](A10-5000-words.txt), and [A10-10000-words.txt](A10-10000-words.txt) to create Arrays of Strings, sort the arrays using the six sorting methods build a table showing the size of the array, number of comparisons, number of swaps and the amount of time it took to run for all sorting methods for the three different files.

Write up a runtime analysis of each of the six sorting methods, giving the big-O of each, and explaining how you got your results. Send your analysis to the TA together with your code. This part counts for 25% of the grade on this assignment. Even if your code doesn't work, you should do this part to the best of your ability.


## Testing

You must also build your own test code to make sure that your implementation works. Turn in your test code together with the driver and ArraySort classes.

Please thoroughly test your code and briefly discuss your testing strategy. Turn in all test code.

## Turning in the Assignment

The assignment is due on Friday at 11:55pm. You may turn it in early.

1. Conduct a personal review of your code before turning it in. Does you code follow the [Java Coding Standard](../010.introduction/reading-java-coding-standard.html)? Is it clear and well commented?
2. Test your code. Did your queue schedule the processes correctly? What happens if they have the same deadline?
3. Sign into Laulima, then navigate to the ICS211 site. In the left hand side of the site, there is an Assignments tab/link.  Click on it and view all of the posted assignments. Select the assignment that you want to turn in and attach your files and accept the honor pledge to submit the assignment. 
  
