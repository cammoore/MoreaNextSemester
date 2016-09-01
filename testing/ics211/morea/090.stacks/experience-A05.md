---
morea_id: experience-A05
morea_type: experience
title: "A05: Stack Assignment"
published: True
morea_summary: "Write a Postfix calculator."
morea_sort_order: 20
morea_start_date: "2016-10-14T23:55:00"
morea_labels: 
  - "Homework Assignment"
---

# ICS 211 Homework A05: Stack Assignment, implement a Postfix calculator.

This assignment requires you to implement a postfix calculator. Your calculator must be able to compute any expression of floating point numbers using the operands +, -, *, or / (you do not need to handle negative input numbers such as "-5").

The essence of your calculator is a class *Calculator* with at least the method *double calculate(String expression)*. Your program should be able to accept arbitrary, valid postfix expressions that use these four operators.

You must also write test code to accept input from the user and print the result. You are welcome to create either a graphical user interface or a text-based user interface.

You must also write a second test class that tests your calculator with the following inputs:

{% highlight java %}
1 2 + 3 * 6 + 2 3 + /            answer 3

2.2 7.0 + 3.0 *                  answer 27.6

1 3 5 + -                        answer -7

{% endhighlight %}

When submitting the assignment, turn in your test code and your *Calculator* class.

For this project, you are welcome to adapt any code from the book. I suggest you use the java.util.Stack&lt;E&gt; class for this project, but if you have extra time, you are welcome to implement your own stack.

Feel free to implement other methods in any of the classes which will help solve this problem.

## Testing

Please thoroughly test your code and briefly discuss your testing strategy. Turn in all test code.

## Turning in the Assignment

The assignment is due on Friday at 11:55pm. You may turn it in early. 

1. Conduct a personal review of your code before turning it in. Does you code follow the
   [Java Coding Standard](../010.introduction/reading-java-coding-standard.html)?
   Is it clear and well commented?
2. Test your code.
3. Sign into Laulima, then navigate to the ICS211 site. In the left hand side of the site, there is an Assignments tab/link.  Click on it and view all of the posted assignments. Select the assignment that you want to turn in and attach your files and accept the honor pledge to submit the assignment.
  
