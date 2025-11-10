import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QColorDialog, QPushButton,
    QVBoxLayout, QLineEdit, QLabel, QHBoxLayout
)
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import Qt





class ColorPickerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Color Picker App 🎨")
        self.resize(500, 400)

        # Layouts
        main_layout = QVBoxLayout()
        input_layout = QHBoxLayout()

        # Widgets
        self.label = QLabel("Preview Area")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 24px; color: black;")

        self.pick_btn = QPushButton("Pick Color")
        self.pick_btn.clicked.connect(self.open_color_dialog)

        self.hex_input = QLineEdit()
        self.hex_input.setPlaceholderText("Enter HEX (e.g. #FF00FF)")
        self.hex_input.returnPressed.connect(self.apply_hex_color)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter color name (e.g. red)")
        self.name_input.returnPressed.connect(self.apply_name_color)

        self.fullscreen_btn = QPushButton("Toggle Fullscreen")
        self.fullscreen_btn.clicked.connect(self.toggle_fullscreen)

        input_layout.addWidget(self.hex_input)
        input_layout.addWidget(self.name_input)

        main_layout.addWidget(self.pick_btn)
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.fullscreen_btn)
        main_layout.addWidget(self.label)

        self.setLayout(main_layout)
        self.current_color = QColor("white")
        self.is_fullscreen = False
        self.update_background()

    # Color picking
    def open_color_dialog(self):
        # Force Qt's own dialog, not Windows native one
        dialog = QColorDialog(self)
        dialog.setOption(QColorDialog.DontUseNativeDialog, True)  # important

        # enable alpha if you want transparency slider
        # dialog.setOption(QColorDialog.ShowAlphaChannel, True)

        # Set initial color
        dialog.setCurrentColor(self.current_color)

        # Force the internal widget to show the circular wheel
        for child in dialog.findChildren(QWidget):
            if child.metaObject().className() == 'QColorPicker':
                child.setProperty("colorDialogMode", 1)  # wheel mode

        if dialog.exec_():
            self.current_color = dialog.currentColor()
            self.update_background()

    # Apply color from hex
    def apply_hex_color(self):
        text = self.hex_input.text().strip()
        if not text.startswith("#"):
            text = "#" + text
        color = QColor(text)
        if color.isValid():
            self.current_color = color
            self.update_background()

    # Apply color from name
    def apply_name_color(self):
        name = self.name_input.text().strip().lower()
        color = QColor(name)
        if color.isValid():
            self.current_color = color
            self.update_background()

    # functiont that will allow to make saturation function 
    def update_saturation(self, value):
        self.saturation = value
        self.current_color = QColor.fromHsv(self.hue, self.saturation, self.value)
        self.update_background()

    # Update background preview
    def update_background(self):
        palette = self.palette()
        palette.setColor(QPalette.Window, self.current_color)
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        # Change label text color for contrast
        brightness = (
            0.299 * self.current_color.red() +
            0.587 * self.current_color.green() +
            0.114 * self.current_color.blue()
        )
        text_color = "black" if brightness > 128 else "white"
        self.label.setStyleSheet(f"font-size: 24px; color: {text_color};")
        self.label.setText(f"{self.current_color.name()}")

    # Fullscreen toggle
    def toggle_fullscreen(self):
        if not self.is_fullscreen:
            self.showFullScreen()
            self.is_fullscreen = True
        else:
            self.showNormal()
            self.is_fullscreen = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ColorPickerApp()
    window.show()
    sys.exit(app.exec_())
