from sklearn.naive_bayes import MultinomialNB;
from sklearn.feature_extraction.text import CountVectorizer;

data = [
    "I love this product!",
    "This is the worst thing I ever bought.",
    "Absolutely fantastic! Highly recommend.",
    "Not what I expected.",
    "I'm so happy with my purchase!"
]
lables = ["positive","negative","positive","negative","positive"]

vec = CountVectorizer();
X = vec.fit_transform(data);
model = MultinomialNB();
model.fit(X,lables);

test_review = ["This is an fantastic item","it is worst of all"];
test_vector = vec.transform(test_review);
predictions = model.predict(test_vector);
print("Test Reviews:", test_review);
print("Predicted Sentiments:", predictions);