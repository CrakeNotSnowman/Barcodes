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
import os
import numpy

def regionOfInterest(barcodeArray, seqName, seq):
    interestFile = open("barcodePointsOfInterest.txt", "a")
    roiPercentile = 5
    #eliminateN's from factoring the low percentile
    avg = numpy.average(barcodeArray)
    for j in range(len(seq)):
	if (seq[j] == "N"):
	    barcodeArray[j] = avg

    mini = numpy.percentile(barcodeArray, roiPercentile)
    maxi = numpy.percentile(barcodeArray, 100 - roiPercentile)
    roiLen = 250
    currRoiLen = 0
    allowedGrey = 10
    currGrey = 0
    interestingStr = ""
    interestingStrHead = -1
    #interestFile.write( "Percentile used: " + str(roiPercentile) + "\n" +\
	#		"\tLower: " + str(mini) + "\n" +\
	#		"\tUpper: " + str(maxi) + "\n" +\
	#		"Min Region of Interest Length: " + str(roiLen) + "\n" +\
	#		"Allowed Number of Non Interesting Entries: " + str(allowedGrey) + "\n\n")
			
    for i in range(len(barcodeArray)):
	if ((barcodeArray[i] > maxi) or ((barcodeArray[i] < mini) and (seq[i] != "N")) ):
	    # if, the index is great than the xth percentile, or 
	    # if, the index is less than the xth percentile AND not an "N" char
	    interestingStr = interestingStr + str(seq[i])
	    if(currRoiLen == 0):
		interestingStrHead = i
	    currRoiLen += 1
	    if ((currRoiLen % roiLen) == 0):
		currGrey = 0
	elif ((currGrey <= allowedGrey) and (currRoiLen > 0)):
	    interestingStr = interestingStr + str(seq[i])
	    currRoiLen += 1
	    currGrey += 1
	    if ((currRoiLen % roiLen) == 0):
		currGrey = 0
	elif ((currRoiLen >= roiLen) and (currGrey > allowedGrey)):
	    interestFile.write(">" + str(seqName) + " Length: "+ str(i-interestingStrHead) + " " + str(interestingStrHead) + "..." + str(i-1) + "\n")
	    interestFile.write(str(interestingStr) + "\n")
	    interestingStrHead = -1
	    currRoiLen = 0
	    currGrey = 0
	    interestingStr = ""
	else:
	    interestingStrHead = -1
	    currRoiLen = 0
	    currGrey = 0
	    interestingStr = ""
    interestFile.close()
    return

def saveArray(arr, fileName):
    target = open(fileName, "a")
    for i in range((len(arr)*3/4-5*512),(len(arr)*3/4+5*512)):
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
    #print "\tBUILT DICTIONARY: Max L: ", maxL
    #D = dictionaryFilter(D)
    seqBarCode = barcodeArrayBuilder.array_Build_C(len(seq), D, seq, maxL)
    #print "\tBUILT ARRAY"
    return seqBarCode

def paintIt(seqBarcode, fileName = "outfile.png"):
    preppedBarcode = GrayScaleCodeTag.arrangeSequence(seqBarcode, 512)
    GrayScaleCodeTag.drawCodeTag(preppedBarcode, fileName)
    return

def otherMain(seq, fileName):
    seq = fasta.fna_read(seq)
    barcode = getArray(seq)
    regionOfInterest(barcode, fileName[0:-4], seq)
    paintIt(barcode, fileName)
    return
    

def main():
    seq = '/home/keith/Documents/filesForProgramming/Seqs/Chlorella/sequence (4).fasta'
    #seq = '/home/keith/Documents/filesForProgramming/Dictionary/Seqs/Bact/Francisella_tularensisNE061598.fna'
    #seq = "randomSeq.tfa"
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


def get_sub_files(start_Folder):
    name_OF_Files = []
    for dirname, dirnames, filenames in os.walk(start_Folder):
	for subdirname in dirnames:
	    print os.path.join(dirname, subdirname)
	for filename in filenames:
	    #print os.path.join(dirname, filename)
	    name_OF_Files.append(os.path.join(dirname, filename))
    #print len(name_OF_Files)
    return name_OF_Files

def startHere():
    sourceFolder = "/home/keith/Documents/filesForProgramming/Seqs/Chlorella/"
    fileList = get_sub_files(sourceFolder)
    for i in range(len(fileList)):
	sourceFile = fileList[i]
	fileName = sourceFile.split("/")[-1]
	fileName = fileName[0:-4]
	print fileName
	fileName = str(fileName) + ".png"
	otherMain(sourceFile, fileName)
    return










startHere()



