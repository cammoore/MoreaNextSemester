---
morea_id: experience-H12
morea_type: experience
title: "H12: Recursion, Anagrams"
published: True
morea_start_date: "2016-12-02T23:55:00"
morea_summary: "Write a recursive method to print out the anagrams of given words."
morea_labels: 
  - "Homework Assignment"
---

# ICS 111 Homework Assignment H12: Recursion, Anagrams

Write a program that lists all the rearrangements of a word entered by the user.
 
The program must have a recursive method {% highlight java %}void printAnagrams(String prefix, String word);{% endhighlight %}

The recursive printAnagrams algorithm looks something like.
{% highlight java %}
if word length is one
  Print the prefix and word
else
  For each letter in the word:
    Print the prefix + letter followed by the rearrangements of the word without the letter.
{% endhighlight %}

## Turning in the Assignment

The assignment is due on Friday, December 2nd at 11:55pm. You may turn it in early. 

1. Conduct a personal review of your code before turning it in. Does your code follow the [Java Coding Standard](../references/reading-java-coding-standard.html)?

   Is it clear and well commented?

2. Test your code.

    * Does it produce the correct output? 

3. Sign into Laulima, then navigate to the ICS111 site. In the left hand side of the site, there is an Assignments tab/link.  Click on it and view all of the posted assignments. Select the assignment that you want to turn in and attach your files and accept the honor pledge to submit the assignment.
  
