from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
document = [
    "Gaint panda gave birth to two twins in tokyo oldest zoo",
    "Great news for panda loves.",
    "Tokyo town is gifted with two baby pandas.",
    "India won womens T20 world cup.",
    "Great Honor for india in T20 world cup.",
    "Indian women cricket team is won the final."
]

vect = TfidfVectorizer()
X = vect.fit_transform(document)

model = KMeans(n_clusters=2, random_state=42)
model.fit(X)
labels = model.labels_

for i,doc in enumerate(document):
    print(f"cluster {labels[i]}: {doc}")