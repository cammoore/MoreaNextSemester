---
morea_id: inclass-w9-c1
morea_type: experience
title: "Practice: Using Queues"
published: True
morea_summary: "Using Queues to simulate a checkout line."
morea_labels:
morea_sort_order:
morea_start_date: "2016-10-17T10:30:00"
---

# Practice: Queues

**Take out a piece of paper. We'll be programming on paper.**

Design a program that calculates the average time it takes to get an order at Taco Hut.  Taco Hut has one order/pick-up window.  The time it takes to serve the customer is: 
 
{% highlight java %}
numTacos * (1.5 + (1.0 - 2.0 * Math.random()));
{% endhighlight %}

* Create a *TacoHut* class with a *Queue* for their window.

* Create a *Customer* class that has a member variable *numTacos*. Instances of this class represent the customers in the store.

* The program should follow this psuedo code.
{% highlight java %}
// Create a TacoHut instance.
// Create customers.
// Put the customers in the TacoHut line.
// Have the TacoHut handle the customers.  This returns the average time it took to make their tacos.
{% endhighlight %}

* You only need to create the method signatures and member variables for your classes.

## Show me your code before you leave


