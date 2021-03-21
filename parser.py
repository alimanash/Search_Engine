import csv
import nltk
import codecs


stream = codecs.open("output.txt", "w", "utf-8")


nltk.download('punkt')

from functools import cmp_to_key
from nltk.stem import PorterStemmer


class SearchEngine:
    def __init__(self):
        self.arcticles = []
        self.tags = {}
        self.parse_files()
        self.det_tags()

    def parse_files(self):
        csv.field_size_limit(100000000)
        for i in range(1, 4):
            with open('C:/Users/Narkhan/Desktop/Projects/HackNU/archive/articles' + str(i) + '.csv', mode='r', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)
                line_id = 0
                for line in csv_reader:
                    line_id += 1
                    if line_id == 1:
                        continue
                    self.arcticles.append({
                        'file_id': i,
                        'id': line[0],
                        'title': line[2],
                        'publication': line[3],
                        'author': line[4],
                        'content': line[9]})

    def det_tags(self):
        for arc in self.arcticles:
            arc_tags = {}
            stemmer = PorterStemmer()
            words = nltk.word_tokenize(arc['content'])
            for word in words:
                stream.write(stemmer.stem(word) + '~')
            stream.write('\n')
                   #print(arc['id'], key, arc_tags[key]



if __name__ == '__main__':
    searchEngine = SearchEngine()
