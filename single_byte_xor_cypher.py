# hex encoded string has been xor'd against a single character
# find the key, decrypt the message. hint: score a piece of text,
# using character frequency. evaluate each output and choose one 
# with the best score. 
# Author: Madison H.

from collections import Counter
from dataclasses import dataclass
from string import ascii_lowercase, ascii_uppercase, ascii_letters
from typing import Optional
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

# dataclass implementation 
@dataclass(order=True)
class ScoredGuess:
    score: float = float("inf")
    key: Optional[int] = None
    cipher: Optional[bytes] = None
    plaintext: Optional[bytes] = None
    
@classmethod
def from_key(cls, ct, key_val):
    full_key = bytes([key_val]) * len(ct)
    pt = bytes_xor(ct, full_key)
    score = score_text(pt)
    return cls(score, key_val, ct, pt)

# score text based on frequencies
def score_text(text: bytes) -> float:
    score = 0.0
    l = len(text)
    
    for letter, freq_expected in frequencies.items():
        freq_actual = text.count(ord(letter)) / l
        err = abs(freq_expected - freq_actual)
        score += err
    
    return score

# simple solution for cracking xor cypher
def crack_xor_cypher(cypher: bytes):
    best_guess = ScoredGuess()
    
    for candidate_key in range(256):
        guess = ScoredGuess.from_key(cypher, candidate_key)  # type: ignore
        best_guess = min(best_guess, guess)
    
    if best_guess.key is None:
        exit("no key found (this should never happen)")
    
    return best_guess
        

if __name__ == "__main__":
    cypher_text = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
    pprint(crack_xor_cypher(cypher_text))
            
