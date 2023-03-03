# --------------------------------------------- #
# --- #    kata -- Playing with digits    # --- #
# --- #   kata/5552101f47fc5178b1000050   # --- #
# --------------------------------------------- #

def dig_pow(n, p):
    end_number = sum([int(num) ** (p + index) for index, num in enumerate(list(str(n)))])
    return end_number / n if end_number / n * n == end_number else -1