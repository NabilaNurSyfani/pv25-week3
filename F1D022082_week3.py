import sys
import random
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt


class MouseTracker(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Task Week 3 - (F1D022082 - Nabila Nur Syfani)")
        self.setGeometry(100, 100, 500, 400)

        self.label = QLabel("x: 0, y: 0", self)
        self.label.setStyleSheet("font-size: 16px;")
        self.label.adjustSize()
        self.label.move(200, 180)

        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        x, y = event.x(), event.y()
        self.label.setText(f"x: {x}, y: {y}")
        self.label.adjustSize()

    def enterEvent(self, event):
        self.setMouseTracking(True)

    def eventFilter(self, obj, event):
        if obj == self.label and event.type() == event.Enter:
            max_x = self.width() - self.label.width()
            max_y = self.height() - self.label.height()
            new_x = random.randint(0, max_x)
            new_y = random.randint(0, max_y)
            self.label.move(new_x, new_y)
        return super().eventFilter(obj, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MouseTracker()
    window.label.installEventFilter(window)
    window.show()
    sys.exit(app.exec_())
