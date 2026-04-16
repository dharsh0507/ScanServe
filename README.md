# 🍽️ QRavings — Smart AI-Powered Restaurant Menu System

> *Scan. Feel. Order. Enjoy.*

QRavings is an intelligent QR-based restaurant menu system that combines **AI food suggestions**, **emotion detection**, **voice ordering**, and **gamification** to deliver a next-generation dining experience.

---

## 🚀 Features

### 1. 🤖 AI-Based Smart Menu
- Detects time of day → shows Breakfast / Lunch / Dinner menu automatically
- Scores dishes based on **popularity** and **customer order history**
- Top 3 personalized suggestions shown on every visit

### 2. 😊 Emotion-Based Food Recommendation
- Opens front camera → detects facial expression using **face-api.js**
- Maps emotion to food category:
  | Emotion | Suggested Food |
  |---------|---------------|
  | 😄 Happy | Desserts, South Indian |
  | 😢 Sad | Comfort food, Full Meal |
  | 😠 Angry | Light food, Curry |
  | 😴 Tired | Protein, Energy food |
  | 😐 Neutral | Balanced Full Meal |
- Manual mood selection always available as fallback

### 3. 🎙️ Voice QR Menu (Tamil + English)
- Click mic → system **reads entire menu aloud** in selected language
- Supports **English** and **Tamil** (phonetic speech)
- Prices spoken in Tamil number words (நாற்பது, மூன்று நூறு...)
- Say a dish name → system finds and displays it instantly
- Uses Web Speech API (Chrome)

### 4. 🎡 Gamified Spin Wheel
- Scan QR → Spin the wheel to win offers
- Prizes: 5% OFF, 10% OFF, 20% OFF, ₹30 OFF, Free Dessert, Free Drink
- One spin per session — discount auto-applied at checkout
- Animated canvas wheel with smooth ease-out spin

### 5. 📊 Customer Analytics Dashboard
- Most ordered dishes with visual bar chart
- Orders by hour (peak time tracking)
- Total orders and total revenue summary
- Real business intelligence for restaurant owners

### 6. 🧾 Smart Billing + UPI Payment
- Add items → auto bill generated
- Spin wheel discount applied automatically
- UPI payment display at checkout
- Order history saved per session

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| Frontend | HTML, CSS, JavaScript |
| AI / ML | face-api.js (TinyFaceDetector + FaceExpressionNet) |
| Voice | Web Speech API (SpeechSynthesis + SpeechRecognition) |
| QR Code | Python `qrcode` library |
| Storage | JSON file (analytics), Flask Session |
| Deployment | Local network (WiFi) |

---

## 📁 Project Structure

```
QRavings/
├── app.py               # Flask backend — all routes
├── data.py              # Menu data, ML logic, emotion map, offers
├── requirements.txt     # Python dependencies
├── analytics.json       # Auto-generated order analytics
└── templates/
    ├── base.html        # Shared nav + layout
    ├── menu.html        # AI smart menu page
    ├── mood.html        # Emotion detection page
    ├── voice.html       # Voice ordering page
    ├── spin.html        # Spin wheel game page
    ├── cart.html        # Cart page
    ├── bill.html        # Bill + UPI payment page
    ├── dashboard.html   # Analytics dashboard
    └── qr.html          # QR code generator
```

---

## ⚙️ Installation & Setup

### Step 1 — Clone / Download the project
```bash
cd Desktop/QRavings
```

### Step 2 — Install dependencies
```bash
pip install flask qrcode pillow
```

### Step 3 — Run the app
```bash
python app.py
```

### Step 4 — Open in browser
```
http://127.0.0.1:5000
```

> ⚠️ For camera/voice features, always use **http://127.0.0.1:5000** (not the network IP).  
> Use **Google Chrome** for full voice and camera support.

---

## 📱 QR Code Usage

1. Go to `http://127.0.0.1:5000/generate_qr`
2. A QR code is generated with your **local network IP**
3. Place it on restaurant tables
4. Customers scan → menu opens on their phone instantly

> Phone and PC must be on the **same WiFi network**

---

## 🧠 ML Logic (data.py)

```python
# Time-based slot detection
6AM  - 11AM  → Breakfast
11AM - 4PM   → Lunch
4PM  - 12AM  → Dinner

# AI Scoring per item
popular item     → +2 points
previously ordered → +3 points
Top 3 scores shown as "AI Suggestions"

# Emotion → Food mapping
happy     → Dessert, South Indian
sad       → Comfort, Full Meal
tired     → Protein, Full Meal
angry     → Light, Curry
neutral   → Full Meal, Rice
```

---

## 🎯 Pages & Routes

| Route | Page | Feature |
|-------|------|---------|
| `/menu` | Smart Menu | AI suggestions + full menu |
| `/mood` | Mood Detection | Camera + manual mood → food |
| `/voice` | Voice Menu | Speak to search dishes |
| `/spin` | Spin Wheel | Win discounts |
| `/cart` | Cart | View and manage order |
| `/place_order` | Billing | Auto bill + UPI |
| `/dashboard` | Analytics | Business insights |
| `/generate_qr` | QR Generator | Table QR code |

---

## 💡 Unique Selling Points

- ✅ No waiter needed — fully self-service
- ✅ AI personalizes menu per customer
- ✅ Emotion detection — first of its kind in restaurant tech
- ✅ Tamil voice support — inclusive for all age groups
- ✅ Gamification increases customer engagement
- ✅ Real-time analytics for restaurant owners

---

## 🗣️ Viva / Presentation Line

> *"QRavings improves traditional QR menu systems by integrating emotion AI, voice accessibility, behavioral personalization, and gamification — creating a complete smart dining ecosystem that benefits both customers and restaurant owners."*

---

## 👨‍💻 Developed By

**[Your Name]**  
Department of [Your Department]  
[Your College Name]  
[Year]

---

## 📄 License

This project is built for educational purposes.
