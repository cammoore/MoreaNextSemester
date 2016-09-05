---
morea_id: reading-midterm1-review-outline
morea_type: reading
title: "Midterm 1 Review"
published: True
morea_summary: "Review for Midterm #1."
morea_sort_order: 4
morea_start_date: "2016-10-03"
morea_labels: 
  - "Lecture"
---


# Outline

* Java review
* Abstract Data Types (ADTs)
* Interfaces
* Class Hierarchy, Abstract Classes, Inheritance
* Lists
  * ArrayList
  * LinkedList
* Runtime analysis
* Iterators
* Java References

## Exam preparation

* All the material in the lectures
* All the material in book in Chapters 1 and 2, and the Java review in appendix A
* All the material in the assignments
* All the quizzes
* Review all the code posted on the course web page. Understand this code well enough to be able to code similar programs. Actual question may ask for something similar, but not quite the same.
* Understand what works in Java and what doesn't:
  * Declare variables before using them
  * Don't pretend that a method exists when you don't know whether it does
  * Return values of the correct type from methods that have a non-void return type,
  * etc.

## Java Review

* Know when to create a new object
* Static methods are called independently of an object, whereas instance methods (non-static methods) can only be called from an object, and only if the object is not null
  examples:

    * *String.length()* is an instance method. So if I have a *String s = ...*, I can call *s.length()*
    * but if *String s = null*, *s.length()* will throw a *NullPointerException*
    * *System.arraycopy()* is a static method. So I can call it without having an object of type System
* Can only use whatever methods the class provides, including methods provided by the superclasses
* *toString()*, *equals* are available for all objects
* Initialize all variables
* Provide at least one constructor for each object
* Parameters must match, and return values must be returned
* Parameters types must match, and return types must match, so for example

{% highlight java %}
public static int foo() {
  return true;
}
{% endhighlight %}

  is incorrect

* Exceptions can be thrown and caught
* Exceptions that are not runtime exceptions must be declared in the method header

{% highlight java %}
public static int foo(int n) throws java.io.IOException {
  if (n < 0)
    throw new java.io.IOException();
  else if (n == 0)
    throw new java.util.NoSuchElementException();
  else
    return n - 1;
}
{% endhighlight %}

* Array indexing and modulo (what is 27 % 8?)
* Private classes

## Abstract Data Types

* A collection of attributes and behaviors makes up an abstract data type
* Similar to the notion of a data type in programming: an int type has an attribute (the value) and several behaviors (addition, subtraction, etc) but not others (negation)
* But an ADT can be much more general than a data type
* ADTs are useful when designing programs
* There are many intuitive ADTs for real-world objects
* ADTs for programs become more intuitive with practice
  * What is the difference between an Abstract Data Type and an Abstract Class?

## Interfaces

* An interface is a list of methods, with their types
* Occasionally interfaces also include constants
* The names of method parameters are significant to the reader, but not to the compiler
* Any class that implements an interface must provide the corresponding methods
* Example: *Iterable*

{% highlight java %}
public interface Iterable<E> {
  java.util.Iterator<E> iterator();
}
{% endhighlight %}

* For exam, need to know the syntax of interfaces, i.e. how to write an interface
* Interfaces can be used as Java types:
  * Any object that implements the interface can be assigned to a variable whose type is the interface
  * For example:

{% highlight java %}
LinkedList<String> list = new LinkedList<String>();
Iterable<String> iterable = list;
{% endhighlight %}
  * Later, could have 

{% highlight java %}
Iterator<String> iter = iterable.iterator();
{% endhighlight %}

  * But: we cannot call *iterable.add("foo")*, even though *iterable* and *list* refer to the same object, and 
    *list.add("foo")* is perfectly legal

## Class Hierarchy, Abstract Classes, Inheritance

* Each class except Object has a superclass
* Each class extends exactly one superclass (if not explicitly stated, it extends Object)
* *this* and *super* references can be used within any instance method
* Every method defined in the superclass is inherited by the subclass
* A class that redefines a superclass's methods is overriding them
* A variable declared to have an interface type can be assigned as a value any object that satisfies (implements) that interface
* An abstract class does not have constructors or objects. Instead, other classes may inherit from the abstract class and use the methods it does define

## Lists

* Variable sized collections of objects in a particular sequence
* Parametrized on the type of the objects that are stored in the list
* Duplicate and *null* elements are permitted
* The [List interface](http://docs.oracle.com/javase/7/docs/api/java/util/List.html) defines required operations, and the [AbstractList class](http://docs.oracle.com/javase/7/docs/api/java/util/AbstractList.html) helps in implementing new list classes
* Some particularly useful methods:
  * [boolean add(E e)](http://docs.oracle.com/javase/7/docs/api/java/util/List.html#add(E)) add at the end of a list
  * [void add(int index, E e)](http://docs.oracle.com/javase/7/docs/api/java/util/List.html#add(int,%20E)) add within the list
  * [Iterator&lt;E&gt; iterator()](http://docs.oracle.com/javase/7/docs/api/java/util/List.html#iterator()) create a new iterator
  * [E remove(int index)](http://docs.oracle.com/javase/7/docs/api/java/util/List.html#remove(int)) remove and return the object at the given position
  * [int size()](http://docs.oracle.com/javase/7/docs/api/java/util/List.html#size())

### Array List

* A list in which the elements are stored in an array
* The array may have more elements than the list, so a class variable is needed to keep track of the size of the list
* As the list grows, may need a new array, so adding at the end of the array is O(n)
* Adding and removing at the beginning or in the middle of the array is always O(n) -- make sure you understand why


### Linked List

* A list in which each element is stored in a node, and nodes are linked to each other
* The number of nodes is exactly the same as the number of elements
* Each node has a reference to the value stored (item, data, value, or a similar name) and a reference to the next node in the list, if any (always called next)
* The end of the list is reached when the *next* field has the value *null*
* A linked list must store the *head* of the list
* Adding at the end of the linked list is faster if a *tail* pointer is kept -- O(1) instead of O(n)
* Adding and removing at the front of a linked list is always O(1)
* In a circular list, the last *next* field refers (back) to the *head* of the list
* In a doubly-linked list, each node has a reference to the node before it (prev or previous)
* In a doubly-linked circular list, the *tail* is the previous node for the *head*, and the *head* is the next node for the *tail*

## Runtime analysis

* Need to meaningfully be able to compare algorithms, independently of which computer they run on
* So ignore constant factors of speed difference
* If two algorithms have different growth rates, e.g. n<sup>2</sup> and n<sup>3</sup>, then for large enough n, the n<sup>3</sup> will take longer even if the constant factor is very small
* Big-O notation: only consider the fastest growing term in the equation, so n<sup>2</sup> + n log n + 5n + 2 is O(n<sup>2</sup>)
* In general, O(1) < O(log n) < O(sqrt(n)) < O(n) < O(n<sup>2</sup>) < O(n<sup>3</sup>) < O(2<sup>n</sup>)
* This also means that O(n) < O(n log n) < O(n sqrt(n)) < O(n<sup>2</sup>)
* If in doubt, review the loops program (and run it yourself!) and make sure you understand the growth rates and where they come from
* Only consider the worst-case running time
* On the exam, you may be asked to do runtime analysis of simple programs or code snippets, or of algorithms studied in this class

## Iterators

* An iterator is an object that keeps track of the state of a traversal of a collection
* An iterator is like a bookmark for a book: there can be many bookmarks for a given book, and they are objects that are different from both the book and the reader
* Calling the *iterator()* method of a collection class is the usual way to create a new iterator
* Once the iterator exists, calls to *hasNext()* and *next()* may continue until there are no more elements
* Or, calling just *next()* until it throws an exception
* For example:

{% highlight java %}
List<E> list = ...
Iterator<E> iter = list.iterator();
while (iter.hasNext()) {
  E variable = iter.next();
  // can use "variable" in the loop
}
{% endhighlight %}

* As an alternative to explicitly calling the iterator methods, use the *foreach* style:

{% highlight java %}
for (E variable: Iterable<E>) {
  // can use "variable" in the loop
}
{% endhighlight %}

* Understand and be able to implement at least the *hasNext()* and *next()* methods of these two iterators: [LinkedListIterator.java](LinkedListIterator.java.html), and [ArrayListIterator.java](ArrayListIterator.java.html)

## Java References

* Every Java variable (that is not of a basic type) is a reference to an object, and may be *null*
* Two objects can be equal in different ways:
  * *a == b* if and only if both references are to the same object, or both are *null*
  * *a.equals(b)* if *a* is not *null*, and *a*'s *equals* method returns *true* when given *b* as a parameter
  * Usually, *a.equals(b)* if the contents of *a* match the contents of *b*
  * For example:

{% highlight java %}
String a = new String("foo");
String b = new String("foo");
if (a == b) {
  System.out.println("two different objects are equal!  Something is wrong");
}
if (a.equals(b)) {
  System.out.println("foo is equal to foo.  Life is good");
}
{% endhighlight %}

* If I pass an *int* as parameter to a method, and the method changes the value of the *int*, my value does not change. For example:

{% highlight java %}
int x = 3;
m(x);
{% endhighlight %}

  The value of x is still 3 after the call, no matter what m does.

* If I pass an object as parameter to a method, and the method changes what object the parameter refers to, my value does not change. For example:

{% highlight java %}
LinkedList<Integer> x = new LinkedList<Integer>();
...
m(x);
...
void m(LinkedList<Integer> parameter) {
  parameter = new LinkedList<Integer>();
}
{% endhighlight %}

  x still refers to the original linked list (not the new list) after the call.

* If I pass an object as parameter to a method, and the method changes the values stored in the object, my value is changed as well. For example:
  
{% highlight java %}
LinkedList<Integer> x = new LinkedList<Integer>();
...
m(x);
...
void m(LinkedList<Integer> parameter) {
  parameter.add(13);
}
{% endhighlight %}

  after this call, x refers to the same list, which now has a new element.
