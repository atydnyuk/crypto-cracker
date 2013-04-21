#!/usr/bin/python

import collections
import itertools
from collections import defaultdict
from collections import Counter

letters = ['a','b','c','d','e','f','g','h','i','j','k','l',
           'm','n','o','p','q','r','s','t','u','v','w','x',
           'y','z']

def main():
    f = open("caesar3.txt","r")
    text = f.read()
    print "This is the cipher read:\n"
    print text;
    text = text.lower()
    int_text = convert_to_int(text)
    basearray = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,
                 14,15,16,17,18,19,20,21,22,23,
                 24,25]
    try_rotations(int_text,basearray)
    frequency_analysis(text,int_text)

def frequency_analysis(text,int_text):
    freq_list = ['e','t','a','o','i','n','s','h','r','d','l','c','u',
                 'm','w','f','g','y','p','b','v','k','j','x','q','z']
    basearray = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,
                 14,15,16,17,18,19,20,21,22,23,
                 24,25]
    d = defaultdict(int)
    for word in int_text:
        d[word] += 1
    commons = Counter(d).most_common(26)
    count = 0
    print "COMMONS: \n"
    print commons
    for k,v in commons:
        if (k>=0 and k < 26):
            print k
            basearray[k] = ord(freq_list[count])-97
            count+=1
    print basearray
    print "Possible solution\n"
    print ''.join(convert_to_text(replace_2(int_text,basearray)))
        
    
def try_rotations(int_text,basearray):
    for i in range(26):
        rotated = replace(int_text,i)
        text_text = convert_to_text(rotated)
        decrypt_string= ''.join(text_text)
        #not exactly a perfect check...
        if ("the" in decrypt_string):
            print "Possible decrypt\n"
            print decrypt_string

def convert_to_int(text):
    array = []
    for c in text:
        if (c in letters): 
            array.append(ord(c)-97) 
        else:
            array.append(ord(c))
    return array

def convert_to_text(ints_array):
    array = []
    for c in ints_array:
        if (c >=0 and c < 26): 
            array.append(str(unichr(c+97))) 
        else:
            array.append(str(unichr(c)))
    return array

def replace(text,rot):
    basearray = collections.deque([0,1,2,3,4,5,6,7,8,9,10,11,12,13,
                                   14,15,16,17,18,19,20,21,22,23,
                                   24,25])
    basearray.rotate(rot)
    newrot = []
    for c in text:
        if c>=0 and c<26:
            newrot.append(list(basearray)[c])
        else:
            newrot.append(c)
    return newrot

def replace_2(text,array):
    newrot = []
    for c in text:
        if c>0 and c<26:
            newrot.append(array[c])
        else:
            newrot.append(c)
    return newrot

if __name__ == "__main__":
    main()
