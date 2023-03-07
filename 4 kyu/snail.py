# ----------------------------------------------- #
# --- #            kata -- Snail            # --- #
# --- #    kata/521c2db8ddc89b9b7a0000c1    # --- #
# ----------------------------------------------- #

def get_side(snail_map, side):
    result_array = []
    for array in snail_map[:]:
        result_array.append(array[side])
        array.pop(side)
    return result_array

def return_final_array(general_array):
    return_array = []
    for array in general_array:
        for value in array:
            return_array.append(value)
    return return_array        

def snail(snail_map):
    result_array = []
    removable_length = len(snail_map)
    
    while True:
        try:
            result_array.append(snail_map[0])
            snail_map.pop(0)
            result_array.append(get_side(snail_map, -1))
            result_array.append(reversed(snail_map[-1]))
            snail_map.pop()
            result_array.append(reversed(get_side(snail_map, 0)))
        except:
            break
        
    return return_final_array(result_array)