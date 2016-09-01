---
morea_id: quiz-paintComponent
morea_type: experience
title: "Q20: paintComponent"
published: True
morea_summary: "What does this code do?"
morea_labels:
  - Quiz
morea_sort_order:
#morea_start_date: "2016-01-12"
#morea_end_date: "2016-01-13"
---

## Q20: paintComponent

#### Take out a piece of paper and put your name on the upper right corner.

Draw the picture that will be produced by the following *paintComponent()* method:

{% highlight java %}
public static void paintComponent(Graphics g) {
    super.paintComponent(g);
    g.drawLine(64, 10, 94, 32);
    g.drawLine(94, 32, 82, 67);
    g.drawLine(82, 67, 45, 67);
    g.drawLine(45, 67, 64, 10);
}
{% endhighlight %}


Finish your answers before the timer runs out.

{% include quiz-timer.html quiz_time="12" %}



