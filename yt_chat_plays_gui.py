#yt_chat_plays_gui.py
import sys, pytchat, pydirectinput

all_inputs = []

def start(keys: dict, chat):
    while chat.is_alive():
        for c in chat.get().sync_items():
            message = c.message.lower()
            if message in keys:
                all_inputs.append(message)
                pydirectinput.press(keys[message])
                print(message)

def stop(filename):
    if len(filename) > 0:
        try:
            with open(f'{filename}.txt', 'w') as f:
                for line in all_inputs:
                    f.write(f"{line}\n")
        except:
            pass
        
    sys.exit()