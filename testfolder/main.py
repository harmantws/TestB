# import sys
# import subprocess
# from PyQt5.QtWidgets import (
#     QApplication,
#     QWidget,
#     QLabel,
#     QLineEdit,
#     QVBoxLayout,
#     QHBoxLayout,
#     QCheckBox,
#     QComboBox,
#     QPushButton,
# )

# class AutoBillingSystem(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle("Auto Billing System")
#         self.setGeometry(100, 100, 400, 600)
#         self.setStyleSheet("background-color: #2E2E2E; color: white;")

#         # Layouts
#         main_layout = QVBoxLayout()

#         # main_layout.setSpacing(0)  # Set spacing to 0
#         key_strokes_layout = self.createKeyStrokesLayout()
#         mouse_clicks_layout = self.createMouseClicksLayout()
#         scroll_actions_layout = self.createScrollActionsLayout()
#         time_selection_layout = self.createTimeSelectionLayout()
#         applications_layout = self.createApplicationsLayout()
#         shutdown_layout = self.createShutdownLayout()

#         # Add layouts to main layout
#         main_layout.addLayout(key_strokes_layout)
#         main_layout.addLayout(mouse_clicks_layout)
#         main_layout.addLayout(scroll_actions_layout)
#         main_layout.addLayout(time_selection_layout)
#         main_layout.addLayout(applications_layout)
#         main_layout.addLayout(shutdown_layout)

#         # Start and Stop buttons
#         start_button = QPushButton("Start Billing")
#         stop_button = QPushButton("Stop Billing")
#         start_button.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold;")
#         stop_button.setStyleSheet("background-color: #F44336; color: white; font-weight: bold;")
#         main_layout.addWidget(start_button)
#         main_layout.addWidget(stop_button)

#         self.setLayout(main_layout)

#     def createKeyStrokesLayout(self):
#         layout = QHBoxLayout()
#         layout.addWidget(QLabel("Key Strokes per Minute"))
#         min_input = QLineEdit()
#         max_input = QLineEdit()
#         min_input.setStyleSheet("background-color: #444; color: white;")
#         max_input.setStyleSheet("background-color: #444; color: white;")
#         layout.addWidget(min_input)
#         layout.addWidget(max_input)
#         return layout

#     def createMouseClicksLayout(self):
#         layout = QHBoxLayout()
#         layout.addWidget(QLabel("Mouse Clicks per Minute"))
#         min_input = QLineEdit()
#         max_input = QLineEdit()
#         min_input.setStyleSheet("background-color: #444; color: white;")
#         max_input.setStyleSheet("background-color: #444; color: white;")
#         layout.addWidget(min_input)
#         layout.addWidget(max_input)
#         return layout

#     def createScrollActionsLayout(self):
#         layout = QHBoxLayout()
#         layout.addWidget(QLabel("Scroll Actions per Minute"))
#         min_input = QLineEdit()
#         max_input = QLineEdit()
#         min_input.setStyleSheet("background-color: #444; color: white;")
#         max_input.setStyleSheet("background-color: #444; color: white;")
#         layout.addWidget(min_input)
#         layout.addWidget(max_input)
#         return layout

#     def createTimeSelectionLayout(self):
#         layout = QVBoxLayout()
#         layout.addWidget(QLabel("Select Time"))
#         start_hour = QComboBox()
#         start_minute = QComboBox()
#         end_hour = QComboBox()
#         end_minute = QComboBox()

#         for i in range(24):
#             start_hour.addItem(str(i))
#             end_hour.addItem(str(i))
#         for i in range(60):
#             start_minute.addItem(str(i))
#             end_minute.addItem(str(i))

#         layout.addWidget(QLabel("Start Hour:"))
#         layout.addWidget(start_hour)
#         layout.addWidget(QLabel("Start Minute:"))
#         layout.addWidget(start_minute)
#         layout.addWidget(QLabel("End Hour:"))
#         layout.addWidget(end_hour)
#         layout.addWidget(QLabel("End Minute:"))
#         layout.addWidget(end_minute)

#         return layout

#     def createApplicationsLayout(self):
#         layout = QVBoxLayout()
#         layout.addWidget(QLabel("Applications List"))

#         # Get the filtered list of currently opened applications
#         apps = self.get_opened_applications()
#         # for app in self.apps:
#         #     checkbox = QCheckBox(app)
#         #     checkbox.setStyleSheet("color: white;")
#         #     layout.addWidget(checkbox)
#         for app in apps:
#             checkbox = QCheckBox(app)
#             # Change the checkbox color
#             checkbox.setStyleSheet("""
#                 QCheckBox {
#                     color: white;  /* Text color */
#                     background-color: #444;  /* Background color */
#                 }
#                 QCheckBox::indicator {
#                     background-color: #555;  /* Indicator background */
#                     border: 1px solid white;  /* Border color */
#                 }
#                 QCheckBox::indicator:checked {
#                     background-color: #f5f5f5;  /* Color when checked */
#                     border: 1px solid white;  /* Border color when checked */
#                 }
#             """)
#             layout.addWidget(checkbox)

#         return layout

#     def get_opened_applications(self):
#         # Execute wmctrl command to get the list of active windows
#         output = subprocess.check_output(['wmctrl', '-l']).decode('utf-8')
#         applications = []
#         for line in output.splitlines():
#             parts = line.split(maxsplit=3)
#             if len(parts) > 3:
#                 applications.append(parts[3])  # Get the title of the active window
#                 print(parts[3])
#         return applications

#     def createShutdownLayout(self):
#         layout = QVBoxLayout()
#         shutdown_checkbox = QCheckBox("Schedule shutdown after 2 minutes of end time")
#         shutdown_checkbox.setStyleSheet("color: white;")
#         layout.addWidget(shutdown_checkbox)
#         return layout

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = AutoBillingSystem()
#     window.show()
#     sys.exit(app.exec_())



















import sys
import subprocess
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QCheckBox,
    QComboBox,
    QPushButton,
)

class AutoBillingSystem(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Auto Billing System")
        self.setGeometry(100, 100, 400, 600)
        self.setStyleSheet("background-color: #2E2E2E; color: white;")

        # Layouts
        main_layout = QVBoxLayout()

        # main_layout.setSpacing(0)  # Set spacing to 0
        key_strokes_layout = self.createKeyStrokesLayout()
        mouse_clicks_layout = self.createMouseClicksLayout()
        scroll_actions_layout = self.createScrollActionsLayout()
        time_selection_layout = self.createTimeSelectionLayout()
        applications_layout = self.createApplicationsLayout()
        shutdown_layout = self.createShutdownLayout()

        # Add layouts to main layout
        main_layout.addLayout(key_strokes_layout)
        main_layout.addLayout(mouse_clicks_layout)
        main_layout.addLayout(scroll_actions_layout)
        main_layout.addLayout(time_selection_layout)
        main_layout.addLayout(applications_layout)
        main_layout.addLayout(shutdown_layout)

        # Start and Stop buttons
        start_button = QPushButton("Start Billing")
        stop_button = QPushButton("Stop Billing")
        start_button.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold;")
        stop_button.setStyleSheet("background-color: #F44336; color: white; font-weight: bold;")
        main_layout.addWidget(start_button)
        main_layout.addWidget(stop_button)

        self.setLayout(main_layout)

    def createKeyStrokesLayout(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("Key Strokes per Minute"))
        min_input = QLineEdit()
        max_input = QLineEdit()
        min_input.setStyleSheet("background-color: #444; color: white;")
        max_input.setStyleSheet("background-color: #444; color: white;")
        layout.addWidget(min_input)
        layout.addWidget(max_input)
        return layout

    def createMouseClicksLayout(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("Mouse Clicks per Minute"))
        min_input = QLineEdit()
        max_input = QLineEdit()
        min_input.setStyleSheet("background-color: #444; color: white;")
        max_input.setStyleSheet("background-color: #444; color: white;")
        layout.addWidget(min_input)
        layout.addWidget(max_input)
        return layout

    def createScrollActionsLayout(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("Scroll Actions per Minute"))
        min_input = QLineEdit()
        max_input = QLineEdit()
        min_input.setStyleSheet("background-color: #444; color: white;")
        max_input.setStyleSheet("background-color: #444; color: white;")
        layout.addWidget(min_input)
        layout.addWidget(max_input)
        return layout

    def createTimeSelectionLayout(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Select Time"))
        start_hour = QComboBox()
        start_minute = QComboBox()
        end_hour = QComboBox()
        end_minute = QComboBox()

        for i in range(24):
            start_hour.addItem(str(i))
            end_hour.addItem(str(i))
        for i in range(60):
            start_minute.addItem(str(i))
            end_minute.addItem(str(i))

        layout.addWidget(QLabel("Start Hour:"))
        layout.addWidget(start_hour)
        layout.addWidget(QLabel("Start Minute:"))
        layout.addWidget(start_minute)
        layout.addWidget(QLabel("End Hour:"))
        layout.addWidget(end_hour)
        layout.addWidget(QLabel("End Minute:"))
        layout.addWidget(end_minute)

        return layout

    # def createApplicationsLayout(self):
    #     layout = QVBoxLayout()
    #     layout.addWidget(QLabel("Applications List"))

    #     # Get the filtered list of currently opened applications
    #     apps = self.get_opened_applications()
    #     # for app in self.apps:
    #     #     checkbox = QCheckBox(app)
    #     #     checkbox.setStyleSheet("color: white;")
    #     #     layout.addWidget(checkbox)
    #     for app in apps:
    #         checkbox = QCheckBox(app)
    #         # Change the checkbox color
    #         checkbox.setStyleSheet("""
    #             QCheckBox {
    #                 color: white;  /* Text color */
    #                 background-color: #444;  /* Background color */
    #             }
    #             QCheckBox::indicator {
    #                 background-color: #555;  /* Indicator background */
    #                 border: 1px solid white;  /* Border color */
    #             }
    #             QCheckBox::indicator:checked {
    #                 background-color: #f5f5f5;  /* Color when checked */
    #                 border: 1px solid white;  /* Border color when checked */
    #             }
    #         """)
    #         layout.addWidget(checkbox)

    #     return layout

    def createApplicationsLayout(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Applications List"))

        # Get the filtered list of currently opened applications
        apps = self.get_opened_applications()
        
        # Limit the number of applications displayed
        max_apps_to_display = 3  # Set the maximum number of applications to show
        if len(apps) > max_apps_to_display:
            apps = apps[:max_apps_to_display]  # Truncate the list
            layout.addWidget(QLabel(f"Displaying {max_apps_to_display} of {len(apps)} applications."))

        for app in apps:
            checkbox = QCheckBox(app)
            # Change the checkbox color
            checkbox.setStyleSheet("""
                QCheckBox {
                    color: white;  /* Text color */
                    background-color: #444;  /* Background color */
                }
                QCheckBox::indicator {
                    background-color: #555;  /* Indicator background */
                    border: 1px solid white;  /* Border color */
                }
                QCheckBox::indicator:checked {
                    background-color: #f5f5f5;  /* Color when checked */
                    border: 1px solid white;  /* Border color when checked */
                }
            """)
            layout.addWidget(checkbox)

        # Optionally, provide a way to show more applications if available
            if len(apps) > max_apps_to_display:
                show_more_button = QPushButton("Show More Applications")
                show_more_button.clicked.connect(lambda: self.show_all_applications(apps))
                layout.addWidget(show_more_button)

        return layout

    def show_all_applications(self, apps):
        # Create a new dialog to show all applications
        dialog = QWidget()
        dialog.setWindowTitle("All Applications")
        dialog.setGeometry(150, 150, 300, 400)
        dialog.setStyleSheet("background-color: #2E2E2E; color: white;")

        layout = QVBoxLayout()
        for app in apps:
            checkbox = QCheckBox(app)
            checkbox.setStyleSheet("""
                QCheckBox {
                    color: white;
                    background-color: #444;
                }
                QCheckBox::indicator {
                    background-color: #555;
                    border: 1px solid white;
                }
                QCheckBox::indicator:checked {
                    background-color: #f5f5f5;
                    border: 1px solid white;
                }
            """)
            layout.addWidget(checkbox)

        dialog.setLayout(layout)
        dialog.show()


    def get_opened_applications(self):
        # Execute wmctrl command to get the list of active windows
        output = subprocess.check_output(['wmctrl', '-l']).decode('utf-8')
        applications = []
        for line in output.splitlines():
            parts = line.split(maxsplit=3)
            if len(parts) > 3:
                applications.append(parts[3])  # Get the title of the active window
                print(parts[3])
        return applications

    def createShutdownLayout(self):
        layout = QVBoxLayout()
        shutdown_checkbox = QCheckBox("Schedule shutdown after 2 minutes of end time")
        shutdown_checkbox.setStyleSheet("color: white;")
        layout.addWidget(shutdown_checkbox)
        return layout

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AutoBillingSystem()
    window.show()
    sys.exit(app.exec_())













