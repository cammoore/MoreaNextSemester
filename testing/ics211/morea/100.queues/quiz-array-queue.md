---
morea_id: quiz-array-queue
morea_type: experience
title: "Q14: ArrayQueue Quiz"
published: True
morea_summary: "Write the add and remove methods for an ArrayQueue."
morea_sort_order: 4
morea_labels: 
  - "Quiz"
---

# Q14: ArrayQueue Quiz

Take out a piece of paper and put your name on the upper right corner.

* **Write the following methods for the ArrayQueue class:**

{% highlight java %}
public class ArrayQueue<E> implements Queue211<E> {
  private E[] data;
  private int front;
  private int rear;
  private int size;
  ...
  public E poll() { // May throw an IllegalStateException
    // your code here.
  }

  public E peek() { // May throw an IllegalStateException
    // your code here.
  }
  ...
}
{% endhighlight %}

  * Be sure to write JavaDoc comments for your code.

* Conduct a quick review of your code, before you are done.

* After the code, write an explanation the Big-O performance of both methods.

* *Bonus point:* implement the LinkedList's *E remove(int index)* method.

* Hand in your code when you are done.

{% include quiz-timer2.html time="10" %}