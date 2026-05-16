import random
import string
from data import load_words, make_fake_word, generate_dataset


from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report





# LOAD DATA

words = load_words("words.txt")

X, y = generate_dataset(words, fake_ratio=0.5, n=10000)

# split into train/test
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# FEATURE EXTRACTION

vectorizer = CountVectorizer(
    analyzer='char',
    ngram_range=(0, 2)
)

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)


# TRAIN MODEL

model = LogisticRegression(max_iter=1000)

model.fit(X_train_vec, y_train)


# EVALUATE

predictions = model.predict(X_test_vec)

print(classification_report(y_test, predictions))


# TRY CUSTOM WORDS

while True:

    text = input("Enter word: ").lower()

    vec = vectorizer.transform([text])

    prob = model.predict_proba(vec)[0][1]

    print(f"English probability: {prob:.3f}")