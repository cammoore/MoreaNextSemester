---
morea_id: experience-H04
morea_type: experience
title: "H04: Processing a file."
published: True
morea_start_date: "2016-09-23T23:55:00"
morea_summary: "Write a program to process a text file."
morea_labels: 
  - "Homework Assignment"
---

# ICS 111 Homework Assignment H04: Processing a file

Suppose that a file contains visitor information about visitors to Hawaii from various countries. Each line of the file contains a country name, followed by a colon (:) followed by the number of visitors for that country, followed by a colon (:), followed by the dollars spent by the visitors. The number of visitors is a number of type **int**. The dollars spent is a number of type **double**. However, for some countries, no data was available. In these lines, the data is replaced by a comment explaining why the data is missing. For example, several lines from the file might look like:

    Canada: 135132: 140020521.00
    Bulgaria: no report received
    Mexico: 200123: 98298734.12

Write a program that will compute and print the total visitors from all the countries together and their average spending.

The program should also report the number of countries for which data was not available. The name of the file is “visitors.dat”. To complete this program, you’ll need one fact about file input with TextIO that was not covered in Subsection 2.4.4. Since you don’t know in advance how many lines there are in the file, you need a way to tell when you have gotten to the end of the file. When TextIO is reading from a file, the function TextIO.eof() can be used to test for end of file. This boolean-valued function returns true if the file has been entirely read and returns false if there is more data to read in the file. This means that you can read the lines of the file in a loop **while (TextIO.eof() == false)...**. The loop will end when all the lines of the file have been read. 

You can download an example [visitors.dat](visitors.dat) file to test your code.  You sould create your own files for testing.

**Suggestion:** For each line, read and ignore characters up to the first colon. Then read the characters up to the second colon into a variable of type String. Try to convert the string into a number, and use **try..catch** to test whether the conversion succeeds. Do the same for the characters after the second colon.


## Turning in the Assignment

The assignment is due on Friday, September 23rd at 11:55pm. You may turn it in early. 

1. Conduct a personal review of your code before turning it in. Does your code follow the [Java Coding Standard](../references/reading-java-coding-standard.html)?

   Is it clear and well commented?

2. Test your code.

    * Does it produce the correct output? Calculate the values by hand then check to see if it gets the math right.

3. Sign into Laulima, then navigate to the ICS111 site. In the left hand side of the site, there is an Assignments tab/link.  Click on it and view all of the posted assignments. Select the assignment that you want to turn in and attach your files and accept the honor pledge to submit the assignment.
  
