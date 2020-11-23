from collections import Counter
import math
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from re import findall
from re import IGNORECASE
'''firt usage'''
#nltk.download('punkt')
#nltk.download('stopwords')

'''
TODO:
    1. Выполнить поиск и выделение лексем/токенов в тексте - V
    2. Удалить стоп-слова - V
    3. Выполнить стемминг токенов - V
    4. Реализовать одну из моделей поиска по материалам лекций.
'''



class Searcher:

    def __init__(self):
        self.stemmer = nltk.stem.SnowballStemmer('english')
        self.stopwords = set(stopwords.words('english'))

    def tokenize(self, data):
        return word_tokenize(data)

    def get_filtered_words(self, data):
        filtered_words = []
        for w in self.tokenize(data):
            filtered_words.append(self.stemmer.stem(w))
        return filtered_words

class TF_IDF:

    def __init__(self, corpus):
        self.corpus = corpus

    def compute_tf(self, document):
        tf_text = Counter(document)
        for i in tf_text:
            tf_text[i] = tf_text[i] / float(len(document))
        return tf_text

    def compute_idf(self, word):
        return math.log(len(self.corpus) /
                        sum([1.0 for doc in self.corpus if word in doc]))

    def compute_tf_idf(self):
        documents = []
        for doc in self.corpus:
            tf_idf_dict = {}
            computed_tf = self.compute_tf(doc)
            for w in computed_tf:
                tf_idf_dict[w] = computed_tf[w] * self.compute_idf(w)

            documents.append(tf_idf_dict)

        return documents


if __name__ == '__main__':
    print('Wait for indexing all words...')
    corpus = []
    files = ['corpus\\1.txt',
             'corpus\\2.txt',
             'corpus\\3.txt',
             'corpus\\5.txt',
             'corpus\\7.txt',
             'corpus\\8.txt',
             'corpus\\9.txt',
             'corpus\\10.txt',
             'corpus\\11.txt',
             'corpus\\12.txt',]
    for f in files:
        with open(f, encoding="utf-8") as file:

            text = file.read().lower()
            list_d = findall('[a-z0-9]+', text, flags=IGNORECASE)
        corpus.append(list_d)

    tf_idf = TF_IDF(corpus)
    computed_tf_idf = tf_idf.compute_tf_idf()

    print('Done...')
    data = input('>>>')
    searcher = Searcher()
    f_words = searcher.get_filtered_words(data)

    sums = []
    for c_doc in computed_tf_idf:
        sum = 0
        for w in f_words:
            for term in c_doc.keys():
                if w in term:
                    sum += c_doc[term]
        sums.append(sum)

    res_dict = {}
    for i in range(len(sums)):
        res_dict.update({'{}'.format(i): sums[i]})

    items = list(res_dict.items())
    items.sort(key=lambda j: j[1], reverse=True)

    for item in items:
        if item[1] != 0:
            print(item, sep='\n')
