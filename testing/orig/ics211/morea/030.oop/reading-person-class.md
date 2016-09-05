---
morea_id: reading-person-class
morea_type: reading
title: "Person Class Quiz Solution"
published: True
morea_summary: "My 'solution' to the OOP Quiz."
morea_sort_order: 4
morea_labels: 
  - "Solution"
---
{% highlight java %}
/**
 * Person.java
 * Copyright (C) Cam Moore 2015
 */
package edu.cam;

/**
 * Represents a Person.
 *
 * @author Cam Moore
 *
 */
public class Person implements Comparable<Person> {

  private String lastName;
  private String firstName;
  private Address address;
  private String phoneNumber;


  /**
   * Default constructor, creates a blank Person.
   */
  public Person() {
    this("", "", null, "");
  }


  /**
   * Creates a new Person.
   * @param firstName the first name.
   * @param lastName the last name.
   * @param address the address.
   * @param phoneNumber the phone number.
   */
  public Person(String firstName, String lastName, Address address, String phoneNumber){
    this.lastName = lastName;
    this.firstName = firstName;
    this.address = address;
    this.phoneNumber = phoneNumber;
  }


  /**
   * @return the lastName value.
   */
  public String getLastName() {
    return lastName;
  }


  /**
   * @param lastName the lastName value to set.
   */
  public void setLastName(String lastName) {
    this.lastName = lastName;
  }


  /**
   * @return the firstName value.
   */
  public String getFirstName() {
    return firstName;
  }


  /**
   * @param firstName the firstName value to set.
   */
  public void setFirstName(String firstName) {
    this.firstName = firstName;
  }


  /**
   * @return the address value.
   */
  public Address getAddress() {
    return address;
  }


  /**
   * @param address the address value to set.
   */
  public void setAddress(Address address) {
    this.address = address;
  }


  /**
   * @return the phoneNumber value.
   */
  public String getPhoneNumber() {
    return phoneNumber;
  }


  /**
   * @param phoneNumber the phoneNumber value to set.
   */
  public void setPhoneNumber(String phoneNumber) {
    this.phoneNumber = phoneNumber;
  }


  /* (non-Javadoc)
   * @see java.lang.Comparable#compareTo(java.lang.Object)
   */
  @Override
  public int compareTo(Person o) {
    int result = this.lastName.compareTo(o.lastName);
    if (result == 0) {
      result = this.firstName.compareTo(o.firstName);
    }
    return result;
  }
}
{% endhighlight %}