import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

data = load_iris()
x = data.data
y = data.target

print("features = ",data.feature_names)
print("labels = ",data.target_names)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
model = Sequential()
model.add(Dense(10,input_dim=4,activation='relu'))
model.add(Dense(8,activation='relu'))
model.add(Dense(3,activation='softmax'))
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.fit(x_train,y_train,epochs=100,batch_size=2,verbose=1)

predictions = model.predict(x_test)
prediction_class = np.argmax(predictions, axis=1)
print("produced values = ",prediction_class.flatten())