#!/usr/bin/python

import collections
import itertools
import nltk
from collections import defaultdict
from collections import Counter
from optparse import OptionParser
from nltk import trigrams

letters = ['a','b','c','d','e','f','g','h','i','j','k','l',
           'm','n','o','p','q','r','s','t','u','v','w','x',
           'y','z']

####
#### OPTIONS AND FLAGS
####

# -f : Specify file
# -e : Explicitly provide the letter substitution array
# -q : Frequency analysis
# -r : Rotation brute force

def main():
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename", default="caesar3.txt",
                      help="Choose input file", metavar="FILE")
    parser.add_option("-e","--explicit", dest="explicit", default=False,
                      help="Explicitly specify replacement array", metavar="ARRAY")
    parser.add_option("-q", "--freq", dest="freq", default=False,
                      action="store_true",help="Use frequency analysis")
    parser.add_option("-r", "--rot", dest="rot", default=False,
                      action="store_true",help="Use rotation brute force")
    parser.add_option("-v","--vigenere",dest="vigenere",default=False,
                      action="store_true",help="Use vigenere counter")

    (options, args) = parser.parse_args()

    f = open(options.filename,"r")
    text = f.read().replace("\n", "")
    print "This is the cipher read:\n"
    print text
    
    text = text.lower()
    
    int_text = convert_to_int(text)
    basearray = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,
                 14,15,16,17,18,19,20,21,22,23,
                 24,25]
    if (options.explicit):
        do_explicit(int_text,options.explicit)
        return
    if (options.rot):
        try_rotations(int_text,basearray)
    if (options.freq):
        frequency_analysis(text,int_text)
    if (options.vigenere):
        vigenere_analysis(text)
        
def do_explicit(int_text,explicit):
    print explicit
    gen_list = explicit.split(',')
    print gen_list

    basearray = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,
                 14,15,16,17,18,19,20,21,22,23,
                 24,25]
    d = defaultdict(int)
    for word in int_text:
        d[word] += 1
    commons = Counter(d).most_common(26)
    count = 0
    
    for k,v in commons:
        if (k>=0 and k < 26):
            basearray[k] = ord(gen_list[count])-97
            count+=1

    print ''.join(convert_to_text(replace_2(int_text,basearray)))

def frequency_analysis(text,int_text):
    #list of letters in order of frequency
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
    
    for k,v in commons:
        if (k>=0 and k < 26):
            basearray[k] = ord(freq_list[count])-97
            count+=1
    
    print "\nFrequency analysis decrypt\n"
    print ''.join(convert_to_text(replace_2(int_text,basearray)))
    print "\n\nThe replacements were as follows : \n"
    print ",".join(letters)
    print ",".join(freq_list)
    print "\nReplace the letters that you want and relaunch with -e"
    
def try_rotations(int_text,basearray):
    for i in range(26):
        rotated = replace(int_text,i)
        text_text = convert_to_text(rotated)
        decrypt_string= ''.join(text_text)
        #not exactly a perfect check...
        if ("the" in decrypt_string):
            print "Rotation decrypt\n"
            print decrypt_string

def vigenere_analysis(text):
    print "Vigenere analysis\n"
    tri_tokens = trigrams(text)
    trigrams_counted = sorted(set(tri_tokens))
    max_seen = 0
    max_trigram = ('a','b','c')
    for item in trigrams_counted:
        if (tri_tokens.count(item) > max_seen):
            max_trigram = item;
            max_seen = tri_tokens.count(item)
            print "new is " + str(max_trigram) + "with a count of "+str(max_seen)
    for i in range(3,11):
        print "we are trying a keylength of "+str(i)
        minitexts = list()
        for j in range(0,i):
            minitexts.append("")
        counter=0
        for j in text:
            minitexts[counter]+=j
            if (counter==(i-1)):
                counter=0
            else:
                counter+=1

        print minitexts
            
        
     
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
