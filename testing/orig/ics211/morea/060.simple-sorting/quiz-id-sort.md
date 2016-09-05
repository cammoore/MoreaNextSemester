---
morea_id: quiz-id-sort
morea_type: experience
title: "Q05: Identify the Sorting Algorithms"
published: True
morea_summary: "Figure out which algorithm each sort method implements."
morea_labels:
  - Quiz
morea_sort_order:
#morea_start_date: "2016-01-27"
---

# Q04: Identify the Sorting Algorithms

* Take out a piece of paper and put your name on the upper right corner.

* Write down which sorting algorithm each of the three methods sort1, sort2, and sort3 implement.

{% highlight java %}
public void sort1(E[] data, Comparator<E> c) {    |   public void sort2(E[] data, Comparator<E> c) {      
  for (int i = 0; i < data.length; i++) {         |     for (int i = 1; i < data.length; i++) {
    for (int j = 0; j < data.length - i; j++) {   |       E temp = data[i];
      if (c.compare(data[j], data[j + 1]) > 0) {  |       int j = i;
        swap(data[j], data[j + 1]);               |       while(j > 0 && c.compare(data[j], temp) > 0) {
      }                                           |         data[j] = data[j - 1];
    }                                             |         j--;
  }                                               |       }
}                                                 |       data[j] = temp;
                                                  |     }
                                                  |   }

public void sort3(E[] data, Comparator<E> c) { 
  for (int i = 0; i < data.length - 1; i++) {
    int posMin = i;
    for (int j = i + 1; j < data.length; j++) {
      if (c.compare(data[j], data[posMin]) < 0) {
        posMin = j;
      }
    }
    swap(data[i], data[posMin]);
  }
}
{% endhighlight %}

* Hand in your quiz when you are done.

{% include quiz-timer2.html time="15" %}
