import os

folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", "images")

if not os.path.exists(folder):
    print("❌ static/images folder does not exist!")
else:
    files = os.listdir(folder)
    if not files:
        print("❌ static/images folder is EMPTY!")
    else:
        print(f"✅ Found {len(files)} files in static/images:\n")
        for f in sorted(files):
            print(f"  {f}")
