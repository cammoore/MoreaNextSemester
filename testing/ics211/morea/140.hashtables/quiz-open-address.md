---
morea_id: quiz-open-address
morea_type: experience
title: "Quiz 23: Open Address Hashmap put."
published: True
morea_summary: "Implement the put method."
morea_sort_order: 4
morea_labels: 
  - "Quiz"
---
Take out a piece of paper and put your name on the upper right corner.

* **Write the V put(K key, V value) method for the following Hashmap.** The Hashmap uses Open Addressing with linear probing.

{% highlight java %}
public class HashmapOpen<K, V> {
  private Entry<K, V>[] table;

  /**
   * Associates the value with the given key.
   * @param key, the key.
   * @parm value, the value.
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
* Be sure to write JavaDoc comments for your code.
* Conduct a quick review of your code, before you are done.
* Hand in your code when you are done.

{% include quiz-timer.html time="20" %}
