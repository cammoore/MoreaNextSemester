---
morea_id: experience-H11
morea_type: experience
title: "H11: Dynamic Array of Strings"
published: True
morea_start_date: "2016-11-23T23:55:00"
morea_summary: "Write a dynamic array of Strings class."
morea_labels: 
  - "Homework Assignment"
---

# ICS 111 Homework Assignment H11: Dynamic Array of Strings

Create a class named *DynamicArrayOfStrings* that implements the following two interfaces.

{% highlight java %}
public interface ICS111List {
  int size(); // return the size of the array.
  boolean add(String s); // Adds s to the end of the array. Returns true.
  boolean add(int index, String s); // Inserts s into position index
  String get(int index); // Returns the string at index.
  String set(int index, String s); // Replaces the string at index with s. Returns old value.
  String remove(int index); // Removes the string at index. Returns string.
  boolean remove(String s); // Removes s from the array, returns true if s was in the array.
  int indexOf(String s); // Returns the index of s or -1 if s is not in the array.
  String toString(); // Returns a string represenation of the array.
}

public interface Sortable {
  void sort();  // Sorts the array in increasing order.
}
{% endhighlight %}

Use the following class to test your implementation [TestDynamicArrayOfStrings.java](TestDynamicArrayOfStrings.java.txt)

## Turning in the Assignment

The assignment is due on Wednesday, November 23rd at 11:55pm. You may turn it in early. 

1. Conduct a personal review of your code before turning it in. Does your code follow the [Java Coding Standard](../references/reading-java-coding-standard.html)?

   Is it clear and well commented?

2. Test your code.

    * Does it produce the correct output? 

3. Sign into Laulima, then navigate to the ICS111 site. In the left hand side of the site, there is an Assignments tab/link.  Click on it and view all of the posted assignments. Select the assignment that you want to turn in and attach your files and accept the honor pledge to submit the assignment.
  
