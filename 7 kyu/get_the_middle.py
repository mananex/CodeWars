# --------------------------------------------- #
# --- #  kata - Get the Middle Character  # --- #
# --- #   kata/56747fd5cb988479af000028   # --- #
# --------------------------------------------- #

def get_middle(s):
    return s[len(s) // 2] if len(s) % 2 != 0 else s[len(s) // 2 - 1:len(s) // 2 + 1]