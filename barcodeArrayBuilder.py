#!/usr/bin/env python

import dictionaryToArrays
import os.path
import numpy
import math


def array_Build_C(seq_Length, Dictionary, seq, maxL):
    array_Built = [ 0 for a in range(seq_Length)]
    maxVal = 0
    for p in range(maxL):
	slide = 0
	while ((slide+p+1) <= seq_Length):
	    if (seq[slide:slide+p+1] in Dictionary):
		for i in range(p+1):
		    array_Built[slide+i] += 1
		    if (maxVal < array_Built[slide+i]):
			maxVal = array_Built[slide+i]
	    slide += 1
    #print Dictionary.keys() 
    #print array_Built
    #print seq
    print maxVal
    return array_Built
	


def array_Build(seq_Length, Dictionary, seq) :
    array_Built = [ 0 for a in range(seq_Length)]
    word_Array = dictionaryToArrays.dictionary_To_Arrays(Dictionary)[0]

    every_Word = 0
    for every_Word in range(len(word_Array)):
        location_Array = Dictionary[word_Array[every_Word]]
        word_Length = len(word_Array[every_Word])

        for every_Occurence in range(len(location_Array)):
            for every_Letter in range (word_Length):
		if (str(seq[(location_Array[every_Occurence] + every_Letter)]) != str("N") ): #Prevents "N" character from impacting barcode
                    array_Built[(location_Array[every_Occurence] + every_Letter)] += 1


    return array_Built

def array_Build_B(seq_Length, Dictionary) :
    array_Built = [ 0 for a in range(seq_Length)]
    word_Array = dictionaryToArrays.dictionary_To_Arrays(Dictionary)[0]

    every_Word = 0
    for every_Word in range(len(word_Array)):
        location_Array = Dictionary[word_Array[every_Word]]
        word_Length = len(word_Array[every_Word])

        for every_Occurence in range(len(location_Array)):
            for every_Letter in range (word_Length):
                array_Built[(location_Array[every_Occurence] + every_Letter)] += ( 1 + int(len(location_Array) * float(word_Length) / 100))

    return array_Built


def barcode_Pre_File(array_Built, save_File_Name, gIDName) :

    array_For_File = []

    indexer_Len = int(len(array_Built) / 1000)
    sum_Tot = 0
    file_Location = []
    max_Num_A = []
    barcode_Style =  []

    for i in range(1000) :
        sum_Tot = 0
        for j in range(indexer_Len) :
            sum_Tot += array_Built[ (i*indexer_Len) + j ]

        if (i == 0) :
            min_Num = sum_Tot
            max_Num = sum_Tot
        if (min_Num > sum_Tot) :
            min_Num = sum_Tot
        if (max_Num < sum_Tot) :
            max_Num = sum_Tot
##    for i in range(len(array_Built)):
##        if (i == 0) :
##            min_Num = array_Built[i]
##            max_Num = array_Built[i]
##        if (min_Num > array_Built[i]) :
##            min_Num = array_Built[i]
##        if (max_Num < array_Built[i]) :
##            max_Num = array_Built[i]
            

        array_For_File.append(sum_Tot)
    #array_For_File = array_Built #TEST
    #Raw
    barcode_Style.append('Raw')
    max_Num_A.append(max_Num)
    file_Location.append('/home/keith/Documents/filesForProgramming/Dictionary/Seqs/FilesForGirus/BarcodeDraftFiles/barcodeFile' + str(save_File_Name) + '.txt') 
    file_Location00 = '/home/keith/Documents/filesForProgramming/Dictionary/Seqs/FilesForGirus/BarcodeDraftFiles/barcodeFile' + str(save_File_Name) + '.txt' 
    file_Write = open(file_Location00, 'w')
    file_Write.write(str(len(array_For_File)))
    file_Write.write("\n")
    for k in range(len(array_For_File)) :
        file_Write.write(str(array_For_File[k]))
        file_Write.write("\n")
    file_Write.close

    #Min Removed
    k = 0
    barcode_Style.append('Minum Removed')
    array01_For_File = []
    for indexer01 in range (len(array_For_File)):
        array01_For_File.append(array_For_File[indexer01] - min_Num)
    file_Location01 = '/home/keith/Documents/filesForProgramming/Dictionary/Seqs/FilesForGirus/BarcodeDraftFiles/barcodeFile01' + str(save_File_Name) + '.txt'
    max_Num_A.append(max_Num - min_Num)
    file_Location.append(file_Location01)     
    file_Write = open(file_Location01, 'w')
    file_Write.write(str(len(array01_For_File)))
    file_Write.write("\n")
    for k in range(len(array01_For_File)) :
        file_Write.write(str(array01_For_File[k]))
        file_Write.write("\n")
    file_Write.close

    #side Bright
    k = 0
    barcode_Style.append('Side Bright')
    array02_For_File = []
    for indexer02 in range (len(array_For_File)):
        step = array_For_File[indexer02] - min_Num
        numNext = step / float(max_Num - min_Num) * 2.
        if (numNext > 1 ) :
            numNext = numNext - 1
            numNext = math.pow(numNext, 0.5)
            numNext = numNext + 1
        if (numNext < 1) :
            numNext = math.pow(numNext, 2.)
        side_Bright = numNext * (max_Num - min_Num) / 2.
        array02_For_File.append(int(side_Bright))        
    file_Location02 = '/home/keith/Documents/filesForProgramming/Dictionary/Seqs/FilesForGirus/BarcodeDraftFiles/barcodeFile02' + str(save_File_Name) + '.txt' 
    file_Location.append(file_Location02) 
    max_Num_A.append(max_Num - min_Num)
    file_Write = open(file_Location02, 'w')
    file_Write.write(str(len(array02_For_File)))
    file_Write.write("\n")
    for k in range(len(array02_For_File)) :
        file_Write.write(str(array02_For_File[k]))
        file_Write.write("\n")
    file_Write.close

    #edge Bright 
    k = 0   
    barcode_Style.append('Edge Bright')
    array03_For_File = []
    for indexer03 in range (len(array_For_File)):
        step = array_For_File[indexer03] - min_Num
        numNext = step / float(max_Num - min_Num) * 2.
        if (numNext < 1 ) :
            numNext = math.pow(numNext, 0.5)
        if (numNext > 1) :
            numNext = numNext - 1
            numNext = math.pow(numNext, 2.)
            numNext = numNext + 1
        edge_Bright = numNext * (max_Num - min_Num) / 2.
        array03_For_File.append(int(edge_Bright))        
    file_Location03 = '/home/keith/Documents/filesForProgramming/Dictionary/Seqs/FilesForGirus/BarcodeDraftFiles/barcodeFile03' + str(save_File_Name) + '.txt' 
    file_Location.append(file_Location03)
    max_Num_A.append(max_Num - min_Num)
    file_Write = open(file_Location03, 'w')
    file_Write.write(str(len(array03_For_File)))
    file_Write.write("\n")
    for k in range(len(array03_For_File)) :
        file_Write.write(str(array03_For_File[k]))
        file_Write.write("\n")
    file_Write.close
    
    vectorFileSave(array_For_File, array01_For_File, array02_For_File, array03_For_File, len(array_Built), max_Num, min_Num, gIDName)

    conV_FileLoc = []
    conV_FileLoc.append('/home/keith/Documents/filesForProgramming/Dictionary/Seqs/FilesForGirus/Barcode_Raw/')#NAME_00.png')
    conV_FileLoc.append('/home/keith/Documents/filesForProgramming/Dictionary/Seqs/FilesForGirus/Barcode_Min_Removed/')#NAME_01.png')
    conV_FileLoc.append('/home/keith/Documents/filesForProgramming/Dictionary/Seqs/FilesForGirus/Barcode_Side_Bright/')#NAME_02.png')
    conV_FileLoc.append('/home/keith/Documents/filesForProgramming/Dictionary/Seqs/FilesForGirus/Barcode_Edge_Bright/')#NAME_03.png')
##    conV_FileLoc00 = 'C:\Python27\\filesForProgramming\\Dictionary\\BarcodePainter\\GenomeImages\\Staph_ATCC12228_00.png'
##    conV_FileLoc01 = 'C:\Python27\\filesForProgramming\\Dictionary\\BarcodePainter\\GenomeImages\\Staph_ATCC12228_01.png'
##    conV_FileLoc02 = 'C:\Python27\\filesForProgramming\\Dictionary\\BarcodePainter\\GenomeImages\\Staph_ATCC12228_02.png'
##    conV_FileLoc03 = 'C:\Python27\\filesForProgramming\\Dictionary\\BarcodePainter\\GenomeImages\\Staph_ATCC12228_03.png'
    
    #return file_Location00, conV_FileLoc02, int(max_Num), min_Num, file_Location01, file_Location02, conV_FileLoc01,conV_FileLoc00
    return file_Location, conV_FileLoc, max_Num_A, int(min_Num), barcode_Style     

def vectorFileSave(orig, minRem, sideB, edgeB, length, max_Num, min_Num, seqName):
    #format:
    #Name of sequence 
    #Length of origional base list
    #Window/k/length of vector
    #vector
    #print "hi"
    
    normalizer = max_Num - min_Num
    
    for i in range(len(orig)):
	orig[i] = float(orig[i]) / max_Num
	minRem[i] = float(minRem[i]) / normalizer
	sideB[i] = float(sideB[i]) / normalizer
	edgeB[i] = float(edgeB[i]) / normalizer

    if (os.path.isfile('DicOrigvectorFile.txt') == False) :
        vectorFile = open('DicOrigvectorFile.txt', "w")
        vectorFile.close()

    vectorFile = open('DicOrigvectorFile.txt', "a")
    vectorFile.write(seqName)
    vectorFile.write("\n")
    vectorFile.write(str(length))
    vectorFile.write("\n")
    vectorFile.write(str(1000))
    vectorFile.write("\n")
    vectorFile.write(str(orig))
    vectorFile.write("\n")

    
    vectorFile.close()  
    #format:
    #Name of sequence 
    #Length of origional base list
    #Window/k/length of vector
    #vector
    #print "hi"
    if (os.path.isfile('DicMinRvectorFile.txt') == False) :
        vectorFile = open('DicMinRvectorFile.txt', "w")
        vectorFile.close()

    vectorFile = open('DicMinRvectorFile.txt', "a")
    vectorFile.write(seqName)
    vectorFile.write("\n")
    vectorFile.write(str(length))
    vectorFile.write("\n")
    vectorFile.write(str(1000))
    vectorFile.write("\n")
    vectorFile.write(str(minRem))
    vectorFile.write("\n")

    
    vectorFile.close()  
    #format:
    #Name of sequence 
    #Length of origional base list
    #Window/k/length of vector
    #vector
    #print "hi"
    if (os.path.isfile('DicEdgeBvectorFile.txt') == False) :
        vectorFile = open('DicEdgeBvectorFile.txt', "w")
        vectorFile.close()

    vectorFile = open('DicEdgeBvectorFile.txt', "a")
    vectorFile.write(seqName)
    vectorFile.write("\n")
    vectorFile.write(str(length))
    vectorFile.write("\n")
    vectorFile.write(str(1000))
    vectorFile.write("\n")
    vectorFile.write(str(edgeB))
    vectorFile.write("\n")

    
    vectorFile.close()  
    #format:
    #Name of sequence 
    #Length of origional base list
    #Window/k/length of vector
    #vector
    #print "hi"
    if (os.path.isfile('DicSideBvectorFile.txt') == False) :
        vectorFile = open('DicSideBvectorFile.txt', "w")
        vectorFile.close()

    vectorFile = open('DicSideBvectorFile.txt', "a")
    vectorFile.write(seqName)
    vectorFile.write("\n")
    vectorFile.write(str(length))
    vectorFile.write("\n")
    vectorFile.write(str(1000))
    vectorFile.write("\n")
    vectorFile.write(str(sideB))
    vectorFile.write("\n")

    
    vectorFile.close()  

    return
 
