from datetime import datetime
import os

# Verified image URLs — Unsplash + Wikimedia for Indian dishes
IMG_URLS = {
    # Breakfast
    "idli_sambar":           "https://images.unsplash.com/photo-1589301760014-d929f3979dbc?w=400&q=80",
    "masala_dosa":           "https://images.unsplash.com/photo-1567337710282-00832b415979?w=400&q=80",
    "poha":                  "https://images.unsplash.com/photo-1606491956689-2ea866880c84?w=400&q=80",
    "upma":                  "https://images.unsplash.com/photo-1631515243349-e0cb75fb8d3a?w=400&q=80",
    "puri_bhaji":            "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=400&q=80",
    "vada_sambar":           "https://images.unsplash.com/photo-1610192244261-3f33de3f55e4?w=400&q=80",
    "bread_omelette":        "https://images.unsplash.com/photo-1482049016688-2d3e1b311543?w=400&q=80",
    "filter_coffee":         "https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=400&q=80",
    "masala_chai":           "https://images.unsplash.com/photo-1561336313-0bd5e0b27ec8?w=400&q=80",
    # Lunch
    "veg_thali":             "https://images.unsplash.com/photo-1567337710282-00832b415979?w=400&q=80",
    "chicken_biryani":       "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=400&q=80",
    "paneer_butter_masala":  "https://images.unsplash.com/photo-1631452180519-c014fe946bc7?w=400&q=80",
    "dal_rice":              "https://images.unsplash.com/photo-1546833999-b9f581a1996d?w=400&q=80",
    "mutton_curry":          "https://images.unsplash.com/photo-1574653853027-5382a3d23a15?w=400&q=80",
    "fish_fry":              "https://images.unsplash.com/photo-1580476262798-bddd9f4b7369?w=400&q=80",
    "veg_fried_rice":        "https://images.unsplash.com/photo-1603133872878-684f208fb84b?w=400&q=80",
    "lemon_rice":            "https://images.unsplash.com/photo-1596797038530-2c107229654b?w=400&q=80",
    "mango_lassi":           "https://images.unsplash.com/photo-1553361371-9b22f78e8b1d?w=400&q=80",
    "lime_soda":             "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=400&q=80",
    # Dinner
    "butter_naan":           "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400&q=80",
    "fried_rice":            "https://images.unsplash.com/photo-1512058564366-18510be2db19?w=400&q=80",
    "chapati":               "https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=400&q=80",
    "grilled_chicken":       "https://images.unsplash.com/photo-1598103442097-8b74394b95c3?w=400&q=80",
    "tandoori_chicken":      "https://images.unsplash.com/photo-1599487488170-d11ec9c172f0?w=400&q=80",
    "palak_paneer":          "https://images.unsplash.com/photo-1631452180519-c014fe946bc7?w=400&q=80",
    "garlic_naan":           "https://images.unsplash.com/photo-1626804475297-41608ea09aeb?w=400&q=80",
    "veg_soup":              "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=400&q=80",
    "cold_coffee":           "https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=400&q=80",
    # Snacks
    "samosa":                "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400&q=80",
    "veg_puff":              "https://images.unsplash.com/photo-1509722747041-616f39b57569?w=400&q=80",
    "paneer_tikka":          "https://images.unsplash.com/photo-1567188040759-fb8a883dc6d8?w=400&q=80",
    "french_fries":          "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=400&q=80",
    "onion_rings":           "https://images.unsplash.com/photo-1639024471283-03518883512d?w=400&q=80",
    "spring_rolls":          "https://images.unsplash.com/photo-1548507769-f8a5b1e3e3e3?w=400&q=80",
    # Desserts
    "gulab_jamun":           "https://images.unsplash.com/photo-1601303516534-bf4b7d1c5a5e?w=400&q=80",
    "brownie":               "https://images.unsplash.com/photo-1564355808539-22fda35bed7e?w=400&q=80",
    "rasgulla":              "https://images.unsplash.com/photo-1666492031773-f7d3f2b5e7b1?w=400&q=80",
    "kheer":                 "https://images.unsplash.com/photo-1571091718767-18b5b1457add?w=400&q=80",
    "jalebi":                "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=400&q=80",
    "halwa":                 "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=400&q=80",
    # Ice Cream
    "vanilla_icecream":      "https://images.unsplash.com/photo-1570197788417-0e82375c9371?w=400&q=80",
    "chocolate_icecream":    "https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=400&q=80",
    "mango_icecream":        "https://images.unsplash.com/photo-1497034825429-c343d7c6a68f?w=400&q=80",
    "strawberry_icecream":   "https://images.unsplash.com/photo-1488900128323-21503983a07e?w=400&q=80",
    "butterscotch_icecream": "https://images.unsplash.com/photo-1551024709-8f23befc6f87?w=400&q=80",
    "sundae":                "https://images.unsplash.com/photo-1551024506-0bccd828d307?w=400&q=80",
    # Milkshakes
    "choco_shake":           "https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=400&q=80",
    "mango_shake":           "https://images.unsplash.com/photo-1546173159-315724a31696?w=400&q=80",
    "strawberry_shake":      "https://images.unsplash.com/photo-1553361371-9b22f78e8b1d?w=400&q=80",
    "oreo_shake":            "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400&q=80",
    "banana_shake":          "https://images.unsplash.com/photo-1587314168485-3236d6710814?w=400&q=80",
    "dryfruit_shake":        "https://images.unsplash.com/photo-1571091718767-18b5b1457add?w=400&q=80",
    # Beverages
    "orange_juice":          "https://images.unsplash.com/photo-1621506289937-a8e4df240d0b?w=400&q=80",
    "watermelon_juice":      "https://images.unsplash.com/photo-1497534446932-c925b458314e?w=400&q=80",
    "coconut_water":         "https://images.unsplash.com/photo-1550583724-b2692b85b150?w=400&q=80",
    "buttermilk":            "https://images.unsplash.com/photo-1553361371-9b22f78e8b1d?w=400&q=80",
    "lemonade":              "https://images.unsplash.com/photo-1523677011781-c91d1bbe2f9e?w=400&q=80",
    "iced_tea":              "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=400&q=80",
    # Mood Food
    "khichdi":               "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=400&q=80",
    "tomato_soup":           "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=400&q=80",
    "fruit_bowl":            "https://images.unsplash.com/photo-1490474418585-ba9bad8fd0ea?w=400&q=80",
    "green_salad":           "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&q=80",
}

_FILE_MAP = {
    "idli_sambar":          "idli-sambar-recipe-sagar-kitchen.jpg",
    "masala_dosa":          "Masala-Dosa-M.jpg",
    "upma":                 "Vegetable-Upma-4.jpg",
    "puri_bhaji":           "puri.avif",
    "vada_sambar":          "vada sambar.jpg",
    "bread_omelette":       "bread ombelet.jpg",
    "filter_coffee":        "Filter Coffee.jpg",
    "masala_chai":          "Masala Chai.png",
    "veg_thali":            "veg-thali.avif",
    "gulab_jamun":          "gulub jam.jpg",
    "rasgulla":             "rasagulla.webp",
    "kheer":                "Kheer.jpg",
    "jalebi":               "jalebi.webp",
    "halwa":                "Halwa.jpg",
    "vanilla_icecream":     "vannila scoop.jpg",
    "chocolate_icecream":   "Chocolate Scoop.jpg",
    "mango_icecream":       "Mango Scoop.jpg",
    "strawberry_icecream":  "Strawberry Scoop.jpg",
    "butterscotch_icecream":"Butterscotch Scoop.jpg",
    "sundae":               "Ice Cream Sundae.jpg",
    "banana_shake":         "Banana Shake.jpg",
    "strawberry_shake":     "Strawberry Shake.jpg",
    "oreo_shake":           "Oreo Milkshake.jpg",
    "dryfruit_shake":       "Dry Fruit Shake.jpg",
    "watermelon_juice":     "Watermelon Juice.jpg",
    "buttermilk":           "Masala Buttermilk.jpg",
    "samosa":               "Samosa.jpg",
    "veg_puff":             "Veg Puff.jpg",
    "spring_rolls":         "spring roll.jpg",
    "garlic_naan":          "garlic-butter-naan-2.jpg",
    "dal_rice":             "Dal Rice.jpg",
    "lemon_rice":           "Lemon Rice.jpg",
    "mango_lassi":          "Mango Lassi.jpg",
}

def img(key):
    _dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", "images")
    filename = _FILE_MAP.get(key, f"{key}.jpg")
    if os.path.exists(os.path.join(_dir, filename)):
        return f"/static/images/{filename}"
    return IMG_URLS.get(key, "https://images.unsplash.com/photo-1546833999-b9f581a1996d?w=400&q=80")


MENU = {
    "breakfast": [
        {"id": 1,  "name": "Idli Sambar",         "price": 40,  "calories": 200, "category": "South Indian", "popular": True,  "emoji": "🥣", "img": img("idli_sambar")},
        {"id": 2,  "name": "Masala Dosa",          "price": 60,  "calories": 350, "category": "South Indian", "popular": True,  "emoji": "🫓", "img": img("masala_dosa")},
        {"id": 3,  "name": "Poha",                 "price": 30,  "calories": 180, "category": "Light",        "popular": False, "emoji": "🍚", "img": img("poha")},
        {"id": 4,  "name": "Upma",                 "price": 35,  "calories": 220, "category": "Light",        "popular": False, "emoji": "🍲", "img": img("upma")},
        {"id": 13, "name": "Puri Bhaji",           "price": 50,  "calories": 400, "category": "North Indian", "popular": True,  "emoji": "🫔", "img": img("puri_bhaji")},
        {"id": 14, "name": "Vada Sambar",          "price": 45,  "calories": 280, "category": "South Indian", "popular": True,  "emoji": "🍩", "img": img("vada_sambar")},
        {"id": 15, "name": "Bread Omelette",       "price": 55,  "calories": 320, "category": "Protein",      "popular": False, "emoji": "🍳", "img": img("bread_omelette")},
        {"id": 16, "name": "Filter Coffee",        "price": 25,  "calories": 80,  "category": "Beverage",     "popular": True,  "emoji": "☕", "img": img("filter_coffee")},
        {"id": 17, "name": "Masala Chai",          "price": 20,  "calories": 60,  "category": "Beverage",     "popular": True,  "emoji": "🍵", "img": img("masala_chai")},
    ],
    "lunch": [
        {"id": 5,  "name": "Veg Thali",            "price": 120, "calories": 650, "category": "Full Meal",    "popular": True,  "emoji": "🍱", "img": img("veg_thali")},
        {"id": 6,  "name": "Chicken Biryani",      "price": 180, "calories": 750, "category": "Rice",         "popular": True,  "emoji": "🍛", "img": img("chicken_biryani")},
        {"id": 7,  "name": "Paneer Butter Masala", "price": 150, "calories": 500, "category": "Curry",        "popular": False, "emoji": "🧆", "img": img("paneer_butter_masala")},
        {"id": 8,  "name": "Dal Rice",             "price": 90,  "calories": 400, "category": "Light",        "popular": False, "emoji": "🍚", "img": img("dal_rice")},
        {"id": 18, "name": "Mutton Curry",         "price": 220, "calories": 680, "category": "Curry",        "popular": True,  "emoji": "🍖", "img": img("mutton_curry")},
        {"id": 19, "name": "Fish Fry",             "price": 200, "calories": 520, "category": "Protein",      "popular": True,  "emoji": "🐟", "img": img("fish_fry")},
        {"id": 20, "name": "Veg Fried Rice",       "price": 110, "calories": 450, "category": "Rice",         "popular": False, "emoji": "🍳", "img": img("veg_fried_rice")},
        {"id": 21, "name": "Lemon Rice",           "price": 80,  "calories": 380, "category": "South Indian", "popular": False, "emoji": "🍋", "img": img("lemon_rice")},
        {"id": 22, "name": "Mango Lassi",          "price": 60,  "calories": 220, "category": "Beverage",     "popular": True,  "emoji": "🥭", "img": img("mango_lassi")},
        {"id": 23, "name": "Fresh Lime Soda",      "price": 40,  "calories": 80,  "category": "Beverage",     "popular": False, "emoji": "🍋", "img": img("lime_soda")},
    ],
    "dinner": [
        {"id": 9,  "name": "Butter Naan + Curry",  "price": 140, "calories": 550, "category": "North Indian", "popular": True,  "emoji": "🫓", "img": img("butter_naan")},
        {"id": 10, "name": "Fried Rice",           "price": 130, "calories": 480, "category": "Rice",         "popular": True,  "emoji": "🍳", "img": img("fried_rice")},
        {"id": 11, "name": "Chapati + Dal",        "price": 80,  "calories": 350, "category": "Light",        "popular": False, "emoji": "🫓", "img": img("chapati")},
        {"id": 12, "name": "Grilled Chicken",      "price": 200, "calories": 420, "category": "Protein",      "popular": False, "emoji": "🍗", "img": img("grilled_chicken")},
        {"id": 24, "name": "Tandoori Chicken",     "price": 250, "calories": 520, "category": "Protein",      "popular": True,  "emoji": "🍗", "img": img("tandoori_chicken")},
        {"id": 25, "name": "Palak Paneer",         "price": 160, "calories": 460, "category": "Curry",        "popular": True,  "emoji": "🥬", "img": img("palak_paneer")},
        {"id": 26, "name": "Garlic Naan",          "price": 40,  "calories": 200, "category": "Bread",        "popular": True,  "emoji": "🫓", "img": img("garlic_naan")},
        {"id": 27, "name": "Veg Soup",             "price": 60,  "calories": 120, "category": "Soup",         "popular": False, "emoji": "🍜", "img": img("veg_soup")},
        {"id": 28, "name": "Cold Coffee",          "price": 70,  "calories": 180, "category": "Beverage",     "popular": True,  "emoji": "☕", "img": img("cold_coffee")},
    ],
}

EXTRAS = {
    "snacks": [
        {"id": 201, "name": "Samosa (2 pcs)",      "price": 30,  "calories": 260, "category": "Snack",      "popular": True,  "emoji": "🥟", "img": img("samosa")},
        {"id": 202, "name": "Veg Puff",            "price": 25,  "calories": 200, "category": "Snack",      "popular": True,  "emoji": "🥐", "img": img("veg_puff")},
        {"id": 203, "name": "Paneer Tikka",        "price": 120, "calories": 380, "category": "Snack",      "popular": True,  "emoji": "🧆", "img": img("paneer_tikka")},
        {"id": 204, "name": "French Fries",        "price": 80,  "calories": 320, "category": "Snack",      "popular": True,  "emoji": "🍟", "img": img("french_fries")},
        {"id": 205, "name": "Onion Rings",         "price": 70,  "calories": 280, "category": "Snack",      "popular": False, "emoji": "🧅", "img": img("onion_rings")},
        {"id": 206, "name": "Spring Rolls",        "price": 90,  "calories": 300, "category": "Snack",      "popular": False, "emoji": "🌯", "img": img("spring_rolls")},
    ],
    "desserts": [
        {"id": 301, "name": "Gulab Jamun",         "price": 50,  "calories": 300, "category": "Dessert",    "popular": True,  "emoji": "🍮", "img": img("gulab_jamun")},
        {"id": 302, "name": "Chocolate Brownie",   "price": 80,  "calories": 350, "category": "Dessert",    "popular": True,  "emoji": "🍫", "img": img("brownie")},
        {"id": 303, "name": "Rasgulla",            "price": 45,  "calories": 250, "category": "Dessert",    "popular": True,  "emoji": "🍡", "img": img("rasgulla")},
        {"id": 304, "name": "Kheer",               "price": 60,  "calories": 280, "category": "Dessert",    "popular": False, "emoji": "🍚", "img": img("kheer")},
        {"id": 305, "name": "Jalebi",              "price": 40,  "calories": 300, "category": "Dessert",    "popular": True,  "emoji": "🍩", "img": img("jalebi")},
        {"id": 306, "name": "Halwa",               "price": 55,  "calories": 320, "category": "Dessert",    "popular": False, "emoji": "🍯", "img": img("halwa")},
    ],
    "ice_cream": [
        {"id": 401, "name": "Vanilla Scoop",       "price": 60,  "calories": 200, "category": "Ice Cream",  "popular": True,  "emoji": "🍦", "img": img("vanilla_icecream")},
        {"id": 402, "name": "Chocolate Scoop",     "price": 60,  "calories": 220, "category": "Ice Cream",  "popular": True,  "emoji": "🍫", "img": img("chocolate_icecream")},
        {"id": 403, "name": "Mango Scoop",         "price": 70,  "calories": 210, "category": "Ice Cream",  "popular": True,  "emoji": "🥭", "img": img("mango_icecream")},
        {"id": 404, "name": "Strawberry Scoop",    "price": 70,  "calories": 200, "category": "Ice Cream",  "popular": False, "emoji": "🍓", "img": img("strawberry_icecream")},
        {"id": 405, "name": "Butterscotch Scoop",  "price": 70,  "calories": 230, "category": "Ice Cream",  "popular": True,  "emoji": "🍨", "img": img("butterscotch_icecream")},
        {"id": 406, "name": "Ice Cream Sundae",    "price": 120, "calories": 420, "category": "Ice Cream",  "popular": True,  "emoji": "🍨", "img": img("sundae")},
    ],
    "milkshakes": [
        {"id": 501, "name": "Chocolate Milkshake", "price": 90,  "calories": 380, "category": "Milkshake",  "popular": True,  "emoji": "🥤", "img": img("choco_shake")},
        {"id": 502, "name": "Mango Milkshake",     "price": 90,  "calories": 350, "category": "Milkshake",  "popular": True,  "emoji": "🥭", "img": img("mango_shake")},
        {"id": 503, "name": "Strawberry Shake",    "price": 90,  "calories": 340, "category": "Milkshake",  "popular": False, "emoji": "🍓", "img": img("strawberry_shake")},
        {"id": 504, "name": "Oreo Milkshake",      "price": 110, "calories": 420, "category": "Milkshake",  "popular": True,  "emoji": "🍪", "img": img("oreo_shake")},
        {"id": 505, "name": "Banana Shake",        "price": 80,  "calories": 360, "category": "Milkshake",  "popular": False, "emoji": "🍌", "img": img("banana_shake")},
        {"id": 506, "name": "Dry Fruit Shake",     "price": 130, "calories": 450, "category": "Milkshake",  "popular": False, "emoji": "🥜", "img": img("dryfruit_shake")},
    ],
    "beverages": [
        {"id": 601, "name": "Fresh Orange Juice",  "price": 70,  "calories": 120, "category": "Beverage",   "popular": True,  "emoji": "🍊", "img": img("orange_juice")},
        {"id": 602, "name": "Watermelon Juice",    "price": 60,  "calories": 90,  "category": "Beverage",   "popular": True,  "emoji": "🍉", "img": img("watermelon_juice")},
        {"id": 603, "name": "Coconut Water",       "price": 50,  "calories": 60,  "category": "Beverage",   "popular": True,  "emoji": "🥥", "img": img("coconut_water")},
        {"id": 604, "name": "Masala Buttermilk",   "price": 30,  "calories": 80,  "category": "Beverage",   "popular": True,  "emoji": "🥛", "img": img("buttermilk")},
        {"id": 605, "name": "Lemonade",            "price": 40,  "calories": 70,  "category": "Beverage",   "popular": False, "emoji": "🍋", "img": img("lemonade")},
        {"id": 606, "name": "Iced Tea",            "price": 60,  "calories": 100, "category": "Beverage",   "popular": False, "emoji": "🧊", "img": img("iced_tea")},
    ],
}

def get_time_slot():
    hour = datetime.now().hour
    if 6 <= hour < 11:    return "breakfast"
    elif 11 <= hour < 16: return "lunch"
    else:                 return "dinner"

def get_suggestions(time_slot, previous_orders):
    scored = []
    for item in MENU[time_slot]:
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
    {"id": 101, "name": "Khichdi",       "price": 70,  "calories": 280, "category": "Comfort",   "popular": False, "emoji": "🍲", "img": img("khichdi")},
    {"id": 102, "name": "Tomato Soup",   "price": 60,  "calories": 120, "category": "Soup",      "popular": False, "emoji": "🍅", "img": img("tomato_soup")},
    {"id": 103, "name": "Protein Shake", "price": 90,  "calories": 200, "category": "Milkshake", "popular": False, "emoji": "💪", "img": img("choco_shake")},
    {"id": 104, "name": "Egg Bhurji",    "price": 80,  "calories": 320, "category": "Protein",   "popular": True,  "emoji": "🍳", "img": img("bread_omelette")},
    {"id": 105, "name": "Fruit Bowl",    "price": 60,  "calories": 150, "category": "Light",     "popular": False, "emoji": "🍓", "img": img("fruit_bowl")},
    {"id": 106, "name": "Green Salad",   "price": 50,  "calories": 100, "category": "Light",     "popular": False, "emoji": "🥗", "img": img("green_salad")},
]

def get_mood_suggestions(emotion):
    emotion = emotion.lower()
    info = EMOTION_MAP.get(emotion, EMOTION_MAP["neutral"])
    all_items = MOOD_FOOD + [i for items in list(MENU.values()) + list(EXTRAS.values()) for i in items]
    matched = [item for item in all_items if item["category"] in info["categories"]]
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
