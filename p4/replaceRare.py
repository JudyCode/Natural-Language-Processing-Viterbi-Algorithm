'''
@author:Zixuan Lu
Uni: zl2348
date:Feb,12,2012
'''
#files open
fcount=open('ner.count')
ftrain=open('ner_train.dat')
fhand=open('ner_train_rare.dat','w')

DicOfWord={'_RARE_\n':0}


#preprocess:
for l in fcount:
    line=l.strip().split(' ')
    if line[1]!='WORDTAG':
        continue
    if int(line[0])<5:
        DicOfWord['_RARE_\n']=DicOfWord['_RARE_\n']+int(line[0])
        continue
    ## add word in dictionary
    if line[3] not in DicOfWord:
        DicOfWord[line[3]]=int(line[0])
    else:
        DicOfWord[line[3]]=DicOfWord[line[3]]+int(line[0])

#writing the replaced word into a new file
for l2 in ftrain:
    if l2=='\n':
        fhand.write('\n')
        continue
    line2=l2.split(' ')
    tmp=line2[0]
    if tmp not in DicOfWord:
        output='_RARE_'+' '+line2[1]
        fhand.write(output)
    else:
        fhand.write(l2)
        
    
print 'Succeed'

