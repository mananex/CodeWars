# --------------------------------------------- #
# --- #    kata - Highest Scoring Word    # --- #
# --- #   kata/57eb8fcdf670e99d9b000272   # --- #
# --------------------------------------------- #

import string

def func(word):
    return_number = 0
    last_letter = ''
    for letter in word:
        return_number += (string.ascii_lowercase.index(letter))
        if letter == last_letter: return_number += 1
        last_letter = letter
    print(word, return_number)
    return return_number
        

def high(input_string):
    return max(input_string.split(' '), key = func)

print(high('rhedylhs sfwueetcw xrm bxsmdqxqkj huriy qec cqgig ijxmwdseyf wxaxumwk lsecvlk epjlystkg xttgs'))