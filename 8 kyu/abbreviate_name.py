# --------------------------------------------- #
# --- # kata - Abbreviate a Two Word Name # --- #
# --- #   kata/57eadb7ecd143f4c9c0000a3   # --- #
# --------------------------------------------- #

def abbrev_name(name):
    return '.'.join([word[0] for word in name.split(' ')]).upper()