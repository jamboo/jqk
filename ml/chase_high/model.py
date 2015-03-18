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


def m_nusvc(learning_sample, learning_target, testing_sample):
    clf = NuSVC()
    return run_model(clf,learning_sample, learning_target, testing_sample)


def m_gaussianNB(learning_sample, learning_target, testing_sample):
    clf = GaussianNB()
    return run_model(clf,learning_sample, learning_target, testing_sample)

def m_svc_gamma(learning_sample, learning_target, testing_sample):
    clf = SVC(gamma=2, C=1)
    return run_model(clf,learning_sample, learning_target, testing_sample)

def m_svc_rbf(learning_sample, learning_target, testing_sample):
    clf = SVC(kernel='rbf')
    return run_model(clf,learning_sample, learning_target, testing_sample)


def m_qda(learning_sample, learning_target, testing_sample):
    clf = QDA()
    return run_model(clf,learning_sample, learning_target, testing_sample)

def run_model(clf,learning_sample, learning_target, testing_sample):
    clf.fit(learning_sample,learning_target)
    return list(clf.predict(testing_sample))

def m_nearest_centroid(learning_sample, learning_target, testing_sample):
    clf = NearestCentroid()
    return run_model(clf,learning_sample, learning_target, testing_sample)

def m_lda(learning_sample, learning_target, testing_sample):
    clf = LDA()
    return run_model(clf,learning_sample, learning_target, testing_sample)


def m_nearest_centroid_selected(learning_sample, learning_target, testing_sample):
    [new_learning_sample, new_testing_sample] = selected_feature(5,2,learning_sample,learning_target,testing_sample)
    return m_nearest_centroid(new_learning_sample,learning_target,new_testing_sample)


def selected_feature(n_components, best_k, learning_sample, learning_target,testing_sample):
    pca = PCA(n_components=n_components)
    selection = SelectKBest(k=best_k)
    combined_features = FeatureUnion([("pca", pca), ("univ_select", selection)])
    new_learning_sample = combined_features.fit(learning_sample, learning_target).transform(learning_sample)
    new_testing_sample = combined_features.fit(learning_sample, learning_target).transform(testing_sample)
    return [new_learning_sample,new_testing_sample]



def performance_evaluation(testing_results, testing_target):
    type_1_error = 0.5  # not buying but choose to buy in model
    type_2_error = 0.5  # buying but choose to not buy in model
    correct_ratio = 0

    buy_correct = 0
    buy_wrong = 0
    for index, value in enumerate(testing_results):
        if value == 1:
            if testing_target[index] == 1: buy_correct += 1
            else: buy_wrong += 1
    if len(testing_results) == len(testing_target):
        type_1_error = list(array(testing_results) - array(testing_target)).count(1) / (len(testing_results)*1.0)
        type_2_error = list(array(testing_target) - array(testing_results)).count(-1) / (len(testing_results)*1.0)
        correct_ratio = list(array(testing_target) - array(testing_results)).count(0) / (len(testing_results)*1.0)
    return {
        'type_1_error': type_1_error,
        'type_2_error': type_2_error,
        'correct_ratio': correct_ratio,
        'buy_correct': buy_correct / ((buy_correct + buy_wrong) * 1.0) if buy_correct+buy_wrong > 0 else 0,
        'total_buy':buy_correct+buy_wrong
    }


