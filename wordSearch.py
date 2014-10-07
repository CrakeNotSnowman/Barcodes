#!/usr/bin/env python
#Word Search


#print "Importing dictionaryToArrays..."
import dictionaryToArrays


D2 = {}


def threshold_Edit(D, count_Threshold, length_Threshold):
    D2 = {}
    word_Array = []
    count_Array = []
    hold_Array = []
    hold_Array = dictionaryToArrays.dictionary_To_Arrays(D)
    word_Array = hold_Array[0]
    
    threshold_Word_Array = []
    threshold_Count_Array = []

    for i in range (len(word_Array)):        
        if (int(len(D[word_Array[i]])) >= int(count_Threshold)):
            if (len(word_Array[i]) >= int(length_Threshold)):
                #flipWord = word_Array[i]#*
                #flipWord = flipWord[::-1]#*
                threshold_Word_Array.append(word_Array[i])
                D2[word_Array[i]] = D[word_Array[i]]
    

    return D2

def letter_Look_Ahead(D, P_of_Occur, count_Threshold) :
    D2 = {}
    word_Array = []
    hold_Array = dictionaryToArrays.dictionary_To_Arrays(D)
    word_Array = hold_Array[0]
    letter_Array = ['A', 'C', 'G', 'T']
    weighted_Prob_Array = [len(D['A']), len(D['C']), len(D['G']), len(D['T'])]
    sum_Prob = float(weighted_Prob_Array[0] + weighted_Prob_Array[1] + weighted_Prob_Array[2] + weighted_Prob_Array[3])   
    weighted_Prob_Array[0] = weighted_Prob_Array[0] / float(sum_Prob)
    weighted_Prob_Array[1] = weighted_Prob_Array[1] / float(sum_Prob)
    weighted_Prob_Array[2] = weighted_Prob_Array[2] / float(sum_Prob)
    weighted_Prob_Array[3] = weighted_Prob_Array[3] / float(sum_Prob)
    print weighted_Prob_Array
    print '^'
    grown_Word_Array = [0, 0, 0, 0]
    errorCheckArray = [] #
    for i in range (len(word_Array)):
        if (int(len(D[word_Array[i]]))>= int(count_Threshold)):
            word_Count = len(D[word_Array[i]])
            word = word_Array[i]

            for j in range (len(letter_Array)):
                new_Word = str(word + str(letter_Array[j]))
                try:
                    new_Word_Count = len(D[new_Word])
                except KeyError:
                    new_Word_Count = 0

                grown_Word_Array[j] = float(new_Word_Count) / word_Count
            if (grown_Word_Array[0] <= (weighted_Prob_Array[0] + .05)) :
                if (grown_Word_Array[1] <= (weighted_Prob_Array[1] + .05)) :
                    if (grown_Word_Array[2] <= (weighted_Prob_Array[2] + .05)) :
                        if (grown_Word_Array[3] <= (weighted_Prob_Array[3] + .05)) :
                            D2[word] = D[word]
            else :
                errorCheckArray.append(D[word])#


    print 'hi says crake'
    print len(errorCheckArray)#
##            word_A = word + 'A'
##            
##
##            
##            word_C = word + 'C'
##            word_G = word + 'G'
##            word_T = word + 'T'



            
    
    return D2

def letter_Look_Ahead_Alpha(D, P_of_Occur, count_Threshold) :
    D2 = {}
    word_Array = []
    hold_Array = dictionaryToArrays.dictionary_To_Arrays(D)
    word_Array = hold_Array[0]
    letter_Array = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    grown_Word_Array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    errorCheckArray = [] #
    for i in range (len(word_Array)):
        if (int(len(D[word_Array[i]]))>= int(count_Threshold)):
            word_Count = len(D[word_Array[i]])
            word = word_Array[i]

            for j in range (len(letter_Array)):
                new_Word = str(word + str(letter_Array[j]))
                try:
                    new_Word_Count = len(D[new_Word])
                except KeyError:
                    new_Word_Count = 0

                grown_Word_Array[j] = float(new_Word_Count) / word_Count
            if (grown_Word_Array[0] <= P_of_Occur) :
                if (grown_Word_Array[1] <= P_of_Occur) :
                    if (grown_Word_Array[2] <= P_of_Occur) :
                        if (grown_Word_Array[3] <= P_of_Occur) :
                            D2[word] = D[word]
            else :
                errorCheckArray.append(D[word])#


    print 'hi says crake'
    print len(errorCheckArray)#
##            word_A = word + 'A'
##            
##
##            
##            word_C = word + 'C'
##            word_G = word + 'G'
##            word_T = word + 'T'



            
    
    return D2





