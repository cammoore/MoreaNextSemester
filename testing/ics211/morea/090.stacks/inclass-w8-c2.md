---
morea_id: inclass-w8-c2
morea_type: experience
title: "Practice: Stacks"
published: True
morea_summary: ""
morea_labels:
morea_sort_order:
morea_start_date: "2016-10-12T10:30:00"
---

# Practice: Linked Stacks

**Take out a piece of paper. We'll be programming on paper.**

### Problem 1

**Implement the LinkedStack class:**

{% highlight java %}
public interface Stack211<E> {
  boolean empty();
  E peek();
  E pop();
  E push(E item);
}

public class LinkedStack<E> implements Stack211<E> {
  private LinkedNode<E> top;

  // your code here.

}
{% endhighlight %}

### Problem 2

Write a *public* *static* method *isPalindrome* that takes one parameter of type *String* and returns *true* if the parameter is a palindrome.

{% highlight java %}

public static boolean isPalindrome(String word) {
  // your code goes here
}

{% endhighlight %}

A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward.


## Show me your code before you leave
