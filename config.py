# config.py
import os

# Fixed developer information
DEVELOPER_NAME = "জাকির হোসেন"
DEVELOPER_WHATSAPP = "01307731628"
DEVELOPER_INFO = f"Developed by {DEVELOPER_NAME}\nWhatsApp: {DEVELOPER_WHATSAPP}"

# Fixed company credentials
COMPANY_NAME = "Your Company Name"  # আপনার কোম্পানির নাম দিন
COMPANY_PASSWORD = "admin123"

# Software name
SOFTWARE_NAME = "Business Pilot"  # সফটওয়ারের নাম

# Database file
DB_FILE = 'business_management.db'

# Logo paths
LOGO_FOLDER = 'logo'
COMPANY_LOGO_PATH = os.path.join(LOGO_FOLDER, 'company_logo.png')
APP_ICON_PATH = os.path.join(LOGO_FOLDER, 'app_icon.ico')

# Create logo folder if not exists
if not os.path.exists(LOGO_FOLDER):
    os.makedirs(LOGO_FOLDER)