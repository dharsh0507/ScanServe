"""
Run: python download_images.py
Downloads correct food images into static/images/
No pip install needed - uses built-in urllib only.
"""
import urllib.request, os, ssl

DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", "images")
os.makedirs(DIR, exist_ok=True)

# SSL fix for Windows
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HDR = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

# Each dish has 2 fallback URLs
IMAGES = {
    # ── BREAKFAST ──
    "idli_sambar.jpg": [
        "https://images.unsplash.com/photo-1589301760014-d929f3979dbc?w=400&q=80",
        "https://images.unsplash.com/photo-1606491956689-2ea866880c84?w=400&q=80",
    ],
    "masala_dosa.jpg": [
        "https://images.unsplash.com/photo-1567337710282-00832b415979?w=400&q=80",
        "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=400&q=80",
    ],
    "poha.jpg": [
        "https://images.unsplash.com/photo-1606491956689-2ea866880c84?w=400&q=80",
        "https://images.unsplash.com/photo-1631515243349-e0cb75fb8d3a?w=400&q=80",
    ],
    "upma.jpg": [
        "https://images.unsplash.com/photo-1631515243349-e0cb75fb8d3a?w=400&q=80",
        "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=400&q=80",
    ],
    "puri_bhaji.jpg": [
        "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=400&q=80",
        "https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=400&q=80",
    ],
    "vada_sambar.jpg": [
        "https://images.unsplash.com/photo-1610192244261-3f33de3f55e4?w=400&q=80",
        "https://images.unsplash.com/photo-1589301760014-d929f3979dbc?w=400&q=80",
    ],
    "bread_omelette.jpg": [
        "https://images.unsplash.com/photo-1482049016688-2d3e1b311543?w=400&q=80",
        "https://images.unsplash.com/photo-1525351484163-7529414344d8?w=400&q=80",
    ],
    "filter_coffee.jpg": [
        "https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=400&q=80",
        "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=400&q=80",
    ],
    "masala_chai.jpg": [
        "https://images.unsplash.com/photo-1561336313-0bd5e0b27ec8?w=400&q=80",
        "https://images.unsplash.com/photo-1571934811356-5cc061b6821f?w=400&q=80",
    ],
    # ── LUNCH ──
    "veg_thali.jpg": [
        "https://images.unsplash.com/photo-1567337710282-00832b415979?w=400&q=80",
        "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=400&q=80",
    ],
    "chicken_biryani.jpg": [
        "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=400&q=80",
        "https://images.unsplash.com/photo-1589302168068-964664d93dc0?w=400&q=80",
    ],
    "paneer_butter_masala.jpg": [
        "https://images.unsplash.com/photo-1631452180519-c014fe946bc7?w=400&q=80",
        "https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=400&q=80",
    ],
    "dal_rice.jpg": [
        "https://images.unsplash.com/photo-1546833999-b9f581a1996d?w=400&q=80",
        "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=400&q=80",
    ],
    "mutton_curry.jpg": [
        "https://images.unsplash.com/photo-1574653853027-5382a3d23a15?w=400&q=80",
        "https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=400&q=80",
    ],
    "fish_fry.jpg": [
        "https://images.unsplash.com/photo-1580476262798-bddd9f4b7369?w=400&q=80",
        "https://images.unsplash.com/photo-1519984388953-d2406bc725e1?w=400&q=80",
    ],
    "veg_fried_rice.jpg": [
        "https://images.unsplash.com/photo-1603133872878-684f208fb84b?w=400&q=80",
        "https://images.unsplash.com/photo-1512058564366-18510be2db19?w=400&q=80",
    ],
    "lemon_rice.jpg": [
        "https://images.unsplash.com/photo-1596797038530-2c107229654b?w=400&q=80",
        "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=400&q=80",
    ],
    "mango_lassi.jpg": [
        "https://images.unsplash.com/photo-1553361371-9b22f78e8b1d?w=400&q=80",
        "https://images.unsplash.com/photo-1546173159-315724a31696?w=400&q=80",
    ],
    "lime_soda.jpg": [
        "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=400&q=80",
        "https://images.unsplash.com/photo-1523677011781-c91d1bbe2f9e?w=400&q=80",
    ],
    # ── DINNER ──
    "butter_naan.jpg": [
        "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400&q=80",
        "https://images.unsplash.com/photo-1626804475297-41608ea09aeb?w=400&q=80",
    ],
    "fried_rice.jpg": [
        "https://images.unsplash.com/photo-1512058564366-18510be2db19?w=400&q=80",
        "https://images.unsplash.com/photo-1603133872878-684f208fb84b?w=400&q=80",
    ],
    "chapati.jpg": [
        "https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=400&q=80",
        "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400&q=80",
    ],
    "grilled_chicken.jpg": [
        "https://images.unsplash.com/photo-1598103442097-8b74394b95c3?w=400&q=80",
        "https://images.unsplash.com/photo-1532550907401-a500c9a57435?w=400&q=80",
    ],
    "tandoori_chicken.jpg": [
        "https://images.unsplash.com/photo-1599487488170-d11ec9c172f0?w=400&q=80",
        "https://images.unsplash.com/photo-1598103442097-8b74394b95c3?w=400&q=80",
    ],
    "palak_paneer.jpg": [
        "https://images.unsplash.com/photo-1631452180519-c014fe946bc7?w=400&q=80",
        "https://images.unsplash.com/photo-1546833999-b9f581a1996d?w=400&q=80",
    ],
    "garlic_naan.jpg": [
        "https://images.unsplash.com/photo-1626804475297-41608ea09aeb?w=400&q=80",
        "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400&q=80",
    ],
    "veg_soup.jpg": [
        "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=400&q=80",
        "https://images.unsplash.com/photo-1603105037880-880cd4edfb0d?w=400&q=80",
    ],
    "cold_coffee.jpg": [
        "https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=400&q=80",
        "https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=400&q=80",
    ],
    # ── SNACKS ──
    "samosa.jpg": [
        "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400&q=80",
        "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=400&q=80",
    ],
    "veg_puff.jpg": [
        "https://images.unsplash.com/photo-1509722747041-616f39b57569?w=400&q=80",
        "https://images.unsplash.com/photo-1558961363-fa8fdf82db35?w=400&q=80",
    ],
    "paneer_tikka.jpg": [
        "https://images.unsplash.com/photo-1567188040759-fb8a883dc6d8?w=400&q=80",
        "https://images.unsplash.com/photo-1599487488170-d11ec9c172f0?w=400&q=80",
    ],
    "french_fries.jpg": [
        "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=400&q=80",
        "https://images.unsplash.com/photo-1541592106381-b31e9677c0e5?w=400&q=80",
    ],
    "onion_rings.jpg": [
        "https://images.unsplash.com/photo-1639024471283-03518883512d?w=400&q=80",
        "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=400&q=80",
    ],
    "spring_rolls.jpg": [
        "https://images.unsplash.com/photo-1548507769-f8a5b1e3e3e3?w=400&q=80",
        "https://images.unsplash.com/photo-1563245372-f21724e3856d?w=400&q=80",
    ],
    # ── DESSERTS ──
    "gulab_jamun.jpg": [
        "https://images.unsplash.com/photo-1601303516534-bf4b7d1c5a5e?w=400&q=80",
        "https://images.unsplash.com/photo-1546833999-b9f581a1996d?w=400&q=80",
    ],
    "brownie.jpg": [
        "https://images.unsplash.com/photo-1564355808539-22fda35bed7e?w=400&q=80",
        "https://images.unsplash.com/photo-1606313564200-e75d5e30476c?w=400&q=80",
    ],
    "rasgulla.jpg": [
        "https://images.unsplash.com/photo-1666492031773-f7d3f2b5e7b1?w=400&q=80",
        "https://images.unsplash.com/photo-1601303516534-bf4b7d1c5a5e?w=400&q=80",
    ],
    "kheer.jpg": [
        "https://images.unsplash.com/photo-1571091718767-18b5b1457add?w=400&q=80",
        "https://images.unsplash.com/photo-1546833999-b9f581a1996d?w=400&q=80",
    ],
    "jalebi.jpg": [
        "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=400&q=80",
        "https://images.unsplash.com/photo-1601303516534-bf4b7d1c5a5e?w=400&q=80",
    ],
    "halwa.jpg": [
        "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=400&q=80",
        "https://images.unsplash.com/photo-1546833999-b9f581a1996d?w=400&q=80",
    ],
    # ── ICE CREAM ──
    "vanilla_icecream.jpg": [
        "https://images.unsplash.com/photo-1570197788417-0e82375c9371?w=400&q=80",
        "https://images.unsplash.com/photo-1551024506-0bccd828d307?w=400&q=80",
    ],
    "chocolate_icecream.jpg": [
        "https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=400&q=80",
        "https://images.unsplash.com/photo-1570197788417-0e82375c9371?w=400&q=80",
    ],
    "mango_icecream.jpg": [
        "https://images.unsplash.com/photo-1497034825429-c343d7c6a68f?w=400&q=80",
        "https://images.unsplash.com/photo-1570197788417-0e82375c9371?w=400&q=80",
    ],
    "strawberry_icecream.jpg": [
        "https://images.unsplash.com/photo-1488900128323-21503983a07e?w=400&q=80",
        "https://images.unsplash.com/photo-1570197788417-0e82375c9371?w=400&q=80",
    ],
    "butterscotch_icecream.jpg": [
        "https://images.unsplash.com/photo-1551024709-8f23befc6f87?w=400&q=80",
        "https://images.unsplash.com/photo-1570197788417-0e82375c9371?w=400&q=80",
    ],
    "sundae.jpg": [
        "https://images.unsplash.com/photo-1551024506-0bccd828d307?w=400&q=80",
        "https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=400&q=80",
    ],
    # ── MILKSHAKES ──
    "choco_shake.jpg": [
        "https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=400&q=80",
        "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400&q=80",
    ],
    "mango_shake.jpg": [
        "https://images.unsplash.com/photo-1546173159-315724a31696?w=400&q=80",
        "https://images.unsplash.com/photo-1553361371-9b22f78e8b1d?w=400&q=80",
    ],
    "strawberry_shake.jpg": [
        "https://images.unsplash.com/photo-1553361371-9b22f78e8b1d?w=400&q=80",
        "https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=400&q=80",
    ],
    "oreo_shake.jpg": [
        "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400&q=80",
        "https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=400&q=80",
    ],
    "banana_shake.jpg": [
        "https://images.unsplash.com/photo-1587314168485-3236d6710814?w=400&q=80",
        "https://images.unsplash.com/photo-1553361371-9b22f78e8b1d?w=400&q=80",
    ],
    "dryfruit_shake.jpg": [
        "https://images.unsplash.com/photo-1571091718767-18b5b1457add?w=400&q=80",
        "https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=400&q=80",
    ],
    # ── BEVERAGES ──
    "orange_juice.jpg": [
        "https://images.unsplash.com/photo-1621506289937-a8e4df240d0b?w=400&q=80",
        "https://images.unsplash.com/photo-1534353436294-0dbd4bdac845?w=400&q=80",
    ],
    "watermelon_juice.jpg": [
        "https://images.unsplash.com/photo-1497534446932-c925b458314e?w=400&q=80",
        "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=400&q=80",
    ],
    "coconut_water.jpg": [
        "https://images.unsplash.com/photo-1550583724-b2692b85b150?w=400&q=80",
        "https://images.unsplash.com/photo-1523677011781-c91d1bbe2f9e?w=400&q=80",
    ],
    "buttermilk.jpg": [
        "https://images.unsplash.com/photo-1553361371-9b22f78e8b1d?w=400&q=80",
        "https://images.unsplash.com/photo-1546173159-315724a31696?w=400&q=80",
    ],
    "lemonade.jpg": [
        "https://images.unsplash.com/photo-1523677011781-c91d1bbe2f9e?w=400&q=80",
        "https://images.unsplash.com/photo-1621506289937-a8e4df240d0b?w=400&q=80",
    ],
    "iced_tea.jpg": [
        "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=400&q=80",
        "https://images.unsplash.com/photo-1497534446932-c925b458314e?w=400&q=80",
    ],
    # ── MOOD FOOD ──
    "khichdi.jpg": [
        "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=400&q=80",
        "https://images.unsplash.com/photo-1546833999-b9f581a1996d?w=400&q=80",
    ],
    "tomato_soup.jpg": [
        "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=400&q=80",
        "https://images.unsplash.com/photo-1603105037880-880cd4edfb0d?w=400&q=80",
    ],
    "fruit_bowl.jpg": [
        "https://images.unsplash.com/photo-1490474418585-ba9bad8fd0ea?w=400&q=80",
        "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&q=80",
    ],
    "green_salad.jpg": [
        "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&q=80",
        "https://images.unsplash.com/photo-1490474418585-ba9bad8fd0ea?w=400&q=80",
    ],
}

ok = 0
fail = 0

def fetch(url):
    req = urllib.request.Request(url, headers=HDR)
    with urllib.request.urlopen(req, timeout=15, context=ctx) as r:
        data = r.read()
    if len(data) < 5000:
        raise ValueError("too small")
    return data

for fname, urls in IMAGES.items():
    dest = os.path.join(DIR, fname)
    if os.path.exists(dest):
        print(f"  skip  {fname}")
        ok += 1
        continue
    saved = False
    for url in urls:
        try:
            data = fetch(url)
            with open(dest, "wb") as f:
                f.write(data)
            print(f"  ok    {fname}")
            ok += 1
            saved = True
            break
        except Exception as e:
            continue
    if not saved:
        print(f"  FAIL  {fname}")
        fail += 1

print(f"\n✅ {ok} saved  |  ❌ {fail} failed")
print(f"📁 Location: {DIR}")
