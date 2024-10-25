from datetime import datetime, timedelta
from pywinauto import Desktop
import random
import time
import pyautogui
import threading
from tkinter import messagebox
import tkinter as tk
import os

def validate_break_hours(new_value):
    placeholder = "Break Hours"
    if new_value == "" or new_value == placeholder:
        return True
    try:
        int(new_value)
        return True
    except ValueError:
        return False
    
def add_placeholder(entry, placeholder_text, placeholder_color='grey', active_color='black'):
    entry.insert(0, placeholder_text)
    entry.config(fg=placeholder_color)

    def on_focus_in(event):
        if entry.get() == placeholder_text:
            entry.delete(0, tk.END)
            entry.config(fg=active_color)

    def on_focus_out(event):
        if entry.get() == '':
            entry.insert(0, placeholder_text)
            entry.config(fg=placeholder_color)
    def validate_entry(event):
        if entry.get() == placeholder_text:
            return True
        return True
    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

def get_applications():
    try:
        print("Getting applications...")
        apps = Desktop(backend='uia').windows()
        app_list = [(i, app) for i, app in enumerate(apps) if app.window_text() and app.window_text() not in ["Taskbar", "Program Manager"]]
        print(f"Applications found: {[app.window_text() for _, app in app_list]}")
        return app_list
    except Exception as e:
        print(f"Error getting applications: {e}")
        return []

def simulate_keypresses(min_keys, max_keys, total_time_seconds):
    keys = ['ctrl', 'shift', 'alt', 'left', 'right']
    num_keys = random.randint(min_keys, max_keys)
    # delay_per_key = total_time_seconds / num_keys if num_keys > 0 else 0
    print(f"Simulating {num_keys} keypresses.")
    for _ in range(num_keys):
        if cancel_flag:
            print("Key press simulation cancelled.")
            return
        key = random.choice(keys)
        print(f"Pressing key: {key}")
        pyautogui.press(key)
        time.sleep(0.5)

def move_mouse_randomly():
    screen_width, screen_height = pyautogui.size()
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    print(f"Moving mouse to ({x}, {y})")
    for _ in range(5):
        pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.5))

def simulate_mouse_clicks(min_clicks, max_clicks,total_time_seconds):
    screen_width, screen_height = pyautogui.size()
    num_clicks = random.randint(min_clicks, max_clicks)
    # delay_per_click = total_time_seconds / num_clicks if num_clicks > 0 else 0
    print(f"Simulating {num_clicks} mouse clicks.")
    for _ in range(num_clicks):
        if cancel_flag:
            print("Mouse click simulation cancelled.")
            return
        print(f"Clicking at ({screen_width}, 300)")
        pyautogui.moveTo(screen_width, 300, duration=0.5)
        pyautogui.click()
        time.sleep(0.5)


def simulate_scrolls(min_scrolls, max_scrolls):
    num_scrolls = random.randint(min_scrolls, max_scrolls)
    print(f"Simulating {num_scrolls} scroll actions.")
    for _ in range(num_scrolls):
        if cancel_flag:
            print("Scroll simulation cancelled.")
            return
        scroll_amount = random.randint(-300, 300)
        print(f"Scrolling by {scroll_amount}")
        pyautogui.scroll(scroll_amount)
        time.sleep(random.uniform(0.1, 0.5))

def force_shutdown():
    os.system("shutdown /s /f /t 0")

# Cancel the running simulation
def cancel_simulation():
    global cancel_flag
    cancel_flag = True
    print('The Billing has been cancelled.')
    messagebox.showinfo("Cancelled", "The Billing has been cancelled.")

TAB_SWITCHING_KEYWORDS = ["Visual Studio Code", "Google Chrome"]

def perform_actions_on_application(app, min_keys, max_keys, min_clicks, max_clicks, min_scrolls, max_scrolls, total_time_seconds):
    try:
        app_title = app.window_text()
        print(f"Focusing on application: {app_title}")
        app.set_focus()
        time.sleep(1)

        # Check if the application title contains any of the specified keywords
        if any(keyword in app_title for keyword in TAB_SWITCHING_KEYWORDS):
            num_tabs = 2
            for _ in range(num_tabs):
                move_mouse_randomly()
                simulate_keypresses(1, 1, total_time_seconds)
                pyautogui.hotkey('ctrl', 'tab')
                time.sleep(1)
        move_mouse_randomly()
        simulate_keypresses(min_keys, max_keys, total_time_seconds)
        move_mouse_randomly()
        simulate_mouse_clicks(min_clicks, max_clicks, total_time_seconds)
        move_mouse_randomly()
        simulate_scrolls(min_scrolls, max_scrolls)

    except Exception as e:
        print(f"Error performing actions on application: {e}")
        return e

# Function to submit form and trigger automation
def submit_form(min_keys_entry, max_keys_entry, min_clicks_entry, max_clicks_entry,
                min_scrolls_entry, max_scrolls_entry, start_hour, start_minute, end_hour, end_minute,
                applications, app_vars, shutdown_var,
                break_entry_value
                ):
    try:
        global cancel_flag
        cancel_flag = False  # Reset the cancel flag

        selected_apps = [app for idx, app in applications if app_vars[idx].get() == 1]

        if not selected_apps:
            messagebox.showwarning("Warning", "Please select at least one application.")
            return
        print('\nSelected Apps:', selected_apps,end='\n')
        min_keys = int(min_keys_entry.get())
        max_keys = int(max_keys_entry.get())
        min_clicks = int(min_clicks_entry.get())
        max_clicks = int(max_clicks_entry.get())
        min_scrolls = int(min_scrolls_entry.get())
        max_scrolls = int(max_scrolls_entry.get())
                                              
        start_time_str = f"{(start_hour.get())}:{(start_minute.get())}"
        end_time_str = f"{(end_hour.get())}:{(end_minute.get())}"
        start_time = datetime.strptime(start_time_str, '%H:%M')
        end_time = datetime.strptime(end_time_str, '%H:%M')

        if break_entry_value.get():
            break_duration = int(break_entry_value.get()) * 60 *60
        else:
            break_duration = None  # No break

        if end_time <= start_time:
            messagebox.showerror("Error", "End time should be greater than start time.")
            return

        total_time_seconds = (end_time - start_time).seconds
        segment_duration = total_time_seconds / len(selected_apps)  # Time per app

        messagebox.showinfo("Submit", "Billing started!")

        def run_simulation(break_duration):
            while datetime.now().time() < start_time.time():
                time.sleep(1)

            simulation_end_time = datetime.now() + (end_time - start_time)

            for app in selected_apps:
                if cancel_flag or datetime.now() >= simulation_end_time:
                    return
                app_end_time = datetime.now() + timedelta(seconds=segment_duration)

                while datetime.now() < app_end_time and datetime.now() < simulation_end_time:
                    if cancel_flag:
                        return
                    perform_actions_on_application(app, min_keys, max_keys, min_clicks, max_clicks, min_scrolls, max_scrolls,total_time_seconds)
                    if break_duration and random.random() < 0.5:
                        break_time_seconds = random.randint(1, 90)
                        if break_time_seconds <= break_duration:
                            print(f"Taking a break of {break_time_seconds} seconds ...")
                            time.sleep(break_time_seconds)
                            break_duration -= break_time_seconds
            print('Billing Completed')
            messagebox.showinfo("Done", "Billing completed!")

            if shutdown_var.get():
                messagebox.showinfo("Done", "Your System will automatically shut down after 2 minutes")
                shutdown_timer = threading.Timer(120, force_shutdown)
                shutdown_timer.start()

            while datetime.now() > end_time and datetime.now() < datetime.now() + timedelta(seconds=120):
                if cancel_flag:
                    if shutdown_timer and shutdown_timer.is_alive():
                        shutdown_timer.cancel()
                        messagebox.showinfo("Cancelled", "Shutdown process has been cancelled.")
                    break
        # Run the simulation in a separate thread
        threading.Thread(target=run_simulation,args=(break_duration,)).start()

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")