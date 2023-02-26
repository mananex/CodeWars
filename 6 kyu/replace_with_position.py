# ------------------------------------------------------------- #
# --- #       kata - Replace With Alphabet Position       # --- #
# --- #           kata/5ce399e0047a45001c853c2b           # --- #
# ------------------------------------------------------------- #

import string

def alphabet_position(text):
    return ' '.join([str(string.ascii_lowercase.index(letter) + 1) for letter in text.lower() if letter.isalpha()])