# ---------------------------------------------- #
# --- #         kata - Fake Binary         # --- #
# --- #   kata/57eae65a4321032ce000002d    # --- #
# ---------------------------------------------- #

def fake_bin(numbers):
    return ''.join('0' if number < '5' else '1' for number in numbers)

