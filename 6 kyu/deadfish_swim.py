# ----------------------------------------------- #
# --- #    kata - Make the Deadfish Swim    # --- #
# --- #    kata/51e0007c1f9378fa810002a9    # --- #
# ----------------------------------------------- #

def parse(data):
    output_array = []
    value = 0
    for letter in data:
        if letter == 'i':
            value += 1
        elif letter == 'd':
            value -= 1
        elif letter == 's':
            value **= 2
        elif letter == 'o':
            output_array.append(value)
            
    return output_array
            