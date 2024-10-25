# from PyQt5 import QtWidgets, QtCore
# from datetime import datetime, timedelta
# from pywinauto import Desktop
# import random
# import time
# import pyautogui
# import threading
# import os

# class App(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#         self.cancel_flag = False

#     def initUI(self):
#         layout = QtWidgets.QVBoxLayout()

#         self.break_entry = QtWidgets.QLineEdit()
#         self.break_entry.setPlaceholderText("Break Hours")
#         self.break_entry.setStyleSheet("color: grey;")
#         self.break_entry.textChanged.connect(self.validate_break_hours)

#         layout.addWidget(self.break_entry)

#         # Create input fields for min_keys, max_keys, min_clicks, max_clicks, min_scrolls, max_scrolls
#         self.min_keys_entry = QtWidgets.QLineEdit(self)
#         self.max_keys_entry = QtWidgets.QLineEdit(self)
#         self.min_clicks_entry = QtWidgets.QLineEdit(self)
#         self.max_clicks_entry = QtWidgets.QLineEdit(self)
#         self.min_scrolls_entry = QtWidgets.QLineEdit(self)
#         self.max_scrolls_entry = QtWidgets.QLineEdit(self)

#         layout.addWidget(QtWidgets.QLabel("Min Keys:"))
#         layout.addWidget(self.min_keys_entry)
#         layout.addWidget(QtWidgets.QLabel("Max Keys:"))
#         layout.addWidget(self.max_keys_entry)
#         layout.addWidget(QtWidgets.QLabel("Min Clicks:"))
#         layout.addWidget(self.min_clicks_entry)
#         layout.addWidget(QtWidgets.QLabel("Max Clicks:"))
#         layout.addWidget(self.max_clicks_entry)
#         layout.addWidget(QtWidgets.QLabel("Min Scrolls:"))
#         layout.addWidget(self.min_scrolls_entry)
#         layout.addWidget(QtWidgets.QLabel("Max Scrolls:"))
#         layout.addWidget(self.max_scrolls_entry)

#         # Start and end time inputs
#         self.start_hour = QtWidgets.QSpinBox(self)
#         self.start_minute = QtWidgets.QSpinBox(self)
#         self.end_hour = QtWidgets.QSpinBox(self)
#         self.end_minute = QtWidgets.QSpinBox(self)
        
#         layout.addWidget(QtWidgets.QLabel("Start Hour:"))
#         layout.addWidget(self.start_hour)
#         layout.addWidget(QtWidgets.QLabel("Start Minute:"))
#         layout.addWidget(self.start_minute)
#         layout.addWidget(QtWidgets.QLabel("End Hour:"))
#         layout.addWidget(self.end_hour)
#         layout.addWidget(QtWidgets.QLabel("End Minute:"))
#         layout.addWidget(self.end_minute)

#         # Application selection
#         self.applications = self.get_applications()
#         self.app_vars = [QtWidgets.QCheckBox(app.window_text()) for _, app in self.applications]
#         for var in self.app_vars:
#             layout.addWidget(var)

#         # Shutdown checkbox
#         self.shutdown_var = QtWidgets.QCheckBox("Shutdown after completion")
#         layout.addWidget(self.shutdown_var)

#         # Submit button
#         self.submit_button = QtWidgets.QPushButton("Start Billing")
#         self.submit_button.clicked.connect(self.submit_form)
#         layout.addWidget(self.submit_button)

#         self.setLayout(layout)
#         self.setWindowTitle('Automation Tool')
#         self.show()

#     def validate_break_hours(self):
#         new_value = self.break_entry.text()
#         if new_value == "" or new_value == "Break Hours":
#             self.break_entry.setStyleSheet("color: grey;")
#         else:
#             self.break_entry.setStyleSheet("color: black;")
        
#         try:
#             int(new_value)
#         except ValueError:
#             pass

#     def get_applications(self):
#         try:
#             print("Getting applications...")
#             apps = Desktop(backend='uia').windows()
#             app_list = [(i, app) for i, app in enumerate(apps) if app.window_text() and app.window_text() not in ["Taskbar", "Program Manager"]]
#             print(f"Applications found: {[app.window_text() for _, app in app_list]}")
#             return app_list
#         except Exception as e:
#             print(f"Error getting applications: {e}")
#             return []

#     def simulate_keypresses(self, min_keys, max_keys, total_time_seconds):
#         keys = ['ctrl', 'shift', 'alt', 'left', 'right']
#         num_keys = random.randint(min_keys, max_keys)
#         print(f"Simulating {num_keys} keypresses.")
#         for _ in range(num_keys):
#             if self.cancel_flag:
#                 print("Key press simulation cancelled.")
#                 return
#             key = random.choice(keys)
#             print(f"Pressing key: {key}")
#             pyautogui.press(key)
#             time.sleep(0.5)

#     def move_mouse_randomly(self):
#         screen_width, screen_height = pyautogui.size()
#         x = random.randint(0, screen_width)
#         y = random.randint(0, screen_height)
#         print(f"Moving mouse to ({x}, {y})")
#         for _ in range(5):
#             pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.5))

#     def simulate_mouse_clicks(self, min_clicks, max_clicks, total_time_seconds):
#         screen_width, screen_height = pyautogui.size()
#         num_clicks = random.randint(min_clicks, max_clicks)
#         print(f"Simulating {num_clicks} mouse clicks.")
#         for _ in range(num_clicks):
#             if self.cancel_flag:
#                 print("Mouse click simulation cancelled.")
#                 return
#             print(f"Clicking at ({screen_width}, 300)")
#             pyautogui.moveTo(screen_width, 300, duration=0.5)
#             pyautogui.click()
#             time.sleep(0.5)

#     def simulate_scrolls(self, min_scrolls, max_scrolls):
#         num_scrolls = random.randint(min_scrolls, max_scrolls)
#         print(f"Simulating {num_scrolls} scroll actions.")
#         for _ in range(num_scrolls):
#             if self.cancel_flag:
#                 print("Scroll simulation cancelled.")
#                 return
#             scroll_amount = random.randint(-300, 300)
#             print(f"Scrolling by {scroll_amount}")
#             pyautogui.scroll(scroll_amount)
#             time.sleep(random.uniform(0.1, 0.5))

#     def force_shutdown(self):
#         os.system("shutdown /s /f /t 0")

#     def cancel_simulation(self):
#         self.cancel_flag = True
#         print('The Billing has been cancelled.')
#         QtWidgets.QMessageBox.information(self, "Cancelled", "The Billing has been cancelled.")

#     def perform_actions_on_application(self, app, min_keys, max_keys, min_clicks, max_clicks, min_scrolls, max_scrolls, total_time_seconds):
#         try:
#             app_title = app.window_text()
#             print(f"Focusing on application: {app_title}")
#             app.set_focus()
#             time.sleep(1)

#             # Simulate actions
#             self.move_mouse_randomly()
#             self.simulate_keypresses(min_keys, max_keys, total_time_seconds)
#             self.move_mouse_randomly()
#             self.simulate_mouse_clicks(min_clicks, max_clicks, total_time_seconds)
#             self.move_mouse_randomly()
#             self.simulate_scrolls(min_scrolls, max_scrolls)

#         except Exception as e:
#             print(f"Error performing actions on application: {e}")

#     def submit_form(self):
#         try:
#             self.cancel_flag = False  # Reset the cancel flag

#             selected_apps = [app for idx, app in self.applications if self.app_vars[idx].isChecked()]

#             if not selected_apps:
#                 QtWidgets.QMessageBox.warning(self, "Warning", "Please select at least one application.")
#                 return
#             print('\nSelected Apps:', selected_apps)

#             min_keys = int(self.min_keys_entry.text())
#             max_keys = int(self.max_keys_entry.text())
#             min_clicks = int(self.min_clicks_entry.text())
#             max_clicks = int(self.max_clicks_entry.text())
#             min_scrolls = int(self.min_scrolls_entry.text())
#             max_scrolls = int(self.max_scrolls_entry.text())

#             start_time_str = f"{self.start_hour.value()}:{self.start_minute.value()}"
#             end_time_str = f"{self.end_hour.value()}:{self.end_minute.value()}"
#             start_time = datetime.strptime(start_time_str, '%H:%M')
#             end_time = datetime.strptime(end_time_str, '%H:%M')

#             if self.break_entry.text():
#                 break_duration = int(self.break_entry.text()) * 60 * 60
#             else:
#                 break_duration = None  # No break

#             if end_time <= start_time:
#                 QtWidgets.QMessageBox.critical(self, "Error", "End time should be greater than start time.")
#                 return

#             total_time_seconds = (end_time - start_time).seconds
#             segment_duration = total_time_seconds / len(selected_apps)  # Time per app

#             QtWidgets.QMessageBox.information(self, "Submit", "Billing started!")

#             def run_simulation(break_duration):
#                 while datetime.now().time() < start_time.time():
#                     time.sleep(1)

#                 simulation_end_time = datetime.now() + (end_time - start_time)

#                 for app in selected_apps:
#                     if self.cancel_flag or datetime.now() >= simulation_end_time:
#                         break

#                     self.perform_actions_on_application(app, min_keys, max_keys, min_clicks, max_clicks, min_scrolls, max_scrolls, segment_duration)

#                     # If there is a break duration, wait for it
#                     if break_duration:
#                         print(f"Taking a break for {break_duration // 60} minutes.")
#                         time.sleep(break_duration)

#                 if self.shutdown_var.isChecked():
#                     self.force_shutdown()

#             simulation_thread = threading.Thread(target=run_simulation, args=(break_duration,))
#             simulation_thread.start()

#         except ValueError as e:
#             QtWidgets.QMessageBox.critical(self, "Error", f"Invalid input: {e}")

# if __name__ == '__main__':
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     ex = App()
#     sys.exit(app.exec_())


# from PyQt5 import QtWidgets, QtCore
# from datetime import datetime, timedelta
# from pywinauto import Desktop
# import random
# import time
# import pyautogui
# import threading
# import os

# class App(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#         self.cancel_flag = False

#     def initUI(self):
#         # Create a scroll area
#         self.scroll_area = QtWidgets.QScrollArea(self)
#         self.scroll_area.setWidgetResizable(True)

#         # Create a widget to contain the layout
#         self.scroll_widget = QtWidgets.QWidget()
#         self.scroll_area.setWidget(self.scroll_widget)

#         # Create a grid layout
#         layout = QtWidgets.QGridLayout(self.scroll_widget)

#         # Headings
#         layout.addWidget(QtWidgets.QLabel("<h2>Billing Automation Tool</h2>"), 0, 0, 1, 2)
#         layout.addWidget(QtWidgets.QLabel("<h3>Input Parameters</h3>"), 1, 0, 1, 2)

#         # Break hours entry
#         self.break_entry = QtWidgets.QLineEdit(self)
#         self.break_entry.setPlaceholderText("Enter break duration in hours")
#         self.break_entry.setStyleSheet("color: grey;")
#         self.break_entry.textChanged.connect(self.validate_break_hours)
#         layout.addWidget(QtWidgets.QLabel("Break Hours:"), 2, 0)
#         layout.addWidget(self.break_entry, 2, 1)

#         # Input fields for min_keys, max_keys, min_clicks, max_clicks, min_scrolls, max_scrolls
#         self.min_keys_entry = QtWidgets.QLineEdit(self)
#         self.max_keys_entry = QtWidgets.QLineEdit(self)
#         self.min_clicks_entry = QtWidgets.QLineEdit(self)
#         self.max_clicks_entry = QtWidgets.QLineEdit(self)
#         self.min_scrolls_entry = QtWidgets.QLineEdit(self)
#         self.max_scrolls_entry = QtWidgets.QLineEdit(self)

#         layout.addWidget(QtWidgets.QLabel("Min Keys:"), 3, 0)
#         layout.addWidget(self.min_keys_entry, 3, 1)
#         layout.addWidget(QtWidgets.QLabel("Max Keys:"), 4, 0)
#         layout.addWidget(self.max_keys_entry, 4, 1)
#         layout.addWidget(QtWidgets.QLabel("Min Clicks:"), 5, 0)
#         layout.addWidget(self.min_clicks_entry, 5, 1)
#         layout.addWidget(QtWidgets.QLabel("Max Clicks:"), 6, 0)
#         layout.addWidget(self.max_clicks_entry, 6, 1)
#         layout.addWidget(QtWidgets.QLabel("Min Scrolls:"), 7, 0)
#         layout.addWidget(self.min_scrolls_entry, 7, 1)
#         layout.addWidget(QtWidgets.QLabel("Max Scrolls:"), 8, 0)
#         layout.addWidget(self.max_scrolls_entry, 8, 1)

#         # Start and end time inputs
#         self.start_hour = QtWidgets.QSpinBox(self)
#         self.start_minute = QtWidgets.QSpinBox(self)
#         self.end_hour = QtWidgets.QSpinBox(self)
#         self.end_minute = QtWidgets.QSpinBox(self)

#         layout.addWidget(QtWidgets.QLabel("Start Hour:"), 9, 0)
#         layout.addWidget(self.start_hour, 9, 1)
#         layout.addWidget(QtWidgets.QLabel("Start Minute:"), 10, 0)
#         layout.addWidget(self.start_minute, 10, 1)
#         layout.addWidget(QtWidgets.QLabel("End Hour:"), 11, 0)
#         layout.addWidget(self.end_hour, 11, 1)
#         layout.addWidget(QtWidgets.QLabel("End Minute:"), 12, 0)
#         layout.addWidget(self.end_minute, 12, 1)

#         # Application selection
#         layout.addWidget(QtWidgets.QLabel("<h3>Select Applications</h3>"), 13, 0, 1, 2)

#         self.applications = self.get_applications()
#         self.app_vars = []
#         for idx, app in self.applications:
#             var = QtWidgets.QCheckBox(app.window_text())
#             self.app_vars.append(var)
#             layout.addWidget(var, 14 + idx, 0, 1, 2)

#         # Shutdown checkbox
#         self.shutdown_var = QtWidgets.QCheckBox("Shutdown after completion")
#         layout.addWidget(self.shutdown_var, 15 + len(self.applications), 0, 1, 2)

#         # Submit button
#         self.submit_button = QtWidgets.QPushButton("Start Billing")
#         self.submit_button.clicked.connect(self.submit_form)
#         layout.addWidget(self.submit_button, 16 + len(self.applications), 0, 1, 2)

#         # Set layout and window properties
#         main_layout = QtWidgets.QVBoxLayout()
#         main_layout.addWidget(self.scroll_area)
#         self.setLayout(main_layout)
#         self.setWindowTitle('Automation Tool')
#         self.setGeometry(100, 100, 400, 600)
#         self.show()

#     def validate_break_hours(self):
#         new_value = self.break_entry.text()
#         if new_value == "" or new_value == "Enter break duration in hours":
#             self.break_entry.setStyleSheet("color: grey;")
#         else:
#             self.break_entry.setStyleSheet("color: black;")
        
#         try:
#             int(new_value)
#         except ValueError:
#             pass

#     def get_applications(self):
#         try:
#             print("Getting applications...")
#             apps = Desktop(backend='uia').windows()
#             app_list = [(i, app) for i, app in enumerate(apps) if app.window_text() and app.window_text() not in ["Taskbar", "Program Manager"]]
#             print(f"Applications found: {[app.window_text() for _, app in app_list]}")
#             return app_list
#         except Exception as e:
#             print(f"Error getting applications: {e}")
#             return []

#     def simulate_keypresses(self, min_keys, max_keys, total_time_seconds):
#         keys = ['ctrl', 'shift', 'alt', 'left', 'right']
#         num_keys = random.randint(min_keys, max_keys)
#         print(f"Simulating {num_keys} keypresses.")
#         for _ in range(num_keys):
#             if self.cancel_flag:
#                 print("Key press simulation cancelled.")
#                 return
#             key = random.choice(keys)
#             print(f"Pressing key: {key}")
#             pyautogui.press(key)
#             time.sleep(0.5)

#     def move_mouse_randomly(self):
#         screen_width, screen_height = pyautogui.size()
#         x = random.randint(0, screen_width)
#         y = random.randint(0, screen_height)
#         print(f"Moving mouse to ({x}, {y})")
#         for _ in range(5):
#             pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.5))

#     def simulate_mouse_clicks(self, min_clicks, max_clicks, total_time_seconds):
#         screen_width, screen_height = pyautogui.size()
#         num_clicks = random.randint(min_clicks, max_clicks)
#         print(f"Simulating {num_clicks} mouse clicks.")
#         for _ in range(num_clicks):
#             if self.cancel_flag:
#                 print("Mouse click simulation cancelled.")
#                 return
#             print(f"Clicking at ({screen_width}, 300)")
#             pyautogui.moveTo(screen_width, 300, duration=0.5)
#             pyautogui.click()
#             time.sleep(0.5)

#     def simulate_scrolls(self, min_scrolls, max_scrolls):
#         num_scrolls = random.randint(min_scrolls, max_scrolls)
#         print(f"Simulating {num_scrolls} scroll actions.")
#         for _ in range(num_scrolls):
#             if self.cancel_flag:
#                 print("Scroll simulation cancelled.")
#                 return
#             scroll_amount = random.randint(-300, 300)
#             print(f"Scrolling by {scroll_amount}")
#             pyautogui.scroll(scroll_amount)
#             time.sleep(random.uniform(0.1, 0.5))

#     def force_shutdown(self):
#         os.system("shutdown /s /f /t 0")

#     def cancel_simulation(self):
#         self.cancel_flag = True
#         print('The Billing has been cancelled.')
#         QtWidgets.QMessageBox.information(self, "Cancelled", "The Billing has been cancelled.")

#     def perform_actions_on_application(self, app, min_keys, max_keys, min_clicks, max_clicks, min_scrolls, max_scrolls, total_time_seconds):
#         try:
#             app_title = app.window_text()
#             print(f"Focusing on application: {app_title}")
#             app.set_focus()
#             time.sleep(1)

#             # Simulate actions
#             self.move_mouse_randomly()
#             self.simulate_keypresses(min_keys, max_keys, total_time_seconds)
#             self.move_mouse_randomly()
#             self.simulate_mouse_clicks(min_clicks, max_clicks, total_time_seconds)
#             self.move_mouse_randomly()
#             self.simulate_scrolls(min_scrolls, max_scrolls)

#         except Exception as e:
#             print(f"Error during simulation: {e}")

#     def submit_form(self):
#         try:
#             # Retrieve user inputs
#             min_keys = int(self.min_keys_entry.text() or 0)
#             max_keys = int(self.max_keys_entry.text() or 0)
#             min_clicks = int(self.min_clicks_entry.text() or 0)
#             max_clicks = int(self.max_clicks_entry.text() or 0)
#             min_scrolls = int(self.min_scrolls_entry.text() or 0)
#             max_scrolls = int(self.max_scrolls_entry.text() or 0)
#             start_hour = self.start_hour.value()
#             start_minute = self.start_minute.value()
#             end_hour = self.end_hour.value()
#             end_minute = self.end_minute.value()

#             # Calculate simulation start and end time
#             start_time = datetime.now().replace(hour=start_hour, minute=start_minute, second=0, microsecond=0)
#             end_time = datetime.now().replace(hour=end_hour, minute=end_minute, second=0, microsecond=0)

#             if end_time < start_time:
#                 end_time += timedelta(days=1)

#             # Get break duration from input field
#             break_duration = int(self.break_entry.text() or 0) * 3600  # convert to seconds

#             print(f"Simulation will run from {start_time} to {end_time} with a break of {break_duration // 60} minutes.")

#             # Run the simulation
#             self.cancel_flag = False

#             def run_simulation(break_duration):
#                 while datetime.now() < start_time:
#                     time.sleep(1)  # Wait until start time

#                 while datetime.now() < end_time:
#                     for app_var in self.app_vars:
#                         if app_var.isChecked():
#                             app = self.applications[self.app_vars.index(app_var)][1]
#                             self.perform_actions_on_application(app, min_keys, max_keys, min_clicks, max_clicks, min_scrolls, max_scrolls, (end_time - start_time).total_seconds())

#                     if self.shutdown_var.isChecked():
#                         self.force_shutdown()

#                 if self.cancel_flag:
#                     self.cancel_simulation()

#             simulation_thread = threading.Thread(target=run_simulation, args=(break_duration,))
#             simulation_thread.start()

#         except ValueError as e:
#             QtWidgets.QMessageBox.critical(self, "Error", f"Invalid input: {e}")

# if __name__ == '__main__':
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     ex = App()
#     sys.exit(app.exec_())


from PyQt5 import QtWidgets, QtCore
from datetime import datetime, timedelta
from pywinauto import Desktop
import random
import time
import pyautogui
import threading
import os

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.cancel_flag = False

    def initUI(self):
        # Create a scroll area
        self.scroll_area = QtWidgets.QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)

        # Create a widget to contain the layout
        self.scroll_widget = QtWidgets.QWidget()
        self.scroll_area.setWidget(self.scroll_widget)

        # Create a grid layout
        layout = QtWidgets.QGridLayout(self.scroll_widget)

        # Headings
        layout.addWidget(QtWidgets.QLabel("<h2>Billing Automation Tool</h2>"), 0, 0, 1, 2)
        
        # Enter Key Presses Section
        layout.addWidget(QtWidgets.QLabel("<h3>Enter Key Presses</h3>"), 1, 0, 1, 2)
        layout.addWidget(QtWidgets.QLabel("Min Key Presses:"), 2, 0)
        self.min_keys_entry = QtWidgets.QLineEdit(self)
        layout.addWidget(self.min_keys_entry, 2, 1)
        layout.addWidget(QtWidgets.QLabel("Max Key Presses:"), 3, 0)
        self.max_keys_entry = QtWidgets.QLineEdit(self)
        layout.addWidget(self.max_keys_entry, 3, 1)

        # Mouse Clicks Section
        layout.addWidget(QtWidgets.QLabel("<h3>Mouse Clicks</h3>"), 4, 0, 1, 2)
        layout.addWidget(QtWidgets.QLabel("Min Clicks:"), 5, 0)
        self.min_clicks_entry = QtWidgets.QLineEdit(self)
        layout.addWidget(self.min_clicks_entry, 5, 1)
        layout.addWidget(QtWidgets.QLabel("Max Clicks:"), 6, 0)
        self.max_clicks_entry = QtWidgets.QLineEdit(self)
        layout.addWidget(self.max_clicks_entry, 6, 1)

        # Scrolls Section
        layout.addWidget(QtWidgets.QLabel("<h3>Scrolls</h3>"), 7, 0, 1, 2)
        layout.addWidget(QtWidgets.QLabel("Min Scrolls:"), 8, 0)
        self.min_scrolls_entry = QtWidgets.QLineEdit(self)
        layout.addWidget(self.min_scrolls_entry, 8, 1)
        layout.addWidget(QtWidgets.QLabel("Max Scrolls:"), 9, 0)
        self.max_scrolls_entry = QtWidgets.QLineEdit(self)
        layout.addWidget(self.max_scrolls_entry, 9, 1)

        # Break hours entry
        layout.addWidget(QtWidgets.QLabel("<h3>Break Duration</h3>"), 10, 0, 1, 2)
        self.break_entry = QtWidgets.QLineEdit(self)
        self.break_entry.setPlaceholderText("Enter break duration in hours")
        self.break_entry.setStyleSheet("color: grey;")
        self.break_entry.textChanged.connect(self.validate_break_hours)
        layout.addWidget(self.break_entry, 11, 0, 1, 2)

        # Start and end time inputs
        layout.addWidget(QtWidgets.QLabel("<h3>Time Settings</h3>"), 12, 0, 1, 2)
        self.start_hour = QtWidgets.QSpinBox(self)
        self.start_minute = QtWidgets.QSpinBox(self)
        self.end_hour = QtWidgets.QSpinBox(self)
        self.end_minute = QtWidgets.QSpinBox(self)

        layout.addWidget(QtWidgets.QLabel("Start Hour:"), 13, 0)
        layout.addWidget(self.start_hour, 13, 1)
        layout.addWidget(QtWidgets.QLabel("Start Minute:"), 14, 0)
        layout.addWidget(self.start_minute, 14, 1)
        layout.addWidget(QtWidgets.QLabel("End Hour:"), 15, 0)
        layout.addWidget(self.end_hour, 15, 1)
        layout.addWidget(QtWidgets.QLabel("End Minute:"), 16, 0)
        layout.addWidget(self.end_minute, 16, 1)

        # Application selection
        layout.addWidget(QtWidgets.QLabel("<h3>Select Applications</h3>"), 17, 0, 1, 2)
        self.applications = self.get_applications()
        self.app_vars = []

        for app in self.applications:
            print(f"Application: {app}")  # Debug print to check application content
            app_name = app  # Assuming `app` is a string, adjust if it’s a tuple
            if isinstance(app_name, str):  # Ensure it's a string
                var = QtWidgets.QCheckBox(app_name)  # Create checkbox with application name
                self.app_vars.append(var)
                layout.addWidget(var)  # Add checkbox to layout
            else:
                print(f"Unexpected type for application name: {type(app_name)}")

    # Add shutdown checkbox and any other UI components
        self.shutdown_var = QtWidgets.QCheckBox("Force Shutdown on Completion")
        layout.addWidget(self.shutdown_var)

        # Buttons
        self.submit_button = QtWidgets.QPushButton("Start Billing")
        self.cancel_button = QtWidgets.QPushButton("Cancel")
        self.submit_button.clicked.connect(self.submit_form)
        self.cancel_button.clicked.connect(self.cancel_simulation)

        layout.addWidget(self.submit_button, 19 + len(self.applications), 0)
        layout.addWidget(self.cancel_button, 19 + len(self.applications), 1)

        # Set layout and window properties
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(self.scroll_area)
        self.setLayout(main_layout)
        self.setWindowTitle('Automation Tool')
        self.setGeometry(100, 100, 400, 600)
        self.show()

    def validate_break_hours(self):
        new_value = self.break_entry.text()
        if new_value == "" or new_value == "Enter break duration in hours":
            self.break_entry.setStyleSheet("color: grey;")
        else:
            self.break_entry.setStyleSheet("color: black;")
        
        try:
            int(new_value)
        except ValueError:
            pass

    def get_applications(self):
        try:
            print("Getting applications...")
            apps = Desktop(backend='uia').windows()
            app_list = [(i, app) for i, app in enumerate(apps) if app.window_text() and app.window_text() not in ["Taskbar", "Program Manager"]]
            print(f"Applications found: {[app.window_text() for _, app in app_list]}")
            return app_list
        except Exception as e:
            print(f"Error getting applications: {e}")
            return []

    def simulate_keypresses(self, min_keys, max_keys, total_time_seconds):
        keys = ['ctrl', 'shift', 'alt', 'left', 'right']
        num_keys = random.randint(min_keys, max_keys)
        print(f"Simulating {num_keys} keypresses.")
        for _ in range(num_keys):
            if self.cancel_flag:
                print("Key press simulation cancelled.")
                return
            key = random.choice(keys)
            print(f"Pressing key: {key}")
            pyautogui.press(key)
            time.sleep(0.5)

    def move_mouse_randomly(self):
        screen_width, screen_height = pyautogui.size()
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        print(f"Moving mouse to ({x}, {y})")
        for _ in range(5):
            pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.5))

    def simulate_mouse_clicks(self, min_clicks, max_clicks, total_time_seconds):
        screen_width, screen_height = pyautogui.size()
        num_clicks = random.randint(min_clicks, max_clicks)
        print(f"Simulating {num_clicks} mouse clicks.")
        for _ in range(num_clicks):
            if self.cancel_flag:
                print("Mouse click simulation cancelled.")
                return
            print(f"Clicking at ({screen_width}, 300)")
            pyautogui.moveTo(screen_width, 300, duration=0.5)
            pyautogui.click()
            time.sleep(0.5)

    def simulate_scrolls(self, min_scrolls, max_scrolls):
        num_scrolls = random.randint(min_scrolls, max_scrolls)
        print(f"Simulating {num_scrolls} scroll actions.")
        for _ in range(num_scrolls):
            if self.cancel_flag:
                print("Scroll simulation cancelled.")
                return
            scroll_amount = random.randint(-300, 300)
            print(f"Scrolling by {scroll_amount}")
            pyautogui.scroll(scroll_amount)
            time.sleep(random.uniform(0.1, 0.5))

    def force_shutdown(self):
        os.system("shutdown /s /f /t 0")

    def cancel_simulation(self):
        self.cancel_flag = True
        print("Simulation cancelled.")

    def perform_actions_on_application(self, app, min_keys, max_keys, min_clicks, max_clicks, min_scrolls, max_scrolls, total_time_seconds):
        try:
            app.set_focus()
            time.sleep(1)  # Wait for the app to focus
            self.simulate_keypresses(min_keys, max_keys, total_time_seconds)
            self.move_mouse_randomly()
            self.simulate_mouse_clicks(min_clicks, max_clicks, total_time_seconds)
            self.simulate_scrolls(min_scrolls, max_scrolls)
        except Exception as e:
            print(f"Error during simulation: {e}")

    def submit_form(self):
        try:
            # Retrieve user inputs
            min_keys = int(self.min_keys_entry.text() or 0)
            max_keys = int(self.max_keys_entry.text() or 0)
            min_clicks = int(self.min_clicks_entry.text() or 0)
            max_clicks = int(self.max_clicks_entry.text() or 0)
            min_scrolls = int(self.min_scrolls_entry.text() or 0)
            max_scrolls = int(self.max_scrolls_entry.text() or 0)
            start_hour = self.start_hour.value()
            start_minute = self.start_minute.value()
            end_hour = self.end_hour.value()
            end_minute = self.end_minute.value()

            # Calculate simulation start and end time
            start_time = datetime.now().replace(hour=start_hour, minute=start_minute, second=0, microsecond=0)
            end_time = datetime.now().replace(hour=end_hour, minute=end_minute, second=0, microsecond=0)

            if end_time < start_time:
                end_time += timedelta(days=1)

            # Get break duration from input field
            break_duration = int(self.break_entry.text() or 0) * 3600  # convert to seconds

            print(f"Simulation will run from {start_time} to {end_time} with a break of {break_duration // 60} minutes.")

            # Run the simulation
            self.cancel_flag = False

            def run_simulation(break_duration):
                while datetime.now() < start_time:
                    time.sleep(1)  # Wait until start time

                while datetime.now() < end_time:
                    for app_var in self.app_vars:
                        if app_var.isChecked():
                            app = self.applications[self.app_vars.index(app_var)][1]
                            self.perform_actions_on_application(app, min_keys, max_keys, min_clicks, max_clicks, min_scrolls, max_scrolls, (end_time - start_time).total_seconds())

                    if self.shutdown_var.isChecked():
                        self.force_shutdown()

                if self.cancel_flag:
                    self.cancel_simulation()

            simulation_thread = threading.Thread(target=run_simulation, args=(break_duration,))
            simulation_thread.start()

        except ValueError as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Invalid input: {e}")

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
