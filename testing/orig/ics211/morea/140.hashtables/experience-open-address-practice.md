---
morea_id: experience-open-address-practice
morea_type: experience
title: "Open Address Hashmap Practice Quiz"
published: True
morea_summary: "Write the get method."
morea_sort_order: 4
morea_labels: 
  - "Practice Quiz"
---
Open Address Hashmap Practice Quiz

Practice Problem

* Take out a piece of paper and put your name on the upper right corner.

* **Write the V get(Object key) method for the following Hashmap.** The Hashmap uses Open Addressing with linear probing.

{% highlight java %}
public class HashmapOpen<K, V> {
  private Entry<K, V>[] table;

  /**
   * Returns the value associated with the given key.
   * @param key, the key.
   * @return The value associated with the given key.
   */
  public V get(Object key) {
    // your code.
  }
  
  private class Entry<K,V> {
    K key;
    V value;
  }
}
{% endhighlight %}

* You can use the **hashCode()** method and linear probing.
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

{% include youtube.html id="oeaZkIm82rI" %}
