# --------------------------------------------- #
# --- #         kata - Two to One         # --- #
# --- #   kata/5656b6906de340bd1b0000ac   # --- #
# --------------------------------------------- #

def longest(a1, a2):
    return ''.join(sorted(set(a1 + a2)))