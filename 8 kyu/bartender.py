# --------------------------------------------- #
# --- #     kata - Bartender, drinks!     # --- #
# --- #   kata/568dc014440f03b13900001d   # --- #
# --------------------------------------------- #

def get_drink_by_profession(param):
    association_dict = { 'jabroni': 'Patron Tequila',
                         'school counselor': 'Anything with Alcohol',
                         'programmer': 'Hipster Craft Beer',
                         'bike gang member': 'Moonshine',
                         'politician': 'Your tax dollars',
                         'rapper': 'Cristal' }
    return association_dict[param.lower()] if param.lower() in association_dict else 'Beer'