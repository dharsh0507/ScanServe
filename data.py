from datetime import datetime

def img(f): return f"/static/images/{f}"

MENU = {
    "breakfast": [
        {"id": 1,  "name": "Idli Sambar",         "price": 40,  "calories": 200, "category": "South Indian", "popular": True,  "emoji": "🥣", "img": img("idli_sambar.jpg")},
        {"id": 2,  "name": "Masala Dosa",          "price": 60,  "calories": 350, "category": "South Indian", "popular": True,  "emoji": "🫓", "img": img("masala_dosa.jpg")},
        {"id": 3,  "name": "Poha",                 "price": 30,  "calories": 180, "category": "Light",        "popular": False, "emoji": "🍚", "img": img("poha.jpg")},
        {"id": 4,  "name": "Upma",                 "price": 35,  "calories": 220, "category": "Light",        "popular": False, "emoji": "🍲", "img": img("upma.jpg")},
        {"id": 13, "name": "Puri Bhaji",           "price": 50,  "calories": 400, "category": "North Indian", "popular": True,  "emoji": "🫔", "img": img("puri_bhaji.jpg")},
        {"id": 14, "name": "Vada Sambar",          "price": 45,  "calories": 280, "category": "South Indian", "popular": True,  "emoji": "🍩", "img": img("vada_sambar.jpg")},
        {"id": 15, "name": "Bread Omelette",       "price": 55,  "calories": 320, "category": "Protein",      "popular": False, "emoji": "🍳", "img": img("bread_omelette.jpg")},
        {"id": 16, "name": "Filter Coffee",        "price": 25,  "calories": 80,  "category": "Beverage",     "popular": True,  "emoji": "☕", "img": img("filter_coffee.jpg")},
        {"id": 17, "name": "Masala Chai",          "price": 20,  "calories": 60,  "category": "Beverage",     "popular": True,  "emoji": "🍵", "img": img("masala_chai.jpg")},
    ],
    "lunch": [
        {"id": 5,  "name": "Veg Thali",            "price": 120, "calories": 650, "category": "Full Meal",    "popular": True,  "emoji": "🍱", "img": img("veg_thali.jpg")},
        {"id": 6,  "name": "Chicken Biryani",      "price": 180, "calories": 750, "category": "Rice",         "popular": True,  "emoji": "🍛", "img": img("chicken_biryani.jpg")},
        {"id": 7,  "name": "Paneer Butter Masala", "price": 150, "calories": 500, "category": "Curry",        "popular": False, "emoji": "🧆", "img": img("paneer_butter_masala.jpg")},
        {"id": 8,  "name": "Dal Rice",             "price": 90,  "calories": 400, "category": "Light",        "popular": False, "emoji": "🍚", "img": img("dal_rice.jpg")},
        {"id": 18, "name": "Mutton Curry",         "price": 220, "calories": 680, "category": "Curry",        "popular": True,  "emoji": "🍖", "img": img("mutton_curry.jpg")},
        {"id": 19, "name": "Fish Fry",             "price": 200, "calories": 520, "category": "Protein",      "popular": True,  "emoji": "🐟", "img": img("fish_fry.jpg")},
        {"id": 20, "name": "Veg Fried Rice",       "price": 110, "calories": 450, "category": "Rice",         "popular": False, "emoji": "🍳", "img": img("veg_fried_rice.jpg")},
        {"id": 21, "name": "Lemon Rice",           "price": 80,  "calories": 380, "category": "South Indian", "popular": False, "emoji": "🍋", "img": img("lemon_rice.jpg")},
        {"id": 22, "name": "Mango Lassi",          "price": 60,  "calories": 220, "category": "Beverage",     "popular": True,  "emoji": "🥭", "img": img("mango_lassi.jpg")},
        {"id": 23, "name": "Fresh Lime Soda",      "price": 40,  "calories": 80,  "category": "Beverage",     "popular": False, "emoji": "🍋", "img": img("lime_soda.jpg")},
    ],
    "dinner": [
        {"id": 9,  "name": "Butter Naan + Curry",  "price": 140, "calories": 550, "category": "North Indian", "popular": True,  "emoji": "🫓", "img": img("butter_naan.jpg")},
        {"id": 10, "name": "Fried Rice",           "price": 130, "calories": 480, "category": "Rice",         "popular": True,  "emoji": "🍳", "img": img("fried_rice.jpg")},
        {"id": 11, "name": "Chapati + Dal",        "price": 80,  "calories": 350, "category": "Light",        "popular": False, "emoji": "🫓", "img": img("chapati.jpg")},
        {"id": 12, "name": "Grilled Chicken",      "price": 200, "calories": 420, "category": "Protein",      "popular": False, "emoji": "🍗", "img": img("grilled_chicken.jpg")},
        {"id": 24, "name": "Tandoori Chicken",     "price": 250, "calories": 520, "category": "Protein",      "popular": True,  "emoji": "🍗", "img": img("tandoori_chicken.jpg")},
        {"id": 25, "name": "Palak Paneer",         "price": 160, "calories": 460, "category": "Curry",        "popular": True,  "emoji": "🥬", "img": img("palak_paneer.jpg")},
        {"id": 26, "name": "Garlic Naan",          "price": 40,  "calories": 200, "category": "Bread",        "popular": True,  "emoji": "🫓", "img": img("garlic_naan.jpg")},
        {"id": 27, "name": "Veg Soup",             "price": 60,  "calories": 120, "category": "Soup",         "popular": False, "emoji": "🍜", "img": img("veg_soup.jpg")},
        {"id": 28, "name": "Cold Coffee",          "price": 70,  "calories": 180, "category": "Beverage",     "popular": True,  "emoji": "☕", "img": img("cold_coffee.jpg")},
    ],
}

EXTRAS = {
    "snacks": [
        {"id": 201, "name": "Samosa (2 pcs)",      "price": 30,  "calories": 260, "category": "Snack",     "popular": True,  "emoji": "🥟", "img": img("samosa.jpg")},
        {"id": 202, "name": "Veg Puff",            "price": 25,  "calories": 200, "category": "Snack",     "popular": True,  "emoji": "🥐", "img": img("veg_puff.jpg")},
        {"id": 203, "name": "Paneer Tikka",        "price": 120, "calories": 380, "category": "Snack",     "popular": True,  "emoji": "🧆", "img": img("paneer_tikka.jpg")},
        {"id": 204, "name": "French Fries",        "price": 80,  "calories": 320, "category": "Snack",     "popular": True,  "emoji": "🍟", "img": img("french_fries.jpg")},
        {"id": 205, "name": "Onion Rings",         "price": 70,  "calories": 280, "category": "Snack",     "popular": False, "emoji": "🧅", "img": img("onion_rings.jpg")},
        {"id": 206, "name": "Spring Rolls",        "price": 90,  "calories": 300, "category": "Snack",     "popular": False, "emoji": "🌯", "img": img("spring_rolls.jpg")},
    ],
    "desserts": [
        {"id": 301, "name": "Gulab Jamun",         "price": 50,  "calories": 300, "category": "Dessert",   "popular": True,  "emoji": "🍮", "img": img("gulab_jamun.jpg")},
        {"id": 302, "name": "Chocolate Brownie",   "price": 80,  "calories": 350, "category": "Dessert",   "popular": True,  "emoji": "🍫", "img": img("brownie.jpg")},
        {"id": 303, "name": "Rasgulla",            "price": 45,  "calories": 250, "category": "Dessert",   "popular": True,  "emoji": "🍡", "img": img("rasgulla.jpg")},
        {"id": 304, "name": "Kheer",               "price": 60,  "calories": 280, "category": "Dessert",   "popular": False, "emoji": "🍚", "img": img("kheer.jpg")},
        {"id": 305, "name": "Jalebi",              "price": 40,  "calories": 300, "category": "Dessert",   "popular": True,  "emoji": "🍩", "img": img("jalebi.jpg")},
        {"id": 306, "name": "Halwa",               "price": 55,  "calories": 320, "category": "Dessert",   "popular": False, "emoji": "🍯", "img": img("halwa.jpg")},
    ],
    "ice_cream": [
        {"id": 401, "name": "Vanilla Scoop",       "price": 60,  "calories": 200, "category": "Ice Cream",  "popular": True,  "emoji": "🍦", "img": img("vanilla_icecream.jpg")},
        {"id": 402, "name": "Chocolate Scoop",     "price": 60,  "calories": 220, "category": "Ice Cream",  "popular": True,  "emoji": "🍫", "img": img("chocolate_icecream.jpg")},
        {"id": 403, "name": "Mango Scoop",         "price": 70,  "calories": 210, "category": "Ice Cream",  "popular": True,  "emoji": "🥭", "img": img("mango_icecream.jpg")},
        {"id": 404, "name": "Strawberry Scoop",    "price": 70,  "calories": 200, "category": "Ice Cream",  "popular": False, "emoji": "🍓", "img": img("strawberry_icecream.jpg")},
        {"id": 405, "name": "Butterscotch Scoop",  "price": 70,  "calories": 230, "category": "Ice Cream",  "popular": True,  "emoji": "🍨", "img": img("butterscotch_icecream.jpg")},
        {"id": 406, "name": "Ice Cream Sundae",    "price": 120, "calories": 420, "category": "Ice Cream",  "popular": True,  "emoji": "🍨", "img": img("sundae.jpg")},
    ],
    "milkshakes": [
        {"id": 501, "name": "Chocolate Milkshake", "price": 90,  "calories": 380, "category": "Milkshake",  "popular": True,  "emoji": "🥤", "img": img("choco_shake.jpg")},
        {"id": 502, "name": "Mango Milkshake",     "price": 90,  "calories": 350, "category": "Milkshake",  "popular": True,  "emoji": "🥭", "img": img("mango_shake.jpg")},
        {"id": 503, "name": "Strawberry Shake",    "price": 90,  "calories": 340, "category": "Milkshake",  "popular": False, "emoji": "🍓", "img": img("strawberry_shake.jpg")},
        {"id": 504, "name": "Oreo Milkshake",      "price": 110, "calories": 420, "category": "Milkshake",  "popular": True,  "emoji": "🍪", "img": img("oreo_shake.jpg")},
        {"id": 505, "name": "Banana Shake",        "price": 80,  "calories": 360, "category": "Milkshake",  "popular": False, "emoji": "🍌", "img": img("banana_shake.jpg")},
        {"id": 506, "name": "Dry Fruit Shake",     "price": 130, "calories": 450, "category": "Milkshake",  "popular": False, "emoji": "🥜", "img": img("dryfruit_shake.jpg")},
    ],
    "beverages": [
        {"id": 601, "name": "Fresh Orange Juice",  "price": 70,  "calories": 120, "category": "Beverage",   "popular": True,  "emoji": "🍊", "img": img("orange_juice.jpg")},
        {"id": 602, "name": "Watermelon Juice",    "price": 60,  "calories": 90,  "category": "Beverage",   "popular": True,  "emoji": "🍉", "img": img("watermelon_juice.jpg")},
        {"id": 603, "name": "Coconut Water",       "price": 50,  "calories": 60,  "category": "Beverage",   "popular": True,  "emoji": "🥥", "img": img("coconut_water.jpg")},
        {"id": 604, "name": "Masala Buttermilk",   "price": 30,  "calories": 80,  "category": "Beverage",   "popular": True,  "emoji": "🥛", "img": img("buttermilk.jpg")},
        {"id": 605, "name": "Lemonade",            "price": 40,  "calories": 70,  "category": "Beverage",   "popular": False, "emoji": "🍋", "img": img("lemonade.jpg")},
        {"id": 606, "name": "Iced Tea",            "price": 60,  "calories": 100, "category": "Beverage",   "popular": False, "emoji": "🧊", "img": img("iced_tea.jpg")},
    ],
}

def get_time_slot():
    hour = datetime.now().hour
    if 6 <= hour < 11:   return "breakfast"
    elif 11 <= hour < 16: return "lunch"
    else:                 return "dinner"

def get_suggestions(time_slot, previous_orders):
    items = MENU[time_slot]
    scored = []
    for item in items:
        score = 0
        if item["popular"]: score += 2
        if item["name"] in previous_orders: score += 3
        scored.append((score, item))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [item for _, item in scored[:3]]

def get_all_items():
    return [i for items in list(MENU.values()) + list(EXTRAS.values()) for i in items]

def get_item_by_id(item_id):
    for items in list(MENU.values()) + list(EXTRAS.values()):
        for item in items:
            if item["id"] == item_id:
                return item
    return None

EMOTION_MAP = {
    "happy":     {"categories": ["Dessert", "Ice Cream", "South Indian"], "emoji": "😄", "reason": "Celebrate with something sweet!"},
    "sad":       {"categories": ["Comfort", "Full Meal", "Milkshake"],    "emoji": "😢", "reason": "Comfort food to lift your mood!"},
    "angry":     {"categories": ["Light", "Beverage", "Soup"],            "emoji": "😠", "reason": "Cool down with light food!"},
    "surprised": {"categories": ["Snack", "Ice Cream", "Milkshake"],      "emoji": "😲", "reason": "Try something exciting!"},
    "fearful":   {"categories": ["Comfort", "Soup", "Beverage"],          "emoji": "😨", "reason": "Soothing food to calm you down!"},
    "disgusted": {"categories": ["Light", "Beverage", "South Indian"],    "emoji": "🤢", "reason": "Simple and easy on the stomach!"},
    "neutral":   {"categories": ["Full Meal", "Rice", "Snack"],           "emoji": "😐", "reason": "A balanced meal for you!"},
    "tired":     {"categories": ["Protein", "Milkshake", "Beverage"],     "emoji": "😴", "reason": "Energy-boosting food to recharge!"},
}

MOOD_FOOD = [
    {"id": 101, "name": "Khichdi",       "price": 70,  "calories": 280, "category": "Comfort",   "popular": False, "emoji": "🍲", "img": img("khichdi.jpg")},
    {"id": 102, "name": "Tomato Soup",   "price": 60,  "calories": 120, "category": "Soup",      "popular": False, "emoji": "🍅", "img": img("tomato_soup.jpg")},
    {"id": 103, "name": "Protein Shake", "price": 90,  "calories": 200, "category": "Milkshake", "popular": False, "emoji": "💪", "img": img("choco_shake.jpg")},
    {"id": 104, "name": "Egg Bhurji",    "price": 80,  "calories": 320, "category": "Protein",   "popular": True,  "emoji": "🍳", "img": img("bread_omelette.jpg")},
    {"id": 105, "name": "Fruit Bowl",    "price": 60,  "calories": 150, "category": "Light",     "popular": False, "emoji": "🍓", "img": img("fruit_bowl.jpg")},
    {"id": 106, "name": "Green Salad",   "price": 50,  "calories": 100, "category": "Light",     "popular": False, "emoji": "🥗", "img": img("green_salad.jpg")},
]

def get_mood_suggestions(emotion):
    emotion = emotion.lower()
    info = EMOTION_MAP.get(emotion, EMOTION_MAP["neutral"])
    target_cats = info["categories"]
    all_items = MOOD_FOOD + [i for items in list(MENU.values()) + list(EXTRAS.values()) for i in items]
    matched = [item for item in all_items if item["category"] in target_cats]
    return matched[:4], info

OFFERS = [
    {"id": 1, "label": "10% OFF",      "discount": 10, "type": "percent"},
    {"id": 2, "label": "Free Dessert", "discount": 0,  "type": "item",  "item": "Gulab Jamun"},
    {"id": 3, "label": "20% OFF",      "discount": 20, "type": "percent"},
    {"id": 4, "label": "₹30 OFF",      "discount": 30, "type": "flat"},
    {"id": 5, "label": "Try Again!",   "discount": 0,  "type": "none"},
    {"id": 6, "label": "5% OFF",       "discount": 5,  "type": "percent"},
    {"id": 7, "label": "Free Shake",   "discount": 0,  "type": "item",  "item": "Mango Milkshake"},
    {"id": 8, "label": "15% OFF",      "discount": 15, "type": "percent"},
]

def apply_offer(offer, total):
    if offer["type"] == "percent": return round(total * offer["discount"] / 100)
    elif offer["type"] == "flat":  return min(offer["discount"], total)
    return 0

def search_items(query):
    query = query.lower()
    all_items = [i for items in list(MENU.values()) + list(EXTRAS.values()) for i in items] + MOOD_FOOD
    return [item for item in all_items if query in item["name"].lower() or query in item["category"].lower()]
