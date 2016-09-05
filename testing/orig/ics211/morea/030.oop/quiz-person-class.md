---
morea_id: quiz-person-class
morea_type: experience
title: "Q03: Person Class"
published: True
morea_summary: "Write a Java Class representing a Person."
morea_sort_order: 4
morea_labels: 
  - "Quiz"
---

# Q03: Person Class

* Take out a piece of paper and put your name on the upper right corner.

* **Write a simple Java class representing a Person.**

  * The class must have the following member variables:

    * String firstName
    * String lastName
    * Address address
    * String phoneNumber

The class must implement the Comparable&lt;E&gt; interface. Compare two persons first by their last name then by their first name.

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

{% include quiz-timer2.html time="15" %}
