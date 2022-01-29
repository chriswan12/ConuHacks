from heapq import nlargest
from string import punctuation
from spacy.lang.en.stop_words import STOP_WORDS
import spacy
text = """
Summarization is the task of condensing a piece of text to a shorter version, reducing the size of the initial text while at the same time preserving key informational elements and the meaning of content. Since manual text summarization is a time expensive and generally laborious task, the automatization of the task is gaining increasing popularity and therefore constitutes a strong motivation for academic research.
There are important applications for text summarization in various NLP related tasks such as text classification, question answering, legal texts summarization, news summarization, and headline generation. Moreover, the generation of summaries can be integrated into these systems as an intermediate stage which helps to reduce the length of the document.
In the big data era, there has been an explosion in the amount of text data from a variety of sources. This volume of text is an inestimable source of information and knowledge which needs to be effectively summarized to be useful. This increasing availability of documents has demanded exhaustive research in the NLP area for automatic text summarization. Automatic text summarization is the task of producing a concise and fluent summary without any human help while preserving the meaning of the original text document.
It is very challenging, because when we as humans summarize a piece of text, we usually read it entirely to develop our understanding, and then write a summary highlighting its main points. Since computers lack human knowledge and language capability, it makes automatic text summarization a very difficult and non-trivial task.
"""

stopwords = list(STOP_WORDS)

nlp = spacy.load('en_core_web_sm')

doc = nlp(text)
tokens = [token.text for token in doc]

punctuation = punctuation + '\n'

# How many times has a word occured in the text -> then determine the most important sentence

word_frequencies = {}
for word in doc:
    if word.text.lower() not in stopwords:
        if word.text.lower() not in punctuation:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1

max_frequency = max(word_frequencies.values())

# normalized frequency
for word in word_frequencies.keys():
    word_frequencies[word] = word_frequencies[word] / max_frequency

# tokenilzation -> get the sentences

sentence_tokens = [sent for sent in doc.sents]


sentence_scores = {}
for sent in sentence_tokens:
    for word in sent:
        if word.text.lower() in word_frequencies.keys():
            if sent not in sentence_scores.keys():
                sentence_scores[sent] = word_frequencies[word.text.lower()]
            else:
                sentence_scores[sent] += word_frequencies[word.text.lower()]

# only select 30% of the sentences
select_length = int(len(sentence_tokens) * 0.3)

summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)

final_summary = [word.text for word in summary]
summary = ' '.join(final_summary)

print(summary)
