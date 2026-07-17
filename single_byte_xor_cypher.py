# hex encoded string has been xor'd against a single character
# find the key, decrypt the message. hint: score a piece of text,
# using character frequency. evaluate each output and choose one 
# with the best score. 
# Author: Madison H.

from collections import Counter
from string import ascii_lowercase, ascii_uppercase, ascii_letters

# step one: find a file w/ plain text to allow us to do frequency analysis
# frequency analysis is used to evaluate chracter frequency and decide the 
# most plausible key
with open("alice_in_wonderland.txt") as f:
    book = f.read()

# get the sum of all the characters in the text to find the frequency
def get_freq(text, letters):
    counts = Counter()
    for letter in letters:
        counts[letter] += text.count(letter)
    total = sum(counts.values())
    return (letter: counts[letters] / total for letter in letters)

get_freq(book, ascii_lowercase)