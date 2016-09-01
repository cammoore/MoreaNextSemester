---
morea_id: inclass-w7-c1
morea_type: experience
title: "Practice: More Subroutines"
published: True
morea_summary: "More practice writing subroutines."
morea_labels:
  - In class
morea_sort_order:
morea_start_date: "2016-10-04T00:00:00"
---

# Practice: Subroutines

**Take out a piece of paper. We'll be programming on paper.**

Write Java code for the following problems.

### Problem 1

Write a *public* *static* subroutine *hexValue* that takes a *char* and returns the *char*'s value as an int. Use the following table:

| char | Hex Value |
| :----: |: ---------: |
| '0' | 0 |
| '1' | 1 |
| '2' | 2 |
| '3' | 3 |
| '4' | 4 |
| '5' | 5 |
| '6' | 6 |
| '7' | 7 |
| '8' | 8 |
| '9' | 9 |
| 'A' | 10 |
| 'B' | 11 |
| 'C' | 12 |
| 'D' | 13 |
| 'E' | 14 |
| 'F' | 15 |

### Problem 2

Write a *public* *static* subroutine *getHexValue* that takes a *String* and calculates the Hexidecimal value fo the string.  Use the *hexValue* subroutine. 

**Big Hint**
{% highlight java %}
value = 0;
for ( i = 0; i < str.length(); i++ )
  value = value*16 + hexValue( str.charAt(i) );
  
{% endhighlight %}


## Show me your code before you leave


