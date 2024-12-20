from pynput import keyboard


listening = False
handlers = {}

def on_press(key):
    try:
        key = key.char
    except AttributeError:
        key = str(key)
    if key in handlers:
        for handler in handlers[key]:
            handler()

listener = keyboard.Listener(on_press=on_press)

def add_handler(key, callback):
    if key not in handlers:
        handlers[key] = []
    handlers[key].append(callback)
    global listening
    if not listening:
        listener.start()
        listening = True

# Controller
controller = keyboard.Controller()