clear 
echo " This is Problem 5 ! "
echo " Runing Problem5.py..."

echo "For the first part, it will output a trigram_prob"
echo "For thr second part, it will output a prediction_filep5"

python Problem5.py
echo "Finished, and now evaluating..."

python eval_ne_tagger.py ner_dev.key prediction_filep5

echo "Everything is finished !"
