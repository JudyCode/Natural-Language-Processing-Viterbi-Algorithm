'''
Author: Lu Zixuan 
Uni : zl2348

'''
import math 
#########################################
#Part 1  
#initialize

f=file('ner_more.counts')
result= f.readlines()

f2 = file('ner_dev.dat')
fileHandle = open ( 'prediction_filep6', 'w' )
result2 = f2.readlines()

#initialization of dictionary

#dictionary of Tag, key: tag name value: appear count
DicOfTag = {}
#dictionary of Emission : key: tag->word ; value: log Prob
DicOfEmi = {}
#record the words that appear in the training sentences
trainWord={}

#build Dic
#result = ner.counts
for l in result:
    #preprocess
    fields = l.strip().split(" ")
    if fields[1] != 'WORDTAG':
        continue
    #add in Dic tag
    if fields[2] not in DicOfTag:
        DicOfTag[fields[2]] = int(fields[0])
    else:
        DicOfTag[fields[2]] = DicOfTag[fields[2]]+int(fields[0])
        
for l in result:
    #preprocess
    fields = l.strip().split(" ")
    if fields[1] != 'WORDTAG':
        continue
    #build emission string
    tmp = fields[2]+' '+fields[3]
    trainWord[fields[3]] = fields[0]
    #add in Dic Emission
    DicOfEmi[tmp] = math.log(float(int(fields[0])/float(DicOfTag[fields[2]])))



#Build dict n-gram
DictGram1 = {}
DictGram2 = {}
DictGram3 = {}
for l in result: 
    fields = l.strip().split(" ")
    if fields[1] == '1-GRAM' : DictGram1[fields[2]] = int(fields[0])
    elif fields[1] == '2-GRAM' :
        tmp = fields[2] + ' ' + fields[3]
        DictGram2[tmp]=int(fields[0])
    elif fields[1] == '3-GRAM':
        tmp1 = fields[2]  + ' ' +  fields[3]  + ' ' + fields[4]
        tmp2 = fields[2] + ' ' + fields[3]
        DictGram3[tmp1] = math.log(float(fields[0]) / float(DictGram2[tmp2])) 

###########################################################
#Part 2    viterbi algorithm
# sentenceO is used for record the original sentence from reading file
# sentenceR is the modified sentence where words that unseen in the trainning set been replaced by '_RARE_'

sentenceO = [];
sentenceR = [];

#result2=ner_dev'
for l in result2:
    if l != '\n':
        ll = l.strip()
        if ll not in trainWord:
            digits = ll.isdigit()
            upper = ll.isupper()
	    title = ll[0].isupper()
            if digits:
                sentenceR.append(['_ALLDIG_'])
            elif upper:
                sentenceR.append(['_ALLCAP_'])
	    elif title:
                sentenceR.append(['_FIRSTCAP_'])
            else:
                sentenceR.append(['_RARE_'])
        else:
            sentenceR.append(l.split())
        sentenceO.append(l.split())
        continue
    else:
        #print sentenceR
        #initialization
        backpoint = []
        tmp = str(0) +' '+ '*' + ' ' + '*'
        PI = {tmp:0.0}
        ArgMaxTag = {}
        for k in range(1,len(sentenceR)+1):
            for u in DicOfTag.keys():
                if k == 1:
                    u = '*'
                for v in DicOfTag.keys():
                    maxtag = 'O'
                    maxval = -100000
                    for w in DicOfTag.keys():
                        if k == 1 or k == 2:
                            w = '*'
                        pik = str(k-1) +' ' + w + ' ' + u
                        q3 = w +' ' + u + ' ' + v
                        emi = v + ' ' + str(sentenceR[k-1][0])

			#clear those unseen combianation before computation
                        if pik not in PI:
                            continue
                        if q3 not in DictGram3:
                            continue
                        if emi not in DicOfEmi:
                            continue                    
                        curVal = PI[pik] + DictGram3[q3] + DicOfEmi[emi]
                        if curVal > maxval:
                            maxval = curVal
                            maxtag = w
                    temp = str(k) +' ' + u + ' ' +v
                    PI[temp] = maxval
                    #print maxval
                    ArgMaxTag[temp] = maxtag

        #deal with the stop case
        maxu = 'O'
        maxv = 'O'
        maxfinal = -10000
        for u in DicOfTag.keys():
            for v in DicOfTag.keys():
                tmp2 = str(len(sentenceR)) +' ' + u + ' ' + v
                tmp3 = u +' ' + v + ' ' +'STOP'
                if tmp2 not in PI:
                    continue
                if tmp3 not in DictGram3:
                    continue
                curVal = PI[tmp2] + DictGram3[tmp3]
                if curVal > maxfinal:
                    maxfinal = curVal
                    maxu = u
                    maxv = v

        backpoint = [maxu, maxv] 
        #retreval the sentence tag y1y2-yn
        for i in range(len(sentenceR)-3, -1, -1):
            backpoint = [ArgMaxTag[str(i+3) + ' ' + backpoint[0] + ' ' + backpoint[1]]] + backpoint
       
#written them into prediction_file
        if (str(1) + ' '+ '*' + ' '+ str(backpoint[0])) in PI:
            fileHandle.write(str(sentenceO[0][0]) + ' ' +str( backpoint[0]) + ' ' + str( PI[str(1) + ' ' + '*' + ' '+ str(backpoint[0])]) + '\n')
        else: 
            fileHandle.write(sentenceO[0][0] + ' ' + 'O'+' '+'-100000'+'\n')

        for i in range(1,len(sentenceR)):
            fileHandle.write(sentenceO[i][0] + ' ' + str(backpoint[i]) + ' ' + str( PI[str(i + 1) + ' ' + backpoint[i - 1] + ' ' + backpoint[i] ] )+ '\n')
        
        sentenceO = []
        sentenceR = []
    
    fileHandle.write('\n')

##########################################################

