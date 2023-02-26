# --------------------------------------------------- #
# --- #    kata -- Pokemon Damage Calculator    # --- #
# --- #      kata/536e9a7973130a06eb000e9f      # --- #
# --------------------------------------------------- #

damage_dict = {
    'fire': {'fire': 0.5, 'water': 0.5, 'grass': 2, 'electric': 1},
    'water': {'water': 0.5, 'fire': 2, 'grass': 0.5, 'electric': 0.5},
    'grass': {'grass': 0.5, 'fire': 0.5, 'water': 2, 'electric': 1},
    'electric': {'electric': 0.5, 'fire': 1, 'water': 2, 'grass': 1}
}

def calculate_damage(your_type, opponent_type, attack, defense):
    return 50 * (attack / defense) * damage_dict[your_type][opponent_type]