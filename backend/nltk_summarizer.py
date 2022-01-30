from string import punctuation
from spacy.lang.en.stop_words import STOP_WORDS
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk


class NLTKSummarizer:
    def __init__(self, text):
        self.text = text
        self.punctuation = punctuation + '\n'

    def summarize(self):

        nltk.download('stopwords')
        nltk.download('punkt')
        with open('formatted.txt', 'r') as f:
            text = f.readline()

            stopWords = set(stopwords.words("english"))
            stopWords.add('um')
            words = word_tokenize(text)
            # print(words)

            freqTable = dict()
            for word in words:
                word = word.lower()
                if word in stopWords:
                    continue
                if word in freqTable:
                    freqTable[word] += 1
                else:
                    freqTable[word] = 1

            sentences = sent_tokenize(text)
            sentenceValue = dict()

            for sentence in sentences:
                for word, freq in freqTable.items():
                    if word in sentence.lower():
                        if sentence in sentenceValue:
                            sentenceValue[sentence] += freq
                        else:
                            sentenceValue[sentence] = freq

            sumValues = 0
            for sentence in sentenceValue:
                sumValues += sentenceValue[sentence]

            average = int(sumValues / len(sentenceValue))

            summary = ''
            for sentence in sentences:
                if (sentence in sentenceValue) and (
                        sentenceValue[sentence] > (1.3 * average)):
                    summary += ' ' + sentence
            summary = summary[1:]
            print(summary)
            print(len(summary), len(text))
            return summary


if __name__ == '__main__':
    pass


