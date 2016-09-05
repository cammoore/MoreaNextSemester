---
morea_id: reading-modified-string-soln
morea_type: reading
title: "Java Review Quiz Solution"
published: True
morea_summary: "My 'solution' to the Java Review Quiz."
morea_sort_order: 4
morea_labels: 
  - "Solution"
---

{% highlight java %}
/**
 * Q02.java
 * Copyright (C) Cam Moore 2016
 */

/**
 * Q02: A program that capitalizes the vowels in a string and counts the non-vowels.
 *
 * @author Cam Moore
 *
 */
public class Q02 {

  /**
   * @param args the command line arguments.
   */
  public static void main(String[] args) {
    if (args.length > 0) {
      int nonVowels = 0;
      String theInput = args[0];
      for (int i = 0; i < theInput.length(); i++) {
        char c = theInput.charAt(i);
//        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
//          String s = "" + c;
//          System.out.print(s.toUpperCase());
//        }
//        else {
//          nonVowels++;
//          System.out.print(c);
//        }
        switch (c) {
        case 'a':
        case 'e':
        case 'i':
        case 'o':
        case 'u':
        case 'A':
        case 'E':
        case 'I':
        case 'O':
        case 'U':
          String s = "" + c;
          System.out.print(s.toUpperCase());
          break;
        default:
          nonVowels++;
          System.out.print(c);
        }
      }
      System.out.println();
      System.out.println(" There are " + nonVowels);

    }

  }

}
{% endhighlight %}