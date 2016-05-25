import numpy
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from .models import Classifier


def get_training_data():

    filtered = Classifier.objects.all().filter(name=name)

    X_train = filtered.objects.values_list('data', flat=True)
    y_train = filtered.objects.values_list('category', flat=True)

    pipe = Pipeline([
            ('vectorizer', CountVectorizer()),
            ('classifier', MultinomialNB())
            ])

    return pipe.fit(X_train, y_train)



def what_is_the_text():

    # some input from an html page is the test data
    train = get_training_data()

    return pipe.predict("")
