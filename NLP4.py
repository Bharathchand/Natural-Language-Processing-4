import nltk
from nltk import FreqDist
    
f=open('constitution.txt','rU')

raw = f.read()
raw = raw.upper()
raw = raw.decode('utf-8')
tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)

fdist1 = FreqDist(text)
vocabulary1 = fdist1.keys()
fdist1.plot(50,cumulative=True)
