---
morea_id: experience-A11
morea_type: experience
title: "A10: Hash Table"
published: True
morea_summary: "Implement two hash tables using open addressing and chained hashing."
morea_sort_order: 40
#morea_start_date: "2016-04-22T23:55:00"
morea_labels: 
  - "Homework Assignment"
---

# ICS 211 Homework A11: Hash Table

In this assignment, you implement a hash table using chained hashing. The hash table size is determined at initialization time and never changes. Each hash table entry is a linked list, so each hash table entry can hold any number of values. You may use a [linked list](http://docs.oracle.com/javase/7/docs/api/java/util/LinkedList.html) from the Java API, or one from one of your previous assignments.

Your hash table must be designed to map keys to values. None of the keys or values are allowed to be *null*. Keys are compared using the *.equals* method.

Your hash table should use the *hashCode()* method to compute the hash for a given string. Use *Math.abs* to turn that into a positive value, and modulo to make it into an array index (this description is not quite enough, so you will have to figure out exactly how to make this work).

Your hash table class (called *Hash211&lt;K,V&gt;*) must provide the following methods:

{% highlight java %}
Hash211<K,V>(int capacity, boolean printTimes);   // constructor
V put(K key, V value);              // add or replace a Key,Value
V get(K key);                  // return a value for the given key
{% endhighlight %}

Each of these functions is described in more detail [here](http://docs.oracle.com/javase/7/docs/api/java/util/Hashtable.html#put(K, V)) and [here](https://docs.oracle.com/javase/7/docs/api/java/util/Hashtable.html#get(java.lang.Object)).

* The second parameter to the constructor specifies whether your code should print out the time (in nanoseconds) for each call to put and get. To do this, you may re-use your code from [Assignment 10](/morea/085.midterm2/experience-A10.html). Since executing any print statements substantially increases the runtime, when *printTimes* is false, your code may run considerably faster.
  

## Analysis and measurement

You should analyze and measure the runtime of your hash table *put* and *get* operations in two cases:

1. When the hash table size *s* is much larger (at least 10 times larger) than the number *n* of elements added.

2. When the hash table size *s* is much less (at least 10 times less) than the number *n* of elements added.  Your analysis should match your measured results. Write up your analysis and make enough measurements to be clear and convincing.

This part of the assignment is worth 20% of the grade.

## Test Code

Anthony Christe has provided a test program, [HashTableStressTest.java](hashtablestresstest.java.html), to make it easy for you to add a large number of strings to your hash table.

It's a command line program that takes two arguments and an optional third argument.

<pre>
java HashTableStressTest dictionary_file capacity [-pt --print-times]
</pre>

where *dictionary_file* is the location of the dictionary file which is a text file with a single word per line, and *capacity* is the initial capacity of the hashtable.

The final option will pass either true or false to *printTimes* in the *Hash211* constructor. If it is not specified then *printTimes* will be false. If the option is specified, then the times will be printed.

Anthony has also provided two dictionary files, [dict.txt](hw11-dict.txt) (234,937 words) and [dict-small.txt](hw11-dict-small.txt) (99,171 words).


## Testing

You must also build your own test code to make sure that your implementation works. Turn in your test code together with the Hash211 class and your analysis.

Please thoroughly test your code and briefly discuss your testing strategy. Turn in all test code.

## Turning in the Assignment

The assignment is due on Friday at 11:55pm. You may turn it in early.

1. Conduct a personal review of your code before turning it in. Does you code follow the [Java Coding Standard](../010.introduction/reading-java-coding-standard.html)?
   Is it clear and well commented?
2. Test your code. Did your hash table perform as expected?
3. Sign into Laulima, then navigate to the ICS211 site. In the left hand side of the site, there is an Assignments tab/link.  Click on it and view all of the posted assignments. Select the assignment that you want to turn in and attach your files and accept the honor pledge to submit the assignment. 
  
