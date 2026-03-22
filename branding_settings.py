# branding_settings.py
import os
import shutil
from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QFormLayout,
                             QLabel, QLineEdit, QPushButton, QGroupBox,
                             QFileDialog, QMessageBox, QDialogButtonBox,
                             QFrame)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QIcon
from config import DEVELOPER_NAME, DEVELOPER_WHATSAPP, DEVELOPER_INFO, LOGO_FOLDER, COMPANY_LOGO_PATH, APP_ICON_PATH

class BrandingSettings(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setWindowTitle("Branding Settings")
        self.setModal(True)
        self.setFixedSize(600, 550)
        
        layout = QVBoxLayout()
        
        # Software Information
        info_group = QGroupBox("Software Information")
        info_layout = QFormLayout()
        
        self.software_name = QLineEdit()
        self.software_name.setText(parent.software_name if parent else "Business Management Software")
        info_layout.addRow("Software Name:", self.software_name)
        
        info_group.setLayout(info_layout)
        layout.addWidget(info_group)
        
        # Logo Settings
        logo_group = QGroupBox("Logo & Icon Settings")
        logo_layout = QVBoxLayout()
        
        # Create logo folder if it doesn't exist
        if not os.path.exists(LOGO_FOLDER):
            os.makedirs(LOGO_FOLDER)
        
        # Company Logo
        logo_label = QLabel("Company Logo (PNG/JPG format):")
        logo_label.setStyleSheet("font-weight: bold; color: #4CAF50;")
        logo_layout.addWidget(logo_label)
        
        self.logo_path = QLineEdit()
        self.logo_path.setReadOnly(True)
        if os.path.exists(COMPANY_LOGO_PATH):
            self.logo_path.setText(COMPANY_LOGO_PATH)
        
        logo_btn_layout = QHBoxLayout()
        browse_logo_btn = QPushButton("Browse Logo")
        browse_logo_btn.clicked.connect(self.browse_logo)
        remove_logo_btn = QPushButton("Remove Logo")
        remove_logo_btn.clicked.connect(self.remove_logo)
        
        logo_btn_layout.addWidget(browse_logo_btn)
        logo_btn_layout.addWidget(remove_logo_btn)
        
        logo_layout.addWidget(self.logo_path)
        logo_layout.addLayout(logo_btn_layout)
        
        # App Icon
        icon_label = QLabel("App Icon (ICO format for EXE):")
        icon_label.setStyleSheet("font-weight: bold; color: #2196F3; margin-top: 10px;")
        logo_layout.addWidget(icon_label)
        
        self.icon_path = QLineEdit()
        self.icon_path.setReadOnly(True)
        if os.path.exists(APP_ICON_PATH):
            self.icon_path.setText(APP_ICON_PATH)
        
        icon_btn_layout = QHBoxLayout()
        browse_icon_btn = QPushButton("Browse Icon")
        browse_icon_btn.clicked.connect(self.browse_icon)
        remove_icon_btn = QPushButton("Remove Icon")
        remove_icon_btn.clicked.connect(self.remove_icon)
        
        icon_btn_layout.addWidget(browse_icon_btn)
        icon_btn_layout.addWidget(remove_icon_btn)
        
        logo_layout.addWidget(self.icon_path)
        logo_layout.addLayout(icon_btn_layout)
        
        # Info label
        info_label = QLabel("Note: For EXE file, use ICO format. You can convert PNG to ICO online.")
        info_label.setStyleSheet("color: #666; font-size: 10px; font-style: italic;")
        logo_layout.addWidget(info_label)
        
        # Preview
        preview_layout = QHBoxLayout()
        
        # Logo preview
        logo_preview_group = QGroupBox("Logo Preview")
        logo_preview_layout = QVBoxLayout()
        self.logo_preview = QLabel()
        self.logo_preview.setFixedSize(100, 100)
        self.logo_preview.setStyleSheet("border: 1px solid #ccc; border-radius: 10px; padding: 5px;")
        self.logo_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo_preview_layout.addWidget(self.logo_preview, alignment=Qt.AlignmentFlag.AlignCenter)
        logo_preview_group.setLayout(logo_preview_layout)
        preview_layout.addWidget(logo_preview_group)
        
        # Icon preview
        icon_preview_group = QGroupBox("Icon Preview")
        icon_preview_layout = QVBoxLayout()
        self.icon_preview = QLabel()
        self.icon_preview.setFixedSize(48, 48)
        self.icon_preview.setStyleSheet("border: 1px solid #ccc; border-radius: 5px; padding: 5px;")
        self.icon_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        icon_preview_layout.addWidget(self.icon_preview, alignment=Qt.AlignmentFlag.AlignCenter)
        icon_preview_group.setLayout(icon_preview_layout)
        preview_layout.addWidget(icon_preview_group)
        
        logo_layout.addLayout(preview_layout)
        logo_group.setLayout(logo_layout)
        layout.addWidget(logo_group)
        
        # Developer Info (Fixed)
        dev_group = QGroupBox("Developer Information")
        dev_layout = QVBoxLayout()
        
        dev_name_label = QLabel(f"Developer Name: {DEVELOPER_NAME}")
        dev_name_label.setStyleSheet("font-weight: bold; color: #2196F3;")
        dev_layout.addWidget(dev_name_label)
        
        dev_contact_label = QLabel(f"WhatsApp: {DEVELOPER_WHATSAPP}")
        dev_contact_label.setStyleSheet("color: #4CAF50;")
        dev_layout.addWidget(dev_contact_label)
        
        dev_info_label = QLabel(DEVELOPER_INFO)
        dev_info_label.setStyleSheet("color: #666;")
        dev_layout.addWidget(dev_info_label)
        
        dev_group.setLayout(dev_layout)
        layout.addWidget(dev_group)
        
        # Buttons
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        button_box.accepted.connect(self.save_settings)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)
        
        self.setLayout(layout)
        
        # Load previews
        self.update_previews()
    
    def browse_logo(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Logo", "", "Images (*.png *.jpg *.jpeg)")
        if file_path:
            # Save as company_logo.png
            dest_path = COMPANY_LOGO_PATH
            
            # Convert to PNG if needed
            if file_path.lower().endswith(('.jpg', '.jpeg')):
                pixmap = QPixmap(file_path)
                pixmap.save(dest_path, 'PNG')
            else:
                shutil.copy2(file_path, dest_path)
            
            self.logo_path.setText(dest_path)
            self.update_previews()
            QMessageBox.information(self, "Success", "Logo saved successfully!")
    
    def browse_icon(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Icon", "", "Icon Files (*.ico)")
        if file_path:
            # Save as app_icon.ico
            dest_path = APP_ICON_PATH
            shutil.copy2(file_path, dest_path)
            
            self.icon_path.setText(dest_path)
            self.update_previews()
            
            # Update app icon
            if self.parent:
                self.parent.setWindowIcon(QIcon(dest_path))
            
            QMessageBox.information(self, "Success", "Icon saved successfully!")
    
    def remove_logo(self):
        if os.path.exists(COMPANY_LOGO_PATH):
            os.remove(COMPANY_LOGO_PATH)
        self.logo_path.clear()
        self.update_previews()
    
    def remove_icon(self):
        if os.path.exists(APP_ICON_PATH):
            os.remove(APP_ICON_PATH)
        self.icon_path.clear()
        self.update_previews()
    
    def update_previews(self):
        # Update logo preview
        if os.path.exists(COMPANY_LOGO_PATH):
            pixmap = QPixmap(COMPANY_LOGO_PATH)
            if not pixmap.isNull():
                scaled = pixmap.scaled(90, 90, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                self.logo_preview.setPixmap(scaled)
        else:
            self.logo_preview.clear()
            self.logo_preview.setText("No Logo")
        
        # Update icon preview
        if os.path.exists(APP_ICON_PATH):
            icon = QIcon(APP_ICON_PATH)
            pixmap = icon.pixmap(48, 48)
            self.icon_preview.setPixmap(pixmap)
        else:
            self.icon_preview.clear()
            self.icon_preview.setText("No Icon")
    
    def save_settings(self):
        self.parent.software_name = self.software_name.text()
        
        # Update window title
        self.parent.setWindowTitle(f"{self.parent.software_name} - {DEVELOPER_NAME}")
        
        # Update status bar
        self.parent.status_bar.showMessage(f"Welcome to {self.parent.software_name}")
        
        self.accept()