# --------------------------------------------- #
# --- #     kata - String ends with ?     # --- #
# --- #   kata/51f2d1cafc9c0f745c00037d   # --- #
# --------------------------------------------- #

def solution(text, ending):
    return text[len(text) - len(ending):] == ending