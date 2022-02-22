import spacy
nlp = spacy.load('en_core_web_sm')

import string
punct = string.punctuation
# punct

from spacy.lang.en.stop_words import STOP_WORDS
stopwords = list(STOP_WORDS) # list of stopwords

class CustomTokenizer():
    def __init__(self):
        pass

    def text_data_cleaning(self,sentence):
        doc = nlp(sentence)                         # spaCy tokenize text & call doc components, in order

        tokens = [] # list of tokens
        for token in doc:
            if token.lemma_ != "-PRON-":
                temp = token.lemma_.lower().strip()
            else:
              temp = token.lower_
            tokens.append(temp)

        cleaned_tokens = []
        for token in tokens:
            if token not in stopwords and token not in punct:
                cleaned_tokens.append(token)
        return cleaned_tokens