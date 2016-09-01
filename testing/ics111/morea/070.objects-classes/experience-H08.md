---
morea_id: experience-H08
morea_type: experience
title: "H08: Addition Quiz with classes."
published: True
morea_start_date: "2016-10-28T23:55:00"
morea_summary: "Update your program that administers a basic hexidecimal addition quiz."
morea_labels: 
  - "Homework Assignment"
---

# ICS 111 Homework Assignment H08: Addition Quiz with classes.

In homework H06 asked you to write a program that administers a 10-question hexadecimal addition quiz. Rewrite that program so that it uses the following class to represent addition questions:

{% highlight java %}
public class HexAdditionQuestion {

    private int a, b;  // The numbers in the problem.

    public HexAdditionQuestion() { // constructor
        a = (int)(Math.random() * 50 + 1);
        b = (int)(Math.random() * 50);
    }

    public String getQuestion() {
        return "What is " + asHex(a) + " + " + asHex(b) + " ?";
    }

    public int getCorrectAnswer() {
        return a + b;
    }
    
    public String correctAnswerAsHex() {
        return Integer.toHexString(a + b);
    }
    
    private String asHex(int val) {
        return Integer.toHexString(val);
    }
}

{% endhighlight %}


## Turning in the Assignment

The assignment is due on Friday, October 28th at 11:55pm. You may turn it in early. 

1. Conduct a personal review of your code before turning it in. Does your code follow the [Java Coding Standard](../references/reading-java-coding-standard.html)?

   Is it clear and well commented?

2. Test your code.

    * Does it produce the correct output? 

3. Sign into Laulima, then navigate to the ICS111 site. In the left hand side of the site, there is an Assignments tab/link.  Click on it and view all of the posted assignments. Select the assignment that you want to turn in and attach your files and accept the honor pledge to submit the assignment.
  
