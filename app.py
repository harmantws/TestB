import tkinter as tk
from tkinter import ttk
from helper import get_applications, add_placeholder, submit_form, cancel_simulation,validate_break_hours

cancel_flag = False
root = tk.Tk()
# root.iconbitmap('crowned-skull_39256.ico')
root.title("Auto Billing System")
root.geometry("450x800")
root.configure(bg='#1E1E1E')
vcmd = (root.register(validate_break_hours), '%S')
# Create a frame for the scrollbar
frame = tk.Frame(root, bg='#1E1E1E')
frame.pack(fill=tk.BOTH, expand=True)

# Create a canvas
canvas = tk.Canvas(frame, bg='#1E1E1E', highlightthickness=0)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a scrollbar
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame to hold the content
content_frame = tk.Frame(canvas, bg='#1E1E1E')
canvas.create_window((0, 0), window=content_frame, anchor='nw')

# Add a label for the text "Key Strokes"
keyboard_label = tk.Label(content_frame, text="Key Strokes per Minute", font=("Arial", 16, "bold"), bg='#1E1E1E', fg='#00FF00')
keyboard_label.pack(pady=10)

keyboard_frame = tk.Frame(content_frame, bg='#1E1E1E')
keyboard_frame.pack(pady=5)

min_entry_keys = tk.Entry(keyboard_frame, width=12, font=("Arial", 12))
add_placeholder(min_entry_keys, "Min")
min_entry_keys.grid(row=0, column=0, padx=10, pady=5, sticky='w')

max_entry_keys = tk.Entry(keyboard_frame, width=12, font=("Arial", 12))
add_placeholder(max_entry_keys, "Max")
max_entry_keys.grid(row=0, column=1, padx=10, pady=5, sticky='w')

# Mouse click section
mouse_label = tk.Label(content_frame, text="Mouse Clicks per Minute", font=("Arial", 16, "bold"), bg='#1E1E1E', fg='#00FF00')
mouse_label.pack(pady=10)

mouse_frame = tk.Frame(content_frame, bg='#1E1E1E')
mouse_frame.pack(pady=5)

min_entry_clicks = tk.Entry(mouse_frame, width=12, font=("Arial", 12))
add_placeholder(min_entry_clicks, "Min")
min_entry_clicks.grid(row=0, column=0, padx=10, pady=5, sticky='w')

max_entry_clicks = tk.Entry(mouse_frame, width=12, font=("Arial", 12))
add_placeholder(max_entry_clicks, "Max")
max_entry_clicks.grid(row=0, column=1, padx=10, pady=5, sticky='w')

# Scroll section
scroll_label = tk.Label(content_frame, text="Scroll Actions per Minute", font=("Arial", 16, "bold"), bg='#1E1E1E', fg='#00FF00')
scroll_label.pack(pady=10)

scroll_frame = tk.Frame(content_frame, bg='#1E1E1E')
scroll_frame.pack(pady=5)

min_entry_scrolls = tk.Entry(scroll_frame, width=12, font=("Arial", 12))
add_placeholder(min_entry_scrolls, "Min")
min_entry_scrolls.grid(row=0, column=0, padx=10, pady=5, sticky='w')

max_entry_scrolls = tk.Entry(scroll_frame, width=12, font=("Arial", 12))
add_placeholder(max_entry_scrolls, "Max")
max_entry_scrolls.grid(row=0, column=1, padx=10, pady=5, sticky='w')

# Time inputs
time_label = tk.Label(content_frame, text="Select Time", font=("Arial", 16, "bold"), bg='#1E1E1E', fg='#00FF00')
time_label.pack(pady=10)

time_frame = tk.Frame(content_frame, bg='#1E1E1E')
time_frame.pack(pady=5)
# Start Time
start_hour_label = tk.Label(time_frame, text="Start Hour:", bg='#1E1E1E', fg='white', font=("Arial", 12))
start_hour_label.grid(row=0, column=0, sticky='w')

start_hour = tk.Spinbox(time_frame, from_=0, to=23, width=5, font=("Arial", 12), format="%02.0f")
start_hour.grid(row=0, column=1, sticky='w')

start_minute_label = tk.Label(time_frame, text="Start Minute:", bg='#1E1E1E', fg='white', font=("Arial", 12))
start_minute_label.grid(row=0, column=2, sticky='w')

start_minute = tk.Spinbox(time_frame, from_=0, to=59, width=5, font=("Arial", 12), format="%02.0f")
start_minute.grid(row=0, column=3, sticky='w')

# End Time
end_hour_label = tk.Label(time_frame, text="End Hour:", bg='#1E1E1E', fg='white', font=("Arial", 12))
end_hour_label.grid(row=1, column=0, sticky='w')

end_hour = tk.Spinbox(time_frame, from_=0, to=23, width=5, font=("Arial", 12), format="%02.0f")
end_hour.grid(row=1, column=1, sticky='w')

end_minute_label = tk.Label(time_frame, text="End Minute:", bg='#1E1E1E', fg='white', font=("Arial", 12))
end_minute_label.grid(row=1, column=2, sticky='w')

end_minute = tk.Spinbox(time_frame, from_=0, to=59, width=5, font=("Arial", 12), format="%02.0f")
end_minute.grid(row=1, column=3, sticky='w')

break_label = tk.Label(content_frame, text="Want to include some break in Hours?", font=("Arial", 16, "bold"), bg='#1E1E1E', fg='#00FF00')
break_label.pack(pady=5)

break_frame = tk.Frame(content_frame, bg='#1E1E1E')
break_frame.pack(pady=5)

break_entry_value = tk.Entry(break_frame, width=12, font=("Arial", 12), validate="key", validatecommand=vcmd)
# add_placeholder(break_entry_value, "Break Hours")
break_entry_value.grid(row=0, column=1, padx=10, pady=5, sticky='w')

# Applications list
app_label = tk.Label(content_frame, text="Applications List", font=("Arial", 16, "bold"), bg='#1E1E1E', fg='#00FF00')
app_label.pack(pady=10)

applications = get_applications()
app_vars = {}
apps_frame = tk.Frame(content_frame, bg='#1E1E1E')
apps_frame.pack(pady=5)
for index, app in applications:
    var = tk.IntVar()
    app_vars[index] = var
    chk = tk.Checkbutton(apps_frame, text=app.window_text(), variable=var, bg='#1E1E1E', fg='white', selectcolor='grey', font=("Arial", 12))
    chk.pack(anchor='w')

shutdown_label = tk.Label(content_frame, text="Schedule Shutdown", font=("Arial", 16, "bold"), bg='#1E1E1E', fg='#00FF00')
shutdown_label.pack(pady=5)

shutdown_var = tk.BooleanVar()
shutdown_check = tk.Checkbutton(content_frame, text="Schedule shutdown after 2 minutes of end time", variable=shutdown_var, bg='#1E1E1E', fg='white', selectcolor='grey', font=("Arial", 12))
shutdown_check.pack()

# Submit button
submit_button = ttk.Button(content_frame, text="Start Billing",
                            command=lambda: submit_form(min_entry_keys, max_entry_keys,
                                                         min_entry_clicks, max_entry_clicks,
                                                         min_entry_scrolls, max_entry_scrolls,
                                                         start_hour, start_minute,
                                                         end_hour, end_minute,
                                                         applications, app_vars, shutdown_var,
                                                         break_entry_value
                                                         ))
submit_button.pack(pady=10)

# Cancel button
cancel_button = ttk.Button(content_frame, text="Stop Billing", command=cancel_simulation)
cancel_button.pack(pady=5)

# Update scroll region
content_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Start the main loop
root.mainloop()