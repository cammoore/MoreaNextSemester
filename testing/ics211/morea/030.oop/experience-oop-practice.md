---
morea_id: experience-oop-practice
morea_type: experience
title: "Object Oriented Programming Practice Quiz"
published: True
morea_summary: "Write a simple Java Class that implements an interface."
morea_sort_order: 4
morea_labels: 
  - "Practice Quiz"
---

# Object Oriented Programming Practice Quiz

Practice Problem

* Take out a piece of paper, put your name on the top right of the paper.

* Write a simple Java class representing a Book.

  * The class must have the following member variables:

    * String title
    * String author
    * String isbn

  The class must implement the Comparable&lt;E&gt; interface.  Compare two books first by their titles then by their authors.

{% highlight java %}
public interface Caparable<E> {
  /**
   * Compares this object to o. Returns a negative integer, zero, or a positive integer as this object is less than, equal to, or greater
   * than the specified object.
   */
  int compareTo(E o);
}
{% endhighlight %}

{% include quiz-timer2.html time="25" %}

You can restart the timer by reloading the page.

**Try to complete the problem in 25 minutes.**

If you cannot complete the program in 25 minutes, you can watch me solve the problem in a text editor.

{% include youtube.html id="zhLhgxvjYcw" %}


