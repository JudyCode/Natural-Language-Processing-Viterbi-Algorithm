

import string

f1=file('ner.counts')
f2=file('ner_train.dat')
fileHandle = open ( 'ner_train1.dat', 'w' )

result= f1.readlines()
l1 = result[0]
fields1 = l1.split(" ")
DicOfWord = {}

AllDig={}
Upper={}
Title={}
Rare={}
for l in result:
    #preprocess
    fields = l.strip().split(" ")

    if fields[1] != 'WORDTAG':
        continue
    if int(fields[0]) < 5:
        digits = fields[3].isdigit()
        upper = fields[3].isupper()
	title = fields[3][0].isupper()
        if digits:
            AllDig[fields[3]] = '_ALLDIG_'
        elif upper:
            Upper[fields[3]] = '_ALLCAP_'
	elif title:
	    Title[fields[3]] = '_FIRSTCAP_'
        else:
            Rare[fields[3]] = '_RARE_' 

#replacing the different tag into ner_train1.dat:
train=f2.readlines()
for l in train:
    if l == '\n':
        fileHandle.write('\n')
        continue
    fields = l.strip().split(' ')
    if fields[0] in AllDig:
        fileHandle.write('_ALLDIG_' + ' ' + fields[1] + '\n')
    elif fields[0] in Upper:
        fileHandle.write('_ALLCAP_' + ' ' + fields[1] + '\n')
    elif fields[0] in Title:
        fileHandle.write('_FIRSTCAP_' + ' ' + fields[1] + '\n')
    elif fields[0] in Rare:
        fileHandle.write('_RARE_' + ' ' + fields[1] + '\n')
    else:
        fileHandle.write(l)




       
        
        
    
        
