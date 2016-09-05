---
morea_id: quiz-2d
morea_type: experience
title: "Q26: Two dimensional arrays"
published: True
morea_summary: "Figure out what the code does."
morea_labels:
  - Quiz
morea_sort_order:
#morea_start_date: "2016-01-12"
#morea_end_date: "2016-01-13"
---

# Q26: Two Dimensional Arrays

* Take out a piece of paper and put your name on the upper right corner.

* Answer the following questions.

  1. What is the purpose of the following subroutine?
  2. What is the meaning of the value that it returns, in terms of the value of its parameter?
  
{% highlight java %}
static double[] sums( double[][] data ) {
    double[] answers = new double[ data.length ];
    for (int i = 0; i < data.length; i++) {
        double sum = 0;
        for (int j = 0; j < data[i].length; i++)
            sum = sum + data[i][j];
        answers[i] = sum;
    }
    return answers;
}
{% endhighlight %}

Finish your answers before the timer runs out.

{% include quiz-timer.html quiz_time="14" %}
