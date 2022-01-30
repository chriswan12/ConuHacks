from text_parser import Parser
from summarizer import SpaCySummarizer
from nltk_summarizer import NLTKSummarizer


class SummaryGenerator:

    def __init__(self, file, speaker=None):
        self.file = file
        self.speaker = speaker

    def _text_processing(self):
        text = Parser(self.file, self.speaker).parse()
        return text

    def generate_spacy_results(self):
        text = self._text_processing()
        return SpaCySummarizer(text).summarize()

    def generate_nltk_results(self):
        text = self._text_processing()
        return NLTKSummarizer(text).summarize()

    @staticmethod
    def export_text(text, output_file):
        SpaCySummarizer.export(text, output_file)


if __name__ == "__main__":
    s = SummaryGenerator('test.txt', 'Sanja Fidler')
    r = s.generate_spacy_results()
    n = s.generate_nltk_results()
    print(r)
    print(n)
    s.export_text(r, 'spacy_sum.txt')
    s.export_text(n, 'nltk_sum.txt')
