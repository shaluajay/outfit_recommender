import random
def recommend_outfit(user_input, outfit_data):
    filtered = outfit_data[outfit_data['Occasion']==user_input['Occasion']]
    if filtered.empty:
        return "No suitable outfits found."
    return filtered.sample(1).iloc[0]