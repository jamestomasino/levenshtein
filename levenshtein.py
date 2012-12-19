#!/usr/local/bin/python
import sys
from fuzzywuzzy import process

dict_file = 'eng.txt' #'/usr/share/dict/words'
match_word = "".join(sys.argv[1:]).lower()

if match_word:
    with open(dict_file, 'rU') as f:
        eng_dict = set(line.strip() for line in f)
    if match_word in eng_dict:
        print match_word
    else:
        print process.extractOne(match_word, eng_dict)[0]
else:
    print ''
