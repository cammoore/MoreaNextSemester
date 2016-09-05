---
morea_id: inclass-w10-c2
morea_type: experience
title: "Practice: Interfaces"
published: True
morea_summary: ""
morea_labels:
  - In class
morea_sort_order:
morea_start_date: "2016-10-27T00:00:00"
---

# Practice: Intefaces

**Take out a piece of paper. We'll be programming on paper.**

### Problem 1

Create a class *Student* with an instance variable *grades* of type array of doubles.  The *Student* class must implement the following interface.

{% highlight java %}
public interface Averageable {
  /**
   * Returns the average value.
   */
  public double average();
}
{% endhighlight %}


### Problem 2

Modify the *Student* class to also implement the following interface.

{% highlight java %}
public interface Minable {
  /**
   * Returns the minimum value.
   */
  public double minimum();
}
{% endhighlight %}

## Show me your code before you leave
