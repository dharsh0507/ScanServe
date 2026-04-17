"""
Run once: python download_images.py
Downloads food images from Unsplash (free, no API key needed) into static/images/
"""
import urllib.request, os, time

os.makedirs("static/images", exist_ok=True)

# All free Unsplash images - direct download links
IMAGES = {
    "idli_sambar.jpg":          "https://images.unsplash.com/photo-1589301760014-d929f3979dbc?w=400&q=80",
    "masala_dosa.jpg":          "https://images.unsplash.com/photo-1630383249896-424e482df921?w=400&q=80",
    "poha.jpg":                 "https://images.unsplash.com/photo-1606491956689-2ea866880c84?w=400&q=80",
    "upma.jpg":                 "https://images.unsplash.com/photo-1567188040759-fb8a883dc6d8?w=400&q=80",
    "puri_bhaji.jpg":           "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400&q=80",
    "vada_sambar.jpg":          "https://images.unsplash.com/photo-1610192244261-3f33de3f55e4?w=400&q=80",
    "bread_omelette.jpg":       "https://images.unsplash.com/photo-1525351484163-7529414344d8?w=400&q=80",
    "filter_coffee.jpg":        "https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=400&q=80",
    "masala_chai.jpg":          "https://images.unsplash.com/photo-1561336313-0bd5e0b27ec8?w=400&q=80",
    "veg_thali.jpg":            "https://images.unsplash.com/photo-1546833999-b9f581a1996d?w=400&q=80",
    "chicken_biryani.jpg":      "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=400&q=80",
    "paneer_butter_masala.jpg": "https://images.unsplash.com/photo-1631452180519-c014fe946bc7?w=400&q=80",
    "dal_rice.jpg":             "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=400&q=80",
    "mutton_curry.jpg":         "https://images.unsplash.com/photo-1574653853027-5382a3d23a15?w=400&q=80",
    "fish_fry.jpg":             "https://images.unsplash.com/photo-1519984388953-d2406bc725e1?w=400&q=80",
    "veg_fried_rice.jpg":       "https://images.unsplash.com/photo-1603133872878-684f208fb84b?w=400&q=80",
    "lemon_rice.jpg":           "https://images.unsplash.com/photo-1596797038530-2c107229654b?w=400&q=80",
    "mango_lassi.jpg":          "https://images.unsplash.com/photo-1571091718767-18b5b1457add?w=400&q=80",
    "lime_soda.jpg":            "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=400&q=80",
    "butter_naan.jpg":          "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400&q=80",
    "fried_rice.jpg":           "https://images.unsplash.com/photo-1603133872878-684f208fb84b?w=400&q=80",
    "chapati.jpg":              "https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=400&q=80",
    "grilled_chicken.jpg":      "https://images.unsplash.com/photo-1598103442097-8b74394b95c3?w=400&q=80",
    "tandoori_chicken.jpg":     "https://images.unsplash.com/photo-1599487488170-d11ec9c172f0?w=400&q=80",
    "palak_paneer.jpg":         "https://images.unsplash.com/photo-1645177628172-a94c1f96e6db?w=400&q=80",
    "garlic_naan.jpg":          "https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=400&q=80",
    "veg_soup.jpg":             "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=400&q=80",
    "cold_coffee.jpg":          "https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=400&q=80",
    "samosa.jpg":               "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400&q=80",
    "veg_puff.jpg":             "https://images.unsplash.com/photo-1558961363-fa8fdf82db35?w=400&q=80",
    "paneer_tikka.jpg":         "https://images.unsplash.com/photo-1567188040759-fb8a883dc6d8?w=400&q=80",
    "french_fries.jpg":         "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=400&q=80",
    "onion_rings.jpg":          "https://images.unsplash.com/photo-1639024471283-03518883512d?w=400&q=80",
    "spring_rolls.jpg":         "https://images.unsplash.com/photo-1548507769-f8a5b2b8b8b8?w=400&q=80",
    "gulab_jamun.jpg":          "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400&q=80",
    "brownie.jpg":              "https://images.unsplash.com/photo-1564355808539-22fda35bed7e?w=400&q=80",
    "rasgulla.jpg":             "https://images.unsplash.com/photo-1606491956689-2ea866880c84?w=400&q=80",
    "kheer.jpg":                "https://images.unsplash.com/photo-1571091718767-18b5b1457add?w=400&q=80",
    "jalebi.jpg":               "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400&q=80",
    "halwa.jpg":                "https://images.unsplash.com/photo-1567188040759-fb8a883dc6d8?w=400&q=80",
    "vanilla_icecream.jpg":     "https://images.unsplash.com/photo-1570197788417-0e82375c9371?w=400&q=80",
    "chocolate_icecream.jpg":   "https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=400&q=80",
    "mango_icecream.jpg":       "https://images.unsplash.com/photo-1497034825429-c343d7c6a68f?w=400&q=80",
    "strawberry_icecream.jpg":  "https://images.unsplash.com/photo-1488900128323-21503983a07e?w=400&q=80",
    "butterscotch_icecream.jpg":"https://images.unsplash.com/photo-1551024709-8f23befc6f87?w=400&q=80",
    "sundae.jpg":               "https://images.unsplash.com/photo-1534790566855-4cb788d389ec?w=400&q=80",
    "choco_shake.jpg":          "https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=400&q=80",
    "mango_shake.jpg":          "https://images.unsplash.com/photo-1546173159-315724a31696?w=400&q=80",
    "strawberry_shake.jpg":     "https://images.unsplash.com/photo-1553361371-9b22f78e8b1d?w=400&q=80",
    "oreo_shake.jpg":           "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400&q=80",
    "banana_shake.jpg":         "https://images.unsplash.com/photo-1553361371-9b22f78e8b1d?w=400&q=80",
    "dryfruit_shake.jpg":       "https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=400&q=80",
    "orange_juice.jpg":         "https://images.unsplash.com/photo-1621506289937-a8e4df240d0b?w=400&q=80",
    "watermelon_juice.jpg":     "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=400&q=80",
    "coconut_water.jpg":        "https://images.unsplash.com/photo-1550583724-b2692b85b150?w=400&q=80",
    "buttermilk.jpg":           "https://images.unsplash.com/photo-1571091718767-18b5b1457add?w=400&q=80",
    "lemonade.jpg":             "https://images.unsplash.com/photo-1621263764928-df1444c5e859?w=400&q=80",
    "iced_tea.jpg":             "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=400&q=80",
    "khichdi.jpg":              "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=400&q=80",
    "tomato_soup.jpg":          "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=400&q=80",
    "fruit_bowl.jpg":           "https://images.unsplash.com/photo-1490474418585-ba9bad8fd0ea?w=400&q=80",
    "green_salad.jpg":          "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&q=80",
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
}

ok = fail = 0
total = len(IMAGES)

for i, (fname, url) in enumerate(IMAGES.items(), 1):
    path = f"static/images/{fname}"
    if os.path.exists(path) and os.path.getsize(path) > 1000:
        print(f"[{i}/{total}] skip  {fname}")
        ok += 1
        continue
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as r, open(path, "wb") as f:
            data = r.read()
            f.write(data)
        print(f"[{i}/{total}] ok    {fname}  ({len(data)//1024}KB)")
        ok += 1
        time.sleep(0.3)   # polite delay
    except Exception as e:
        print(f"[{i}/{total}] FAIL  {fname}  ({e})")
        fail += 1
        time.sleep(0.5)

print(f"\nDone: {ok} ok, {fail} failed.")
if fail:
    print("Failed items will show emoji fallback — that's fine!")
