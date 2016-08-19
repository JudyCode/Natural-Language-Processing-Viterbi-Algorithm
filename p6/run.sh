echo 'This is Problem 6'

python count_freqs.py ner_train.dat > ner.counts
echo 'Now running problem6.py'

python problem6.py

python count_freqs.py ner_train1.dat > ner_more.counts

echo 'Now running Problem62.py!'
python Problem62.py

python eval_ne_tagger.py ner_dev.key prediction_filep6