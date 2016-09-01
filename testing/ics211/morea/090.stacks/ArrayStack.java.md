---
morea_id: reading-array-stack
morea_type: reading
title: "ArrayStack.java"
published: True
morea_summary: ""
morea_sort_order: 4
morea_labels: 
---

{% highlight java %}
/** 
 * A stack implemented using an array
 * @author	Biagioni, Edoardo and Cam Moore
 * @assignment	lecture 7
 * @date	February 4, 2008
 */

import java.util.EmptyStackException;

public class ArrayStack<E> implements StackInterface<E> {
  /* fields to store the stack elements and the location of the
   * top of the stack.
   * the values are in array locations 0..top if top >= 0
   * for an empty array, top is -1
   */
  private int top;
  private E[] array;

  /** no-arguments default constructor creates an empty stack */
  @SuppressWarnings("unchecked")
  public ArrayStack() {
    top = -1;  // empty stack
    array = (E []) (new Object[10]);  // make room for at least 10 items
  }

  /** @return	whether the stack is empty */
  public boolean empty() {
    return (top == -1);
  }
       
  /** @param	value to push onto the stack */
  public void push(E value) {
    /* make sure there is room in the array */
    if (array.length == top + 1) {
      array = java.util.Arrays.copyOf(array, array.length * 2);
    } // else, there already is room for one new element
    top++;
    array[top] = value;
  }

  /** @return	the top value on the stack */
  public E pop() throws EmptyStackException {
    if (empty()) {
      throw new EmptyStackException();
    }
    E result = array[top];
    top--;
    return result;
  }

  /** Different implementation of pop, does exactly the same.
   * @return the top value on the stack
   */
  public E pop2() throws EmptyStackException {
    try {
      return array[top--];
    } catch(java.lang.ArrayIndexOutOfBoundsException error) {
      top = -1;		// just to be sure
      throw new EmptyStackException();
    }
  }

  /** @return the top value on the stack */
  public E peek() throws EmptyStackException {
    if (empty()) {
      throw new EmptyStackException();
    }
    return array[top];
  }

  /** convert the stack to a printable string
   * @return	a string representing the stack
   */
  public String toString() {
    if (empty()) {
      return "Empty Stack";
    } else {
      return recursiveToString(0);
    }
  }

  /** Recursive method to print a non-empty stack
   * @param	the starting index in the array
   * @return	a string representing the stack
   */
  private String recursiveToString(int startPos) {
    if (startPos > top) {
      return "";
    }
    String separator = "";
    if (startPos > 0) {
      separator = " :: ";
    }
    return separator + array[startPos] + recursiveToString(startPos + 1);
  }

  // simple test
  public static void main(String[] args) {
    StackInterface<String> s = new ArrayStack<String>();

    System.out.println("before pushing anything, " + s);
    s.push("hello");
    s.push("world");
    System.out.println("after pushing hello and world, " + s);
    System.out.println("pop returns " + s.pop());
    System.out.println("after popping, " + s);
    StackInterface<Integer> si = new ArrayStack<Integer>();
    // push 100 values
    for (int i = 0; i < 100; i++) {
      si.push(i);
    }
    // now pop them and make sure the same values are returned
    // in LIFO order
    for (int i = 99; i >= 0; i--) {
      Integer returned = si.pop();
      if (! returned.equals(i)) {
        System.out.println("error: pop returns " + returned + ", expected " + i);
      }
    }
    s.push("a");
    s.push("beautiful");
    s.push("day");
    System.out.println("after pushing 'a beautiful day', " + s);
    System.out.println("pop returns " + s.pop());
    System.out.println("pop returns " + s.pop());
    System.out.println("pop returns " + s.pop());
    System.out.println("pop returns " + s.pop());
    System.out.println("after popping, " + s);
	/* expected output:
	 * before pushing anything, Empty Stack
	 * after pushing hello and world, hello :: world
	 * pop returns world
	 * after popping, hello
	 * after pushing 'a beautiful day', hello :: a :: beautiful :: day
	 * pop returns day
	 * pop returns beautiful
	 * pop returns a
	 * pop returns hello
	 * after popping, Empty Stack
	 */
    }
}
{% endhighlight %}
