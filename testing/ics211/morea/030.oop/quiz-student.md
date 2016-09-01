---
morea_id: quiz-student
morea_type: experience
title: "Q04: Student Class"
published: True
morea_summary: "Write a simple student class."
morea_labels:
morea_sort_order:
---

# Q04: Student Class

* Take out a piece of paper and put your name on the upper right corner.

* **Write a simple Java class representing a Student.**

  * The class must extend *Person* and have the following member variables:

    * Double gpa
    * String gradeLevel
    * String major

The class must implement the Comparable&lt;E&gt; interface. Compare two students first by their gradeLevel then by their gpa.

{% highlight java %}
public interface Comparable<E> {
  /**
   * Compares this object to o. Returns a negative integer, zero, or a positive integer as this object is less than, equal to, or greater
   * than the specified object.
   */
  int compareTo(E o);
}
{% endhighlight %}

  * Be sure to write JavaDoc comments for your code.

* Conduct a quick review of your code, before you turn it in.

* Hand in your code when you are done.

{% include quiz-timer2.html time="12" %}