---
morea_id: reading-insertion-sort-soln
morea_type: reading
title: "Insertion Sort Quiz Solution"
published: True
morea_summary: "My 'solution' to the Insertion Sort Quiz."
morea_sort_order: 4
morea_labels: 
  - "Solution"
---
{% highlight java %}
/**
 * ArraySorter.java
 * Copyright (C) Cam Moore 2015
 */
package edu.cam;

import java.util.Comparator;

/**
 * Represents a ArraySorter.
 *
 * @author Cam Moore
 *
 */
public class ArraySorter<E> {

  /**
   * Uses the insertion sort algorithm to sort the array data, using the Comparator c.
   *
   * @param data The array to sort.
   * @param c a Comparator used to determine order of the items in the array.
   */
  public void insertionSort(E[] data, Comparator<E> c) {
    for (int i = 1; i < data.length; i ++) {
      E tempVal = data[i];
      int j = i;
      while (j > 0 && c.compare(data[j - 1], tempVal) > 0) { 
        data[j] = data[j - 1];
        j--;
      }
      data[j] = tempVal;
    }
  }

}

{% endhighlight %}