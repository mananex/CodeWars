# --------------------------------------------- #
# --- #       kata -- Ones and Zeros      # --- #
# --- #   kata/578553c3a1b8d5c40300037c   # --- #
# --------------------------------------------- #

def binary_array_to_number(arr):
    return sum([bit * 2 ** count for count, bit in enumerate(reversed(arr))])