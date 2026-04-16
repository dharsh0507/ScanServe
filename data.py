from datetime import datetime

MENU = {
    "breakfast": [
        {"id": 1, "name": "Idli Sambar", "price": 40, "calories": 200, "category": "South Indian", "popular": True},
        {"id": 2, "name": "Masala Dosa", "price": 60, "calories": 350, "category": "South Indian", "popular": True},
        {"id": 3, "name": "Poha", "price": 30, "calories": 180, "category": "Light", "popular": False},
        {"id": 4, "name": "Upma", "price": 35, "calories": 220, "category": "Light", "popular": False},
    ],
    "lunch": [
        {"id": 5, "name": "Veg Thali", "price": 120, "calories": 650, "category": "Full Meal", "popular": True},
        {"id": 6, "name": "Chicken Biryani", "price": 180, "calories": 750, "category": "Rice", "popular": True},
        {"id": 7, "name": "Paneer Butter Masala", "price": 150, "calories": 500, "category": "Curry", "popular": False},
        {"id": 8, "name": "Dal Rice", "price": 90, "calories": 400, "category": "Light", "popular": False},
    ],
    "dinner": [
        {"id": 9,  "name": "Butter Naan + Curry", "price": 140, "calories": 550, "category": "North Indian", "popular": True},
        {"id": 10, "name": "Fried Rice", "price": 130, "calories": 480, "category": "Rice", "popular": True},
        {"id": 11, "name": "Chapati + Dal", "price": 80, "calories": 350, "category": "Light", "popular": False},
        {"id": 12, "name": "Grilled Chicken", "price": 200, "calories": 420, "category": "Protein", "popular": False},
    ],
}

def get_time_slot():
    hour = datetime.now().hour
    if 6 <= hour < 11:
        return "breakfast"
    elif 11 <= hour < 16:
        return "lunch"
    else:
        return "dinner"

def get_suggestions(time_slot, previous_orders: list):
    items = MENU[time_slot]
    # Score: popular = +2, previously ordered = +3
    scored = []
    for item in items:
        score = 0
        if item["popular"]:
            score += 2
        if item["name"] in previous_orders:
            score += 3
        scored.append((score, item))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [item for _, item in scored[:3]]

def get_all_items():
    all_items = []
    for items in MENU.values():
        all_items.extend(items)
    return all_items

def get_item_by_id(item_id):
    for items in MENU.values():
        for item in items:
            if item["id"] == item_id:
                return item
    return None

# Emotion → food category mapping
EMOTION_MAP = {
    "happy":     {"categories": ["Dessert", "South Indian"], "emoji": "😄", "reason": "Celebrate with something sweet!"},
    "sad":       {"categories": ["Comfort", "Full Meal"],    "emoji": "😢", "reason": "Comfort food to lift your mood!"},
    "angry":     {"categories": ["Light", "Curry"],          "emoji": "😠", "reason": "Cool down with some light food!"},
    "surprised": {"categories": ["Rice", "North Indian"],    "emoji": "😲", "reason": "Try something exciting!"},
    "fearful":   {"categories": ["Comfort", "Light"],        "emoji": "😨", "reason": "Soothing food to calm you down!"},
    "disgusted": {"categories": ["Light", "South Indian"],   "emoji": "🤢", "reason": "Simple and easy on the stomach!"},
    "neutral":   {"categories": ["Full Meal", "Rice"],       "emoji": "😐", "reason": "A balanced meal for you!"},
    "tired":     {"categories": ["Protein", "Full Meal"],    "emoji": "😴", "reason": "Energy-boosting food to recharge!"},
}

MOOD_FOOD = [
    {"id": 101, "name": "Gulab Jamun",       "price": 50,  "calories": 300, "category": "Dessert",     "popular": True},
    {"id": 102, "name": "Chocolate Brownie", "price": 80,  "calories": 350, "category": "Dessert",     "popular": True},
    {"id": 103, "name": "Khichdi",           "price": 70,  "calories": 280, "category": "Comfort",     "popular": False},
    {"id": 104, "name": "Tomato Soup",       "price": 60,  "calories": 120, "category": "Comfort",     "popular": False},
    {"id": 105, "name": "Protein Shake",     "price": 90,  "calories": 200, "category": "Protein",     "popular": False},
    {"id": 106, "name": "Egg Bhurji",        "price": 80,  "calories": 320, "category": "Protein",     "popular": True},
    {"id": 107, "name": "Fruit Bowl",        "price": 60,  "calories": 150, "category": "Light",       "popular": False},
    {"id": 108, "name": "Green Salad",       "price": 50,  "calories": 100, "category": "Light",       "popular": False},
]

def get_mood_suggestions(emotion):
    emotion = emotion.lower()
    info = EMOTION_MAP.get(emotion, EMOTION_MAP["neutral"])
    target_cats = info["categories"]
    all_items = MOOD_FOOD + [i for items in MENU.values() for i in items]
    matched = [item for item in all_items if item["category"] in target_cats]
    return matched[:4], info

# Spin wheel offers
OFFERS = [
    {"id": 1, "label": "10% OFF",        "discount": 10,  "type": "percent", "color": "#e65c00"},
    {"id": 2, "label": "Free Dessert",   "discount": 0,   "type": "item",    "color": "#f7a800", "item": "Gulab Jamun"},
    {"id": 3, "label": "20% OFF",        "discount": 20,  "type": "percent", "color": "#e65c00"},
    {"id": 4, "label": "₹30 OFF",        "discount": 30,  "type": "flat",    "color": "#f7a800"},
    {"id": 5, "label": "Better Luck!",   "discount": 0,   "type": "none",    "color": "#ccc"},
    {"id": 6, "label": "5% OFF",         "discount": 5,   "type": "percent", "color": "#e65c00"},
    {"id": 7, "label": "Free Drink",     "discount": 0,   "type": "item",    "color": "#f7a800", "item": "Tomato Soup"},
    {"id": 8, "label": "15% OFF",        "discount": 15,  "type": "percent", "color": "#e65c00"},
]

def apply_offer(offer, total):
    if offer["type"] == "percent":
        return round(total * offer["discount"] / 100)
    elif offer["type"] == "flat":
        return min(offer["discount"], total)
    return 0

# Voice search
def search_items(query):
    query = query.lower()
    all_items = [i for items in MENU.values() for i in items] + MOOD_FOOD
    return [item for item in all_items if query in item["name"].lower() or query in item["category"].lower()]
