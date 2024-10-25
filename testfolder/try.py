import sys
import subprocess
import warnings
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
from PyQt5.QtCore import QTimer

# Suppress DeprecationWarnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

class AutoBillingSystem(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.timer = QTimer()
        self.billing_active = False

    def initUI(self):
        self.setWindowTitle("Auto Billing System")
        self.setGeometry(100, 100, 400, 600)
        self.setStyleSheet("background-color: #2E2E2E; color: white;")

        main_layout = QVBoxLayout()

        main_layout.addLayout(self.createKeyStrokesLayout())
        main_layout.addLayout(self.createMouseClicksLayout())
        main_layout.addLayout(self.createScrollActionsLayout())
        main_layout.addLayout(self.createTimeSelectionLayout())
        main_layout.addLayout(self.createApplicationsLayout())
        main_layout.addLayout(self.createShutdownLayout())

        # Start and Stop buttons
        start_button = QPushButton("Start Billing")
        stop_button = QPushButton("Stop Billing")
        start_button.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold;")
        stop_button.setStyleSheet("background-color: #F44336; color: white; font-weight: bold;")
        
        # Connect buttons to functions
        start_button.clicked.connect(self.start_billing)
        stop_button.clicked.connect(self.stop_billing)

        main_layout.addWidget(start_button)
        main_layout.addWidget(stop_button)

        self.setLayout(main_layout)

    def createKeyStrokesLayout(self):
        return self.createInputLayout("Key Strokes per Minute")

    def createMouseClicksLayout(self):
        return self.createInputLayout("Mouse Clicks per Minute")

    def createScrollActionsLayout(self):
        return self.createInputLayout("Scroll Actions per Minute")

    def createInputLayout(self, label_text):
        layout = QHBoxLayout()
        layout.addWidget(QLabel(label_text))
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
        start_hour, start_minute, end_hour, end_minute = QComboBox(), QComboBox(), QComboBox(), QComboBox()

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

    def createApplicationsLayout(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Applications List"))

        apps = self.get_opened_applications()
        max_apps_to_display = 3
        if len(apps) > max_apps_to_display:
            apps = apps[:max_apps_to_display]
            layout.addWidget(QLabel(f"Displaying {max_apps_to_display} of {len(apps)} applications."))

        for app in apps:
            checkbox = self.createAppCheckbox(app)
            layout.addWidget(checkbox)

        if len(apps) > max_apps_to_display:
            show_more_button = QPushButton("Show More Applications")
            show_more_button.clicked.connect(lambda: self.show_all_applications(apps))
            layout.addWidget(show_more_button)

        return layout

    def createAppCheckbox(self, app):
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
        return checkbox

    def show_all_applications(self, apps):
        dialog = QWidget()
        dialog.setWindowTitle("All Applications")
        dialog.setGeometry(150, 150, 300, 400)
        dialog.setStyleSheet("background-color: #2E2E2E; color: white;")

        layout = QVBoxLayout()
        for app in apps:
            layout.addWidget(self.createAppCheckbox(app))

        dialog.setLayout(layout)
        dialog.show()

    def get_opened_applications(self):
        output = subprocess.check_output(['wmctrl', '-l']).decode('utf-8')
        applications = [line.split(maxsplit=3)[3] for line in output.splitlines() if len(line.split(maxsplit=3)) > 3]
        return applications

    def createShutdownLayout(self):
        layout = QVBoxLayout()
        shutdown_checkbox = QCheckBox("Schedule shutdown after 2 minutes of end time")
        shutdown_checkbox.setStyleSheet("color: white;")
        layout.addWidget(shutdown_checkbox)
        return layout

    def start_billing(self):
        if not self.billing_active:
            self.billing_active = True
            self.timer.timeout.connect(self.perform_billing_action)
            self.timer.start(1000)  # Call the function every second
            print("Billing started.")

    def stop_billing(self):
        if self.billing_active:
            self.timer.stop()
            self.billing_active = False
            print("Billing stopped.")

    def perform_billing_action(self):
        # Here you can implement the actual billing logic
        print("Performing billing action...")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AutoBillingSystem()
    window.show()
    sys.exit(app.exec_())
