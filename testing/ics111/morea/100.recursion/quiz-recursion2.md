---
morea_id: quiz-recursion2
morea_type: experience
title: "Q28: Recursion"
published: True
morea_summary: "What does this code do?"
morea_labels:
  - Quiz
morea_sort_order:
#morea_start_date: "2016-01-12"
#morea_end_date: "2016-01-13"
---

# Q26: Recursion

**Take out a piece of paper and put your name on the upper right corner.**

* Consider the following subroutine:

{% highlight java %}
  static void printStuff(int level) {
      if (level == 0) {
         System.out.print("=");
      }
      else {
         System.out.print("(");
         printStuff(level - 1);
         System.out.print(",");
         printStuff(level - 1);
         System.out.print(")");
      }
  }
{% endhighlight %}
  
* Show the output that would be produced by the subroutine calls printStuff(0), printStuff(1), printStuff(2), and printStuff(3).
  
Finish your answer before the timer runs out.

{% include quiz-timer.html quiz_time="15" %}


