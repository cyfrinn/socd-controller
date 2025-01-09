import keyboard
import tkinter as tk

keys_pressed = set()
socd_enabled = True
last_pressed_key_w_s = None
last_pressed_key_a_d = None

def handle_socd():
    global last_pressed_key_w_s, last_pressed_key_a_d
    if socd_enabled:
        if "w" in keys_pressed and "s" in keys_pressed:
            if last_pressed_key_w_s == "w":
                keyboard.release("s")
            elif last_pressed_key_w_s == "s":
                keyboard.release("w")
        elif "w" in keys_pressed:
            pass
        elif "s" in keys_pressed:
            pass

        if "a" in keys_pressed and "d" in keys_pressed:
            if last_pressed_key_a_d == "a":
                keyboard.release("d")
            elif last_pressed_key_a_d == "d":
                keyboard.release("a")
        elif "a" in keys_pressed:
            pass
        elif "d" in keys_pressed:
            pass
    else:
        pass

def on_key_press(event):
    global last_pressed_key_w_s, last_pressed_key_a_d
    key = event.name
    if key in ["w", "a", "s", "d"]:
        keys_pressed.add(key)
        if key in ["w", "s"]:
            last_pressed_key_w_s = key
        if key in ["a", "d"]:
            last_pressed_key_a_d = key
        handle_socd()

def on_key_release(event):
    key = event.name
    if key in keys_pressed:
        keys_pressed.discard(key)
    handle_socd()

def toggle_socd():
    global socd_enabled
    socd_enabled = not socd_enabled

def create_gui():
    window = tk.Tk()
    window.title("SOCD Controller")
    window.geometry("200x100")
    socd_var = tk.BooleanVar(value=socd_enabled)

    def on_checkbox_toggle():
        global socd_enabled
        socd_enabled = socd_var.get()

    checkbox = tk.Checkbutton(
        window, text="Enable SOCD", variable=socd_var, command=on_checkbox_toggle
    )
    checkbox.pack(pady=10)

    exit_button = tk.Button(window, text="Exit", command=window.quit)
    exit_button.pack(pady=10)

    window.mainloop()

keyboard.on_press(on_key_press)
keyboard.on_release(on_key_release)
create_gui()
