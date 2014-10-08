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

def saveArray(arr, fileName):
    target = open(fileName, "a")
    for i in range((len(arr)*3/4-20*512),(len(arr)*3/4+20*512)):
	target.write(str(arr[i]))
	target.write("\t")
    target.write("\n")
    target.close()
    return

def dictionaryFilter(D):
    count_Threshold = 30     #greater than or equal to
    length_Threshold = 3    #greater than or equal to
    p_Of_Occur = 0.30    #less than or equal to
    D = wordSearch.letter_Look_Ahead(D, p_Of_Occur, count_Threshold)
    return D

def getArray(seq):
    D, maxL = grammar2.LZ78_av(seq)
    print "\tBUILT DICTIONARY: Max L: ", maxL
    #D = dictionaryFilter(D)
    seqBarCode = barcodeArrayBuilder.array_Build_C(len(seq), D, seq, maxL)
    print "\tBUILT ARRAY"
    return seqBarCode

def paintIt(seqBarcode, fileName = "outfile.png"):
    preppedBarcode = GrayScaleCodeTag.arrangeSequence(seqBarcode, 512)
    GrayScaleCodeTag.drawCodeTag(preppedBarcode, fileName)
    return

def main():
    seq = '/home/keith/Documents/filesForProgramming/Seqs/Chlorella/sequence (4).fasta'
    #seq = '/home/keith/Documents/filesForProgramming/Dictionary/Seqs/Bact/Francisella_tularensisNE061598.fna'
    seq = "randomSeq.tfa"
    seq = fasta.fna_read(seq)
    saveArray(list(seq), "ErrorSearch.txt")
    #seq = "GAGACAAATACTCTTTTGGTTTACCGTTAAAAGAAAAATATGTTNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNTTTGATAGTTTTGTTGTTGGAGATGCTAACAAAATTGCTAGAGCAGCAGCTATGCAGGTATCGATAAATCCAGGTAAATTACATAACCCTTTATTCATTTATGGTGGTAGTGGTTTAGGTAAAACTCACTTAATGCAAGCAATAGGTAATCATGCAAGAGAAGTTAATCCTAATGCCAAAATTATTTATACAAATTCAGAACAATTTATTAAAGATTATGTAAATTCTATTCGTTTACAAGATCAAGATGAGTTTCAAAGAGTTTATAGATCTGCGGATATACTTTTGATTGATGATATTCAATTTATCGCTGGTAAAGAGGGTACTGCTCAGGAGTTTTTCCATACTTTTAATGCATTGTATGAAAATGGTAAACAGATAATTCTAACTAGTGATAAGTATCCAAATGAAATAGAAGGGCTTGAAGAAAGACTAGTTTCGCGTTTTGGTTATGGTTTAACAGTTTCTGTTGATATGCCAGATTTAGAAACCAGAATTGCTATCTTGCTCAAAAAAGCTCATGATTTAGGTCAGAAATTACCTAACGAAACAGCAGCTTTTATTGCTGAGAATGTACGTACTAATGTCAGAGAACTAGAAGGTGCTCTAAATAGGGTTCTTACTACCTCTAAATTTAATCATAAAGATCCTACTATCGAAGTT"
    #seq = "GAGACATAAAAGCTAGACAT"
    #seq = '''CATMAN '''
    #seq = seq.split()
    #seq = [x.strip() for x in seq]
    #seq = "".join(seq)
    #seq = seq.upper()
    barcode = getArray(seq)
    saveArray(barcode, "ErrorSearch.txt")
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



