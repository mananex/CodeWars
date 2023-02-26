# --------------------------------------------- #
# --- #       kata -- Sums of Parts       # --- #
# --- #   kata/5ce399e0047a45001c853c2b   # --- #
# --------------------------------------------- #

def parts_sums(ls):
    return [sum(ls[count:]) for count in range(len(ls) + 1)]