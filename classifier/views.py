from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline

# Create your views here.
def create_classifier(request):
    # get input from User
    X_train = data.Classifier.get()
    y_train = category.Classifier.get()
    # run training for text input
    pipe = Pipeline([('vectorizer', CountVectorizer()), ('classifier', MultinomialNB())])
    pipe.fit(X_train, y_train)
    # save somehow
