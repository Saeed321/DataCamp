# Exploding gradient problem

# In the video exercise, you learned about two problems that may arise when working with RNN models: the vanishing and exploding gradient problems.

# This exercise explores the exploding gradient problem, showing that the derivative of a function can increase exponentially, 
# and how to solve it with a simple technique.
# The data is already loaded on the environment as X_train, X_test, y_train and y_test.
# You will use a Stochastic Gradient Descent (SGD) optimizer and Mean Squared Error (MSE) as the loss function.

# In the first step you will observe the gradient exploding by computing the MSE on the train and test sets. 
# On step 2, you will change the optimizer using the clipvalue parameter to solve the problem.

# The Stochastic Gradient Descent in Keras is loaded as SGD.
# •	Use SGD() as optimizer and (X_test, y_test) as validation data.
# •	Evaluate train performance and print all the MSE values.

# Create a Keras model with one hidden Dense layer
model = Sequential()
model.add(Dense(25, input_dim=20, activation='relu', kernel_initializer=he_uniform(seed=42)))
model.add(Dense(1, activation='linear'))

# Compile and fit the model
model.compile(loss='mean_squared_error', optimizer=SGD(lr=0.01, momentum=0.9))
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=100, verbose=0)

# See Mean Square Error for train and test data
train_mse = model.evaluate(X_train, y_train, verbose=0)
test_mse = model.evaluate(X_test, y_test, verbose=0)

# Print the values of MSE
print('Train: %.3f, Test: %.3f' % (train_mse, test_mse))

•	Set the SGD() parameter clipvalue equal to 3.0.
•	Compute the MSE values and store them on train_mse and test_mse variables.
# Create a Keras model with one hidden Dense layer
model = Sequential()
model.add(Dense(25, input_dim=20, activation='relu', kernel_initializer=he_uniform(seed=42)))
model.add(Dense(1, activation='linear'))

# Compile and fit the model
model.compile(loss='mean_squared_error', optimizer=SGD(lr=0.01, momentum=0.9, clipvalue=3.0))
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=100, verbose=0)

# See Mean Square Error for train and test data
train_mse = model.evaluate(X_train, y_train, verbose=0)
test_mse = model.evaluate(X_test, y_test, verbose=0)

# Print the values of MSE
print('Train: %.3f, Test: %.3f' % (train_mse, test_mse))
