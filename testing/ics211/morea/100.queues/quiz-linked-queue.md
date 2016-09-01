---
morea_id: quiz-linked-queue
morea_type: experience
title: "Q15: LinkedQueue Quiz"
published: True
morea_summary: "Write the add and remove methods for a LinkedQueue."
morea_sort_order: 4
morea_labels: 
  - "Quiz"
---

# Q15: LinkedQueue Quiz

Take out a piece of paper and put your name on the upper right corner.

* **Write the following methods for the LinkedQueue class:**

{% highlight java %}
public class LinkedQueue<E> implements Queue211<E> {
  private LinkedNode<E> front;
  private LinkedNode<E> rear;
  private int size;
  ...
  public boolean add(E e) { // Does not throw exception
    // your code here.
  }

  public E remove() { // Does not throw exception
    // your code here.
  }
  ...
}
{% endhighlight %}

  * Be sure to write JavaDoc comments for your code.

* Conduct a quick review of your code, before you are done.

* After the code, write an explanation the Big-O performance of both methods.

* **Bonus point:** implement the ArrayList's *E get(int index)* method.

* Hand in your code when you are done.

{% include quiz-timer2.html time="14" %}