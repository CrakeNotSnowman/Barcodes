#! /usr/bin/env python

#print "Importing grammar2..."
import grammar2
#print "Importing Dstore..."
#import Dstore
import wordSearch
import dictionaryToArrays
#import sendMessage
#import saveFile
import fasta
import barcodeArrayBuilder
import GrayScaleCodeTag


def dictionaryFilter(D):
    count_Threshold = 30     #greater than or equal to
    length_Threshold = 3    #greater than or equal to
    p_Of_Occur = 0.30    #less than or equal to
    D = wordSearch.letter_Look_Ahead(D, p_Of_Occur, count_Threshold)
    return D

def getArray(seq):
    D, maxL = grammar2.LZ78_av(seq)
    print "\tBUILT DICTIONARY"
    #D = dictionaryFilter(D)
    seqBarCode = barcodeArrayBuilder.array_Build_C(len(seq), D, seq, maxL)
    print "\tBUILT ARRAY"
    return seqBarCode

def paintIt(seqBarcode, fileName = "outfile.png"):
    preppedBarcode = GrayScaleCodeTag.arrangeSequence(seqBarcode, 512)
    GrayScaleCodeTag.drawCodeTag(preppedBarcode, fileName)
    return

def main():
    seq = '/home/keith/Documents/filesForProgramming/Seqs/Chlorella/sequence (29).fasta'
    #seq = 'SEQTESTS.txt'
    seq = fasta.fna_read(seq)
    #seq = "GAGACAAATACTCTTTTGGTTTACCGTTAAAAGAAAAATATGTTNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNTTTGATAGTTTTGTTGTTGGAGATGCTAACAAAATTGCTAGAGCAGCAGCTATGCAGGTATCGATAAATCCAGGTAAATTACATAACCCTTTATTCATTTATGGTGGTAGTGGTTTAGGTAAAACTCACTTAATGCAAGCAATAGGTAATCATGCAAGAGAAGTTAATCCTAATGCCAAAATTATTTATACAAATTCAGAACAATTTATTAAAGATTATGTAAATTCTATTCGTTTACAAGATCAAGATGAGTTTCAAAGAGTTTATAGATCTGCGGATATACTTTTGATTGATGATATTCAATTTATCGCTGGTAAAGAGGGTACTGCTCAGGAGTTTTTCCATACTTTTAATGCATTGTATGAAAATGGTAAACAGATAATTCTAACTAGTGATAAGTATCCAAATGAAATAGAAGGGCTTGAAGAAAGACTAGTTTCGCGTTTTGGTTATGGTTTAACAGTTTCTGTTGATATGCCAGATTTAGAAACCAGAATTGCTATCTTGCTCAAAAAAGCTCATGATTTAGGTCAGAAATTACCTAACGAAACAGCAGCTTTTATTGCTGAGAATGTACGTACTAATGTCAGAGAACTAGAAGGTGCTCTAAATAGGGTTCTTACTACCTCTAAATTTAATCATAAAGATCCTACTATCGAAGTT"
    seq = "GAGACATAAAAGCTAGACAT"
    seq = '''dearJoferyYouSuckhereishamletusage: BarcodePainter.py [-h] [-i INPUT_FILE] [-o OUTPUT_FILE] [-c NUM_COLORS] [-w OUTPUT_WIDTH] [-t OUTPUT_HEIGHT]



Create a barcode image for a vector of colors

optional arguments:
 
	-h, --help
	                show this help message and exit

	-i INPUT_FILE, --input-file INPUT_FILE

                        Input coloring file*
  
	-o OUTPUT_FILE, --output-file OUTPUT_FILE

                        Output image filename
	-c NUM_COLORS, --num-colors NUM_COLORS

                        Number of colors used to paint the vector
 
	-w OUTPUT_WIDTH, --output-width OUTPUT_WIDTH

                        Width of each block (pixels)
  
	-t OUTPUT_HEIGHT, --output-height OUTPUT_HEIGHT

                        Height of each string (pixels)



* Coloring file format : 

The first line of the file should contain a single integer N, the size of the vector being painted.

The following N lines should contain a single integer k, denoting the zero-indexed color of the corresponding vector entry.


Example:

    3

    0

    0

    1


The example above will create an image including three sections.  
The first two elements are colored with color[0]. 

*NOTE*: There appears to be only two colors possible in this example.  
If this is the case, don't forget to specify '-c 2' '''
    seq = seq.split()
    seq = [x.strip() for x in seq]
    seq = "".join(seq)
    seq = seq.upper()
    barcode = getArray(seq)
    paintIt(barcode)

'''
    seq = '/home/keith/Documents/filesForProgramming/Seqs/Chlorella/sequence (30).fasta'
    seq = fasta.fna_read(seq)
    barcode = getArray(seq)
    paintIt(barcode, "outfile21.png")


    seq = '/home/keith/Documents/filesForProgramming/Seqs/Chlorella/sequence (31).fasta'
    seq = fasta.fna_read(seq)
    barcode = getArray(seq)
    paintIt(barcode, "outfile22.png")


    seq = '/home/keith/Documents/filesForProgramming/Seqs/Chlorella/sequence (23).fasta'
    seq = fasta.fna_read(seq)
    barcode = getArray(seq)
    paintIt(barcode, "outfile23.png")


    seq = '/home/keith/Documents/filesForProgramming/Seqs/Chlorella/sequence (24).fasta'
    seq = fasta.fna_read(seq)
    barcode = getArray(seq)
    paintIt(barcode, "outfile24.png")


    seq = '/home/keith/Documents/filesForProgramming/Seqs/Chlorella/sequence (25).fasta'
    seq = fasta.fna_read(seq)
    barcode = getArray(seq)
    paintIt(barcode, "outfile25.png")


    seq = '/home/keith/Documents/filesForProgramming/Seqs/Chlorella/sequence (26).fasta'
    seq = fasta.fna_read(seq)
    barcode = getArray(seq)
    paintIt(barcode, "outfile26.png")


    seq = '/home/keith/Documents/filesForProgramming/Seqs/Chlorella/sequence (27).fasta'
    seq = fasta.fna_read(seq)
    barcode = getArray(seq)
    paintIt(barcode, "outfile27.png")


    seq = '/home/keith/Documents/filesForProgramming/Seqs/Chlorella/sequence (28).fasta'
    seq = fasta.fna_read(seq)
    barcode = getArray(seq)
    paintIt(barcode, "outfile28.png")
'''

main()



