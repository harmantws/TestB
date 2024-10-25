import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QSpinBox, QCheckBox, QPushButton,
                             QScrollArea, QFrame, QGridLayout)
from helper import get_applications, add_placeholder, submit_form, cancel_simulation, validate_break_hours

class AutoBillingSystem(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Auto Billing System")
        self.setGeometry(100, 100, 450, 800)
        self.setStyleSheet("background-color: #1E1E1E; color: white;")

        # Create the main layout
        main_layout = QVBoxLayout()

        # Create a scroll area
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        
        # Create a content widget to hold all controls
        self.content_widget = QWidget()
        self.scroll_area.setWidget(self.content_widget)

        # Create a vertical layout for the content widget
        content_layout = QVBoxLayout(self.content_widget)

        # Key Strokes section
        self.add_label(content_layout, "Key Strokes per Minute")
        self.add_entry_section(content_layout, "Min", "Max")

        # Mouse Clicks section
        self.add_label(content_layout, "Mouse Clicks per Minute")
        self.add_entry_section(content_layout, "Min", "Max")

        # Scroll Actions section
        self.add_label(content_layout, "Scroll Actions per Minute")
        self.add_entry_section(content_layout, "Min", "Max")

        # Select Time section
        self.add_label(content_layout, "Select Time")
        time_layout = QGridLayout()
        self.add_time_input(time_layout, "Start Hour", "Start Minute", 0)
        self.add_time_input(time_layout, "End Hour", "End Minute", 1)
        content_layout.addLayout(time_layout)

        # Break Hours section
        self.add_label(content_layout, "Want to include some break in Hours?")
        self.break_entry_value = QLineEdit()
        self.break_entry_value.setStyleSheet("font-size: 12px;")
        content_layout.addWidget(self.break_entry_value)

        # Applications List section
        self.add_label(content_layout, "Applications List")
        self.app_vars = {}
        applications = get_applications()
        for index, app in applications:
            var = QCheckBox(app.window_text())
            var.setStyleSheet("font-size: 12px;")
            content_layout.addWidget(var)
            self.app_vars[index] = var

        # Schedule Shutdown section
        self.shutdown_var = QCheckBox("Schedule shutdown after 2 minutes of end time")
        self.shutdown_var.setStyleSheet("font-size: 12px;")
        content_layout.addWidget(self.shutdown_var)

        # Buttons
        button_layout = QHBoxLayout()
        self.submit_button = QPushButton("Start Billing")
        self.submit_button.clicked.connect(self.start_billing)
        button_layout.addWidget(self.submit_button)

        self.cancel_button = QPushButton("Stop Billing")
        self.cancel_button.clicked.connect(cancel_simulation)
        button_layout.addWidget(self.cancel_button)

        content_layout.addLayout(button_layout)

        # Add scroll area to the main layout
        main_layout.addWidget(self.scroll_area)
        self.setLayout(main_layout)

    def add_label(self, layout, text):
        label = QLabel(text)
        label.setStyleSheet("font-size: 16px; font-weight: bold; color: #00FF00;")
        layout.addWidget(label)

    def add_entry_section(self, layout, min_label_text, max_label_text):
        entry_layout = QHBoxLayout()
        min_entry = QLineEdit()
        add_placeholder(min_entry, min_label_text)
        max_entry = QLineEdit()
        add_placeholder(max_entry, max_label_text)
        entry_layout.addWidget(min_entry)
        entry_layout.addWidget(max_entry)
        layout.addLayout(entry_layout)

    def add_time_input(self, layout, hour_label_text, minute_label_text, row):
        hour_label = QLabel(hour_label_text)
        hour_label.setStyleSheet("font-size: 12px;")
        layout.addWidget(hour_label, row, 0)
        hour_spinbox = QSpinBox()
        hour_spinbox.setRange(0, 23)
        layout.addWidget(hour_spinbox, row, 1)

        minute_label = QLabel(minute_label_text)
        minute_label.setStyleSheet("font-size: 12px;")
        layout.addWidget(minute_label, row, 2)
        minute_spinbox = QSpinBox()
        minute_spinbox.setRange(0, 59)
        layout.addWidget(minute_spinbox, row, 3)

    # def start_billing(self):
    #     # Implement the logic for starting the billing process here
    #     submit_form(self.break_entry_value, self.app_vars, self.shutdown_var)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AutoBillingSystem()
    window.show()
    sys.exit(app.exec_())
