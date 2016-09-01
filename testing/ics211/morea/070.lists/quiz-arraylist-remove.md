---
morea_id: quiz-arraylist-remove
morea_type: experience
title: "Q07: ArrayList remove Quiz"
published: True
morea_summary: "Write the remove method for the ArrayList class."
morea_sort_order: 4
morea_labels: 
  - "Quiz"
---
# Q07: ArrayList *remove* Quiz

* Take out a piece of paper and put your name on the upper right corner.

* **Write a Generic Java class ArrayList&lt;E&gt; that has one method:**

{% highlight java %}
public class ArrayList<E> implements List<E> {
  /** Holds the items in the list. */
  private E[] data;
  /** The size of the list. */
  private int size;

  public E remove(int index) {
    // Your code goes here.
  }
}
{% endhighlight %}

  The method must remove the item at the given index.

  * Be sure to write JavaDoc comments for your code.

* Conduct a quick review of your code, before you turn it in.

* After the code, write an explanation the Big-O performance of the *remove* method.

* Hand in your code when you are done.

{% include quiz-timer2.html time="15" %}
