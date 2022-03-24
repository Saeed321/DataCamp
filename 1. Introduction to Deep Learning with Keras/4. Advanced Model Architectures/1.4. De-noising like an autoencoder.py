•	Build an encoder model with the first layer of your trained autoencoder model.
•	Predict on X_test_noise with your encoder and show the results with show_encodings().

# Build your encoder
encoder = Sequential()
encoder.add(autoencoder.layers[0])

# Encode the images and show the encodings
preds = encoder.predict(X_test_noise)
show_encodings(preds)


•	Predict on X_test_noise with your autoencoder.
•	Plot noisy vs decoded images with compare_plot().

# Build your encoder
encoder = Sequential()
encoder.add(autoencoder.layers[0])

# Encode the images and show the encodings
preds = encoder.predict(X_test_noise)
show_encodings(preds)

# Predict on the noisy images with your autoencoder
decoded_imgs = autoencoder.predict(X_test_noise)

# Plot noisy vs decoded images
compare_plot(X_test_noise, decoded_imgs)
