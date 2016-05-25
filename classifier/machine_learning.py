import numpy
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from .models import Classifier


def get_training_data(text):

    # filtered = Classifier.objects.all().filter(name=name)

    X_train = Classifier.objects.values_list('data', flat=True)
    y_train = Classifier.objects.values_list('category', flat=True)

    pipe = Pipeline([
            ('vectorizer', CountVectorizer()),
            ('classifier', MultinomialNB())
            ])

    pipe.fit(X_train, y_train)

    return pipe.predict([text])[0]
