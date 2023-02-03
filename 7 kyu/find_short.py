# --------------------------------------------- #
# --- #       kata - Shortest Word        # --- #
# --- #   kata/57cebe1dc6fdc20c57000ac9   # --- #
# --------------------------------------------- #

def find_short(s):
    return min(list(map(lambda word: len(word), s.split(' '))))