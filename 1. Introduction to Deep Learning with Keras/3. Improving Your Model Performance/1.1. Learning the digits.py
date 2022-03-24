•	Add a Dense layer of 16 neurons with relu activation and input_shape being the total number of pixels of each image.
•	Add a Dense layer with 10 outputs and softmax activation.
•	Compile your model with adam, categorical_crossentropy, and accuracy metrics.
•	Make sure your model works by predicting on X_train.

# Instantiate a Sequential model
model = Sequential()

# Input and hidden layer with input_shape, 16 neurons, and relu 
model.add(Dense(16, input_shape = (64,), activation = 'relu'))

# Output layer with 10 neurons (one per digit) and softmax
model.add(Dense(10, activation='softmax'))

# Compile your model
model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

# Test if your model works and can process input data
print(model.predict(X_train))
