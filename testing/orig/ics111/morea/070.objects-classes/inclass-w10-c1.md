---
morea_id: inclass-w10-c1
morea_type: experience
title: "Practice: Inheritance"
published: True
morea_summary: ""
morea_labels:
  - In class
morea_sort_order:
morea_start_date: "2016-10-25T00:00:00"
---

# Practice: Inheritance

**Take out a piece of paper. We'll be programming on paper.**

### Problem 1

Create a *Student* class that is a subclass of *Person*. The Student has two additional *instance variables*:

  * *studentId* an eight digit number.
  
  * *gradeLevel* a String
  
The *instance variables* must be *private*. This means you need *accessor* methods.  Be sure the Student's constructor initializes the Student's name.

{% highlight java %}
public class Person {
  private String name;
  
  public Person(String name) {
    this.name = name;
  }
  
  public String getName() {
    return name;
  }
}
{% endhighlight %}

### Problem 2

Write a subclass of *Student* named *StudentAthlete*. *StudentAthlete* has a private instance variable *team* of type *String*.  Write three constructors for *StudentAthlete*. One with four parameters, one with three parameters and one with just one parameter.


## Show me your code before you leave
