---
morea_id: inclass-w7-c1
morea_type: experience
title: "Practice: Reading Code"
published: True
morea_summary: ""
morea_labels:
morea_sort_order:
morea_start_date: "2016-10-03T10:30:00"
---

## Identify the bugs in the following code

* Take out a sheet of paper.

* Form teams of two.

* Write down the bugs in the following code.

{% highlight java %}
01   public class LinkedList<E> {
02     private LinkedNode<E> head;
03     private int size;
04     public E add(E item) {
05       E temp = head;
06       for (int i = 0; i < size; i++) {
07         temp = temp.next;
08         temp.data = data[i];
09       }
10       temp.next = item;
11     }
{% endhighlight %}

{% include quiz-timer2.html time="10" %}