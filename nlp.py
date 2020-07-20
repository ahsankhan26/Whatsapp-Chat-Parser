from __future__ import print_function
import nltk
import time
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

fin = open('test.txt', 'r', encoding="utf8")
fout = open('tokens.txt', 'w', encoding="utf8")

for line in fin:
    tokens = word_tokenize(line)
    print('\n'.join(tokens), end='\n', file=fout)

fin.close()
fout.close()

fin = open('tokens.txt', 'r', encoding="utf8")
fout = open('token1.txt', 'w', encoding="utf8")

stoplist = stopwords.words('english')
additional_stopwords = """< Media omitted >"""
stoplist += additional_stopwords.split()

print(stoplist)
# # print(word)

for word in fin.read().split('\n'):
    if word not in stoplist:
        fout.write(word+'\n')
