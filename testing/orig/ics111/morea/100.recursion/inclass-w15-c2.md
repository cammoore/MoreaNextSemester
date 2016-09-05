---
morea_id: inclass-w15-c2
morea_type: experience
title: "Practice: Recursion"
published: True
morea_summary: "Write a recursive factorial function."
morea_labels:
  - In class
morea_sort_order:
morea_start_date: "2016-12-01T00:00:00"
---

# Practice: Recursion

**Take out a piece of paper. We'll be programming on paper.**

### Problem 1

Write a method *factorial* that takes an integer parameter *N* and returns N!

n!, is the product of all positive integers less than or equal to n.

5! = 5 x 4 x 3 x 2 x 1

## Problem 2

Start to write a method {% highlight java %}public void printAnagrams(String prefix, String word){% endhighlight %}  Implement the reducing the problem step for the recursion.
{% highlight java %}
else
  For each letter in the word:
    Print the prefix + letter followed by the rearrangements of the word without the letter.
{% endhighlight %}

Focus on building the new prefix and word.  The new prefix is the old prefix + letter.  The new word is the old word without the letter.

You should use:

* [char String.charAt(int index)](http://docs.oracle.com/javase/8/docs/api/java/lang/String.html#charAt-int-)

* [String String.substring(int beginIndex)](http://docs.oracle.com/javase/8/docs/api/java/lang/String.html#substring-int-)

* [String String.substring(int beginIndex, int endIndex)](http://docs.oracle.com/javase/8/docs/api/java/lang/String.html#substring-int-int-)


### Show me your code.
