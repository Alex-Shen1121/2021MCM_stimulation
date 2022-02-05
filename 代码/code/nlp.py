import spacy
import pandas as pd
import scattertext as st
from spacy.lang.en import English
twitter_df = pd.read_excel('../dataset/2021MCMProblemC_DataSet.xlsx',dtype='string')
twitter_df = twitter_df.loc[twitter_df['Lab Comments'] != ' ']['Lab Comments']
# nlp = spacy.load('en_core_web_sm')
# # nlp = English()
# doc = nlp(twitter_df[0])
# print(doc.text)
# for token in doc:
#     print(token.text, token.pos_, token.dep_)

from textblob import TextBlob
sum = 0
for text in twitter_df[:]:
    blob = TextBlob(text)
    print(text)
    print(blob.sentiment)
# text = ''
# blob = TextBlob(text)
# print(blob.sentiment)
    