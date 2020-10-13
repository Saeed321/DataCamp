# Images as data: visualizations

# To display image data, you will rely on Python's Matplotlib library, 
# and specifically use matplotlib's pyplot sub-module, that contains many plotting commands. 
# Some of these commands allow you to display the content of images stored in arrays.

# �	Import the image from the file bricks.png into data.
# �	Display the image in data on the screen.

# Import matplotlib
import matplotlib.pyplot as plt

# Load the image
data = plt.imread('bricks.png')

# Display the image
plt.imshow(data)
plt.show()
