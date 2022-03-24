•	Instantiate a ResNet50 model, setting the weights parameter to be 'imagenet'.
•	Use the model to predict on your processed image.
•	Decode the first 3 predictions with decode_predictions().

# Instantiate a ResNet50 model with 'imagenet' weights
model = ResNet50(weights='imagenet')

# Predict with ResNet50 on your already processed img
preds = model.predict(img_ready)

# Decode the first 3 predictions
print('Predicted:', decode_predictions(preds, top=3)[0])
