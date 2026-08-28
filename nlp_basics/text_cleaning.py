import nltk
import string

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


# Download required NLTK data
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")


# 1. Raw text
text = "Rahul will prepare the Project Report and send it to the team tomorrow!"

print("Original Text:")
print(text)


# 2. Tokenization
tokens = word_tokenize(text)

print("\nAfter Tokenization:")
print(tokens)


# 3. Convert to lowercase
tokens = [word.lower() for word in tokens]

print("\nAfter Lowercase:")
print(tokens)


# 4. Remove punctuation
tokens = [
    word for word in tokens
    if word not in string.punctuation
]

print("\nAfter Removing Punctuation:")
print(tokens)


# 5. Remove stopwords
stop_words = set(stopwords.words("english"))

tokens = [
    word for word in tokens
    if word not in stop_words
]

print("\nFinal Clean Text:")
print(tokens)