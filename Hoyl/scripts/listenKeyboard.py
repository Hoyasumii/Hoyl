import keyboard

def listenKeyboard():
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            return event.name