# ----------------------------------------------- #
# --- #    kata -- Where my anagrams at?    # --- #
# --- #    kata/523a86aa4230ebb5420001e1    # --- #
# ----------------------------------------------- #

def anagrams(check_word, words):
    sorted_check_word = ''.join(sorted(check_word))
    return [word for word in words if sorted_check_word == ''.join(sorted(word))]