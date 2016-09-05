---
morea_id: quiz-array-stack
morea_type: experience
title: "Q11: ArrayStack Quiz"
published: True
morea_summary: 'Implement a couple of ArrayStack methods."'
morea_sort_order: 4
morea_labels: 
  - "Quiz"
---

ArrayStack Quiz


* **Write the following methods for the ArrayStack class:**

{% highlight java %}
public interface Stack211<E> {
  boolean empty();
  E peek();
  E pop();
  E push(E item);
}

public class ArrayStack<E> implements Stack211<E> {
  private E[] data;
  private int top;
  ...
  public E pop() {
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