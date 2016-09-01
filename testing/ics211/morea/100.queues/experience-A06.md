---
morea_id: experience-A06
morea_type: experience
title: "A06: Queues Assignment"
published: True
morea_summary: "Write a simulator of the checkout lines at Foodland."
morea_sort_order: 20
morea_start_date: "2016-10-21T23:55:00"
morea_labels: 
  - "Homework Assignment"
---

# ICS 211 Homework A06: Write a simulator of the checkout lines at a store like Foodland.

* Create a *CircularArrayQueue* class that implements the following interface using a circular array to hold the items in the queue.

{% highlight java %}
public interface Queue211<E> {
  boolean add(E e);  // adds e to the end of the queue. May throw an IllegalStateException if the queue is full.
  E element(); // Retrieves, but doesn't remove the head of the queue. Throws NoSuchElementException if queue is empty.
  boolean offer(E e); // adds e to the end of the queue. Returns false if the queue is full.
  E peek(); // Retrieves, but doesn't remove the head of the queue. Return null if queue is empty.
  E poll(); // Retrieves and removes the head of the queue. Returns null if the queue is empty.
  E remove(); // Retrieves and removes the head of the queue. Throws NoSuchElementException if queue is empty.
  int size(); // Returns the size of the queue.
}
{% endhighlight %}

* All the methods should run in Big O(1).

* Create a *Shopper* class that has a member variable *numItems*. Instances of this class represent the shoppers in the store.

* Create a *CheckoutLanes* class that has some express lines and regular lines. The class should look something like:

{% highlight java %}
public class CheckoutLanes {
  ...
  public CheckoutLanes(int numExpress, int numRegular) { ... }
  public void enterLane(int laneNumber, Shopper shopper) { ... }
  public void simulateCheckout() { ... }
  ...
}
{% endhighlight %}

  * The constructor should create CircularArrayQueues&lt;Shopper&gt;s for the express lanes and the regular lanes. Store the queues in an array. You can use two arrays. There must be at least one regular lane.

  * The *void enterLane(int laneNumber, Shopper shopper)* method adds the shopper to the given checkout lane. Express lanes come before regular lanes.  If you had 2 express lanes and 4 regular lanes, lanes 0 and 1 are express and 2 - 5 are regular. This method does not check the shopper's number of items.

  * The *void simulateCheckout()* method should loop until all checkout lanes are empty.
    * Each time through the outer loop, the method should process the shopper at the head of the queue.
      * For express lanes, if the shopper has more than 10 items they are placed at the end of a regular lane. Print out "Express lane shopper with &lt;numItems&gt; items moved to lane &lt;laneNumber&gt;". Else the method should print out "Express Lane &lt;laneNumber&gt;, shopper had &lt;numItems&gt; items" indicating the shopper has checked out.
      * For regular lanes, the method should print out "Regular Lane &lt;laneNumber&gt;, shopper had &lt;numItems&gt; items" indicating that the shopper has checked out.

## Testing

Create a test class that instantiates your CheckoutLanes class and adds several shoppers with different number of items. Then run the *simulateCheckout* method.

Here's an example:
{% highlight java %}
CheckoutLanes checkout = new CheckoutLanes(1, 2);
checkout.enterLane(0, new Shopper(15));
checkout.enterLane(0, new Shopper(3));
checkout.enterLane(1, new Shopper(20));
checkout.enterLane(2, new Shopper(17));
checkout.simulateCheckout();
{% endhighlight %}
Could produce the following output:
{% highlight bash %}
Express lane shopper with 15 items moved to lane 1
Regular lane 1, shopper had 20 items
Regular lane 2, shopper had 17 items
Express lane 0, shopper had 3 items
Regular lane 1, shopper had 15 items
{% endhighlight %}

Please thoroughly test your code and briefly discuss your testing strategy. Turn in all test code.

## Turning in the Assignment

The assignment is due on Friday at 11:55pm. You may turn it in early. 

1. Conduct a personal review of your code before turning it in. Does    you code follow the
   [Java Coding Standard](../010.introduction/reading-java-coding-standard.html)?
   Is it clear and well commented?
2. Test your code.
3. Sign into Laulima, then navigate to the ICS211 site. In the left hand side of the site, there is an Assignments tab/link.  Click on it and view all of the posted assignments. Select the assignment that you want to turn in and attach your files and accept the honor pledge to submit the assignment.
  
