import random
import string

def load_words(path="words.txt"):
    with open(path, "r") as f:
        return [line.strip().lower() for line in f if line.strip()]

def make_fake_word(length=5):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))

def generate_dataset(word_list, n=1000, fake_ratio=0.5):
    X = []
    y = []

    for _ in range(n):
        if random.random() < fake_ratio:
            # fake word
            X.append(make_fake_word())
            y.append(0)
        else:
            # real word
            X.append(random.choice(word_list))
            y.append(1)

    return X, y


# ---- example usage ----
words = load_words("words.txt")
X, y = generate_dataset(words, n=3000)

print(X[:10])
print(y[:10])