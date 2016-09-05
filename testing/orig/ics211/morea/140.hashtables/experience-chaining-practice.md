---
morea_id: experience-chaining-practice
morea_type: experience
title: "Chaining Hashmap Practice Quiz"
published: True
morea_summary: "Write the put method."
morea_sort_order: 4
morea_labels: 
  - "Practice Quiz"
---
Chaining Hashmap Practice Quiz

Practice Problem

* Take out a piece of paper and put your name on the upper right corner.

* **Write the V put(K key, V value) method for the following Hashmap.** The Hashmap uses Chaining.

{% highlight java %}
public class HashmapChaining<K, V> {
  private LinkedList<Entry<K, V>>[] table;

  /**
   * Associates the value with the given key.
   * @param key, the key.
   * @param value, the value.
   * @return The previous value associated with the given key.
   */
  public V put(K key, V value) {
    // your code.
  }
  
  private class Entry<K,V> {
    K key;
    V value;
  }
}
{% endhighlight %}

* You can use the **hashCode()** method.
* Be sure to write JavaDoc comments for your code.

**Time Remaining:**

<script src="{{ site.baseurl }}/js/countdown.js" type="text/javascript"></script>
<!-- =========================================================== -->
<script type="application/javascript">
var myCountdown2 = new Countdown({
									time: 15 * 60,
									width:150,
									height:80,
									rangeHi:"minute"	// <- no comma on last item!
									});
</script>

You can restart the timer by reloading the page.

**Try to complete the problem in 15 minutes.**

If you cannot complete the program in 15 minutes, you can watch me solve the problem in a text editor.

{% include youtube.html id="aUbncZ5rALE" %}