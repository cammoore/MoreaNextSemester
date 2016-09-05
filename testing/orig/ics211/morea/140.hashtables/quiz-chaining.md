---
morea_id: quiz-chaining
morea_type: experience
title: "Quiz 24: Chained Hashmap get."
published: True
morea_summary: "Implement the get method."
morea_sort_order: 4
morea_labels: 
  - "Quiz"
---
Take out a piece of paper and put your name on the upper right corner.

* **Write the V get(Object key) method for the following Hashmap.** The Hashmap uses Chaining.

{% highlight java %}
public class HashmapChaining<K, V> {
  private LinkedList<Entry<K, V>>[] table;

  /**
   * Associates the value with the given key.
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
* Be sure to write JavaDoc comments for your code.
* Conduct a quick review of your code, before you are done.
* **Bonus point:** Write the **Queue** interface.
* Hand in your code when you are done.

{% include quiz-timer.html time="20" %}
