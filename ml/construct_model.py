__author__ = 'yingbozhan'

from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest
from sklearn.pipeline import Pipeline, FeatureUnion
from numpy import array
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, NuSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.lda import LDA
from sklearn.qda import QDA
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier


def m_nusvc(learning_sample, learning_target, testing_sample, run=False):
    clf = NuSVC()
    if not run:
        return find_model(clf, learning_sample, learning_target)
    return run_model(clf,learning_sample, learning_target, testing_sample)


def m_gaussianNB(learning_sample, learning_target, testing_sample, run=False):
    clf = GaussianNB()
    if not run:
        return find_model(clf, learning_sample, learning_target)
    return run_model(clf,learning_sample, learning_target, testing_sample)

def m_svc_gamma(learning_sample, learning_target, testing_sample, run=False):
    clf = SVC(gamma=2, C=1)
    if not run:
        return find_model(clf, learning_sample, learning_target)
    return run_model(clf,learning_sample, learning_target, testing_sample)

def m_svc_rbf(learning_sample, learning_target, testing_sample, run=False):
    clf = SVC(kernel='rbf')
    if not run:
        return find_model(clf, learning_sample, learning_target)
    return run_model(clf,learning_sample, learning_target, testing_sample)


def m_qda(learning_sample, learning_target, testing_sample, run=False):
    clf = QDA()
    if not run:
        return find_model(clf, learning_sample, learning_target)
    return run_model(clf,learning_sample, learning_target, testing_sample)

def m_nearest_centroid(learning_sample, learning_target, testing_sample, run=False):
    clf = NearestCentroid()
    if not run:
        return find_model(clf, learning_sample, learning_target)
    return run_model(clf,learning_sample, learning_target, testing_sample)

def m_lda(learning_sample, learning_target, testing_sample, run=False):
    clf = LDA()
    if not run:
        return find_model(clf, learning_sample, learning_target)
    return run_model(clf,learning_sample, learning_target, testing_sample)


def run_model(clf,learning_sample, learning_target, testing_sample):
    clf.fit(learning_sample,learning_target)
    return list(clf.predict(testing_sample))

def find_model(clf, learning_sample, learning_target):
    clf.fit(learning_sample, learning_target)
    return clf