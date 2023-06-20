import smtplib

import requests
import yagmail
from PySide6.QtWidgets import QMessageBox
from ui_MainWindow import *

API_URL = "http://0.0.0.0:8000/api"


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Setup the UI from the UI file
        self.setupUi(self)

        # API key authentication
        self.api_key: str
        self.api_key_login_button.clicked.connect(self.api_key_auth)

        # Event details
        self.event_details: dict

        # Mailing list
        self.server: yagmail.SMTP
        self.attachments: list

        self.mailing_list_email_login_button.clicked.connect(self.mailing_list_auth)

    def api_key_auth(self):
        """
        Authenticate the event head through the API.
        """
        api_key = self.api_key_field.text()
        request = requests.get(f"{API_URL}/api-key", params={"api-key": api_key})

        if request.status_code == 200:
            self.api_key = api_key
            QMessageBox.information(
                self, "Success!", f"Successfully logged in as {request.json()['user']}!"
            )
            self.api_key_field.setEnabled(False)
            self.api_key_login_button.setEnabled(False)
            self.main_window_tabs.setEnabled(True)
            self.post_api_key_auth()
            return

        QMessageBox.warning(self, "Invalid Credentials", "Invalid API key!")

    def post_api_key_auth(self):
        self.event_details = requests.get(
            f"{API_URL}/event/details", params={"api-key": self.api_key}
        ).json()
        self.fill_recipients_combo_box()

    def mailing_list_auth(self):
        try:
            email_address = self.mailing_list_email_address_field.text()

            email_password = self.mailing_list_email_password_field.text()

            self.server = yagmail.SMTP(
                email_address,
                email_password,
                host="smtp.office365.com",
                port=587,
                smtp_starttls=True,
                smtp_ssl=False,
            )

            self.server.send(to="test@gmail.com", subject="test")

            QMessageBox.information(
                self, "Success!", f"Successfully logged into {email_address}!"
            )

            self.mailing_list_email_address_field.setEnabled(False)
            self.mailing_list_email_password_field.setEnabled(False)

            self.mailing_list_recipients_combo_box.setEnabled(True)
            self.mailing_list_subject_field.setEnabled(True)
            self.mailing_list_mail_body_field.setEnabled(True)
            self.mailing_list_add_attachments_button.setEnabled(True)
            self.mailing_list_send_email_button.setEnabled(True)

        except smtplib.SMTPAuthenticationError:
            QMessageBox.warning(
                self, "Invalid Credentials", "Invalid email address or password!"
            )

        except Exception as e:
            QMessageBox.warning(
                self, "Error", f"An error occurred while logging in: {e}"
            )

    def fill_recipients_combo_box(self):
        self.mailing_list_recipients_combo_box.addItem("All participants")

        for event in self.event_details:
            self.mailing_list_recipients_combo_box.addItem(event["event_name"])


app = QApplication([])
app.setStyle("Fusion")

window = MainWindow()
window.show()

app.exec()
