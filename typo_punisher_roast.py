import time
import threading
from pynput import keyboard
from spellchecker import SpellChecker
import notify2
import random

# Initialize notifier and spellchecker
notify2.init("Typo Punisher")
spell = SpellChecker()

typed_word = ""
last_key_time = time.time()

# List of random roasts
roasts = [
    "Bro, your keyboard deserves better 😭",
    "That spelling just hurt my soul 💀",
    "Are you typing with your elbows?",
    "Spellcheck just rage quit.",
    "You invented a new word again 👏",
    "Even autocorrect gave up on you 💔",
    "Dictionaries hate you personally.",
    "That word didn’t even sound right in my brain 💢",
    "You type like you’re speedrunning typos 🏃‍♀️",
    "🔥 Congratulations! Another typo unlocked."
]

def roast_popup():
    message = random.choice(roasts)
    n = notify2.Notification("💢 Typo Detected!", message)
    n.show()

def check_word(word):
    if not word:
        return
    word = word.strip()
    if word not in spell:
        roast_popup()

def on_press(key):
    global typed_word, last_key_time

    try:
        if hasattr(key, 'char') and key.char is not None:
            typed_word += key.char
        elif key == keyboard.Key.space:
            check_word(typed_word)
            typed_word = ""
        elif key == keyboard.Key.enter:
            check_word(typed_word)
            typed_word = ""
    except Exception:
        pass

def on_release(key):
    pass

def start_listener():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    t = threading.Thread(target=start_listener, daemon=True)
    t.start()
    while True:
        time.sleep(10)



