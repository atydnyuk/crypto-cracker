import nltk
from nltk import trigrams
from collections import defaultdict
from collections import Counter

class Vigenere:
    def separate_into_caesar_list(self,text,i):
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
        return minitexts


    def vigenere_analysis(self,text):
        print "Vigenere analysis\n"
        
        #for now we will skip the part where we find the keylength
        for i in range(3,21):
            minitexts = self.separate_into_caesar_list(text,i)
            code = self.find_code_from_caesar_list(minitexts)
            self.decipher_with_code(text,code)

    def vigenere_given_length(self,length,text):
        minitexts = self.separate_into_caesar_list(text,length)
        code = self.find_code_from_caesar_list(minitexts)
        self.decipher_with_code(text,code)


    def find_code_from_caesar_list(self,textlist):
        code = ""
        for item in textlist:
            common = self.most_common_letter(item)
            code_letter = self.subtract_letters(common,'e')
            code += code_letter
        print code
        return code

    def most_common_letter(self,text):
        d = defaultdict(int)
        for letter in text:
            d[letter] += 1
            commons = Counter(d).most_common(26)
        return commons[0][0]
        
    def subtract_letters(self,a,b):
        difference = ord(a) - ord(b)
        if (difference < 0):
            difference = 26+difference
        return str(unichr(difference+97))

    def decipher_with_code(self,text,code):
        result = ""
        keylength = len(code)
        index = 0
        for letter in text:
            diff = ord(letter)-ord(code[index%keylength])
            if (diff < 0):
                diff+=26
            decoded=unichr(diff+ord('a'))
            result+=decoded
            index+=1
        print result
        return result
    
