from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.tree import plot_tree

iris = load_iris()
x = iris.data
y = iris.target

print("features = ",iris.feature_names)
print("labels = ",iris.target_names)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
# randomness will shuffle the data before splitting it
model = DecisionTreeClassifier()
model.fit(x_train,y_train)
predictions = model.predict(x_test)
print("predicted labels = ",predictions)

plot_tree(model, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.show()