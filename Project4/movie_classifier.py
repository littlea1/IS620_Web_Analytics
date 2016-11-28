import nltk
import random
from nltk.corpus import movie_reviews

# code based on Chap. 6 Movie Review classifier NLP with Python

class MovieClassifier(object):

    def __init__(self):
        # initialize instance vars and run setup
        self.documents = None
        self.classifier = None
        self.train_set = None
        self.test_set = None

        self.word_features = None
        self.feature_func = None
        self.__setup()

    def __setup(self):
        # build and shuffle documents; extract 2000 word features
        self.documents = [
            (list(movie_reviews.words(fileid)),category)
            for category in movie_reviews.categories()
            for fileid in movie_reviews.fileids(category)
        ]
        random.shuffle(self.documents)

        all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
        self.word_features = all_words.keys()[:2000]


    def __build_featuresets(self, feature_func):
        # build the training and test sets given a feature function
        self.featuresets = [(feature_func(d, self.word_features),c) for (d,c) in self.documents]
        self.train_set, self.test_set = self.featuresets[100:],self.featuresets[:100]

    def train(self, feature_func):
        #
        self.feature_func = feature_func
        self.__build_featuresets(self.feature_func)
        self.classifier = nltk.NaiveBayesClassifier.train(self.train_set)

    def most_informative(self, n):
        # show n most informative features using nltk
        self.classifier.show_most_informative_features(n)

    def report_accuracy(self):
        # reports accuracy on the test set
        if self.classifier is not None:
            return nltk.classify.accuracy(self.classifier,self.test_set)
        print "no classifier set"


if __name__ == '__main__':

    # feature function from p228 NLP for Python
    def document_features(document, word_features):
        document_words = set(document)
        features = {}
        for w in word_features:
            features['contains({})'.format(w)] = (w in document_words)
        return features

    m = MovieClassifier()
    #m.train_set
    m.train(document_features)
    print m.most_informative(10)
