import numpy as np
from collections import Counter
import math

def tfidf_vectorizer(documents):
    """
    Build TF-IDF matrix from a list of text documents.
    Returns tuple of (tfidf_matrix, vocabulary).
    """
    tokenized_docs = [doc.lower().split() for doc in documents]

    # Step 2: build sorted vocabulary
    vocab = sorted(set(word for doc in tokenized_docs for word in doc))
    vocab_index = {word: i for i, word in enumerate(vocab)}

    N = len(documents)

    # Step 3: compute document frequency
    df = Counter()
    for doc in tokenized_docs:
        unique_words = set(doc)
        for word in unique_words:
            df[word] += 1

    # Step 4: compute TF-IDF matrix
    tfidf_matrix = np.zeros((N, len(vocab)))

    for i, doc in enumerate(tokenized_docs):
        counts = Counter(doc)
        total_words = len(doc)

        for word, count in counts.items():
            j = vocab_index[word]

            tf = count / total_words
            idf = math.log(N / df[word])

            tfidf_matrix[i][j] = tf * idf

    return tfidf_matrix, vocab
    