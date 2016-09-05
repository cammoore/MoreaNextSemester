---
morea_id: experience-A04
morea_type: experience
title: "A04: List Iterators"
published: True
morea_summary: "Write ListIterators for both the ArrayList and DoubleLinkedList Classes."
morea_start_date: "2016-09-30T23:55:00"
morea_labels: 
  - "Homework Assignment"
---

# ICS 211 Homework A04: Implement ListIterators for both the ArrayList and DoubleLinkedList Classes.

## Part 1: Add ListIterator to your MyArrayList and MyLinkedList classes

Modify your *MyArrayList* and *MyLinkedList* classes from the previous two assignments to include a ListIterator.  Use the following ListIterator interface:

{% highlight java %}
public interface ListIterator<E> {
  boolean hasNext(); // Returns true if this list iterator has more elements while traversing in the forward direction.
  boolean hasPrevious(); // Returns true if this list iterator has more elements while traversing in the reverse direction.
  E next(); // Returns the next Element.
  int nextIndex(); // Returns the index of the next element.
  E previous(); // Returns the previous Element
  int previousIndex(); // Returns the index of the previous element.
}
{% endhighlight %}

## Part 2: Modify your MyArrayList and MyLinked list to implement the Iterable<E> interface.

Using your ListIterator implementations, update your *MyArrayList* and *MyLinkedList* classes so that they implemement the *Iterable<E>* interface.  Demonstrate this by printing out the elements in your lists using the *foreach* Java for loop.
 
{% highlight java %}
List<Contact> list;  // Use both your MyArrayList and MyLinkedList
for (Contact c: list) {
  System.out.println(c);
}
{% endhighlight %}

## Testing

Please thoroughly test your code and briefly discuss your testing strategy. Make sure that you test the different sorting algorithms. Turn in all your test code.

## Turning in the Assignment

The assignment is due on Friday at 11:55pm. You may turn it in early.

1. Conduct a personal review of your code before turning it in. Does you code follow the
   [Java Coding Standard](../010.introduction/reading-java-coding-standard.html)?
   Is it clear and well commented?
2. Test your code.
3. Sign into Laulima, then navigate to the ICS211 site. In the left hand side of the site, there is an Assignments tab/link.  Click on it and view all of the posted assignments. Select the assignment that you want to turn in and attach your files and accept the honor pledge to submit the assignment.
  
