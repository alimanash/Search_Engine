import sys 
import nltk
import codecs

from functools import cmp_to_key
from nltk.stem import PorterStemmer

stream = codecs.open("getTag.txt", "w", "utf-8")

with open('KeyWords.in', mode='r', encoding='utf-8') as f:
    data = f.read()
    arc_tags = {}
    stemmer = PorterStemmer()
    words = nltk.word_tokenize(data)
    for word in words:
        arc_tags[stemmer.stem(word)] = 1
    for key in arc_tags:
        stream.write(key + ' ')
