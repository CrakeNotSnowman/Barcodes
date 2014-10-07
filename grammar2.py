#!/usr/bin/env python
"""
Created on Thu May 31 12:05:46 2012

@author: oun
"""

def LZ78_av(s): # LZ78 algorithm looking for words at each position
    s=s.upper()     # make the sequence uppercase
    #D={'A':[],'C':[],'G':[],'T':[]}     # initial dictionary
    D = {}
    loc = []
    word = []
    both = []
    maxL = 0
    

    for i in xrange(len(s)):        # do for the whole sequence
        word_len=1                  # start with 1 letter word
        while s[i:i+word_len] in D: #if we have this word in the dictionary
            if (i+word_len)==len(s):    #if we reached the end stop the process
                break
	    if (s[i] == "N"):
		break
            D[s[i:i+word_len]] +=[i]  # counting how many times we look for this word in the dictionary
            word_len +=1            # we had the word in the dictionary, now look for a longer one with an extra letter at the end
	    if (word_len > maxL):
		maxL = word_len
            
        
        if (i+word_len)<len(s):  # if we are at the end of the sequence, don't to anything
            D[s[i:i+word_len]] = [i]   # this is a new word, add it to the dictionarym and say it we encountered it once
        if (i+word_len == len(s)) :
            if ((s[i:i+word_len] in D)) :
                D[s[i:i+word_len]] += [i]
                
            else :
                
                D[s[i:i+word_len]] = [i]
                if (word_len > maxL):
		    maxL = word_len
        i = i+word_len
    return D, maxL  # report the dictionary to the program

def LZ78_av_km(s):
    s = s.upper()
    D = { 'N':0 }
    word_array = []
    count_array = []
    
    cursor = 0
    while cursor in range(len(s)):
        grown_Word_Length = 1
        word = s[cursor : cursor+grown_Word_Length]
        new_word = 0
        for indexer in range(len(word_array)): #check and see if the word already exists
            if (word == word_array[indexer]):
                count_array[indexer] += 1
                grown_Word_Length += 1
                
                word = s[cursor : cursor+grown_Word_Length]
                #print word

        
        word_array.append(word)
        count_array.append(1)
        cursor = (cursor + len(word))

    print word_array
    print count_array
        

    i = 0
    for i in range(len(word_array)):
        D[word_array[i]] = count_array[i]


    print D
    return D
        


#%%%%%%%%%%%%%%%%%%%%%%%%%
def LZ78(s):    # standard LZ78 algorithm
    s=s.upper()     # make the sequence uppercase
    D={'A':0,'C':0,'G':0,'T':0}     # initial dictionary
    cursor_pos=0    # place the cursor to the beginning

    while cursor_pos < len(s):        # do for the whole sequence
        word_len=1                  # start with 1 letter word
        while s[cursor_pos:cursor_pos+word_len] in D: #if we have this word in the dictionary
            if (cursor_pos+word_len)==len(s):    #if we reached the end stop the process
                break
            D[s[cursor_pos:cursor_pos+word_len]] +=1  # counting how many times we look for this word in the dictionary
            word_len +=1            # we had the word in the dictionary, now look for a longer one with an extra letter at the end
        if (cursor_pos+word_len)<(len(s)):  # if we are at the end of the sequence, don't to anything
            D[s[cursor_pos:cursor_pos+word_len]] =1   # this is a new word, add it to the dictionarym and say it we encountered it once
        cursor_pos +=word_len   #we added an item to the dictionary, now move to the next phrase, by changing the cursor position
    
    return D    # report the dictionary to the program
    
    
    
#%%%%%%%%%%%%%%%%%%%%%%%    
def distance(D1,D2):
    d1 = len(set(D1.keys())&set(D2.keys())) # number of common words in two dictionaries
    
    d2=0                        #multiply and add the counts of common words in two dictionaries
    for word in D1.keys():
        if D2.has_key(word):
            d2 += D2[word]*D1[word]

    return (d1,d2)




