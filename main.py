import csv
import nltk
import os
from functools import cmp_to_key
from nltk.stem import PorterStemmer


number_files = len(os.listdir('files'))


class SearchEngine:
    def __init__(self):
        self.arcticles = []
        self.tags = {}
        self.parse_files()
        self.det_tags()

    def parse_files(self):
        csv.field_size_limit(100000000)
        for i in range(1, 2):
            with open('C:/work/Search Engine/files/articles' + str(i) + '.csv', mode='r', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)
                line_id = 0
                for line in csv_reader:
                    if line_id == 100:
                        break
                    line_id += 1
                    if line_id == 1:
                        continue
                    self.arcticles.append({
                        'file_id': i,
                        'id': line[0],
                        'title': line[2],
                        'publication': line[3],
                        'author': line[4],
                        'content': line[2] + line[9]})

    def det_tags(self):
        for arc in self.arcticles:
            arc_tags = {}
            stemmer = PorterStemmer()
            words = nltk.word_tokenize(arc['content'])
            for word in words:
                if arc_tags.get(stemmer.stem(word)) is None:
                    arc_tags[stemmer.stem(word)] = 1
                else:
                    arc_tags[stemmer.stem(word)] += 1
            for key in arc_tags:
                if self.tags.get(key) is None:
                    self.tags[key] = [{'file_id': arc['file_id'], 'id': arc['id'], 'cnt': arc_tags[key]}]
                else:
                    self.tags[key].append({'file_id': arc['file_id'], 'id': arc['id'], 'cnt': arc_tags[key]})
        for tag in self.tags:
            for i in range(len(self.tags[tag])):
                for j in range(len(self.tags[tag])):
                    if i != j and self.tags[tag][i]['cnt'] <= self.tags[tag][j]['cnt']:
                        x = self.tags[tag][i]
                        self.tags[tag][i] = self.tags[tag][j]
                        self.tags[tag][j] = x

    def response(self, request):
        stemmer = PorterStemmer()
        sent = nltk.word_tokenize(request)
        words = [stemmer.stem(word) for word in sent]
        st = set()
        answer = []
        index = {}
        for word in words:
            if self.tags.get(word) is not None:
                added = 0
                for i in range(len(self.tags[word]) - 1, -1, -1):
                    if added == 5:
                        break
                    item = self.tags[word][i]
                    if str(item['file_id']) + '.' + str(item['id']) not in st:
                        st.add(str(item['file_id']) + '.' + str(item['id']))
                        added += 1
                        answer.append({'id': str(item['file_id']) + '.' + str(item['id']), 'num': 1})
                        index[str(item['file_id']) + '.' + str(item['id'])] = len(answer) - 1
                    else:
                        answer[index[str(item['file_id']) + '.' + str(item['id'])]]['num'] += 1
        for i in range(len(answer)):
            for j in range(len(answer)):
                if answer[i]['num'] >= answer[j]['num']:
                    x = answer[i]
                    answer[i] = answer[j]
                    answer[j] = x
        if len(answer) > 5:
            answer = answer[:5]
        print(answer)


if __name__ == '__main__':
    searchEngine = SearchEngine()
    request = input()
    searchEngine.response(request)