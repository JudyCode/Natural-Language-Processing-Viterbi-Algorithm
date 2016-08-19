clear
echo “Problem 4”
 
python replaceRare.py

echo "Now the words has been replaced by ‘_RARE_’ "
echo " Now recounting the new ner_train.dat " 

python count_freqs.py ner_train_rare.dat > ner_rare.counts

echo "Now doing the prediction of the test data and gather the evaluation "

python Problem4.py
echo “ Now doing the evaluation “
python eval_ne_tagger.py ner_dev.key prediction_file