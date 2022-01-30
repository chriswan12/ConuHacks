from heapq import nlargest
from string import punctuation
from spacy.lang.en.stop_words import STOP_WORDS
import spacy


class SpaCySummarizer:
    def __init__(self, text):
        self.text = text
        self.punctuation = punctuation + '\n'

    def summarize(self):
        stopwords = list(STOP_WORDS) + ['um']
        nlp = spacy.load('en_core_web_sm')

        doc = nlp(self.text)
        tokens = [token.text for token in doc]
        self.punctuation += '\n'

        # How many times has a word occured in the text -> then determine the most important sentence

        word_frequencies = {}
        for word in doc:
            if word.text.lower() not in stopwords:
                if word.text.lower() not in self.punctuation:
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
        # print(sentence_tokens)
        sentence_scores = {}
        for sent in sentence_tokens:
            for word in sent:
                if word.text.lower() in word_frequencies.keys():
                    if len(sent.text.split(' ')) < 50:
                        if sent not in sentence_scores.keys():
                            sentence_scores[sent] = word_frequencies[
                                word.text.lower()]
                        else:
                            sentence_scores[sent] += word_frequencies[
                                word.text.lower()]
        # print(sentence_scores)
        # print(sentence_tokens)
        # only select 30% of the sentences
        # select_length = int(len(sentence_tokens) * 0.3)
        #
        # summary = nlargest(select_length, sentence_scores,
        #                    key=sentence_scores.get)
        threshold = 2
        summary = ''
        total = 0
        for i in sentence_scores.keys():
            total += sentence_scores[i]
            if sentence_scores[i] > threshold:
                summary += str(i) + '\n'

        print(total / len(sentence_scores))

        # final_summary = [word.text for word in summary]
        # summary = ' '.join(final_summary)
        self.export(summary, 'summary.txt')
        return summary

    @staticmethod
    def export(summary, filename):
        with open(filename, 'w') as f:
            f.write(summary)


if __name__ == '__main__':
    result = None
    with open('formatted.txt', 'r') as f:
        text = f.readline()

        s = SpaCySummarizer(text)
        s.summarize()


