# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowPwyqdj.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
                               QHBoxLayout, QHeaderView, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QSizePolicy,
                               QSpacerItem, QSpinBox, QTabWidget, QTextEdit,
                               QTreeWidget, QTreeWidgetItem, QVBoxLayout,
                               QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 872)
        font = QFont()
        font.setFamilies(["JetBrainsMono Nerd Font"])
        font.setPointSize(16)
        MainWindow.setFont(font)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.welcome_label = QLabel(self.centralwidget)
        self.welcome_label.setObjectName("welcome_label")
        font1 = QFont()
        font1.setFamilies(["JetBrainsMono Nerd Font"])
        font1.setPointSize(36)
        self.welcome_label.setFont(font1)

        self.horizontalLayout_3.addWidget(self.welcome_label)

        self.horizontalSpacer_6 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.main_window_tabs = QTabWidget(self.centralwidget)
        self.main_window_tabs.setObjectName("main_window_tabs")
        self.main_window_tabs.setEnabled(False)
        self.main_window_tabs.setTabShape(QTabWidget.Rounded)
        self.mailing_list_tab = QWidget()
        self.mailing_list_tab.setObjectName("mailing_list_tab")
        self.verticalLayout_6 = QVBoxLayout(self.mailing_list_tab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.mailing_list_email_address_label = QLabel(self.mailing_list_tab)
        self.mailing_list_email_address_label.setObjectName(
            "mailing_list_email_address_label"
        )

        self.gridLayout.addWidget(self.mailing_list_email_address_label, 0, 0, 1, 1)

        self.mailing_list_email_address_field = QLineEdit(self.mailing_list_tab)
        self.mailing_list_email_address_field.setObjectName(
            "mailing_list_email_address_field"
        )

        self.gridLayout.addWidget(self.mailing_list_email_address_field, 0, 1, 1, 1)

        self.mailing_list_email_password_label = QLabel(self.mailing_list_tab)
        self.mailing_list_email_password_label.setObjectName(
            "mailing_list_email_password_label"
        )

        self.gridLayout.addWidget(self.mailing_list_email_password_label, 1, 0, 1, 1)

        self.mailing_list_email_password_field = QLineEdit(self.mailing_list_tab)
        self.mailing_list_email_password_field.setObjectName(
            "mailing_list_email_password_field"
        )
        self.mailing_list_email_password_field.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.mailing_list_email_password_field, 1, 1, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.mailing_list_email_login_button = QPushButton(self.mailing_list_tab)
        self.mailing_list_email_login_button.setObjectName(
            "mailing_list_email_login_button"
        )

        self.horizontalLayout_6.addWidget(self.mailing_list_email_login_button)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.line = QFrame(self.mailing_list_tab)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.mailing_list_recipients_label = QLabel(self.mailing_list_tab)
        self.mailing_list_recipients_label.setObjectName(
            "mailing_list_recipients_label"
        )

        self.horizontalLayout_4.addWidget(self.mailing_list_recipients_label)

        self.mailing_list_recipients_combo_box = QComboBox(self.mailing_list_tab)
        self.mailing_list_recipients_combo_box.setObjectName(
            "mailing_list_recipients_combo_box"
        )
        self.mailing_list_recipients_combo_box.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.mailing_list_recipients_combo_box)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.mailing_list_subject_label = QLabel(self.mailing_list_tab)
        self.mailing_list_subject_label.setObjectName("mailing_list_subject_label")

        self.horizontalLayout_5.addWidget(self.mailing_list_subject_label)

        self.mailing_list_subject_field = QLineEdit(self.mailing_list_tab)
        self.mailing_list_subject_field.setObjectName("mailing_list_subject_field")
        self.mailing_list_subject_field.setEnabled(False)

        self.horizontalLayout_5.addWidget(self.mailing_list_subject_field)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.mailing_list_mail_body_label = QLabel(self.mailing_list_tab)
        self.mailing_list_mail_body_label.setObjectName("mailing_list_mail_body_label")

        self.verticalLayout_2.addWidget(self.mailing_list_mail_body_label)

        self.mailing_list_mail_body_field = QTextEdit(self.mailing_list_tab)
        self.mailing_list_mail_body_field.setObjectName("mailing_list_mail_body_field")
        self.mailing_list_mail_body_field.setEnabled(False)

        self.verticalLayout_2.addWidget(self.mailing_list_mail_body_field)

        self.attachments_label = QLabel(self.mailing_list_tab)
        self.attachments_label.setObjectName("attachments_label")

        self.verticalLayout_2.addWidget(self.attachments_label)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalSpacer_4 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.mailing_list_add_attachments_button = QPushButton(self.mailing_list_tab)
        self.mailing_list_add_attachments_button.setObjectName(
            "mailing_list_add_attachments_button"
        )
        self.mailing_list_add_attachments_button.setEnabled(False)

        self.horizontalLayout_7.addWidget(self.mailing_list_add_attachments_button)

        self.horizontalSpacer_7 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.line_2 = QFrame(self.mailing_list_tab)
        self.line_2.setObjectName("line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalSpacer_8 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)

        self.mailing_list_send_email_button = QPushButton(self.mailing_list_tab)
        self.mailing_list_send_email_button.setObjectName(
            "mailing_list_send_email_button"
        )
        self.mailing_list_send_email_button.setEnabled(False)

        self.horizontalLayout_8.addWidget(self.mailing_list_send_email_button)

        self.horizontalSpacer_9 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_8.addItem(self.horizontalSpacer_9)

        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.verticalLayout_6.addLayout(self.verticalLayout_2)

        self.main_window_tabs.addTab(self.mailing_list_tab, "")
        self.on_spot_registration_tab = QWidget()
        self.on_spot_registration_tab.setObjectName("on_spot_registration_tab")
        self.verticalLayout_3 = QVBoxLayout(self.on_spot_registration_tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.on_spot_registration_team_name_label = QLabel(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_team_name_label.setObjectName(
            "on_spot_registration_team_name_label"
        )

        self.horizontalLayout_9.addWidget(self.on_spot_registration_team_name_label)

        self.on_spot_registration_team_name_field = QLineEdit(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_team_name_field.setObjectName(
            "on_spot_registration_team_name_field"
        )

        self.horizontalLayout_9.addWidget(self.on_spot_registration_team_name_field)

        self.on_spot_registration_team_school_label = QLabel(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_team_school_label.setObjectName(
            "on_spot_registration_team_school_label"
        )

        self.horizontalLayout_9.addWidget(self.on_spot_registration_team_school_label)

        self.on_spot_registration_team_school_field = QLineEdit(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_team_school_field.setObjectName(
            "on_spot_registration_team_school_field"
        )

        self.horizontalLayout_9.addWidget(self.on_spot_registration_team_school_field)

        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.on_spot_registration_event_label = QLabel(self.on_spot_registration_tab)
        self.on_spot_registration_event_label.setObjectName(
            "on_spot_registration_event_label"
        )

        self.horizontalLayout_16.addWidget(self.on_spot_registration_event_label)

        self.on_spot_registration_event_combo_box = QComboBox(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_event_combo_box.setObjectName(
            "on_spot_registration_event_combo_box"
        )

        self.horizontalLayout_16.addWidget(self.on_spot_registration_event_combo_box)

        self.verticalLayout_3.addLayout(self.horizontalLayout_16)

        self.line_3 = QFrame(self.on_spot_registration_tab)
        self.line_3.setObjectName("line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_3)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.line_7 = QFrame(self.on_spot_registration_tab)
        self.line_7.setObjectName("line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_7, 0, 1, 1, 1)

        self.line_5 = QFrame(self.on_spot_registration_tab)
        self.line_5.setObjectName("line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_5, 1, 0, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.on_spot_registration_member_name_label_6 = QLabel(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_name_label_6.setObjectName(
            "on_spot_registration_member_name_label_6"
        )

        self.gridLayout_8.addWidget(
            self.on_spot_registration_member_name_label_6, 0, 0, 1, 1
        )

        self.on_spot_registration_member_name_field_6 = QLineEdit(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_name_field_6.setObjectName(
            "on_spot_registration_member_name_field_6"
        )

        self.gridLayout_8.addWidget(
            self.on_spot_registration_member_name_field_6, 0, 1, 1, 1
        )

        self.on_spot_registration_member_email_label_6 = QLabel(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_email_label_6.setObjectName(
            "on_spot_registration_member_email_label_6"
        )

        self.gridLayout_8.addWidget(
            self.on_spot_registration_member_email_label_6, 1, 0, 1, 1
        )

        self.on_spot_registration_member_email_field_6 = QLineEdit(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_email_field_6.setObjectName(
            "on_spot_registration_member_email_field_6"
        )

        self.gridLayout_8.addWidget(
            self.on_spot_registration_member_email_field_6, 1, 1, 1, 1
        )

        self.on_spot_registration_member_phone_label_6 = QLabel(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_phone_label_6.setObjectName(
            "on_spot_registration_member_phone_label_6"
        )

        self.gridLayout_8.addWidget(
            self.on_spot_registration_member_phone_label_6, 2, 0, 1, 1
        )

        self.on_spot_registration_member_phone_field_6 = QLineEdit(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_phone_field_6.setObjectName(
            "on_spot_registration_member_phone_field_6"
        )

        self.gridLayout_8.addWidget(
            self.on_spot_registration_member_phone_field_6, 2, 1, 1, 1
        )

        self.gridLayout_11.addLayout(self.gridLayout_8, 4, 2, 1, 1)

        self.line_10 = QFrame(self.on_spot_registration_tab)
        self.line_10.setObjectName("line_10")
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_10, 6, 1, 1, 1)

        self.line_11 = QFrame(self.on_spot_registration_tab)
        self.line_11.setObjectName("line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_11, 3, 0, 1, 1)

        self.line_8 = QFrame(self.on_spot_registration_tab)
        self.line_8.setObjectName("line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_8, 2, 1, 1, 1)

        self.line_6 = QFrame(self.on_spot_registration_tab)
        self.line_6.setObjectName("line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_6, 1, 2, 1, 1)

        self.line_9 = QFrame(self.on_spot_registration_tab)
        self.line_9.setObjectName("line_9")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_9, 4, 1, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.on_spot_registration_member_name_label_7 = QLabel(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_name_label_7.setObjectName(
            "on_spot_registration_member_name_label_7"
        )

        self.gridLayout_9.addWidget(
            self.on_spot_registration_member_name_label_7, 0, 0, 1, 1
        )

        self.on_spot_registration_member_name_field_7 = QLineEdit(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_name_field_7.setObjectName(
            "on_spot_registration_member_name_field_7"
        )

        self.gridLayout_9.addWidget(
            self.on_spot_registration_member_name_field_7, 0, 1, 1, 1
        )

        self.on_spot_registration_member_email_label_7 = QLabel(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_email_label_7.setObjectName(
            "on_spot_registration_member_email_label_7"
        )

        self.gridLayout_9.addWidget(
            self.on_spot_registration_member_email_label_7, 1, 0, 1, 1
        )

        self.on_spot_registration_member_email_field_7 = QLineEdit(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_email_field_7.setObjectName(
            "on_spot_registration_member_email_field_7"
        )

        self.gridLayout_9.addWidget(
            self.on_spot_registration_member_email_field_7, 1, 1, 1, 1
        )

        self.on_spot_registration_member_phone_label_7 = QLabel(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_phone_label_7.setObjectName(
            "on_spot_registration_member_phone_label_7"
        )

        self.gridLayout_9.addWidget(
            self.on_spot_registration_member_phone_label_7, 2, 0, 1, 1
        )

        self.on_spot_registration_member_phone_field_7 = QLineEdit(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_phone_field_7.setObjectName(
            "on_spot_registration_member_phone_field_7"
        )

        self.gridLayout_9.addWidget(
            self.on_spot_registration_member_phone_field_7, 2, 1, 1, 1
        )

        self.gridLayout_11.addLayout(self.gridLayout_9, 6, 0, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.on_spot_registration_member_name_label_4 = QLabel(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_name_label_4.setObjectName(
            "on_spot_registration_member_name_label_4"
        )

        self.gridLayout_6.addWidget(
            self.on_spot_registration_member_name_label_4, 0, 0, 1, 1
        )

        self.on_spot_registration_member_name_field_4 = QLineEdit(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_name_field_4.setObjectName(
            "on_spot_registration_member_name_field_4"
        )

        self.gridLayout_6.addWidget(
            self.on_spot_registration_member_name_field_4, 0, 1, 1, 1
        )

        self.on_spot_registration_member_email_label_4 = QLabel(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_email_label_4.setObjectName(
            "on_spot_registration_member_email_label_4"
        )

        self.gridLayout_6.addWidget(
            self.on_spot_registration_member_email_label_4, 1, 0, 1, 1
        )

        self.on_spot_registration_member_email_field_4 = QLineEdit(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_email_field_4.setObjectName(
            "on_spot_registration_member_email_field_4"
        )

        self.gridLayout_6.addWidget(
            self.on_spot_registration_member_email_field_4, 1, 1, 1, 1
        )

        self.on_spot_registration_member_phone_label_4 = QLabel(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_phone_label_4.setObjectName(
            "on_spot_registration_member_phone_label_4"
        )

        self.gridLayout_6.addWidget(
            self.on_spot_registration_member_phone_label_4, 2, 0, 1, 1
        )

        self.on_spot_registration_member_phone_field_4 = QLineEdit(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_phone_field_4.setObjectName(
            "on_spot_registration_member_phone_field_4"
        )

        self.gridLayout_6.addWidget(
            self.on_spot_registration_member_phone_field_4, 2, 1, 1, 1
        )

        self.gridLayout_11.addLayout(self.gridLayout_6, 2, 2, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.on_spot_registration_member_name_label_5 = QLabel(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_name_label_5.setObjectName(
            "on_spot_registration_member_name_label_5"
        )

        self.gridLayout_7.addWidget(
            self.on_spot_registration_member_name_label_5, 0, 0, 1, 1
        )

        self.on_spot_registration_member_name_field_5 = QLineEdit(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_name_field_5.setObjectName(
            "on_spot_registration_member_name_field_5"
        )

        self.gridLayout_7.addWidget(
            self.on_spot_registration_member_name_field_5, 0, 1, 1, 1
        )

        self.on_spot_registration_member_email_label_5 = QLabel(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_email_label_5.setObjectName(
            "on_spot_registration_member_email_label_5"
        )

        self.gridLayout_7.addWidget(
            self.on_spot_registration_member_email_label_5, 1, 0, 1, 1
        )

        self.on_spot_registration_member_email_field_5 = QLineEdit(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_email_field_5.setObjectName(
            "on_spot_registration_member_email_field_5"
        )

        self.gridLayout_7.addWidget(
            self.on_spot_registration_member_email_field_5, 1, 1, 1, 1
        )

        self.on_spot_registration_member_phone_label_5 = QLabel(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_phone_label_5.setObjectName(
            "on_spot_registration_member_phone_label_5"
        )

        self.gridLayout_7.addWidget(
            self.on_spot_registration_member_phone_label_5, 2, 0, 1, 1
        )

        self.on_spot_registration_member_phone_field_5 = QLineEdit(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_phone_field_5.setObjectName(
            "on_spot_registration_member_phone_field_5"
        )

        self.gridLayout_7.addWidget(
            self.on_spot_registration_member_phone_field_5, 2, 1, 1, 1
        )

        self.gridLayout_11.addLayout(self.gridLayout_7, 4, 0, 1, 1)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.on_spot_registration_member_name_label_8 = QLabel(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_name_label_8.setObjectName(
            "on_spot_registration_member_name_label_8"
        )

        self.gridLayout_10.addWidget(
            self.on_spot_registration_member_name_label_8, 0, 0, 1, 1
        )

        self.on_spot_registration_member_email_label_8 = QLabel(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_email_label_8.setObjectName(
            "on_spot_registration_member_email_label_8"
        )

        self.gridLayout_10.addWidget(
            self.on_spot_registration_member_email_label_8, 1, 0, 1, 1
        )

        self.on_spot_registration_member_email_field_8 = QLineEdit(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_email_field_8.setObjectName(
            "on_spot_registration_member_email_field_8"
        )

        self.gridLayout_10.addWidget(
            self.on_spot_registration_member_email_field_8, 1, 1, 1, 1
        )

        self.on_spot_registration_member_phone_label_8 = QLabel(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_phone_label_8.setObjectName(
            "on_spot_registration_member_phone_label_8"
        )

        self.gridLayout_10.addWidget(
            self.on_spot_registration_member_phone_label_8, 2, 0, 1, 1
        )

        self.on_spot_registration_member_phone_field_8 = QLineEdit(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_phone_field_8.setObjectName(
            "on_spot_registration_member_phone_field_8"
        )

        self.gridLayout_10.addWidget(
            self.on_spot_registration_member_phone_field_8, 2, 1, 1, 1
        )

        self.on_spot_registration_member_name_field_8 = QLineEdit(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_name_field_8.setObjectName(
            "on_spot_registration_member_name_field_8"
        )

        self.gridLayout_10.addWidget(
            self.on_spot_registration_member_name_field_8, 0, 1, 1, 1
        )

        self.gridLayout_11.addLayout(self.gridLayout_10, 6, 2, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.on_spot_registration_member_name_label_1 = QLabel(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_name_label_1.setObjectName(
            "on_spot_registration_member_name_label_1"
        )

        self.gridLayout_2.addWidget(
            self.on_spot_registration_member_name_label_1, 0, 0, 1, 1
        )

        self.on_spot_registration_member_name_field_1 = QLineEdit(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_name_field_1.setObjectName(
            "on_spot_registration_member_name_field_1"
        )

        self.gridLayout_2.addWidget(
            self.on_spot_registration_member_name_field_1, 0, 1, 1, 1
        )

        self.on_spot_registration_member_email_label_1 = QLabel(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_email_label_1.setObjectName(
            "on_spot_registration_member_email_label_1"
        )

        self.gridLayout_2.addWidget(
            self.on_spot_registration_member_email_label_1, 1, 0, 1, 1
        )

        self.on_spot_registration_member_email_field_1 = QLineEdit(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_email_field_1.setObjectName(
            "on_spot_registration_member_email_field_1"
        )

        self.gridLayout_2.addWidget(
            self.on_spot_registration_member_email_field_1, 1, 1, 1, 1
        )

        self.on_spot_registration_member_phone_label_1 = QLabel(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_phone_label_1.setObjectName(
            "on_spot_registration_member_phone_label_1"
        )

        self.gridLayout_2.addWidget(
            self.on_spot_registration_member_phone_label_1, 2, 0, 1, 1
        )

        self.on_spot_registration_member_phone_field_1 = QLineEdit(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_phone_field_1.setObjectName(
            "on_spot_registration_member_phone_field_1"
        )

        self.gridLayout_2.addWidget(
            self.on_spot_registration_member_phone_field_1, 2, 1, 1, 1
        )

        self.gridLayout_11.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.on_spot_registration_member_name_field_2 = QLineEdit(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_name_field_2.setObjectName(
            "on_spot_registration_member_name_field_2"
        )

        self.gridLayout_4.addWidget(
            self.on_spot_registration_member_name_field_2, 0, 1, 1, 1
        )

        self.on_spot_registration_member_name_label_2 = QLabel(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_name_label_2.setObjectName(
            "on_spot_registration_member_name_label_2"
        )

        self.gridLayout_4.addWidget(
            self.on_spot_registration_member_name_label_2, 0, 0, 1, 1
        )

        self.on_spot_registration_member_phone_field_2 = QLineEdit(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_phone_field_2.setObjectName(
            "on_spot_registration_member_phone_field_2"
        )

        self.gridLayout_4.addWidget(
            self.on_spot_registration_member_phone_field_2, 2, 1, 1, 1
        )

        self.on_spot_registration_member_phone_label_2 = QLabel(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_phone_label_2.setObjectName(
            "on_spot_registration_member_phone_label_2"
        )

        self.gridLayout_4.addWidget(
            self.on_spot_registration_member_phone_label_2, 2, 0, 1, 1
        )

        self.on_spot_registration_member_email_label_2 = QLabel(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_email_label_2.setObjectName(
            "on_spot_registration_member_email_label_2"
        )

        self.gridLayout_4.addWidget(
            self.on_spot_registration_member_email_label_2, 1, 0, 1, 1
        )

        self.on_spot_registration_member_email_field_2 = QLineEdit(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_email_field_2.setObjectName(
            "on_spot_registration_member_email_field_2"
        )

        self.gridLayout_4.addWidget(
            self.on_spot_registration_member_email_field_2, 1, 1, 1, 1
        )

        self.gridLayout_11.addLayout(self.gridLayout_4, 0, 2, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.on_spot_registration_member_phone_field_3 = QLineEdit(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_phone_field_3.setObjectName(
            "on_spot_registration_member_phone_field_3"
        )

        self.gridLayout_5.addWidget(
            self.on_spot_registration_member_phone_field_3, 2, 1, 1, 1
        )

        self.on_spot_registration_member_email_label_3 = QLabel(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_email_label_3.setObjectName(
            "on_spot_registration_member_email_label_3"
        )

        self.gridLayout_5.addWidget(
            self.on_spot_registration_member_email_label_3, 1, 0, 1, 1
        )

        self.on_spot_registration_member_phone_label_3 = QLabel(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_phone_label_3.setObjectName(
            "on_spot_registration_member_phone_label_3"
        )

        self.gridLayout_5.addWidget(
            self.on_spot_registration_member_phone_label_3, 2, 0, 1, 1
        )

        self.on_spot_registration_member_name_label_3 = QLabel(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_name_label_3.setObjectName(
            "on_spot_registration_member_name_label_3"
        )

        self.gridLayout_5.addWidget(
            self.on_spot_registration_member_name_label_3, 0, 0, 1, 1
        )

        self.on_spot_registration_member_email_field_3 = QLineEdit(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_email_field_3.setObjectName(
            "on_spot_registration_member_email_field_3"
        )

        self.gridLayout_5.addWidget(
            self.on_spot_registration_member_email_field_3, 1, 1, 1, 1
        )

        self.on_spot_registration_member_name_field_3 = QLineEdit(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_member_name_field_3.setObjectName(
            "on_spot_registration_member_name_field_3"
        )

        self.gridLayout_5.addWidget(
            self.on_spot_registration_member_name_field_3, 0, 1, 1, 1
        )

        self.gridLayout_11.addLayout(self.gridLayout_5, 2, 0, 1, 1)

        self.line_12 = QFrame(self.on_spot_registration_tab)
        self.line_12.setObjectName("line_12")
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_12, 3, 2, 1, 1)

        self.line_13 = QFrame(self.on_spot_registration_tab)
        self.line_13.setObjectName("line_13")
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_13, 5, 0, 1, 1)

        self.line_14 = QFrame(self.on_spot_registration_tab)
        self.line_14.setObjectName("line_14")
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_14, 5, 2, 1, 1)

        self.verticalLayout_3.addLayout(self.gridLayout_11)

        self.line_15 = QFrame(self.on_spot_registration_tab)
        self.line_15.setObjectName("line_15")
        self.line_15.setFrameShape(QFrame.HLine)
        self.line_15.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_15)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.horizontalSpacer_18 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_15.addItem(self.horizontalSpacer_18)

        self.on_spot_registration_create_team_button = QPushButton(
            self.on_spot_registration_tab
        )
        self.on_spot_registration_create_team_button.setObjectName(
            "on_spot_registration_create_team_button"
        )

        self.horizontalLayout_15.addWidget(self.on_spot_registration_create_team_button)

        self.horizontalSpacer_19 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_15.addItem(self.horizontalSpacer_19)

        self.verticalLayout_3.addLayout(self.horizontalLayout_15)

        self.main_window_tabs.addTab(self.on_spot_registration_tab, "")
        self.update_event_tab = QWidget()
        self.update_event_tab.setObjectName("update_event_tab")
        self.gridLayout_3 = QGridLayout(self.update_event_tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.update_event_event_label = QLabel(self.update_event_tab)
        self.update_event_event_label.setObjectName("update_event_event_label")

        self.horizontalLayout_17.addWidget(self.update_event_event_label)

        self.update_event_combo_box = QComboBox(self.update_event_tab)
        self.update_event_combo_box.setObjectName("update_event_combo_box")

        self.horizontalLayout_17.addWidget(self.update_event_combo_box)

        self.gridLayout_3.addLayout(self.horizontalLayout_17, 0, 0, 1, 2)

        self.line_4 = QFrame(self.update_event_tab)
        self.line_4.setObjectName("line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_4, 1, 0, 1, 2)

        self.update_event_maximum_participants_label = QLabel(self.update_event_tab)
        self.update_event_maximum_participants_label.setObjectName(
            "update_event_maximum_participants_label"
        )

        self.gridLayout_3.addWidget(
            self.update_event_maximum_participants_label, 2, 0, 1, 1
        )

        self.update_event_event_icon_label = QLabel(self.update_event_tab)
        self.update_event_event_icon_label.setObjectName(
            "update_event_event_icon_label"
        )

        self.gridLayout_3.addWidget(self.update_event_event_icon_label, 2, 1, 1, 1)

        self.update_event_maximum_participants_spinbox = QSpinBox(self.update_event_tab)
        self.update_event_maximum_participants_spinbox.setObjectName(
            "update_event_maximum_participants_spinbox"
        )

        self.gridLayout_3.addWidget(
            self.update_event_maximum_participants_spinbox, 3, 0, 1, 1
        )

        self.update_event_event_icon_field = QLineEdit(self.update_event_tab)
        self.update_event_event_icon_field.setObjectName(
            "update_event_event_icon_field"
        )

        self.gridLayout_3.addWidget(self.update_event_event_icon_field, 3, 1, 1, 1)

        self.update_event_event_tagline_label = QLabel(self.update_event_tab)
        self.update_event_event_tagline_label.setObjectName(
            "update_event_event_tagline_label"
        )

        self.gridLayout_3.addWidget(self.update_event_event_tagline_label, 4, 0, 1, 1)

        self.update_event_event_rules_label = QLabel(self.update_event_tab)
        self.update_event_event_rules_label.setObjectName(
            "update_event_event_rules_label"
        )

        self.gridLayout_3.addWidget(self.update_event_event_rules_label, 4, 1, 1, 1)

        self.update_event_event_tagline_field = QTextEdit(self.update_event_tab)
        self.update_event_event_tagline_field.setObjectName(
            "update_event_event_tagline_field"
        )

        self.gridLayout_3.addWidget(self.update_event_event_tagline_field, 5, 0, 1, 1)

        self.update_event_event_rules_field = QTextEdit(self.update_event_tab)
        self.update_event_event_rules_field.setObjectName(
            "update_event_event_rules_field"
        )

        self.gridLayout_3.addWidget(self.update_event_event_rules_field, 5, 1, 1, 1)

        self.update_event_event_description_label = QLabel(self.update_event_tab)
        self.update_event_event_description_label.setObjectName(
            "update_event_event_description_label"
        )

        self.gridLayout_3.addWidget(
            self.update_event_event_description_label, 6, 0, 1, 1
        )

        self.update_event_event_heads_label = QLabel(self.update_event_tab)
        self.update_event_event_heads_label.setObjectName(
            "update_event_event_heads_label"
        )

        self.gridLayout_3.addWidget(self.update_event_event_heads_label, 6, 1, 1, 1)

        self.update_event_event_description_field = QTextEdit(self.update_event_tab)
        self.update_event_event_description_field.setObjectName(
            "update_event_event_description_field"
        )

        self.gridLayout_3.addWidget(
            self.update_event_event_description_field, 7, 0, 1, 1
        )

        self.update_event_event_heads_field = QTextEdit(self.update_event_tab)
        self.update_event_event_heads_field.setObjectName(
            "update_event_event_heads_field"
        )

        self.gridLayout_3.addWidget(self.update_event_event_heads_field, 7, 1, 1, 1)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.horizontalSpacer_26 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_21.addItem(self.horizontalSpacer_26)

        self.update_event_update_button = QPushButton(self.update_event_tab)
        self.update_event_update_button.setObjectName("update_event_update_button")

        self.horizontalLayout_21.addWidget(self.update_event_update_button)

        self.horizontalSpacer_27 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_21.addItem(self.horizontalSpacer_27)

        self.gridLayout_3.addLayout(self.horizontalLayout_21, 8, 0, 1, 1)

        self.main_window_tabs.addTab(self.update_event_tab, "")
        self.event_member_details_tab = QWidget()
        self.event_member_details_tab.setObjectName("event_member_details_tab")
        self.verticalLayout_7 = QVBoxLayout(self.event_member_details_tab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.event_member_details_event_label = QLabel(self.event_member_details_tab)
        self.event_member_details_event_label.setObjectName(
            "event_member_details_event_label"
        )

        self.horizontalLayout_18.addWidget(self.event_member_details_event_label)

        self.event_member_details_combo_box = QComboBox(self.event_member_details_tab)
        self.event_member_details_combo_box.setObjectName(
            "event_member_details_combo_box"
        )

        self.horizontalLayout_18.addWidget(self.event_member_details_combo_box)

        self.verticalLayout_7.addLayout(self.horizontalLayout_18)

        self.event_member_details_tree = QTreeWidget(self.event_member_details_tab)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, "1")
        self.event_member_details_tree.setHeaderItem(__qtreewidgetitem)
        self.event_member_details_tree.setObjectName("event_member_details_tree")

        self.verticalLayout_7.addWidget(self.event_member_details_tree)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.horizontalSpacer_28 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_22.addItem(self.horizontalSpacer_28)

        self.event_member_details_refresh_button = QPushButton(
            self.event_member_details_tab
        )
        self.event_member_details_refresh_button.setObjectName(
            "event_member_details_refresh_button"
        )

        self.horizontalLayout_22.addWidget(self.event_member_details_refresh_button)

        self.horizontalSpacer_29 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_22.addItem(self.horizontalSpacer_29)

        self.verticalLayout_7.addLayout(self.horizontalLayout_22)

        self.main_window_tabs.addTab(self.event_member_details_tab, "")

        self.verticalLayout.addWidget(self.main_window_tabs)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.api_key_label = QLabel(self.centralwidget)
        self.api_key_label.setObjectName("api_key_label")
        self.api_key_label.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter
        )

        self.horizontalLayout.addWidget(self.api_key_label)

        self.api_key_field = QLineEdit(self.centralwidget)
        self.api_key_field.setObjectName("api_key_field")
        self.api_key_field.setEchoMode(QLineEdit.Password)

        self.horizontalLayout.addWidget(self.api_key_field)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.api_key_login_button = QPushButton(self.centralwidget)
        self.api_key_login_button.setObjectName("api_key_login_button")

        self.horizontalLayout_2.addWidget(self.api_key_login_button)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.copyright_label = QLabel(self.centralwidget)
        self.copyright_label.setObjectName("copyright_label")
        self.copyright_label.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )

        self.horizontalLayout_2.addWidget(self.copyright_label)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.main_window_tabs.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Mathtrix Management Suite", None)
        )
        self.actionNew.setText(QCoreApplication.translate("MainWindow", "New", None))
        self.welcome_label.setText(
            QCoreApplication.translate(
                "MainWindow", "Welcome to Mathtrix Management Suite", None
            )
        )
        self.mailing_list_email_address_label.setText(
            QCoreApplication.translate("MainWindow", "Email Address:", None)
        )
        self.mailing_list_email_password_label.setText(
            QCoreApplication.translate("MainWindow", "Email Password:", None)
        )
        self.mailing_list_email_login_button.setText(
            QCoreApplication.translate("MainWindow", "Login", None)
        )
        self.mailing_list_recipients_label.setText(
            QCoreApplication.translate("MainWindow", "Recipients:", None)
        )
        self.mailing_list_subject_label.setText(
            QCoreApplication.translate("MainWindow", "Subject:", None)
        )
        self.mailing_list_mail_body_label.setText(
            QCoreApplication.translate("MainWindow", "Mail Body:", None)
        )
        self.attachments_label.setText(
            QCoreApplication.translate("MainWindow", "Attachments:", None)
        )
        self.mailing_list_add_attachments_button.setText(
            QCoreApplication.translate("MainWindow", "Add Attachments", None)
        )
        self.mailing_list_send_email_button.setText(
            QCoreApplication.translate("MainWindow", "Send Email", None)
        )
        self.main_window_tabs.setTabText(
            self.main_window_tabs.indexOf(self.mailing_list_tab),
            QCoreApplication.translate("MainWindow", "Mailing List", None),
        )
        self.on_spot_registration_team_name_label.setText(
            QCoreApplication.translate("MainWindow", "Team Name:", None)
        )
        self.on_spot_registration_team_school_label.setText(
            QCoreApplication.translate("MainWindow", "Team School:", None)
        )
        self.on_spot_registration_event_label.setText(
            QCoreApplication.translate("MainWindow", "Event:", None)
        )
        self.on_spot_registration_member_name_label_6.setText(
            QCoreApplication.translate("MainWindow", "Member Name 6:", None)
        )
        self.on_spot_registration_member_email_label_6.setText(
            QCoreApplication.translate("MainWindow", "Member Email 6:", None)
        )
        self.on_spot_registration_member_email_field_6.setText("")
        self.on_spot_registration_member_phone_label_6.setText(
            QCoreApplication.translate("MainWindow", "Member Phone 6:", None)
        )
        self.on_spot_registration_member_phone_field_6.setText("")
        self.on_spot_registration_member_name_label_7.setText(
            QCoreApplication.translate("MainWindow", "Member Name 7:", None)
        )
        self.on_spot_registration_member_email_label_7.setText(
            QCoreApplication.translate("MainWindow", "Member Email 7:", None)
        )
        self.on_spot_registration_member_email_field_7.setText("")
        self.on_spot_registration_member_phone_label_7.setText(
            QCoreApplication.translate("MainWindow", "Member Phone 7:", None)
        )
        self.on_spot_registration_member_phone_field_7.setText("")
        self.on_spot_registration_member_name_label_4.setText(
            QCoreApplication.translate("MainWindow", "Member Name 4:", None)
        )
        self.on_spot_registration_member_email_label_4.setText(
            QCoreApplication.translate("MainWindow", "Member Email 4:", None)
        )
        self.on_spot_registration_member_email_field_4.setText("")
        self.on_spot_registration_member_phone_label_4.setText(
            QCoreApplication.translate("MainWindow", "Member Phone 4:", None)
        )
        self.on_spot_registration_member_phone_field_4.setText("")
        self.on_spot_registration_member_name_label_5.setText(
            QCoreApplication.translate("MainWindow", "Member Name 5:", None)
        )
        self.on_spot_registration_member_email_label_5.setText(
            QCoreApplication.translate("MainWindow", "Member Email 5:", None)
        )
        self.on_spot_registration_member_email_field_5.setText("")
        self.on_spot_registration_member_phone_label_5.setText(
            QCoreApplication.translate("MainWindow", "Member Phone 5:", None)
        )
        self.on_spot_registration_member_phone_field_5.setText("")
        self.on_spot_registration_member_name_label_8.setText(
            QCoreApplication.translate("MainWindow", "Member Name 8:", None)
        )
        self.on_spot_registration_member_email_label_8.setText(
            QCoreApplication.translate("MainWindow", "Member Email 8:", None)
        )
        self.on_spot_registration_member_email_field_8.setText("")
        self.on_spot_registration_member_phone_label_8.setText(
            QCoreApplication.translate("MainWindow", "Member Phone 8:", None)
        )
        self.on_spot_registration_member_phone_field_8.setText("")
        self.on_spot_registration_member_name_label_1.setText(
            QCoreApplication.translate("MainWindow", "Member Name 1:", None)
        )
        self.on_spot_registration_member_email_label_1.setText(
            QCoreApplication.translate("MainWindow", "Member Email 1:", None)
        )
        self.on_spot_registration_member_email_field_1.setText("")
        self.on_spot_registration_member_phone_label_1.setText(
            QCoreApplication.translate("MainWindow", "Member Phone 1:", None)
        )
        self.on_spot_registration_member_phone_field_1.setText("")
        self.on_spot_registration_member_name_label_2.setText(
            QCoreApplication.translate("MainWindow", "Member Name 2:", None)
        )
        self.on_spot_registration_member_phone_field_2.setText("")
        self.on_spot_registration_member_phone_label_2.setText(
            QCoreApplication.translate("MainWindow", "Member Phone 2:", None)
        )
        self.on_spot_registration_member_email_label_2.setText(
            QCoreApplication.translate("MainWindow", "Member Email 2:", None)
        )
        self.on_spot_registration_member_email_field_2.setText("")
        self.on_spot_registration_member_phone_field_3.setText("")
        self.on_spot_registration_member_email_label_3.setText(
            QCoreApplication.translate("MainWindow", "Member Email 3:", None)
        )
        self.on_spot_registration_member_phone_label_3.setText(
            QCoreApplication.translate("MainWindow", "Member Phone 3:", None)
        )
        self.on_spot_registration_member_name_label_3.setText(
            QCoreApplication.translate("MainWindow", "Member Name 3:", None)
        )
        self.on_spot_registration_member_email_field_3.setText("")
        self.on_spot_registration_create_team_button.setText(
            QCoreApplication.translate("MainWindow", "Create Team", None)
        )
        self.main_window_tabs.setTabText(
            self.main_window_tabs.indexOf(self.on_spot_registration_tab),
            QCoreApplication.translate("MainWindow", "On Spot Registration", None),
        )
        self.update_event_event_label.setText(
            QCoreApplication.translate("MainWindow", "Event:", None)
        )
        self.update_event_maximum_participants_label.setText(
            QCoreApplication.translate("MainWindow", "Maximum Participants:", None)
        )
        self.update_event_event_icon_label.setText(
            QCoreApplication.translate("MainWindow", "Event Icon URL:", None)
        )
        self.update_event_event_tagline_label.setText(
            QCoreApplication.translate("MainWindow", "Event Tagline:", None)
        )
        self.update_event_event_rules_label.setText(
            QCoreApplication.translate("MainWindow", "Event Rules:", None)
        )
        self.update_event_event_description_label.setText(
            QCoreApplication.translate("MainWindow", "Event Description:", None)
        )
        self.update_event_event_heads_label.setText(
            QCoreApplication.translate("MainWindow", "Event Heads:", None)
        )
        self.update_event_update_button.setText(
            QCoreApplication.translate("MainWindow", "Update Event", None)
        )
        self.main_window_tabs.setTabText(
            self.main_window_tabs.indexOf(self.update_event_tab),
            QCoreApplication.translate("MainWindow", "Update Event", None),
        )
        self.event_member_details_event_label.setText(
            QCoreApplication.translate("MainWindow", "Event:", None)
        )
        self.event_member_details_refresh_button.setText(
            QCoreApplication.translate("MainWindow", "Refresh Details", None)
        )
        self.main_window_tabs.setTabText(
            self.main_window_tabs.indexOf(self.event_member_details_tab),
            QCoreApplication.translate("MainWindow", "Event Member Details", None),
        )
        self.api_key_label.setText(
            QCoreApplication.translate("MainWindow", "API Key:", None)
        )
        self.api_key_login_button.setText(
            QCoreApplication.translate("MainWindow", "Login", None)
        )
        self.copyright_label.setText(
            QCoreApplication.translate(
                "MainWindow",
                "Copyright \u00a9 2023 National Public School Indiranagar. All rights reserved.",
                None,
            )
        )

    # retranslateUi
