#文字レベルでのホットエンコーディング
import string
import numpy as np
np.set_printoptions(threshold=np.inf)

samples = ['The cat sat on the mat.', 'The dog ate my homework.']
characters = string.printable
token_index = dict(zip(characters, range(1, len(characters) + 1)))
#print(characters)
max_length = 50
results = np.zeros((len(samples), max_length, max(token_index.values()) + 1))

for i, sample in enumerate(samples):
    for j , character in enumerate(samples):
        index = token_index.get(character)
        results[i, j, index] = 1

#print(results)
