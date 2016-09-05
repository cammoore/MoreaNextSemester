---
morea_id: quiz-linked-stack
morea_type: experience
title: "Q12: LinkedStack Quiz"
published: True
morea_summary: 'Implement a couple of LinkedStack methods."'
morea_sort_order: 4
morea_labels: 
  - "Quiz"
---

LinkedStack Quiz


* **Write the following methods for the LinkedStack class:**

{% highlight java %}
public interface Stack211<E> {
  boolean empty();
  E peek();
  E pop();
  E push(E item);
}

public class LinkedStack<E> implements Stack211<E> {
  private LinkedNode<E> top;
  ...
  public E peek() {
    // your code here.
  }

  public boolean empty() {
    // your code here.
  }
  ...
}
{% endhighlight %}

  * Be sure to write JavaDoc comments for your code.

* Conduct a quick review of your code, before you are done.

* After the code, write an explanation the Big-O performance of both methods.

* Hand in your code when you are done.

{% include quiz-timer2.html time="14" %}