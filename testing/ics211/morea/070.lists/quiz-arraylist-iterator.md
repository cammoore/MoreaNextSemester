---
morea_id: quiz-arraylist-iterator
morea_type: experience
title: "Q09: ArrayList iterator Quiz"
published: True
morea_summary: "Write the next method for the ArrayListIterator class."
morea_sort_order: 4
morea_labels: 
  - "Quiz"
---
# Q09: ArrayListIterator *next* Quiz

* Take out a piece of paper and put your name on the upper right corner.

* **Write a Generic Java class ArrayList&lt;E&gt; that has one method:**

{% highlight java %}
public class ArrayList<E> implements List<E> {
  private E[] data;
  private int size;
   ...
  private class ArrayListIterator<E> implements Iterator<E> {
    private int nextIndex;
    ...
    public E next() { // May throw a NoSuchElementException
      // your code here.
    }
  }
}
{% endhighlight %}

  The method must return the next item in the iteration.

  * Be sure to write JavaDoc comments for your code.

* Conduct a quick review of your code, before you turn it in.

* After the code, write an explanation the Big-O performance of the *next* method.

* Hand in your code when you are done.

{% include quiz-timer2.html time="15" %}
