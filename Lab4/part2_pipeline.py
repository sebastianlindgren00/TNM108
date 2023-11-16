from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_files #new
from sklearn.model_selection import train_test_split #new

moviedir = "/Users/sebastianlindgren/Documents/Fork_Projects/TNM108/Lab4/movie_reviews"

# loading all files. 
movie = load_files(moviedir, shuffle=True)

# Split data into training and test sets
docs_train, docs_test, y_train, y_test = train_test_split(movie.data, movie.target, test_size = 0.20, random_state = 12)

# Checking labels again
print ("Y-Train")
print(np.unique(y_train))
print("Y_Test")
print(np.unique(y_test))

# training SVM classifier
text_clf = Pipeline([
 ('vect', CountVectorizer()),
 ('tfidf', TfidfTransformer()),
 ('clf', MultinomialNB()),
])
text_clf.fit(docs_train, y_train)
predicted = text_clf.predict(docs_test)
print("SVM accuracy ",np.mean(predicted == y_test))

print(metrics.classification_report(y_test, predicted,
 target_names=movie.target_names))

# Confusion matrix T = True, F = False, P = Positive, N = Negative
#179 (TN) |  27 (FP)

#46 (FN) | 148 (TP)

print(metrics.confusion_matrix(y_test, predicted))

parameters = { 
    'vect__ngram_range': [(1, 1), (1, 2)],
    'tfidf__use_idf': (True, False),
    'clf__alpha': (1e-2, 1e-3)
    }

gs_clf = GridSearchCV(text_clf, parameters, cv=5, n_jobs=-1)

gs_clf = gs_clf.fit(docs_train[:400], y_train[:400])

# very short and fake movie reviews
reviews_new = ['This movie was excellent', 'Absolute joy ride', 
            'Steven Seagal was terrible', 'Steven Seagal shone through.', 
              'This was certainly a movie', 'Two thumbs up', 'I fell asleep halfway through', 
              "We can't wait for the sequel!!", '!', '?', 'I cannot recommend this highly enough', 
              'instant classic.', 'Steven Seagal was amazing. His performance was Oscar-worthy.']



for param_name in sorted(parameters.keys()):
    print("%s: %r" % (param_name, gs_clf.best_params_[param_name]))

# print out results
pred = gs_clf.predict(reviews_new)
print("Best estimator:")
for review, category in zip(reviews_new, pred):
    print('%r => %s' % (review, movie.target_names[category]))

print("Best score:")
print(gs_clf.best_score_)
print("Movie target names")
print(movie.target_names)
print(pred)
# Label-checking for neg and pos mix up.
print(np.unique(movie.target))

# Why did it choose vect_ngram_range (1, 1) here instead of vect__ngram_range: (1, 2) as it did in the example?