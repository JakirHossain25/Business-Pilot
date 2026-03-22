import sys
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QCheckBox,
    QMessageBox, QApplication
)
from PyQt6.QtCore import Qt, QPropertyAnimation, QPoint
from PyQt6.QtGui import QPixmap, QPainter, QColor, QFont
from config import COMPANY_NAME, COMPANY_PASSWORD


# 🔵 Custom Logo
class CustomLogo(QLabel):
    def __init__(self):
        super().__init__()
        self.setFixedSize(140, 140)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.create_logo()

    def create_logo(self):
        pixmap = QPixmap(140, 140)
        pixmap.fill(Qt.GlobalColor.transparent)

        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Circle
        painter.setBrush(QColor("#4CAF50"))
        painter.drawEllipse(0, 0, 140, 140)

        # Text
        font = QFont("Arial", 40, QFont.Weight.Bold)
        painter.setFont(font)
        painter.setPen(QColor("white"))
        painter.drawText(pixmap.rect(), Qt.AlignmentFlag.AlignCenter, "BP")

        painter.end()
        self.setPixmap(pixmap)


# 🔐 Login Dialog
class ModernLoginDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setFixedSize(420, 520)

        self.setup_ui()

        # Enter press login
        self.password.returnPressed.connect(self.login)

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(15)

        # 🔵 Logo
        self.logo = CustomLogo()
        layout.addWidget(self.logo, alignment=Qt.AlignmentFlag.AlignCenter)

        # ✅ Company name (NO BOX)
        company = QLabel(COMPANY_NAME)
        company.setAlignment(Qt.AlignmentFlag.AlignCenter)
        company.setStyleSheet("""
            font-size: 22px;
            font-weight: bold;
            color: #4CAF50;
        """)
        layout.addWidget(company)

        # Welcome text
        welcome = QLabel("Welcome Back")
        welcome.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome.setStyleSheet("color: gray;")
        layout.addWidget(welcome)

        # 🔒 Password field
        self.password = QLineEdit()
        self.password.setPlaceholderText("Enter Password")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.password.setStyleSheet("""
            padding: 10px;
            border: 2px solid #ccc;
            border-radius: 10px;
        """)
        layout.addWidget(self.password)

        # Remember me
        self.remember = QCheckBox("Remember me")
        layout.addWidget(self.remember)

        # 🔘 Login button
        self.login_btn = QPushButton("LOGIN")
        self.login_btn.setStyleSheet("""
            background-color: #4CAF50;
            color: white;
            padding: 12px;
            border-radius: 10px;
            font-weight: bold;
        """)
        self.login_btn.clicked.connect(self.login)
        layout.addWidget(self.login_btn)

        # Cancel button
        cancel = QPushButton("CANCEL")
        cancel.clicked.connect(self.reject)
        layout.addWidget(cancel)

    # 🔐 Login function
    def login(self):
        if self.password.text() == COMPANY_PASSWORD:
            QMessageBox.information(self, "Success", "Login Successful")
            self.accept()
        else:
            self.shake_window()
            QMessageBox.warning(self, "Error", "Wrong Password")
            self.password.clear()

    # 🔥 Shake animation
    def shake_window(self):
        animation = QPropertyAnimation(self, b"pos")
        pos = self.pos()

        animation.setDuration(300)
        animation.setKeyValueAt(0, pos)
        animation.setKeyValueAt(0.25, pos + QPoint(-10, 0))
        animation.setKeyValueAt(0.5, pos + QPoint(10, 0))
        animation.setKeyValueAt(0.75, pos + QPoint(-10, 0))
        animation.setKeyValueAt(1, pos)

        animation.start()
        self.animation = animation


# ▶ Run App
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ModernLoginDialog()
    win.exec()