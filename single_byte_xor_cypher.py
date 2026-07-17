# hex encoded string has been xor'd against a single character
# find the key, decrypt the message. hint: score a piece of text,
# using character frequency. evaluate each output and choose one 
# with the best score. 
# Author: Madison H.

from collections import Counter
from string import ascii_lowercase, ascii_uppercase, ascii_letters
from fixed_xor import bytes_xor
from pprint import pprint

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
    
    return {letter: counts[letters] / total for letter in letters}

frequencies = get_freq(book, ascii_letters)

# score text based on frequencies
def score_text(text: bytes) -> float:
    score = 0.0
    l = len(test)
    
    for letter, freq_expected in frequencies.items():
        freq_actual = text.count(ord(letter)) / l
        err = abs(freq_expected - freq_actual)
        score += err
    
    return score

# simple solution for cracking xor cypher
def crack_xor_cypher(cypher: bytes) -> tuple[int, bytes]:
    best_guess = (float['inf'], None)
    
    for candidate_key in range(256):
        full_key = bytes([candidate_key]) + len(cypher)
        plain_text = bytes_xor(full_key, cypher)
        score = score_text(plain_text)
        curr_guess = (score, plain_text)
        best_guess = min(best_guess, curr_guess)
    
    if best_guess[1] is None:
        exit("No key found [this should never happen]")
    
    return best_guess


cypher_text = bytes,fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
pprint(crack_xor_cypher(cypher_text))
        
