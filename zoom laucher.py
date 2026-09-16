import time
import webbrowser

# Your specific class meeting link
CLASS_LINK = "PASTE_YOUR_ZOOM_LINK_HERE"

print("Launching your Zoom class...")
# Opens the link and prompts the Zoom app to launch automatically
webbrowser.open(CLASS_LINK)

# Keeps the window active for 3 seconds before automatically closing the script
time.sleep(3)

