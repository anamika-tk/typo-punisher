# 🔥 Typo Punisher

> “You make a typo… and it *lets you know* — brutally.” 😈  

Typo Punisher is a fun and simple Python script that detects when you make typos while typing and sends you a hilarious “roast” message right on your desktop.  
Built using `notify2` for notifications — because who doesn’t love a little sarcasm with their debugging?

---

## 🧠 What It Does

- Detects typos while you type (from logs or input)
- Sends notifications to your desktop with `notify2`
- Roasts you with random funny messages when you slip up
- Helps you type better — by bullying you (gently)

---

## ✨ Features

- 🪶 Lightweight — no complex setup required  
- 🔔 Real-time desktop notifications  
- 🎭 Random roast messages for every mistake  
- 🧰 Works across Linux distros  
- 💻 Perfect for learning, pranks, or just fun coding practice  

---

## ⚙️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/anamika-tk/typo-punisher.git
cd typo-punisher
2️⃣ Create and Activate a Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate
🪟 For Windows:

bash
Copy code
venv\Scripts\activate
📦 Install Dependencies
bash
Copy code
pip install notify2
If you get the following error:

vbnet
Copy code
ModuleNotFoundError: No module named 'dbus'
Fix it by installing the system package for your distro:

OS	Command
🐧 Arch / Manjaro	sudo pacman -S python-dbus
🧊 Ubuntu / Debian	sudo apt install python3-dbus
🧩 Fedora	sudo dnf install python3-dbus

▶️ Running the Script
Once everything is set up, run:

bash
Copy code
python typo_punisher_roast.py
You’ll start seeing desktop notifications every time the script detects a typo.
If you type fast or mess up often, expect to get roasted in style 🔥

🧠 How to Activate / Deactivate the Virtual Environment
▶️ Activate
If your environment isn’t active yet:

bash
Copy code
source venv/bin/activate
or (on Windows):

bash
Copy code
venv\Scripts\activate
Then run:

bash
Copy code
python typo_punisher_roast.py
🛑 Deactivate
To stop Typo Punisher:

Press Ctrl + C in your terminal to stop the running script.

Run:

bash
Copy code
deactivate
📂 Project Structure
bash
Copy code
typo-punisher/
│
├── typo_punisher_roast.py   # Main script that detects typos and sends roasts
├── README.md                # You’re reading it!
└── venv/                    # Virtual environment (not tracked by Git)
🪄 Example Output
💬 Typo Detected!
“You type like you’re speedrunning typos.”

💬 Oops Again!
“Did you just invent a new word? Dictionary pending approval.”

💬 Another One!
“Your keyboard is crying. Please stop.”

🧰 Troubleshooting
❌ notify2 not found?
→ Run: pip install notify2

❌ dbus module missing?
→ Install via your distro package manager (see table above).

❌ Notifications not showing?
→ Make sure your desktop notification system is enabled.
→ Try running a test:

bash
Copy code
notify-send "Test" "Notification system working!"
💡 Future Ideas
Add more roast lines and randomization

Add a GUI for settings and roast customization

Enable cross-platform support (Windows notifications)

Integrate with typing speed trackers


