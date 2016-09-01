---
morea_id: experience-A09
morea_type: experience
title: "A09: Huffman Trees"
published: True
morea_summary: "Implement Huffman encoding using a Huffman Tree."
#morea_start_date: "2016-04-15T23:55:00"
morea_sort_order: 36
morea_labels: 
  - "Homework Assignment"
---


# ICS 211 Homework A09: Compress and Decompress files using Huffman Coding.

In this assignment you will write a program that decompresses files that were compressed using Huffman encoding.

Your program should take a filename as a command line argument. If no such argument is given, print a usage message explaining what the program does and how to use it.

If the filename ends with a ".huff" extension, decompress the file. Remove the .huff extension to get the output filename. For example, if you run your program as

{% highlight bash %}
$ java A09Huffman homework.txt.huff
{% endhighlight %}

your program will decompress homework.txt.huff into homework.txt.

If the filename does not end with a ".huff" extension, what your program does is up to you (so long as it doesn't crash). You can compress the given file instead (using the code given below), or you can just print an error message and quit. If the file you are extracting to (such as homework.txt in the example above) already exists, it is also up to you whether to simply overwrite it or to ask the user if they would like to abort.

A valid .huff file will contain the following segments in this order:

  * count: 4 bytes (an int) containing a count of the number of bytes in the original uncompressed file.
  * tree data: A pre-order traversal of the Huffman tree used, with 0 marking internal nodes and 1 marking leaf nodes. Every leaf node (1) is followed by 8 bits containing the byte of data for that leaf node. Every tree will have at least one internal node at the root.
  * traversal data: A series of paths that each start at the root and lead to a leaf node that specifies the corresponding symbol in the original file. A 0 bit means go left, a 1 bit means go right. The valid traversal data ends when count symbols have been decoded. There may be extra bits remaining to complete the last byte of the file.

There are no extra bits or markers between the three file segments.

The following source code files should be useful:

* [BitReader.java](bitreader-java.html)
* [BitWriter.java](bitwriter-java.html)
* [HexFileDump.java](hexfiledump-java.html)
* [HuffmanNode.java](huffmannode-java.html)
* [Huffman.java](huffman-java.html)

You need to modify the `Huffman.java` file to implement:
 
* The `public Huffman(BitReader input)` constructor. The constructor initializes the Huffman tree starting with the pre-order traversal of the Huffman tree. You should create a private recursive method that returns the root of the Huffman Tree and call this method in the constructor. Look at the constructors for the `HuffmanNode` class (especially `public HuffmanNode(E data, int count)` and `public HuffmanNode(HuffmanNode<E> left, HuffmanNode<E> right)`). Nodes in a Huffman Tree are either internal nodes with no data or leaf nodes, with no children, holding the data.
 
* The `public static void decompress(InputStream in, OutputStream out)` method. Follow the comments in the method. You should the `decode(int bytes, BitReader in, OutputStream out)` method.  

* and the `public void decode(int bytes, BitReader in, OutputStream out)` method. You could write a method something like `private byte getByte(Huffman tree, BitReader encoding)`. This method uses encoding to traverse the Huffman tree from the root to the correct leaf and returns the byte value stored in the leaf node. If the encoding bit is 0 you traverse left, if 1 traverse right, till you get to a leaf. Then just loop bytes times calling the `getByte` method.


You also need to create the A09Huffman class that takes the command line arguments.

You can use the following files to test your code:

* [ics211.bmp](files/ics211.bmp)
* [ics211.bmp.huff](files/ics211.bmp.huff)
* [image.bmp.huff](files/image.bmp.huff)
* [jabberwocky.txt](files/jabberwocky.txt)
* [jabberwocky.txt.huff](files/jabberwocky.txt.huff)
* [mission.huff](files/mission.huff)
* [short.txt.huff](files/short.txt.huff)
* [sounds.mp3.huff](files/sounds.mp3.huff)
* [triangles.txt.huff](files/triangles.txt.huff)
* [zorro.txt.huff](files/zorro.txt.huff)


## Testing

You must also build your own test code to make sure that your implementation works. Please thoroughly test your code and briefly discuss your testing strategy. Turn in all test code.

## Turning in the Assignment

The assignment is due on Friday at 11:55pm. You may turn it in early. 

1. Conduct a personal review of your code before turning it in. Does you code follow the [Java Coding Standard](../010.introduction/reading-java-coding-standard.html)? Is it clear and well commented?
2. Test your code. Did you get an ArrayIndexOutOfBoundsException?
3. Sign into Laulima, then navigate to the ICS211 site. In the left hand side of the site, there is an Assignments tab/link.  Click on it and view all of the posted assignments. Select the assignment that you want to turn in and attach your files and accept the honor pledge to submit the assignment. 
  
