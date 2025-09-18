import tensorflow as tf
from tensorflow.keras import layers,models
import matplotlib.pyplot as plt

(X_train,y_train),(X_test,y_test) = tf.keras.datasets.mnist.load_data()

#Normalise data
X_train = X_train.astype("float32")
X_test = X_test.astype("float32")

#Reshape data (CNN expects 3D:height,width,channels)
X_train = X_train.reshape(-1,28,28,1)
X_test = X_test.reshape(-1,28,28,1)
#-1 means "figure this dimension out automatically"
#1 is the number of channels

#Build a sample CNN model
model = models.Sequential([
    layers.Conv2D(32,(3,3),activation = 'relu',input_shape = (28,28,1)),
    layers.MaxPooling2D((2,2)),
    layers.Flatten(),
    layers.Dense(64,activation = 'relu'),
    layers.Dense(10,activation = 'softmax')
])

#Compile model
model.compile(optimizer = 'adam',
              loss = 'sparse_categorical_crossentropy',
              metrics = ['accuracy'])

#Train the model
history = model.fit(
    X_train,y_train,
    epochs = 5,
    batch_size = 64, #faster training
    validation_data = (X_test,y_test),
    verbose = 1 #show progress bar
)

#Evaluate on test data
test_loss,test_acc = model.evaluate(X_test,y_test,verbose = 0)
print("Test Accuracy:",round(test_acc*100,2),"%")

#Predict example
prediction = model.predict(X_test[:1]) #get prediction probabilities
predicted_label = prediction.argmax() #find the most likely class

plt.imshow(X_test[0].reshape(28,28),cmap = "gray")
plt.title("Prediction: "+ str(predicted_label))
plt.axis("off")
plt.show()