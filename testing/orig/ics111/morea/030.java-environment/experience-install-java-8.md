---
morea_id: experience-install-java-8
morea_type: experience
title: "Install Java 8"
published: True
morea_summary: "Install Java and avoid gotchas"
morea_labels: 
---

# Install Java 8

## Determine if you need to install Java 8

Most of the time, you will need to install a new version of Java for this course.  To see whether you will need to do so, open a command shell and type `java -version`:

    $ java -version 
      java version "1.8.0_05"
      Java(TM) SE Runtime Environment (build 1.8.0_05-b13)
      Java HotSpot(TM) 64-Bit Server VM (build 25.5-b02, mixed mode)

## Install the Java JDK

If the 'java' command does not work, or if the version is not 1.8, then you will need to install a new version of Java JDK following the directions at the [Java SDK Downloads Page](http://www.oracle.com/technetwork/java/javase/downloads/index.html). 

You must download and install the **JDK** version of Java, not just the JRE.
 
## Verify JAVA_HOME

In addition to the `java -version` command working properly, you must also make sure that the JAVA_HOME environment variable is set correctly.  

On Unix machines (Linux, Mac), you can check as follows:

    $ printenv | grep JAVA_HOME
      JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_05.jdk/Contents/Home

This output indicates that the JAVA_HOME environment variable is set and it is set to the Java 8 installation. 

On Windows, you can type `set` to see the list of all environment variables.

## Switch between versions of Java (optional)

Some of you might need to switch back and forth among different versions of Java. For example, you might need to use Java 8 for this course and Java 7 for your research project (because, for example, it requires a library that only runs on Java 7).

There are a variety of ways to switch between Java versions:

  *  For Mac users, see [this post](http://superuser.com/questions/490425/how-do-i-switch-between-java-7-and-java-6-on-os-x-10-8-2), or use the [jEnv](http://www.jenv.be/) environment.
  *  For Windows users, see [this post](https://blogs.oracle.com/pranav/entry/switch_between_different_jdk_v).



## Submission Instructions

To be completed by the time and date indicated on the Schedule page.


 


