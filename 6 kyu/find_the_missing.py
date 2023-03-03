# --------------------------------------------------------------------------- #
# --- #    kata - Find the missing term in an Arithmetic Progression    # --- #
# --- #                  kata/52de553ebb55d1fca3000371                  # --- #
# --------------------------------------------------------------------------- #

def find_missing(array):
    missing_number = 0
    progression = 0
    for number in range(len(array)):
        try:
            if not array[number + 1] + (array[number + 1] - array[number]) == array[number + 2]:
                missing_number = array[number]
                continue
            progression = array[number + 1] - array[number]
        except:
            pass
        
    return missing_number + progression