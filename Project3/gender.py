import nltk
import random
import pandas as pd
from nltk.corpus import names

class GenderClassifier(object):

    def __init__(self, names):
        self.test_names = None
        self.train_names = None
        self.testdev_names = None
        self.classifier = None

        self.train_set = None
        self.testdev_set = None
        self.test_set = None

        self.feature_func = None # set by client in train

        self.__setup(names) # pass in imported corpus


    def __setup(self,names):
        ## builds and shuffles corpus for the object
        # note: training set will be further split into dev-test and training for error analysis
        male_names = [(n,'male') for n in names.words('male.txt')]
        female_names = [(n,'female') for n in names.words('female.txt')]
        names = male_names + female_names
        random.shuffle(names)

        self.test_names = names[0:500] # testing and training sets
        self.train_names = names[500:]


    def __build_featuresets(self, feature_func):
        ## build testset if not already built for object
        # reshuffle and select training and test dev sets for classifier
        if self.test_set is None:
            self.test_set = [(feature_func(n),g) for (n,g) in self.test_names]

        random.shuffle(self.train_names)
        self.testdev_names = self.train_names[0:500]
        self.train_names = self.train_names[500:]

        self.testdev_set = [(feature_func(n),g) for (n,g) in self.testdev_names]
        self.train_set = [(feature_func(n),g) for (n,g) in self.train_names]

    def train(self, feature_func):
        # sets feature_func and builds classifier
        self.feature_func = feature_func
        self.__build_featuresets(self.feature_func)
        self.classifier = nltk.NaiveBayesClassifier.train(self.train_set)

    def informative_features(self):
        self.classifier.show_most_informative_features(10)

    def error_analysis_table(self):
        errors = []
        for (name, correct) in self.testdev_names:
            guess = self.classifier.classify(self.feature_func(name))
            if guess != correct:
                errors.append((correct, guess, name))
        return pd.DataFrame(errors,columns=['correct', 'guess', 'names'])

    def report_dev_accuracy(self):
        # reports accuracy on the test set
        return nltk.classify.accuracy(self.classifier,self.test_set)

    def report_test_accuracy(self):
        # reports accuracy on the test dev set.. useful for fine tuning
        return nltk.classify.accuracy(self.classifer,self.testdev_set)


if __name__ == '__main__':
    g = GenderClassifier(names)
    print g.test_names[0:5]
    print g.train_names[0:5]

    def gender_feature(name):
        return {'last': name[-1].lower()}

    g.train(gender_feature)
    g.informative_features()
    g.report_dev_accuracy()
