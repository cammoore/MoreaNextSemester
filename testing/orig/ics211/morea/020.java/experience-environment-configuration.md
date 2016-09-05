---
morea_id: experience-environment-configuration
morea_type: experience
title: "Environment configuration"
published: True
morea_summary: "Learn how to configure your development environment."
morea_sort_order: 8
morea_labels: 
  - "Optional"
  - "Recommended"
---

# Environment configuration

For ICS 211 and the rest of your ICS career it is highly recommended that you set up a good software development environment. In this experience you will begin the process of creating a high quality software engineering environment on your computer.

This is an optional experience.

## Task 1: Have appropriate hardware

Preferred hardware is a laptop with >= 2 Ghz processor, >= 2 GB RAM, >= 20 GB free disk space, and wireless access. As noted in the lecture, a Dell Laptop satisfies these requirements for $500-$1000. Note that “netbooks” are not suited for professional software development: while more portable, their screens are too small and they generally have less RAM and slower CPUs.

## Task 2: Install an appropriate operating system

An up to date release of Mac OS/X or a Linux-based OS are the preferred operating systems for this class. If you must use Windows, you should use the latest release.

## Task 3: Install Java 8

### Windows/Linux

Download and install the Java 8 JDK and JavaDoc documentation
from [here](http://www.oracle.com/technetwork/java/javase/downloads/index.html).
Be sure to download and install the "JDK" package, which includes both the JRE and additional tools such as ‘jar’ , ‘javadoc’, and ‘javac’. Don’t download the “JRE” package.

On Windows, you must change the default installation directory to a file path that does not contain spaces. The default on Windows is c:\Program Files\Java, which is bogus. Change it to something like c:\Java. You will run into problems if you install the JDK inside c:\Program Files\.

Add {java}/bin to your PATH variable, where {java} is replaced by the location where you installed it.

Also download the Java SE 8 Documentation. Unzip the documentation package into {java}. If you have installed Java correctly, then you should be able to type “java -version” and “jar -help” at the command line and get reasonable responses. If you have installed the documentation correctly, then you should be able to retrieve it in a browser using a local URL such as:
`file:///C:/Java/jdk1.8.0_65/docs/index.html`. 

The most useful link is to the JavaDocs, at an URL like: `file:///C:/Java/jdk1.8.0_65/docs/api/index.html`.

### Macintosh

You must be running Snow Leopard (10.6) or later. To ensure you are running Java 8 by default, see the [JDK 8 Mac Install Page](http://docs.oracle.com/javase/8/docs/technotes/guides/install/mac_jdk.html).

## Task 4: Install a good Java IDE (Integrated Development Environment)

You can program in Java just using a text editor and the Java compiler and virtual machine. Please don't. Modern IDEs make you a vastly more productive developer. There are many popular IDEs available:

 * Eclipse
 * Netbeans
 * IntelliJ IDEA
 * Visual Studio

Install your chosen IDE and learn how to use it.  Follow the tutorials and become proficient with your IDE.

