import os
from NLPSummaryGenerator import SummaryGenerator
import requests
import json
from ms_word_converter import GenerateMSWord


def main():
    cwd = os.getcwd()
    if len(os.listdir(cwd + '/NoteIt/media')) != 0:
        try:
            response = requests.get('http://127.0.0.1:8000/api/get')
            file_name = response.json()[-1]['file_upload'].split('/')[-1]
            email = response.json()[-1]['useremail']
            print(email)
            s = SummaryGenerator(file_name)
            n = s.generate_nltk_results()
            GenerateMSWord(
                n, "Test Summary of Part of the Lecture").generate_docx(email)

        except:
            print("An error has occured")


if __name__ == "__main__":
    main()
