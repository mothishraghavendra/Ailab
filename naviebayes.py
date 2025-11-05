from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

datasets =[
    "Free Money now",
    "Hi, how are you?",
    "Win a lottery",
    "Let's catch up for lunch",
    "Congratulations, you have won a prize",
    "Are you coming to the meeting?",
    "Claim your free vacation",
    "Don't forget our appointment",
    "You have been selected for a gift",
    "Looking forward to our collaboration"
]
labels = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0] 
vect = CountVectorizer()
X = vect.fit_transform(datasets)
model = MultinomialNB()
model.fit(X, labels)

test_email = ["Congratulations! You have won a lottery", "Claim your free vacation"]
test_vector = vect.transform(test_email)
prediction = model.predict(test_vector)
print("Test Emails:", test_email)
print("note: 1 indicates spam, 0 indicates ham")
print("Predictions of spam and ham emails are:", prediction)