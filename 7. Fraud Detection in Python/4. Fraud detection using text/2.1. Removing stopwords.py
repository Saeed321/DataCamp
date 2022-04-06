•	Import the stopwords from ntlk.
•	Define 'english' words to use as stopwords under the variable stop.
•	Get the punctuation set from the string package and assign it to exclude.

# Import nltk packages and string 
from nltk.corpus import stopwords
import string

# Define stopwords to exclude
stop = set(stopwords.words('english'))
stop.update(("to","cc","subject","http","from","sent", "ect", "u", "fwd", "www", "com"))

# Define punctuations to exclude and lemmatizer
exclude = set(string.punctuation)
