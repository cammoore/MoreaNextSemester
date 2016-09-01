---
morea_id: experience-A02
morea_type: experience
title: "A02: ArrayList and Simple Sorting"
published: True
morea_summary: "Implement an ArrayList class with simple sort methods.."
morea_sort_order: 8
morea_start_date: "2016-09-16T23:55:00"
morea_labels: 
  - "Homework Assignment"
---

# ICS 211 Homework A02: ArrayList class.

## Part 1: Implement an ArrayList

Implement the following *List* interface using an array to store the data.

{% highlight java %}
public interface List211<E> {
  boolean add(E e);
  void add(int index, E element);
  E get(int index);
  E remove(int index);
  E set(int index, E element);
  int size();
}
{% endhighlight %}

Name your class **MyArrayList**.

In addition to the *List* interface implement the following sort methods:

{% highlight java %}
public class MyArrayList<E> implements List211<E> {
  private E[] data;
  private int size;

  public void insertionSort(Comparator<? super E> compare);
  public void bubbleSort(Comparator<? super E> compare);
  public void selectionSort(Comparator<? super E> compare);
{% endhighlight %}

Use the Comparator to compare the items in the array. The sort methods should sort the list in ascending order, smallest at the beginning, largest at the end.


## Part2: Create a Contact List that automatically sorts the list of Contacts.

Download and use the [Contact.java](Contact.java) and [ContactComparator.java](ContactComparator.java) classes to creat a **ContactList** that automatically sorts the list when ever a new contact is added to the list.  You should use your **MyArrayList** class as the basis of your **ContactList**.


## Testing

Please thoroughly test your code and briefly discuss your testing strategy. Make sure that you test the different sorting algorithms. Turn in all your test code.



## Turning in the Assignment

The assignment is due on Friday at 11:55pm. You may turn it in early. 

1. Conduct a personal review of your code before turning it in. Does you code follow the
   [Java Coding Standard](../010.introduction/reading-java-coding-standard.html)?
   Is it clear and well commented?
2. Test your code.
3. Sign into Laulima, then navigate to the ICS211 site. In the left hand side of the site, there is an Assignments tab/link.  Click on it and view all of the posted assignments. Select the assignment that you want to turn in and attach your files and accept the honor pledge to submit the assignment.
  
