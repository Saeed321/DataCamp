•	Import image from keras.preprocessing and preprocess_input from keras.applications.resnet50.
•	Load the image with the right target_size for your model.
•	Turn it into an array with image.img_to_array().
•	Pre-process img_expanded the same way the original ResNet50 training images were processed with preprocess_input().

# Import image and preprocess_input
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input

# Load the image with the right target size for your model
img = image.load_img(img_path, target_size=(224, 224))

# Turn it into an array
img_array = image.img_to_array(img)

# Expand the dimensions of the image
img_expanded = np.expand_dims(img_array, axis = 0)

# Pre-process the img in the same way original images were
img_ready = preprocess_input(img_expanded)
