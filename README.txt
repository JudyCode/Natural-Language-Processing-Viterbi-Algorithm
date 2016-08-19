README
==================
Author : Lu Zixuan
Uni : zl2348
Date: Feb 18, 2015
==================

*** HOW TO RUN ***

Homework 1 contains three forders , they are p4, p5 and p6 perspectively. Each foulder contains all the files that are needed, including:

 * main function .py files 
 * the original data files(ner_train.dat etc.)
 * a shell sciprt (run.sh) which is used for running the whole problem.

==================
PROBLEM 4:

*** FILE ***

replaceRare.py : used to replace the word whose counts are less than 5 to be '_RARE_' and write the new version training data into a new data file called 'ner_train_rare.dat'.
the new counts generrated by this new training file will be stored in a new file called "ner_rare.counts" 

Problem4.py : used to compute the emission parameters and generated the logprobability for each prediction. the prediction result will be recorded into "prediction_file". 

 * estimation of running time : 1s

*** RESULTS ***

Found 14066 NEs. Expected 5931 NEs; Correct: 3097.

	 precision 	recall 		F1-Score
Total:	 0.220176	0.522172	0.309746
PER:	 0.429461	0.225245	0.295503
ORG:	 0.476755	0.390882	0.429569
LOC:	 0.147110	0.872955	0.251789
MISC:	 0.498217	0.606949	0.547234
zl2348@pretoria:~/Downloads/h1/p4$ ^C

***SUMMARY & MY OBSERVATION:***

From the result, we can see that total F1-Score is 0.3, which is not that high.The score for recall is higher than the that of precision. For different tags, their performance and impact is also differernt, for MISC, it's F1-Score is pretty high conpared to other tags. for LOC, although it's precision is pretty low, nearly the lowest among the other tag, it's recall is pretty high which reaches to 0.87. 

================
PROBLEM 5:

*** FILE ***

Problem5.py: 
the first part of the file implements the computation of transmision part (q), for each trigram yi-2,yi-1,yi, it computes it's log probability and print them into a new file called 'trigram_prob'.

the second part implements the Viterbi algorithm and also implements the functions of the baseline tagger does and compute the log-probability of the tagged sequence up to each word.

 * estimation running time: 1 min

*** RESULTS ***

zl2348@vt:~/Downloads/h1$ python eval_ne_tagger.py ner_dev.key prediction_filep5
Found 4663 NEs. Expected 5931 NEs; Correct: 3614.

	 precision 	recall 		F1-Score
Total:	 0.775038	0.609341	0.682273
PER:	 0.776278	0.594668	0.673444
ORG:	 0.598485	0.472347	0.527987
LOC:	 0.876045	0.685932	0.769419
MISC:	 0.826999	0.685125	0.749406

***SUMMARY & MY OBSERVATION:***

From the result, we can see that the performance of HMM tagger is highly improved than the baesline tagger, which merely based on the emission rate.  

ALthough we are given the psudo code for Viterbi algorithm, there are many details and sensitive cases need to be considered. Such as the start state and STOP case, I handled them specially and seperately. When computing the log probabilty we also need to handle the case like that some trigram may not be seen in the dictionories. I initlaized a default tag 'O' and value '-100000' for each tag, before computing the log Pi(K), I deleted the items that are not stored in the dictionary. Before handling each sentence, I replaced the word that is not been seen in the train corpus into '_RARE_' which also avoid the potential fault.


==================
Problem 6:

For problem6, I add three more tag classes, they are '_ALLDIG_','_ALLCAP_' and '_FIRSTCAP_'. 

*** FILE ***

problem6.py : this file implements that replace the rare words into different class.

problem62.py : is a little modification of Problem5.py, add codes to deal with several rare tag.

 * estimaiton running time: <1 min


*** RESULTS ***

zl2348@bern:~/Downloads/h1/p6$ sh run.sh
This is Problem 6
Now running problem6.py
Now running Problem62.py!
Found 5679 NEs. Expected 5931 NEs; Correct: 3515.

	 precision 	recall 		F1-Score
Total:	 0.618947	0.592649	0.605512
PER:	 0.707668	0.723069	0.715285
ORG:	 0.397067	0.566517	0.466893
LOC:	 0.750849	0.603053	0.668884
MISC:	 0.768496	0.349620	0.480597

***SUMMARY & MY OBSERVATION:***

From the result, we can see that although the performance of this did have a higher score than baseline tagger, it didn't arrive or even  exceed the result for the problem5(only rare class) which was out of my expection. I thought the score for the modified rare data should be higher because we group rare words into more specific classes,and given more informations on word's attributes. For example, I observed that the words with first letter capitalized are more likely to be tagged as I-PER or I_LOC, and words which are all written in capitalized are more likely to be I-ORG. However, my experiment's score doesn't show this very well. At the beginning, I only used two more classes which are ' _ALLDIGIT_' (all digits )and '_ALLCAP_'(all capitalize), however the result was not good, so I add one more class '_FISRTCAP_'(First letter is capitalized), it improved a little bit as shown in the result, but still worse than that of problem 5. I tried many times, but haven't figured out the reasons, I list the count of different classes with tags after the replacement in the following, I will really appreciate if you can give any suggestions to me, thank you~

class  tag    count
_RARE_ I-ORG : 329
_RARE_ O : 58509
_RARE_ I-LOC : 46
_RARE_ I-PER : 68
_RARE_ I-MISC : 125
_RARE_ B-MISC: 1

_FIRSTCAP_ O : 3699
_FIRSTCAP_ B-ORG : 6
_FIRSTCAP_ I_MISC : 2216
_FISRTCAP_ B_LOC : 2
_FISRTCAP_ I_LOC : 3804
_FIRSTCAP_ B-MISC : 28
_FIRSTCAP_ I-ORG : 4557
_FIRSTCAP_ I-PER : 5979

_ALLCAP_ I_MISC : 279
_ALLCAP_ I-ORG : 961
_ALLCAP_ I_PER : 170
_ALLCAP_ O : 1267
_ALLCAP_ I_LOC : 698
_ALLCAP_ B_LOC : 9
_ALLCAP_ B_MISC : 8

_ALLDIG_ O : 4731
_ALLDIG_ I_ORG : 7
_ALLDIG_ I_LOC : 1
_ALLDIG_ I_MISC : 23




