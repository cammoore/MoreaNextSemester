---
morea_id: experience-H06
morea_type: experience
title: "H06: Addition Quiz."
published: True
morea_start_date: "2016-10-07T23:55:00"
morea_summary: "Write a program that administers a basic hexidecimal addition quiz."
morea_labels: 
  - "Homework Assignment"
---

# ICS 111 Homework Assignment H06: Addition Quiz.

Write a program that administers a basic hexidecimal addition quiz to the user. There should be ten questions. Each question is a simple addition problem such as "2C + 12 = ", where the numbers are hexidecimal. The numbers in the problem are chosen at random (and are not too big, < 100). The program should ask the user all ten questions and get the user’s answers. The user will answer in hexidecimal numbers. After asking all the questions, the user should print each question again, with the user’s answer. If the user got the answer right, the program should say so; if not, the program should give the correct answer. At the end, tell the user their score on the quiz, where each correct answer counts for ten points.

You can use as many subroutines as you want. I suggest at least four subroutines, one to create the quiz, one to administer the quiz, one to convert the user's answers to *ints*, and one to grade the quiz. It can use three arrays, with three global variables of type *int[ ]*, to refer to the arrays. The first array holds the first number from every question, the second holds the second number from every questions, and the third holds the user’s answers.

**Hint:** You can output hexidecimal values by using the following:
{% highlight java %}
int x = 16;
System.out.printf("x = %2X\n", x); // prints out "10"
{% endhighlight %}

## Turning in the Assignment

The assignment is due on Friday, October 7th at 11:55pm. You may turn it in early. 

1. Conduct a personal review of your code before turning it in. Does your code follow the [Java Coding Standard](../references/reading-java-coding-standard.html)?

   Is it clear and well commented?

2. Test your code.

    * Does it produce the correct output? 

3. Sign into Laulima, then navigate to the ICS111 site. In the left hand side of the site, there is an Assignments tab/link.  Click on it and view all of the posted assignments. Select the assignment that you want to turn in and attach your files and accept the honor pledge to submit the assignment.
  
