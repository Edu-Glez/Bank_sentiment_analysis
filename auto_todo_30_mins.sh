#!/bin/bash
# -*- ENCODING: UTF-8 -*-



source /home/graduate/Bank_sentiment_analysis/env/bin/activate
tom_man=`expr $(date +%d) + 1`

python /home/graduate/Bank_sentiment_analysis/test_embed_today.py bancomer $(date +%Y-%m-%d) $(date +%Y-%m-$tom_man)
python /home/graduate/Bank_sentiment_analysis/test_embed_today.py banorte $(date +%Y-%m-%d) $(date +%Y-%m-$tom_man) 
python /home/graduate/Bank_sentiment_analysis/test_embed_today.py banamex $(date +%Y-%m-%d) $(date +%Y-%m-$tom_man) 
python /home/graduate/Bank_sentiment_analysis/test_embed_today.py scotiabank $(date +%Y-%m-%d) $(date +%Y-%m-$tom_man) 
python /home/graduate/Bank_sentiment_analysis/test_embed_today.py HSBC $(date +%Y-%m-%d) $(date +%Y-%m-$tom_man)
python /home/graduate/Bank_sentiment_analysis/test_embed_today.py santander $(date +%Y-%m-%d) $(date +%Y-%m-$tom_man)
#python charls.py bancomer 2017-03-16 2017-03-17

