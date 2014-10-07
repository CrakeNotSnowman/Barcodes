#!/usr/bin/env python
#Words into arrays



def dictionary_To_Arrays(Dictionary):
    D_Array_01 = []
    D_Array_01 = Dictionary.items()
    word_Array = []
    count_Array = []
    word_Hold = ""
    count_Hold = []

    i = 0
    for i in range (len(D_Array_01)):
        word_Hold = str(D_Array_01[i])
        #if (i < 2) :
            #print word_Hold
        word_Hold = word_Hold.strip('(')
        word_Hold = word_Hold.strip(')')
        word_Hold = word_Hold.strip('"')
        word_Hold = word_Hold.strip("'")
        #if (i < 2) :
           # print word_Hold
        temp_Word_Array = []
        temp_Word_Array = word_Hold.split("', ")
        #print temp_Word_Array[0]
        
        #print temp_Word_Array[1]
        word_Array.append(temp_Word_Array[0])
        
        count_Array.append(len(Dictionary[word_Array[i]]))

    
    
    return word_Array, count_Array
    



