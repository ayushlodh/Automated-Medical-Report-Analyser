import nltk
from nltk.corpus import stopwords
import spacy
import random
import time
import numpy as np
import sys
from spacy import displacy
from itertools import chain
import matplotlib.pyplot as plt 
from matplotlib.ticker import MaxNLocator
nltk.download('punkt')
nltk.download('stopwords')
sent=input("Enter the sentence")
tok_sent=nltk.word_tokenize(sent)
print(tok_sent)
sent2=[]
act_sent=[]
stop_words=stopwords.words('english')
for word in tok_sent:
    sent2.append(word.lower())
print(sent2)
for i in sent2:
    if (i not in stop_words):
        act_sent.append(i)
print(act_sent)
fin_sent=""
for i in act_sent:
    fin_sent=fin_sent+" "+i
print(fin_sent)
import spacy
#fin_sent = "ayush suffering cold fever"
ner = spacy.load(R"ner_demo/training/model-best") #load the best model
doc = ner(fin_sent)
result = ""
for ent in doc.ents:
    texts = ent.text
    label = ent.label_
    result = result + texts + " : " + label + "\n"
print(result)
displacy.render(doc,jupyter=True, style = "ent")
