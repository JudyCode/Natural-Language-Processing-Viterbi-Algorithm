# coding: utf-8
'''
Author : Lu zixuan
UNI: zl2348
'''

import math 
f = file("ner_rare.counts")
result = f.readlines()

#initialize the dictionary
DicOfTag={}
DicOfEmi = {}

#build Dic
for l in result:
    #preprocess
    fields = l.split(" ")
    if fields[1] != 'WORDTAG':
        continue
    #add in Dic tag
    if fields[2] not in DicOfTag:
        DicOfTag[fields[2]] = int(fields[0])
    else:
        DicOfTag[fields[2]] = DicOfTag[fields[2]]+int(fields[0])
        
for l in result:
    #preprocess
    fields = l.split(" ")
    if fields[1] != 'WORDTAG':
        continue
    #build emission string
    tmp = fields[2]+' '+fields[3]
    #add in Dic Emission
    DicOfEmi[tmp] = math.log(float(int(fields[0])/float(DicOfTag[fields[2]])))

#tag each word according to the emi values
f2=file('ner_dev.dat')
fileHandle = open ( 'prediction_file', 'w' )
result2 = f2.readlines()

for l in result2:
    if l=='\n':
        fileHandle.write ('\n')
        continue
    fields = l.split('\n')
    bestword = 'O'
    bestvalue = -10000
    for word in DicOfTag:
        newword = word +' ' + fields[0] + '\n'
        if newword in DicOfEmi:
            if DicOfEmi[newword] >= float(bestvalue):
                bestword = word
                bestvalue = DicOfEmi[newword]
    if bestvalue == -10000:
        for word in DicOfTag:
            newword = word +' ' + '_RARE_' + '\n'
            if newword in DicOfEmi:
                if DicOfEmi[newword] >= float(bestvalue):
                    bestword = word
                    bestvalue = DicOfEmi[newword]        
    output = fields[0] + ' ' + bestword + ' ' + str(bestvalue) + '\n' 
    fileHandle.write (output)
        


    
    
    
    
