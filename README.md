# 🍽️ QRavings — Smart AI-Powered Restaurant Menu System

> *Scan. Feel. Order. Enjoy.*

QRavings is an intelligent QR-based restaurant menu system built for **DD Restaurant** that combines AI food suggestions, emotion detection, voice ordering, and gamification.

---

## 🚀 Features

| Feature | Description |
|---------|-------------|
| 🤖 AI Smart Menu | Time-based menu + personalized suggestions using ML scoring |
| 😊 Mood Detection | Camera detects emotion → suggests matching food |
| 🎙️ Voice Ordering | Speak dish name → system finds and adds it |
| 🎡 Spin Wheel | Win discounts — 5% to 20% OFF, Free Dessert, Free Shake |
| 📊 Analytics | Daily dashboard with orders, revenue, peak hours |
| 🧾 Smart Billing | Auto bill + UPI payment + spin discount applied |
| 📱 QR Code | Auto-generates table QR with local network IP |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| Frontend | HTML, CSS, JavaScript, Poppins Font |
| AI / ML | face-api.js (TinyFaceDetector + FaceExpressionNet) |
| Voice | Web Speech API (SpeechSynthesis + SpeechRecognition) |
| QR Code | Python `qrcode` library |
| Storage | JSON (analytics), Flask Session |

---

## 📁 Project Structure

```
QRavings/
├── app.py                  # Flask backend — all routes
├── data.py                 # Menu data, ML logic, emotion map
├── requirements.txt        # Python dependencies
├── download_images.py      # One-time image downloader
├── static/images/          # Food photos (run download_images.py)
└── templates/
    ├── welcome.html        # Splash / landing page
    ├── base.html           # Shared layout + animations
    ├── menu.html           # AI smart menu with category tabs
    ├── mood.html           # Emotion detection page
    ├── voice.html          # Voice ordering page
    ├── spin.html           # Spin wheel game
    ├── cart.html           # Cart page
    ├── bill.html           # Bill + UPI payment
    ├── dashboard.html      # Daily analytics dashboard
    └── qr.html             # QR code generator
```

---

## ⚙️ Setup

```bash
# 1. Install dependencies
pip install flask qrcode pillow

# 2. Download food images (one time)
python download_images.py

# 3. Run the app
python app.py

# 4. Open in browser
# http://127.0.0.1:5000
```

> Use **Google Chrome** for voice and camera features.  
> Camera works only on `http://127.0.0.1:5000` (not network IP).

---

## 🎯 Routes

| Route | Page |
|-------|------|
| `/` | Welcome — DD Restaurant |
| `/menu` | AI Smart Menu |
| `/mood` | Mood Detection |
| `/voice` | Voice Ordering |
| `/spin` | Spin Wheel |
| `/cart` | Cart |
| `/place_order` | Billing |
| `/dashboard` | Analytics |
| `/generate_qr` | QR Generator |

---

## 🗣️ Viva Line

> *"QRavings transforms traditional QR menus by integrating emotion AI, voice accessibility, behavioral personalization, and gamification — creating a complete smart dining ecosystem for DD Restaurant."*

---

**Developed by DHARSHINI — Department of IT**
