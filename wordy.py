# wordy.py
from itertools import permutations
import math


def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


def wordlist(prompt, n):
    word = ''
    low = set()
    words = permutations(prompt, n)
    # print(list(permutations(prompt)))
    for tup in words:
        word = ''.join(tup)
        low.add(word)
        word = ''
    # print(low)
    return low


if __name__ == '__main__':
    english_words = load_words()
    # minsize = input("Minimum character length: ")
    while True:
        prompt = input("Enter prompt: ")
        prompt = prompt.lower()
        print("\n")
        
        count = 3
        wordset = set()
        while count <= len(prompt):
            wordset.update(wordlist(prompt, count))
            count += 1
        resultwords = wordset.intersection(english_words)
        result = sorted(sorted(list(resultwords)), key=len)

        print(result)
        print("\n")
 