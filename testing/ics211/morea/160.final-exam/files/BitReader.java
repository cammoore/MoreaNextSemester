import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;

/**
 * A class that wraps any InputStream to support bitwise reads.
 * @author Michael Goldwasser
 *
 */
public class BitReader {
    private int buf;
    private int numBitsBuffered;
    private InputStream stream;
	
    /**
     * Creates a new BitInStream instance that wraps the given InputStream.
     * @param s an underlying InputStream
     */
    public BitReader(InputStream s) {
	stream = s;
	numBitsBuffered = 0;
    }
	
    /**
     * Closes the underlying InputStream.
     * @throws IOException if underlying InputStream throws such an exception
     */
    public void close() throws IOException {
	stream.close();
    }
	
    /**
     * Reads the next bit, returning true if 1, false if 0.
     * @return true if next bit is 1; false otherwise
     * @throws IOException if underlying InputStream throws such an exception
     */
    public boolean readBit() throws IOException {
	if (numBitsBuffered == 0) {
	    buf = stream.read();
	    if (buf == -1) {
		throw new IOException();
	    }
	    numBitsBuffered = 8;
	}
	boolean result = (buf & (1 << (numBitsBuffered-1))) > 0;
	numBitsBuffered--;
	return result;
    }

    /**
     * Reads the next n bits, and returns them as the
     * least significant n bits of an int, with earliest
     * read bit at high-end.
     * 
     * @param n Number of bits (must be 0 <= n <= 32)
     * @return integer with least-significant n bits read
     * @throws IOException if underlying InputStrea throws such an exception
     */
    public int readBits(int n) throws IOException {
	if (n < 0 || n > 32)
	    throw new IllegalArgumentException("must have 0 <= n <= 32");
	int result = 0;
	for (int k = n-1; k >= 0; k--)
	    if (readBit())		
		result |= 1 << k;
	return result;
    }
	
    /**
     * Unit test on file test.txt presumed to have contents "Hello."
     * @param args
     * @throws IOException
     */
    public static void main(String[] args) throws IOException {
	java.io.FileInputStream fis = new java.io.FileInputStream("test.txt");
	BitReader bis = new BitReader(fis);
	boolean[] code = {false, true, false, false, true, false, false, false};
	for (int i=0; i < code.length; i++)
	    if (bis.readBit() != code[i])
		System.out.println("Error on bit " + i);
	if (bis.readBits(8) != 101)
	    System.out.println("Error reading 'e'");
	if (bis.readBit())
	    System.out.println("Error on first 'l'");
	if (bis.readBits(8) != 216)
	    System.out.println("Error on 'll' combo");
	if (bis.readBits(7) != 108)
	    System.out.println("Error on second 'l'");
	if (bis.readBits(4) != 6)
	    System.out.println("Error on first half of 'o'");
	if (bis.readBits(4) != 15)
	    System.out.println("Error on second half of 'o'");
	if (bis.readBits(8) != 46)
	    System.out.println("Error on '.'");
    }	
}
