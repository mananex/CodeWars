# --------------------------------------------- #
# --- #    kata - Counting Duplicates     # --- #
# --- #   kata/54bf1c2cd5b56cc47f0007a1   # --- #
# --------------------------------------------- #

from collections import Counter

def duplicate_count(text):
    return len([count for count in Counter(text.lower()).values() if count > 1])