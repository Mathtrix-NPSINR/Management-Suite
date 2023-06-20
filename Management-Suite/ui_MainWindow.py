# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowWiBRnq.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTextEdit, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1440, 872)
        font = QFont()
        font.setFamilies([u"JetBrainsMono Nerd Font"])
        font.setPointSize(16)
        MainWindow.setFont(font)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.welcome_label = QLabel(self.centralwidget)
        self.welcome_label.setObjectName(u"welcome_label")
        font1 = QFont()
        font1.setFamilies([u"JetBrainsMono Nerd Font"])
        font1.setPointSize(36)
        self.welcome_label.setFont(font1)

        self.horizontalLayout_3.addWidget(self.welcome_label)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.main_window_tabs = QTabWidget(self.centralwidget)
        self.main_window_tabs.setObjectName(u"main_window_tabs")
        self.main_window_tabs.setEnabled(False)
        self.main_window_tabs.setTabShape(QTabWidget.Rounded)
        self.mailing_list_tab = QWidget()
        self.mailing_list_tab.setObjectName(u"mailing_list_tab")
        self.verticalLayout_6 = QVBoxLayout(self.mailing_list_tab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.mailing_list_email_address_label = QLabel(self.mailing_list_tab)
        self.mailing_list_email_address_label.setObjectName(u"mailing_list_email_address_label")

        self.gridLayout.addWidget(self.mailing_list_email_address_label, 0, 0, 1, 1)

        self.mailing_list_email_address_field = QLineEdit(self.mailing_list_tab)
        self.mailing_list_email_address_field.setObjectName(u"mailing_list_email_address_field")

        self.gridLayout.addWidget(self.mailing_list_email_address_field, 0, 1, 1, 1)

        self.mailing_list_email_password_label = QLabel(self.mailing_list_tab)
        self.mailing_list_email_password_label.setObjectName(u"mailing_list_email_password_label")

        self.gridLayout.addWidget(self.mailing_list_email_password_label, 1, 0, 1, 1)

        self.mailing_list_email_password_field = QLineEdit(self.mailing_list_tab)
        self.mailing_list_email_password_field.setObjectName(u"mailing_list_email_password_field")
        self.mailing_list_email_password_field.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.mailing_list_email_password_field, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.mailing_list_email_login_button = QPushButton(self.mailing_list_tab)
        self.mailing_list_email_login_button.setObjectName(u"mailing_list_email_login_button")

        self.horizontalLayout_6.addWidget(self.mailing_list_email_login_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.line = QFrame(self.mailing_list_tab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.mailing_list_recipients_label = QLabel(self.mailing_list_tab)
        self.mailing_list_recipients_label.setObjectName(u"mailing_list_recipients_label")

        self.horizontalLayout_4.addWidget(self.mailing_list_recipients_label)

        self.mailing_list_recipients_combo_box = QComboBox(self.mailing_list_tab)
        self.mailing_list_recipients_combo_box.setObjectName(u"mailing_list_recipients_combo_box")
        self.mailing_list_recipients_combo_box.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.mailing_list_recipients_combo_box)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.mailing_list_subject_label = QLabel(self.mailing_list_tab)
        self.mailing_list_subject_label.setObjectName(u"mailing_list_subject_label")

        self.horizontalLayout_5.addWidget(self.mailing_list_subject_label)

        self.mailing_list_subject_field = QLineEdit(self.mailing_list_tab)
        self.mailing_list_subject_field.setObjectName(u"mailing_list_subject_field")
        self.mailing_list_subject_field.setEnabled(False)

        self.horizontalLayout_5.addWidget(self.mailing_list_subject_field)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.mailing_list_mail_body_label = QLabel(self.mailing_list_tab)
        self.mailing_list_mail_body_label.setObjectName(u"mailing_list_mail_body_label")

        self.verticalLayout_2.addWidget(self.mailing_list_mail_body_label)

        self.mailing_list_mail_body_field = QTextEdit(self.mailing_list_tab)
        self.mailing_list_mail_body_field.setObjectName(u"mailing_list_mail_body_field")
        self.mailing_list_mail_body_field.setEnabled(False)

        self.verticalLayout_2.addWidget(self.mailing_list_mail_body_field)

        self.attachments_label = QLabel(self.mailing_list_tab)
        self.attachments_label.setObjectName(u"attachments_label")

        self.verticalLayout_2.addWidget(self.attachments_label)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.mailing_list_add_attachments_button = QPushButton(self.mailing_list_tab)
        self.mailing_list_add_attachments_button.setObjectName(u"mailing_list_add_attachments_button")
        self.mailing_list_add_attachments_button.setEnabled(False)

        self.horizontalLayout_7.addWidget(self.mailing_list_add_attachments_button)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.line_2 = QFrame(self.mailing_list_tab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)

        self.mailing_list_send_email_button = QPushButton(self.mailing_list_tab)
        self.mailing_list_send_email_button.setObjectName(u"mailing_list_send_email_button")
        self.mailing_list_send_email_button.setEnabled(False)

        self.horizontalLayout_8.addWidget(self.mailing_list_send_email_button)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_9)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)


        self.verticalLayout_6.addLayout(self.verticalLayout_2)

        self.main_window_tabs.addTab(self.mailing_list_tab, "")
        self.on_spot_registration_tab = QWidget()
        self.on_spot_registration_tab.setObjectName(u"on_spot_registration_tab")
        self.verticalLayout_4 = QVBoxLayout(self.on_spot_registration_tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_11)

        self.on_spot_registration_team_name_label = QLabel(self.on_spot_registration_tab)
        self.on_spot_registration_team_name_label.setObjectName(u"on_spot_registration_team_name_label")

        self.horizontalLayout_9.addWidget(self.on_spot_registration_team_name_label)

        self.on_spot_registration_team_name_field = QLineEdit(self.on_spot_registration_tab)
        self.on_spot_registration_team_name_field.setObjectName(u"on_spot_registration_team_name_field")

        self.horizontalLayout_9.addWidget(self.on_spot_registration_team_name_field)

        self.on_spot_registration_team_school_label = QLabel(self.on_spot_registration_tab)
        self.on_spot_registration_team_school_label.setObjectName(u"on_spot_registration_team_school_label")

        self.horizontalLayout_9.addWidget(self.on_spot_registration_team_school_label)

        self.on_spot_registration_team_school_field = QLineEdit(self.on_spot_registration_tab)
        self.on_spot_registration_team_school_field.setObjectName(u"on_spot_registration_team_school_field")

        self.horizontalLayout_9.addWidget(self.on_spot_registration_team_school_field)

        self.on_spot_registration_event_label = QLabel(self.on_spot_registration_tab)
        self.on_spot_registration_event_label.setObjectName(u"on_spot_registration_event_label")

        self.horizontalLayout_9.addWidget(self.on_spot_registration_event_label)

        self.on_spot_registration_event_combo_box = QComboBox(self.on_spot_registration_tab)
        self.on_spot_registration_event_combo_box.setObjectName(u"on_spot_registration_event_combo_box")

        self.horizontalLayout_9.addWidget(self.on_spot_registration_event_combo_box)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_10)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.line_3 = QFrame(self.on_spot_registration_tab)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_3)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_17)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.on_spot_registration_member_name_label_1 = QLabel(self.on_spot_registration_tab)
        self.on_spot_registration_member_name_label_1.setObjectName(u"on_spot_registration_member_name_label_1")

        self.gridLayout_2.addWidget(self.on_spot_registration_member_name_label_1, 0, 0, 1, 1)

        self.on_spot_registration_member_name_field_1 = QLineEdit(self.on_spot_registration_tab)
        self.on_spot_registration_member_name_field_1.setObjectName(u"on_spot_registration_member_name_field_1")

        self.gridLayout_2.addWidget(self.on_spot_registration_member_name_field_1, 0, 1, 1, 1)

        self.on_spot_registration_member_email_label_1 = QLabel(self.on_spot_registration_tab)
        self.on_spot_registration_member_email_label_1.setObjectName(u"on_spot_registration_member_email_label_1")

        self.gridLayout_2.addWidget(self.on_spot_registration_member_email_label_1, 1, 0, 1, 1)

        self.on_spot_registration_member_email_field_1 = QLineEdit(self.on_spot_registration_tab)
        self.on_spot_registration_member_email_field_1.setObjectName(u"on_spot_registration_member_email_field_1")

        self.gridLayout_2.addWidget(self.on_spot_registration_member_email_field_1, 1, 1, 1, 1)

        self.on_spot_registration_member_phone_label_1 = QLabel(self.on_spot_registration_tab)
        self.on_spot_registration_member_phone_label_1.setObjectName(u"on_spot_registration_member_phone_label_1")

        self.gridLayout_2.addWidget(self.on_spot_registration_member_phone_label_1, 2, 0, 1, 1)

        self.on_spot_registration_member_phone_field_1 = QLineEdit(self.on_spot_registration_tab)
        self.on_spot_registration_member_phone_field_1.setObjectName(u"on_spot_registration_member_phone_field_1")

        self.gridLayout_2.addWidget(self.on_spot_registration_member_phone_field_1, 2, 1, 1, 1)


        self.horizontalLayout_10.addLayout(self.gridLayout_2)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_12)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.on_spot_registration_member_name_field_2 = QLineEdit(self.on_spot_registration_tab)
        self.on_spot_registration_member_name_field_2.setObjectName(u"on_spot_registration_member_name_field_2")

        self.gridLayout_4.addWidget(self.on_spot_registration_member_name_field_2, 0, 1, 1, 1)

        self.on_spot_registration_member_name_label_2 = QLabel(self.on_spot_registration_tab)
        self.on_spot_registration_member_name_label_2.setObjectName(u"on_spot_registration_member_name_label_2")

        self.gridLayout_4.addWidget(self.on_spot_registration_member_name_label_2, 0, 0, 1, 1)

        self.on_spot_registration_member_phone_field_2 = QLineEdit(self.on_spot_registration_tab)
        self.on_spot_registration_member_phone_field_2.setObjectName(u"on_spot_registration_member_phone_field_2")

        self.gridLayout_4.addWidget(self.on_spot_registration_member_phone_field_2, 2, 1, 1, 1)

        self.on_spot_registration_member_phone_label_2 = QLabel(self.on_spot_registration_tab)
        self.on_spot_registration_member_phone_label_2.setObjectName(u"on_spot_registration_member_phone_label_2")

        self.gridLayout_4.addWidget(self.on_spot_registration_member_phone_label_2, 2, 0, 1, 1)

        self.on_spot_registration_member_email_label_2 = QLabel(self.on_spot_registration_tab)
        self.on_spot_registration_member_email_label_2.setObjectName(u"on_spot_registration_member_email_label_2")

        self.gridLayout_4.addWidget(self.on_spot_registration_member_email_label_2, 1, 0, 1, 1)

        self.on_spot_registration_member_email_field_2 = QLineEdit(self.on_spot_registration_tab)
        self.on_spot_registration_member_email_field_2.setObjectName(u"on_spot_registration_member_email_field_2")

        self.gridLayout_4.addWidget(self.on_spot_registration_member_email_field_2, 1, 1, 1, 1)


        self.horizontalLayout_10.addLayout(self.gridLayout_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.on_spot_registration_member_name_label_3 = QLabel(self.on_spot_registration_tab)
        self.on_spot_registration_member_name_label_3.setObjectName(u"on_spot_registration_member_name_label_3")

        self.gridLayout_5.addWidget(self.on_spot_registration_member_name_label_3, 0, 0, 1, 1)

        self.on_spot_registration_member_name_field_3 = QLineEdit(self.on_spot_registration_tab)
        self.on_spot_registration_member_name_field_3.setObjectName(u"on_spot_registration_member_name_field_3")

        self.gridLayout_5.addWidget(self.on_spot_registration_member_name_field_3, 0, 1, 1, 1)

        self.on_spot_registration_member_email_label_3 = QLabel(self.on_spot_registration_tab)
        self.on_spot_registration_member_email_label_3.setObjectName(u"on_spot_registration_member_email_label_3")

        self.gridLayout_5.addWidget(self.on_spot_registration_member_email_label_3, 1, 0, 1, 1)

        self.on_spot_registration_member_email_field_3 = QLineEdit(self.on_spot_registration_tab)
        self.on_spot_registration_member_email_field_3.setObjectName(u"on_spot_registration_member_email_field_3")

        self.gridLayout_5.addWidget(self.on_spot_registration_member_email_field_3, 1, 1, 1, 1)

        self.on_spot_registration_member_phone_label_3 = QLabel(self.on_spot_registration_tab)
        self.on_spot_registration_member_phone_label_3.setObjectName(u"on_spot_registration_member_phone_label_3")

        self.gridLayout_5.addWidget(self.on_spot_registration_member_phone_label_3, 2, 0, 1, 1)

        self.on_spot_registration_member_phone_field_3 = QLineEdit(self.on_spot_registration_tab)
        self.on_spot_registration_member_phone_field_3.setObjectName(u"on_spot_registration_member_phone_field_3")

        self.gridLayout_5.addWidget(self.on_spot_registration_member_phone_field_3, 2, 1, 1, 1)


        self.horizontalLayout_11.addLayout(self.gridLayout_5)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_13)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.on_spot_registration_member_name_label_4 = QLabel(self.on_spot_registration_tab)
        self.on_spot_registration_member_name_label_4.setObjectName(u"on_spot_registration_member_name_label_4")

        self.gridLayout_6.addWidget(self.on_spot_registration_member_name_label_4, 0, 0, 1, 1)

        self.on_spot_registration_member_name_field_4 = QLineEdit(self.on_spot_registration_tab)
        self.on_spot_registration_member_name_field_4.setObjectName(u"on_spot_registration_member_name_field_4")

        self.gridLayout_6.addWidget(self.on_spot_registration_member_name_field_4, 0, 1, 1, 1)

        self.on_spot_registration_member_email_label_4 = QLabel(self.on_spot_registration_tab)
        self.on_spot_registration_member_email_label_4.setObjectName(u"on_spot_registration_member_email_label_4")

        self.gridLayout_6.addWidget(self.on_spot_registration_member_email_label_4, 1, 0, 1, 1)

        self.on_spot_registration_member_email_field_4 = QLineEdit(self.on_spot_registration_tab)
        self.on_spot_registration_member_email_field_4.setObjectName(u"on_spot_registration_member_email_field_4")

        self.gridLayout_6.addWidget(self.on_spot_registration_member_email_field_4, 1, 1, 1, 1)

        self.on_spot_registration_member_phone_label_4 = QLabel(self.on_spot_registration_tab)
        self.on_spot_registration_member_phone_label_4.setObjectName(u"on_spot_registration_member_phone_label_4")

        self.gridLayout_6.addWidget(self.on_spot_registration_member_phone_label_4, 2, 0, 1, 1)

        self.on_spot_registration_member_phone_field_4 = QLineEdit(self.on_spot_registration_tab)
        self.on_spot_registration_member_phone_field_4.setObjectName(u"on_spot_registration_member_phone_field_4")

        self.gridLayout_6.addWidget(self.on_spot_registration_member_phone_field_4, 2, 1, 1, 1)


        self.horizontalLayout_11.addLayout(self.gridLayout_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_6)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.on_spot_registration_member_name_label_5 = QLabel(self.on_spot_registration_tab)
        self.on_spot_registration_member_name_label_5.setObjectName(u"on_spot_registration_member_name_label_5")

        self.gridLayout_7.addWidget(self.on_spot_registration_member_name_label_5, 0, 0, 1, 1)

        self.on_spot_registration_member_name_field_5 = QLineEdit(self.on_spot_registration_tab)
        self.on_spot_registration_member_name_field_5.setObjectName(u"on_spot_registration_member_name_field_5")

        self.gridLayout_7.addWidget(self.on_spot_registration_member_name_field_5, 0, 1, 1, 1)

        self.on_spot_registration_member_email_label_5 = QLabel(self.on_spot_registration_tab)
        self.on_spot_registration_member_email_label_5.setObjectName(u"on_spot_registration_member_email_label_5")

        self.gridLayout_7.addWidget(self.on_spot_registration_member_email_label_5, 1, 0, 1, 1)

        self.on_spot_registration_member_email_field_5 = QLineEdit(self.on_spot_registration_tab)
        self.on_spot_registration_member_email_field_5.setObjectName(u"on_spot_registration_member_email_field_5")

        self.gridLayout_7.addWidget(self.on_spot_registration_member_email_field_5, 1, 1, 1, 1)

        self.on_spot_registration_member_phone_label_5 = QLabel(self.on_spot_registration_tab)
        self.on_spot_registration_member_phone_label_5.setObjectName(u"on_spot_registration_member_phone_label_5")

        self.gridLayout_7.addWidget(self.on_spot_registration_member_phone_label_5, 2, 0, 1, 1)

        self.on_spot_registration_member_phone_field_5 = QLineEdit(self.on_spot_registration_tab)
        self.on_spot_registration_member_phone_field_5.setObjectName(u"on_spot_registration_member_phone_field_5")

        self.gridLayout_7.addWidget(self.on_spot_registration_member_phone_field_5, 2, 1, 1, 1)


        self.horizontalLayout_12.addLayout(self.gridLayout_7)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_14)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.on_spot_registration_member_name_label_6 = QLabel(self.on_spot_registration_tab)
        self.on_spot_registration_member_name_label_6.setObjectName(u"on_spot_registration_member_name_label_6")

        self.gridLayout_8.addWidget(self.on_spot_registration_member_name_label_6, 0, 0, 1, 1)

        self.on_spot_registration_member_name_field_6 = QLineEdit(self.on_spot_registration_tab)
        self.on_spot_registration_member_name_field_6.setObjectName(u"on_spot_registration_member_name_field_6")

        self.gridLayout_8.addWidget(self.on_spot_registration_member_name_field_6, 0, 1, 1, 1)

        self.on_spot_registration_member_email_label_6 = QLabel(self.on_spot_registration_tab)
        self.on_spot_registration_member_email_label_6.setObjectName(u"on_spot_registration_member_email_label_6")

        self.gridLayout_8.addWidget(self.on_spot_registration_member_email_label_6, 1, 0, 1, 1)

        self.on_spot_registration_member_email_field_6 = QLineEdit(self.on_spot_registration_tab)
        self.on_spot_registration_member_email_field_6.setObjectName(u"on_spot_registration_member_email_field_6")

        self.gridLayout_8.addWidget(self.on_spot_registration_member_email_field_6, 1, 1, 1, 1)

        self.on_spot_registration_member_phone_label_6 = QLabel(self.on_spot_registration_tab)
        self.on_spot_registration_member_phone_label_6.setObjectName(u"on_spot_registration_member_phone_label_6")

        self.gridLayout_8.addWidget(self.on_spot_registration_member_phone_label_6, 2, 0, 1, 1)

        self.on_spot_registration_member_phone_field_6 = QLineEdit(self.on_spot_registration_tab)
        self.on_spot_registration_member_phone_field_6.setObjectName(u"on_spot_registration_member_phone_field_6")

        self.gridLayout_8.addWidget(self.on_spot_registration_member_phone_field_6, 2, 1, 1, 1)


        self.horizontalLayout_12.addLayout(self.gridLayout_8)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.on_spot_registration_member_name_label_7 = QLabel(self.on_spot_registration_tab)
        self.on_spot_registration_member_name_label_7.setObjectName(u"on_spot_registration_member_name_label_7")

        self.gridLayout_9.addWidget(self.on_spot_registration_member_name_label_7, 0, 0, 1, 1)

        self.on_spot_registration_member_name_field_7 = QLineEdit(self.on_spot_registration_tab)
        self.on_spot_registration_member_name_field_7.setObjectName(u"on_spot_registration_member_name_field_7")

        self.gridLayout_9.addWidget(self.on_spot_registration_member_name_field_7, 0, 1, 1, 1)

        self.on_spot_registration_member_email_label_7 = QLabel(self.on_spot_registration_tab)
        self.on_spot_registration_member_email_label_7.setObjectName(u"on_spot_registration_member_email_label_7")

        self.gridLayout_9.addWidget(self.on_spot_registration_member_email_label_7, 1, 0, 1, 1)

        self.on_spot_registration_member_email_field_7 = QLineEdit(self.on_spot_registration_tab)
        self.on_spot_registration_member_email_field_7.setObjectName(u"on_spot_registration_member_email_field_7")

        self.gridLayout_9.addWidget(self.on_spot_registration_member_email_field_7, 1, 1, 1, 1)

        self.on_spot_registration_member_phone_label_7 = QLabel(self.on_spot_registration_tab)
        self.on_spot_registration_member_phone_label_7.setObjectName(u"on_spot_registration_member_phone_label_7")

        self.gridLayout_9.addWidget(self.on_spot_registration_member_phone_label_7, 2, 0, 1, 1)

        self.on_spot_registration_member_phone_field_7 = QLineEdit(self.on_spot_registration_tab)
        self.on_spot_registration_member_phone_field_7.setObjectName(u"on_spot_registration_member_phone_field_7")

        self.gridLayout_9.addWidget(self.on_spot_registration_member_phone_field_7, 2, 1, 1, 1)


        self.horizontalLayout_13.addLayout(self.gridLayout_9)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_15)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.on_spot_registration_member_name_label_8 = QLabel(self.on_spot_registration_tab)
        self.on_spot_registration_member_name_label_8.setObjectName(u"on_spot_registration_member_name_label_8")

        self.gridLayout_10.addWidget(self.on_spot_registration_member_name_label_8, 0, 0, 1, 1)

        self.on_spot_registration_member_name_field_8 = QLineEdit(self.on_spot_registration_tab)
        self.on_spot_registration_member_name_field_8.setObjectName(u"on_spot_registration_member_name_field_8")

        self.gridLayout_10.addWidget(self.on_spot_registration_member_name_field_8, 0, 1, 1, 1)

        self.on_spot_registration_member_email_label_8 = QLabel(self.on_spot_registration_tab)
        self.on_spot_registration_member_email_label_8.setObjectName(u"on_spot_registration_member_email_label_8")

        self.gridLayout_10.addWidget(self.on_spot_registration_member_email_label_8, 1, 0, 1, 1)

        self.on_spot_registration_member_email_field_8 = QLineEdit(self.on_spot_registration_tab)
        self.on_spot_registration_member_email_field_8.setObjectName(u"on_spot_registration_member_email_field_8")

        self.gridLayout_10.addWidget(self.on_spot_registration_member_email_field_8, 1, 1, 1, 1)

        self.on_spot_registration_member_phone_label_8 = QLabel(self.on_spot_registration_tab)
        self.on_spot_registration_member_phone_label_8.setObjectName(u"on_spot_registration_member_phone_label_8")

        self.gridLayout_10.addWidget(self.on_spot_registration_member_phone_label_8, 2, 0, 1, 1)

        self.on_spot_registration_member_phone_field_8 = QLineEdit(self.on_spot_registration_tab)
        self.on_spot_registration_member_phone_field_8.setObjectName(u"on_spot_registration_member_phone_field_8")

        self.gridLayout_10.addWidget(self.on_spot_registration_member_phone_field_8, 2, 1, 1, 1)


        self.horizontalLayout_13.addLayout(self.gridLayout_10)


        self.verticalLayout_3.addLayout(self.horizontalLayout_13)


        self.horizontalLayout_14.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_16)


        self.verticalLayout_4.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_18)

        self.pushButton = QPushButton(self.on_spot_registration_tab)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_15.addWidget(self.pushButton)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_19)


        self.verticalLayout_4.addLayout(self.horizontalLayout_15)

        self.main_window_tabs.addTab(self.on_spot_registration_tab, "")
        self.update_event_tab = QWidget()
        self.update_event_tab.setObjectName(u"update_event_tab")
        self.verticalLayout_5 = QVBoxLayout(self.update_event_tab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_23)

        self.update_event_event_label = QLabel(self.update_event_tab)
        self.update_event_event_label.setObjectName(u"update_event_event_label")

        self.horizontalLayout_17.addWidget(self.update_event_event_label)

        self.update_event_combo_box = QComboBox(self.update_event_tab)
        self.update_event_combo_box.setObjectName(u"update_event_combo_box")

        self.horizontalLayout_17.addWidget(self.update_event_combo_box)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_22)


        self.verticalLayout_5.addLayout(self.horizontalLayout_17)

        self.line_4 = QFrame(self.update_event_tab)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_4)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.update_event_event_name_label = QLabel(self.update_event_tab)
        self.update_event_event_name_label.setObjectName(u"update_event_event_name_label")

        self.gridLayout_11.addWidget(self.update_event_event_name_label, 0, 0, 1, 1)

        self.update_event_event_icon_label = QLabel(self.update_event_tab)
        self.update_event_event_icon_label.setObjectName(u"update_event_event_icon_label")

        self.gridLayout_11.addWidget(self.update_event_event_icon_label, 0, 1, 1, 1)

        self.update_event_event_name_field = QLineEdit(self.update_event_tab)
        self.update_event_event_name_field.setObjectName(u"update_event_event_name_field")

        self.gridLayout_11.addWidget(self.update_event_event_name_field, 1, 0, 1, 1)

        self.update_event_event_icon_field = QLineEdit(self.update_event_tab)
        self.update_event_event_icon_field.setObjectName(u"update_event_event_icon_field")

        self.gridLayout_11.addWidget(self.update_event_event_icon_field, 1, 1, 1, 1)

        self.update_event_event_tagline_label = QLabel(self.update_event_tab)
        self.update_event_event_tagline_label.setObjectName(u"update_event_event_tagline_label")

        self.gridLayout_11.addWidget(self.update_event_event_tagline_label, 2, 0, 1, 1)

        self.update_event_event_rules_label = QLabel(self.update_event_tab)
        self.update_event_event_rules_label.setObjectName(u"update_event_event_rules_label")

        self.gridLayout_11.addWidget(self.update_event_event_rules_label, 2, 1, 1, 1)

        self.update_event_event_tagline_field = QTextEdit(self.update_event_tab)
        self.update_event_event_tagline_field.setObjectName(u"update_event_event_tagline_field")

        self.gridLayout_11.addWidget(self.update_event_event_tagline_field, 3, 0, 1, 1)

        self.update_event_event_rules_field = QTextEdit(self.update_event_tab)
        self.update_event_event_rules_field.setObjectName(u"update_event_event_rules_field")

        self.gridLayout_11.addWidget(self.update_event_event_rules_field, 3, 1, 1, 1)

        self.update_event_event_description_label = QLabel(self.update_event_tab)
        self.update_event_event_description_label.setObjectName(u"update_event_event_description_label")

        self.gridLayout_11.addWidget(self.update_event_event_description_label, 4, 0, 1, 1)

        self.update_event_event_heads_label = QLabel(self.update_event_tab)
        self.update_event_event_heads_label.setObjectName(u"update_event_event_heads_label")

        self.gridLayout_11.addWidget(self.update_event_event_heads_label, 4, 1, 1, 1)

        self.update_event_event_description_field = QTextEdit(self.update_event_tab)
        self.update_event_event_description_field.setObjectName(u"update_event_event_description_field")

        self.gridLayout_11.addWidget(self.update_event_event_description_field, 5, 0, 1, 1)

        self.update_event_event_heads_field = QTextEdit(self.update_event_tab)
        self.update_event_event_heads_field.setObjectName(u"update_event_event_heads_field")

        self.gridLayout_11.addWidget(self.update_event_event_heads_field, 5, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_11)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_26)

        self.update_event_update_button = QPushButton(self.update_event_tab)
        self.update_event_update_button.setObjectName(u"update_event_update_button")

        self.horizontalLayout_21.addWidget(self.update_event_update_button)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_27)


        self.verticalLayout_5.addLayout(self.horizontalLayout_21)

        self.main_window_tabs.addTab(self.update_event_tab, "")
        self.event_member_details_tab = QWidget()
        self.event_member_details_tab.setObjectName(u"event_member_details_tab")
        self.verticalLayout_7 = QVBoxLayout(self.event_member_details_tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_24)

        self.event_member_details_event_label = QLabel(self.event_member_details_tab)
        self.event_member_details_event_label.setObjectName(u"event_member_details_event_label")

        self.horizontalLayout_18.addWidget(self.event_member_details_event_label)

        self.event_member_details_combo_box = QComboBox(self.event_member_details_tab)
        self.event_member_details_combo_box.setObjectName(u"event_member_details_combo_box")

        self.horizontalLayout_18.addWidget(self.event_member_details_combo_box)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_25)


        self.verticalLayout_7.addLayout(self.horizontalLayout_18)

        self.event_member_details_tree = QTreeWidget(self.event_member_details_tab)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.event_member_details_tree.setHeaderItem(__qtreewidgetitem)
        self.event_member_details_tree.setObjectName(u"event_member_details_tree")

        self.verticalLayout_7.addWidget(self.event_member_details_tree)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_28)

        self.event_member_details_refresh_button = QPushButton(self.event_member_details_tab)
        self.event_member_details_refresh_button.setObjectName(u"event_member_details_refresh_button")

        self.horizontalLayout_22.addWidget(self.event_member_details_refresh_button)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_29)


        self.verticalLayout_7.addLayout(self.horizontalLayout_22)

        self.main_window_tabs.addTab(self.event_member_details_tab, "")

        self.verticalLayout.addWidget(self.main_window_tabs)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.api_key_label = QLabel(self.centralwidget)
        self.api_key_label.setObjectName(u"api_key_label")
        self.api_key_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.api_key_label)

        self.api_key_field = QLineEdit(self.centralwidget)
        self.api_key_field.setObjectName(u"api_key_field")
        self.api_key_field.setEchoMode(QLineEdit.Password)

        self.horizontalLayout.addWidget(self.api_key_field)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.api_key_login_button = QPushButton(self.centralwidget)
        self.api_key_login_button.setObjectName(u"api_key_login_button")

        self.horizontalLayout_2.addWidget(self.api_key_login_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.copyright_label = QLabel(self.centralwidget)
        self.copyright_label.setObjectName(u"copyright_label")
        self.copyright_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.copyright_label)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.main_window_tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Mathtrix Management Suite", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.welcome_label.setText(QCoreApplication.translate("MainWindow", u"Welcome to Mathtrix Management Suite", None))
        self.mailing_list_email_address_label.setText(QCoreApplication.translate("MainWindow", u"Email Address:", None))
        self.mailing_list_email_password_label.setText(QCoreApplication.translate("MainWindow", u"Email Password:", None))
        self.mailing_list_email_login_button.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.mailing_list_recipients_label.setText(QCoreApplication.translate("MainWindow", u"Recipients:", None))
        self.mailing_list_subject_label.setText(QCoreApplication.translate("MainWindow", u"Subject:", None))
        self.mailing_list_mail_body_label.setText(QCoreApplication.translate("MainWindow", u"Mail Body:", None))
        self.attachments_label.setText(QCoreApplication.translate("MainWindow", u"Attachments:", None))
        self.mailing_list_add_attachments_button.setText(QCoreApplication.translate("MainWindow", u"Add Attachments", None))
        self.mailing_list_send_email_button.setText(QCoreApplication.translate("MainWindow", u"Send Email", None))
        self.main_window_tabs.setTabText(self.main_window_tabs.indexOf(self.mailing_list_tab), QCoreApplication.translate("MainWindow", u"Mailing List", None))
        self.on_spot_registration_team_name_label.setText(QCoreApplication.translate("MainWindow", u"Team Name:", None))
        self.on_spot_registration_team_school_label.setText(QCoreApplication.translate("MainWindow", u"Team School:", None))
        self.on_spot_registration_event_label.setText(QCoreApplication.translate("MainWindow", u"Event:", None))
        self.on_spot_registration_member_name_label_1.setText(QCoreApplication.translate("MainWindow", u"Member Name 1:", None))
        self.on_spot_registration_member_email_label_1.setText(QCoreApplication.translate("MainWindow", u"Member Email 1:", None))
        self.on_spot_registration_member_email_field_1.setText("")
        self.on_spot_registration_member_phone_label_1.setText(QCoreApplication.translate("MainWindow", u"Member Phone 1:", None))
        self.on_spot_registration_member_phone_field_1.setText("")
        self.on_spot_registration_member_name_label_2.setText(QCoreApplication.translate("MainWindow", u"Member Name 2:", None))
        self.on_spot_registration_member_phone_field_2.setText("")
        self.on_spot_registration_member_phone_label_2.setText(QCoreApplication.translate("MainWindow", u"Member Phone 2:", None))
        self.on_spot_registration_member_email_label_2.setText(QCoreApplication.translate("MainWindow", u"Member Email 2:", None))
        self.on_spot_registration_member_email_field_2.setText("")
        self.on_spot_registration_member_name_label_3.setText(QCoreApplication.translate("MainWindow", u"Member Name 3:", None))
        self.on_spot_registration_member_email_label_3.setText(QCoreApplication.translate("MainWindow", u"Member Email 3:", None))
        self.on_spot_registration_member_email_field_3.setText("")
        self.on_spot_registration_member_phone_label_3.setText(QCoreApplication.translate("MainWindow", u"Member Phone 3:", None))
        self.on_spot_registration_member_phone_field_3.setText("")
        self.on_spot_registration_member_name_label_4.setText(QCoreApplication.translate("MainWindow", u"Member Name 4:", None))
        self.on_spot_registration_member_email_label_4.setText(QCoreApplication.translate("MainWindow", u"Member Email 4:", None))
        self.on_spot_registration_member_email_field_4.setText("")
        self.on_spot_registration_member_phone_label_4.setText(QCoreApplication.translate("MainWindow", u"Member Phone 4:", None))
        self.on_spot_registration_member_phone_field_4.setText("")
        self.on_spot_registration_member_name_label_5.setText(QCoreApplication.translate("MainWindow", u"Member Name 5:", None))
        self.on_spot_registration_member_email_label_5.setText(QCoreApplication.translate("MainWindow", u"Member Email 5:", None))
        self.on_spot_registration_member_email_field_5.setText("")
        self.on_spot_registration_member_phone_label_5.setText(QCoreApplication.translate("MainWindow", u"Member Phone 5:", None))
        self.on_spot_registration_member_phone_field_5.setText("")
        self.on_spot_registration_member_name_label_6.setText(QCoreApplication.translate("MainWindow", u"Member Name 6:", None))
        self.on_spot_registration_member_email_label_6.setText(QCoreApplication.translate("MainWindow", u"Member Email 6:", None))
        self.on_spot_registration_member_email_field_6.setText("")
        self.on_spot_registration_member_phone_label_6.setText(QCoreApplication.translate("MainWindow", u"Member Phone 6:", None))
        self.on_spot_registration_member_phone_field_6.setText("")
        self.on_spot_registration_member_name_label_7.setText(QCoreApplication.translate("MainWindow", u"Member Name 7:", None))
        self.on_spot_registration_member_email_label_7.setText(QCoreApplication.translate("MainWindow", u"Member Email 7:", None))
        self.on_spot_registration_member_email_field_7.setText("")
        self.on_spot_registration_member_phone_label_7.setText(QCoreApplication.translate("MainWindow", u"Member Phone 7:", None))
        self.on_spot_registration_member_phone_field_7.setText("")
        self.on_spot_registration_member_name_label_8.setText(QCoreApplication.translate("MainWindow", u"Member Name 8:", None))
        self.on_spot_registration_member_email_label_8.setText(QCoreApplication.translate("MainWindow", u"Member Email 8:", None))
        self.on_spot_registration_member_email_field_8.setText("")
        self.on_spot_registration_member_phone_label_8.setText(QCoreApplication.translate("MainWindow", u"Member Phone 8:", None))
        self.on_spot_registration_member_phone_field_8.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Create Team", None))
        self.main_window_tabs.setTabText(self.main_window_tabs.indexOf(self.on_spot_registration_tab), QCoreApplication.translate("MainWindow", u"On Spot Registration", None))
        self.update_event_event_label.setText(QCoreApplication.translate("MainWindow", u"Event:", None))
        self.update_event_event_name_label.setText(QCoreApplication.translate("MainWindow", u"Event Name:", None))
        self.update_event_event_icon_label.setText(QCoreApplication.translate("MainWindow", u"Event Icon URL:", None))
        self.update_event_event_tagline_label.setText(QCoreApplication.translate("MainWindow", u"Event Tagline:", None))
        self.update_event_event_rules_label.setText(QCoreApplication.translate("MainWindow", u"Event Rules:", None))
        self.update_event_event_description_label.setText(QCoreApplication.translate("MainWindow", u"Event Description:", None))
        self.update_event_event_heads_label.setText(QCoreApplication.translate("MainWindow", u"Event Heads:", None))
        self.update_event_update_button.setText(QCoreApplication.translate("MainWindow", u"Update Event", None))
        self.main_window_tabs.setTabText(self.main_window_tabs.indexOf(self.update_event_tab), QCoreApplication.translate("MainWindow", u"Update Event", None))
        self.event_member_details_event_label.setText(QCoreApplication.translate("MainWindow", u"Event:", None))
        self.event_member_details_refresh_button.setText(QCoreApplication.translate("MainWindow", u"Refresh Details", None))
        self.main_window_tabs.setTabText(self.main_window_tabs.indexOf(self.event_member_details_tab), QCoreApplication.translate("MainWindow", u"Event Member Details", None))
        self.api_key_label.setText(QCoreApplication.translate("MainWindow", u"API Key:", None))
        self.api_key_login_button.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.copyright_label.setText(QCoreApplication.translate("MainWindow", u"Copyright \u00a9 2023 National Public School Indiranagar. All rights reserved.", None))
    # retranslateUi

