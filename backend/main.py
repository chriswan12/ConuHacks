import os
from NLPSummaryGenerator import SummaryGenerator
import requests
import json


def main():
    cwd = os.getcwd()
    print(cwd + '/NoteIt/media')
    if len(os.listdir(cwd + '/NoteIt/media')) != 0:
        response = requests.get('http://127.0.0.1:8000/api/get')
        file_name = response.json()[-1]['file_upload'].split('/')[-1]
        s = SummaryGenerator(file_name)
        r = s.generate_spacy_results()
        n = s.generate_nltk_results()
        print(r)
        print(n)
        s.export_text(r, 'spacy_sum.txt')
        s.export_text(n, 'nltk_sum.txt')


if __name__ == "__main__":
    main()
