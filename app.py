from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from data import get_time_slot, get_suggestions, get_all_items, get_item_by_id, MENU, get_mood_suggestions, MOOD_FOOD, OFFERS, apply_offer, search_items
from datetime import datetime
import json, os

app = Flask(__name__)
app.secret_key = "qr_menu_secret"

ANALYTICS_FILE = "analytics.json"

def load_analytics():
    if os.path.exists(ANALYTICS_FILE):
        with open(ANALYTICS_FILE) as f:
            return json.load(f)
    return {"orders": [], "item_counts": {}, "hourly": {}}

def save_analytics(data):
    with open(ANALYTICS_FILE, "w") as f:
        json.dump(data, f)

@app.route("/")
def index():
    return redirect(url_for("menu"))

@app.route("/menu")
def menu():
    time_slot = get_time_slot()
    previous = session.get("previous_orders", [])
    suggestions = get_suggestions(time_slot, previous)
    all_items = MENU[time_slot]
    cart = session.get("cart", [])
    return render_template("menu.html",
        suggestions=suggestions,
        all_items=all_items,
        time_slot=time_slot,
        cart=cart,
        cart_count=len(cart)
    )

@app.route("/add_to_cart/<int:item_id>")
def add_to_cart(item_id):
    item = get_item_by_id(item_id)
    if item:
        cart = session.get("cart", [])
        cart.append(item)
        session["cart"] = cart
    return redirect(url_for("menu"))

@app.route("/cart")
def cart():
    cart = session.get("cart", [])
    total = sum(i["price"] for i in cart)
    return render_template("cart.html", cart=cart, total=total)

@app.route("/place_order", methods=["POST"])
def place_order():
    cart = session.get("cart", [])
    if not cart:
        return redirect(url_for("menu"))

    analytics = load_analytics()
    hour = str(datetime.now().hour)
    order_record = {
        "items": [i["name"] for i in cart],
        "total": sum(i["price"] for i in cart),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    analytics["orders"].append(order_record)
    for item in cart:
        analytics["item_counts"][item["name"]] = analytics["item_counts"].get(item["name"], 0) + 1
    analytics["hourly"][hour] = analytics["hourly"].get(hour, 0) + 1
    save_analytics(analytics)

    # Save to session history
    prev = session.get("previous_orders", [])
    prev.extend([i["name"] for i in cart])
    session["previous_orders"] = prev[-10:]  # keep last 10

    total = sum(i["price"] for i in cart)
    offer = session.get("offer", None)
    discount = apply_offer(offer, total) if offer else 0
    final_total = total - discount
    session["cart"] = []
    session["spun"] = False
    session["offer"] = None
    return render_template("bill.html", cart=cart, total=total, discount=discount, final_total=final_total, offer=offer, order_time=order_record["time"])

@app.route("/dashboard")
def dashboard():
    analytics = load_analytics()
    item_counts = sorted(analytics["item_counts"].items(), key=lambda x: x[1], reverse=True)
    hourly = sorted(analytics["hourly"].items(), key=lambda x: int(x[0]))
    total_orders = len(analytics["orders"])
    total_revenue = sum(o["total"] for o in analytics["orders"])
    return render_template("dashboard.html",
        item_counts=item_counts,
        hourly=hourly,
        total_orders=total_orders,
        total_revenue=total_revenue
    )

@app.route("/mood")
def mood():
    return render_template("mood.html")

@app.route("/mood_result", methods=["POST"])
def mood_result():
    emotion = request.json.get("emotion", "neutral")
    session["mood"] = emotion
    suggestions, info = get_mood_suggestions(emotion)
    return jsonify({"suggestions": suggestions, "info": info})

@app.route("/add_mood_item/<int:item_id>")
def add_mood_item(item_id):
    # Check MOOD_FOOD first, then regular menu
    item = next((i for i in MOOD_FOOD if i["id"] == item_id), None) or get_item_by_id(item_id)
    if item:
        cart = session.get("cart", [])
        cart.append(item)
        session["cart"] = cart
    return redirect(url_for("mood"))

@app.route("/spin")
def spin():
    already_spun = session.get("spun", False)
    offer = session.get("offer", None)
    return render_template("spin.html", offers=OFFERS, already_spun=already_spun, offer=offer)

@app.route("/spin_result", methods=["POST"])
def spin_result():
    if session.get("spun"):
        return jsonify({"error": "Already spun"}), 400
    idx = request.json.get("index", 0)
    offer = OFFERS[idx % len(OFFERS)]
    session["spun"] = True
    session["offer"] = offer
    return jsonify(offer)

@app.route("/voice")
def voice():
    return render_template("voice.html", menu=MENU)

@app.route("/voice_search")
def voice_search():
    query = request.args.get("q", "")
    results = search_items(query)
    return jsonify(results)

@app.route("/generate_qr")
def generate_qr():
    import qrcode, io, base64, socket
    # Get local network IP so phones on same WiFi can scan and open
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
    except Exception:
        local_ip = "127.0.0.1"
    port = request.host.split(":")[1] if ":" in request.host else "5000"
    url = f"http://{local_ip}:{port}/menu"
    img = qrcode.make(url)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    qr_b64 = base64.b64encode(buf.getvalue()).decode()
    return render_template("qr.html", qr_b64=qr_b64, url=url)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)