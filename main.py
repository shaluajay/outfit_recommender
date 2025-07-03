
from recommender.data_loader import load_outfit_data
from recommender.model import recommend_outfit

if __name__ == "__main__":
    outfit_data = load_outfit_data("data/outfits.csv")
    user_input = {'occasion': 'casual'}
    outfit = recommend_outfit(user_input, outfit_data)
    print("Recommended Outfit:\n", outfit)