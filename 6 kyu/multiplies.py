# --------------------------------------------- #
# --- #    kata - Multiples of 3 or 5     # --- #
# --- #   kata/514b92a657cdc65150000006   # --- #
# --------------------------------------------- #

def solution(number):
    return sum([natural for natural in range(number) if natural % 3 == 0 or natural % 5 == 0])
