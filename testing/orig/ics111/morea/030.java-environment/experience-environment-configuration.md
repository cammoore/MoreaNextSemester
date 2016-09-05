---
morea_id: experience-environment-configuration
morea_type: experience
title: "E01: Environment configuration"
published: True
morea_start_date: "2016-08-29T00:00:00"
morea_summary: "Configure your development environment."
morea_labels: 
---

# E01: Environment configuration

For ICS 111 and the rest of your ICS career it is highly recommended that you set up a good software development environment. In this experience you will begin the process of creating a high quality software engineering environment on your computer.

This is an optional experience.

## Task 1: Have appropriate hardware

Preferred hardware is a laptop with >= 2 Ghz processor, >= 2 GB RAM, >= 20 GB free disk space, and wireless access. As noted in the lecture, a Dell Laptop satisfies these requirements for $500-$1000. Note that “netbooks” are not suited for professional software development: while more portable, their screens are too small and they generally have less RAM and slower CPUs.

## Task 2: Install an appropriate operating system

An up to date release of Mac OS/X or a Linux-based OS are the preferred operating systems for this class. If you must use Windows, you should use the latest release.

If needed, I can sign you up for MSDNAA, which will provide you with a free copy of the latest Windows OS.

## Task 3: Install Java 8

### Determine if you need to install Java 8

Most of the time, you will need to install a new version of Java for this course.  To see whether you will need to do so, open a command shell and type `java -version`:

    $ java -version 
      java version "1.8.0_05"
      Java(TM) SE Runtime Environment (build 1.8.0_05-b13)
      Java HotSpot(TM) 64-Bit Server VM (build 25.5-b02, mixed mode)

### Install the Java JDK

If the 'java' command does not work, or if the version is not 1.8, then you will need to install a new version of Java JDK following the directions at the [Java SDK Downloads Page](http://www.oracle.com/technetwork/java/javase/downloads/index.html). 

You must download and install the **JDK** version of Java, not just the JRE.
 
### Verify JAVA_HOME

In addition to the `java -version` command working properly, you must also make sure that the JAVA_HOME environment variable is set correctly.  

On Unix machines (Linux, Mac), you can check as follows:

    $ printenv | grep JAVA_HOME
      JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_05.jdk/Contents/Home

This output indicates that the JAVA_HOME environment variable is set and it is set to the Java 8 installation. 

On Windows, you can type `set` to see the list of all environment variables.

### Switch between versions of Java (optional)

Some of you might need to switch back and forth among different versions of Java. For example, you might need to use Java 8 for this course and Java 7 for your research project (because, for example, it requires a library that only runs on Java 7).

There are a variety of ways to switch between Java versions:

  *  For Mac users, see [this post](http://superuser.com/questions/490425/how-do-i-switch-between-java-7-and-java-6-on-os-x-10-8-2), or use the [jEnv](http://www.jenv.be/) environment.
  *  For Windows users, see [this post](https://blogs.oracle.com/pranav/entry/switch_between_different_jdk_v).


## Task 4: Install the Eclipse IDE (Integrated Development Environment)

You can program in Java just using a text editor and the Java compiler and virtual machine. Please don't. Modern IDEs make you a vastly more productive developer. There are many popular IDEs available:

 * Eclipse
 * jGRASP
 * Netbeans
 * IntelliJ IDEA
 * Visual Studio

We are going to use Eclipse as our IDE. [Download the Eclipse installer](http://www.eclipse.org/downloads/) and install it on your computer.  Follow the [Getting Started with the Eclipse Workbench](http://help.eclipse.org/mars/index.jsp?nav=%2F0) and [Getting Started with Java development](http://help.eclipse.org/mars/index.jsp?nav=%2F1) tutorials.


You can watch this quick screen cast of me installing Eclipse Mars.1.

{% include youtube.html id="IKbACaJt6n0" %}

## Submission Instructions

To be completed by the time and date indicated on the Schedule page.
