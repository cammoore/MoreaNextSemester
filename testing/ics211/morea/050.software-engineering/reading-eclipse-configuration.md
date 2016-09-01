---
morea_id: reading-eclipse-configuration
morea_type: reading
title: "Eclipse configuration guide"
published: True
morea_summary: "Installation, the ICS-211 formatter, Checkstyle, editor configuration"
morea_sort_order: 12
morea_labels: 
  - "Optional"
---


# Eclipse configuration guide

## Download and install Eclipse

Download and install Eclipse (neon) from [http://www.eclipse.org](http://www.eclipse.org/).

Click the Download button. This will give you the Eclipse installer for your platform. Run the installer and choose "Eclipse IDE for Java Developers". Do not install it into a file path containing spaces, such as (on Windows) c:\Program Files. Instead, install it in c:\eclipse, c:\ics314\eclipse, or whatever. 

**If you already have an older version of Eclipse installed,**
delete your ~/workspace/ directory or create a new one for the newer version of Eclipse. 

## Install the ICS-211 Java formatter

This simplifies the creation of Java programs that satisfy our formatting
conventions. Download [ics211-format.xml](ics211-format.xml) to your local computer. 

In Eclipse, select "Eclipse / Preferences / Java / Code Style / Formatter" to bring up the following window: 

![eclipse-formatter-window](http://ics314f13.files.wordpress.com/2013/08/eclipse-formatter-window.png?w=300) 

Now click "Import" and choose the file you just downloaded.

The "active profile" should now change to "ICS-211". Click "OK". Now when you
are editing Java source code, you can invoke "Source / Format" to reformat the
Java source code according to our class conventions.

## Install Checkstyle (Very very optional, but useful)

Like the formatter, Checkstyle helps ensure that your code implements our
class coding conventions. Follow the instructions at [http://eclipse-cs.sourceforge.net/downloads.html ](http://eclipse-cs.sourceforge.net/downloads.html) to install the Checkstyle Plugin for
Eclipse. 

You can install both the "Eclipse Checkstyle Plugin" as well as the
"Extension for EclipseCS Plugin with Additional Checks". To verify, go to
"About Eclipse / Installation Details". The window above shows the Checkstyle plugin.

## Install the ICS-211 Checkstyle Ruleset

This task configures Checkstyle to our class's specific coding conventions.
Note: if you are updating checkstyle.xml rather than installing it for the
first time, the easiest way is to simply delete all current projects from
Eclipse, then delete the current checkstyle.xml configuration, then download
and install the new version following the instructions below.

Download [checkstyle.xml](checkstyle.xml) to your local
computer. 

In Eclipse, select "Eclipse / Preferences / Checkstyle", then click
"New.." to bring up the "Check Configuration Properties" window. Select
"External Configuration File" as the Type, provide "ICS-211" as the Name, and
browse to the file to fill the Location field. 

The resulting dialog box should
look like this: 

![ics-211-checkstyle-configuration](CheckstyleConfigDialog.png?w=300) 

Now click "OK" to load that configuration and return
to the Checkstyle Preferences window. In that window, select the ICS-SE
configuration and click "Set as Default". The resulting dialog box should look
like this: 

![checkstyle-preferences](CheckstylePreferencesDialog.png?w=289) 

Click OK to save these changes. Now the Project
Properties dialog will include a Checkstyle pane where you can activate,
deactivate, and customize the application of Checkstyle, as illustrated here:

![checkstyle-project-properties](ProjectPropertiesDialog.png?w=300)

