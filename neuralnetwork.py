import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# [study][sleep]
X = np.array([
    [2,7],
    [5,6],
    [1,8],
    [6,5],
    [3,7],
    [7,4],
    [4,6],
    [2,8]
])
y = np.array([0,1,0,1,0,1,1,0])

model = Sequential()
model.add(Dense(4,input_dim=2,activation='relu'))
model.add(Dense(1,activation='sigmoid'))
model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
model.fit(X,y,epochs=100,batch_size=2,verbose=1)

predictions = model.predict(X)
prediction_class = (predictions>0.5).astype(int)
print("produced values = ",prediction_class.flatten())