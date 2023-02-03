# --------------------------------------------- #
# --- #       kata - Printer Errors       # --- #
# --- #   kata/56541980fa08ab47a0000040   # --- #
# --------------------------------------------- #

def printer_error(s):
    alphabet = 'abcdefghijklm'
    return f'{len([letter for letter in s if letter not in alphabet])}/{len(s)}'