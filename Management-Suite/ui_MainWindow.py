# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowOKRWfl.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTextEdit, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

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
        self.verticalLayout_8 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
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


        self.verticalLayout_8.addLayout(self.horizontalLayout_3)

        self.main_widget = QWidget(self.centralwidget)
        self.main_widget.setObjectName(u"main_widget")
        self.main_widget.setEnabled(False)
        self.verticalLayout = QVBoxLayout(self.main_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main_window_tabs = QTabWidget(self.main_widget)
        self.main_window_tabs.setObjectName(u"main_window_tabs")
        self.main_window_tabs.setEnabled(True)
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
        self.verticalLayout_3 = QVBoxLayout(self.on_spot_registration_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
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


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.on_spot_registration_event_label = QLabel(self.on_spot_registration_tab)
        self.on_spot_registration_event_label.setObjectName(u"on_spot_registration_event_label")

        self.horizontalLayout_16.addWidget(self.on_spot_registration_event_label)

        self.on_spot_registration_event_combo_box = QComboBox(self.on_spot_registration_tab)
        self.on_spot_registration_event_combo_box.setObjectName(u"on_spot_registration_event_combo_box")

        self.horizontalLayout_16.addWidget(self.on_spot_registration_event_combo_box)


        self.verticalLayout_3.addLayout(self.horizontalLayout_16)

        self.line_3 = QFrame(self.on_spot_registration_tab)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_3)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.line_7 = QFrame(self.on_spot_registration_tab)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_7, 0, 1, 1, 1)

        self.line_5 = QFrame(self.on_spot_registration_tab)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_5, 1, 0, 1, 1)

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


        self.gridLayout_11.addLayout(self.gridLayout_8, 4, 2, 1, 1)

        self.line_10 = QFrame(self.on_spot_registration_tab)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_10, 6, 1, 1, 1)

        self.line_11 = QFrame(self.on_spot_registration_tab)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_11, 3, 0, 1, 1)

        self.line_8 = QFrame(self.on_spot_registration_tab)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_8, 2, 1, 1, 1)

        self.line_6 = QFrame(self.on_spot_registration_tab)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_6, 1, 2, 1, 1)

        self.line_9 = QFrame(self.on_spot_registration_tab)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_9, 4, 1, 1, 1)

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


        self.gridLayout_11.addLayout(self.gridLayout_9, 6, 0, 1, 1)

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


        self.gridLayout_11.addLayout(self.gridLayout_6, 2, 2, 1, 1)

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


        self.gridLayout_11.addLayout(self.gridLayout_7, 4, 0, 1, 1)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.on_spot_registration_member_name_label_8 = QLabel(self.on_spot_registration_tab)
        self.on_spot_registration_member_name_label_8.setObjectName(u"on_spot_registration_member_name_label_8")

        self.gridLayout_10.addWidget(self.on_spot_registration_member_name_label_8, 0, 0, 1, 1)

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

        self.on_spot_registration_member_name_field_8 = QLineEdit(self.on_spot_registration_tab)
        self.on_spot_registration_member_name_field_8.setObjectName(u"on_spot_registration_member_name_field_8")

        self.gridLayout_10.addWidget(self.on_spot_registration_member_name_field_8, 0, 1, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_10, 6, 2, 1, 1)

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


        self.gridLayout_11.addLayout(self.gridLayout_2, 0, 0, 1, 1)

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


        self.gridLayout_11.addLayout(self.gridLayout_4, 0, 2, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.on_spot_registration_member_phone_field_3 = QLineEdit(self.on_spot_registration_tab)
        self.on_spot_registration_member_phone_field_3.setObjectName(u"on_spot_registration_member_phone_field_3")

        self.gridLayout_5.addWidget(self.on_spot_registration_member_phone_field_3, 2, 1, 1, 1)

        self.on_spot_registration_member_email_label_3 = QLabel(self.on_spot_registration_tab)
        self.on_spot_registration_member_email_label_3.setObjectName(u"on_spot_registration_member_email_label_3")

        self.gridLayout_5.addWidget(self.on_spot_registration_member_email_label_3, 1, 0, 1, 1)

        self.on_spot_registration_member_phone_label_3 = QLabel(self.on_spot_registration_tab)
        self.on_spot_registration_member_phone_label_3.setObjectName(u"on_spot_registration_member_phone_label_3")

        self.gridLayout_5.addWidget(self.on_spot_registration_member_phone_label_3, 2, 0, 1, 1)

        self.on_spot_registration_member_name_label_3 = QLabel(self.on_spot_registration_tab)
        self.on_spot_registration_member_name_label_3.setObjectName(u"on_spot_registration_member_name_label_3")

        self.gridLayout_5.addWidget(self.on_spot_registration_member_name_label_3, 0, 0, 1, 1)

        self.on_spot_registration_member_email_field_3 = QLineEdit(self.on_spot_registration_tab)
        self.on_spot_registration_member_email_field_3.setObjectName(u"on_spot_registration_member_email_field_3")

        self.gridLayout_5.addWidget(self.on_spot_registration_member_email_field_3, 1, 1, 1, 1)

        self.on_spot_registration_member_name_field_3 = QLineEdit(self.on_spot_registration_tab)
        self.on_spot_registration_member_name_field_3.setObjectName(u"on_spot_registration_member_name_field_3")

        self.gridLayout_5.addWidget(self.on_spot_registration_member_name_field_3, 0, 1, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_5, 2, 0, 1, 1)

        self.line_12 = QFrame(self.on_spot_registration_tab)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_12, 3, 2, 1, 1)

        self.line_13 = QFrame(self.on_spot_registration_tab)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_13, 5, 0, 1, 1)

        self.line_14 = QFrame(self.on_spot_registration_tab)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_14, 5, 2, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_11)

        self.line_15 = QFrame(self.on_spot_registration_tab)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.HLine)
        self.line_15.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_15)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_18)

        self.on_spot_registration_create_team_button = QPushButton(self.on_spot_registration_tab)
        self.on_spot_registration_create_team_button.setObjectName(u"on_spot_registration_create_team_button")

        self.horizontalLayout_15.addWidget(self.on_spot_registration_create_team_button)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_19)


        self.verticalLayout_3.addLayout(self.horizontalLayout_15)

        self.main_window_tabs.addTab(self.on_spot_registration_tab, "")
        self.event_member_details_tab = QWidget()
        self.event_member_details_tab.setObjectName(u"event_member_details_tab")
        self.verticalLayout_7 = QVBoxLayout(self.event_member_details_tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.event_member_details_event_label = QLabel(self.event_member_details_tab)
        self.event_member_details_event_label.setObjectName(u"event_member_details_event_label")

        self.horizontalLayout_18.addWidget(self.event_member_details_event_label)

        self.event_member_details_combo_box = QComboBox(self.event_member_details_tab)
        self.event_member_details_combo_box.setObjectName(u"event_member_details_combo_box")

        self.horizontalLayout_18.addWidget(self.event_member_details_combo_box)


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
        self.update_details_tab = QWidget()
        self.update_details_tab.setObjectName(u"update_details_tab")
        self.horizontalLayout_30 = QHBoxLayout(self.update_details_tab)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.update_details_team_id_label = QLabel(self.update_details_tab)
        self.update_details_team_id_label.setObjectName(u"update_details_team_id_label")

        self.horizontalLayout_10.addWidget(self.update_details_team_id_label)

        self.update_details_team_id_field = QLineEdit(self.update_details_tab)
        self.update_details_team_id_field.setObjectName(u"update_details_team_id_field")

        self.horizontalLayout_10.addWidget(self.update_details_team_id_field)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_11)

        self.update_details_load_team_details_button = QPushButton(self.update_details_tab)
        self.update_details_load_team_details_button.setObjectName(u"update_details_load_team_details_button")

        self.horizontalLayout_13.addWidget(self.update_details_load_team_details_button)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_10)


        self.verticalLayout_4.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.update_details_team_name_label = QLabel(self.update_details_tab)
        self.update_details_team_name_label.setObjectName(u"update_details_team_name_label")

        self.horizontalLayout_11.addWidget(self.update_details_team_name_label)

        self.update_details_team_name_field = QLineEdit(self.update_details_tab)
        self.update_details_team_name_field.setObjectName(u"update_details_team_name_field")
        self.update_details_team_name_field.setEnabled(False)

        self.horizontalLayout_11.addWidget(self.update_details_team_name_field)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.update_details_team_school_label = QLabel(self.update_details_tab)
        self.update_details_team_school_label.setObjectName(u"update_details_team_school_label")

        self.horizontalLayout_12.addWidget(self.update_details_team_school_label)

        self.update_details_team_school_field = QLineEdit(self.update_details_tab)
        self.update_details_team_school_field.setObjectName(u"update_details_team_school_field")
        self.update_details_team_school_field.setEnabled(False)

        self.horizontalLayout_12.addWidget(self.update_details_team_school_field)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_14)

        self.update_details_update_team_details_button = QPushButton(self.update_details_tab)
        self.update_details_update_team_details_button.setObjectName(u"update_details_update_team_details_button")
        self.update_details_update_team_details_button.setEnabled(False)

        self.horizontalLayout_21.addWidget(self.update_details_update_team_details_button)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_15)


        self.verticalLayout_4.addLayout(self.horizontalLayout_21)

        self.update_details_updated_team_details_display_label = QLabel(self.update_details_tab)
        self.update_details_updated_team_details_display_label.setObjectName(u"update_details_updated_team_details_display_label")

        self.verticalLayout_4.addWidget(self.update_details_updated_team_details_display_label)

        self.update_details_updated_team_details_tree = QTreeWidget(self.update_details_tab)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"1");
        self.update_details_updated_team_details_tree.setHeaderItem(__qtreewidgetitem1)
        self.update_details_updated_team_details_tree.setObjectName(u"update_details_updated_team_details_tree")

        self.verticalLayout_4.addWidget(self.update_details_updated_team_details_tree)


        self.horizontalLayout_30.addLayout(self.verticalLayout_4)

        self.line_4 = QFrame(self.update_details_tab)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_30.addWidget(self.line_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.update_details_user_id_label = QLabel(self.update_details_tab)
        self.update_details_user_id_label.setObjectName(u"update_details_user_id_label")

        self.horizontalLayout_23.addWidget(self.update_details_user_id_label)

        self.update_details_user_id_field = QLineEdit(self.update_details_tab)
        self.update_details_user_id_field.setObjectName(u"update_details_user_id_field")

        self.horizontalLayout_23.addWidget(self.update_details_user_id_field)


        self.verticalLayout_5.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_16)

        self.update_details_load_user_details_button = QPushButton(self.update_details_tab)
        self.update_details_load_user_details_button.setObjectName(u"update_details_load_user_details_button")

        self.horizontalLayout_24.addWidget(self.update_details_load_user_details_button)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_17)


        self.verticalLayout_5.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.update_details_user_name_label = QLabel(self.update_details_tab)
        self.update_details_user_name_label.setObjectName(u"update_details_user_name_label")

        self.horizontalLayout_25.addWidget(self.update_details_user_name_label)

        self.update_details_user_name_field = QLineEdit(self.update_details_tab)
        self.update_details_user_name_field.setObjectName(u"update_details_user_name_field")
        self.update_details_user_name_field.setEnabled(False)

        self.horizontalLayout_25.addWidget(self.update_details_user_name_field)


        self.verticalLayout_5.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.update_details_user_email_label = QLabel(self.update_details_tab)
        self.update_details_user_email_label.setObjectName(u"update_details_user_email_label")

        self.horizontalLayout_26.addWidget(self.update_details_user_email_label)

        self.update_details_user_email_field = QLineEdit(self.update_details_tab)
        self.update_details_user_email_field.setObjectName(u"update_details_user_email_field")
        self.update_details_user_email_field.setEnabled(False)

        self.horizontalLayout_26.addWidget(self.update_details_user_email_field)


        self.verticalLayout_5.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.update_details_user_phone_label = QLabel(self.update_details_tab)
        self.update_details_user_phone_label.setObjectName(u"update_details_user_phone_label")

        self.horizontalLayout_28.addWidget(self.update_details_user_phone_label)

        self.update_details_user_phone_field = QLineEdit(self.update_details_tab)
        self.update_details_user_phone_field.setObjectName(u"update_details_user_phone_field")
        self.update_details_user_phone_field.setEnabled(False)

        self.horizontalLayout_28.addWidget(self.update_details_user_phone_field)


        self.verticalLayout_5.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.update_details_user_attendance_label = QLabel(self.update_details_tab)
        self.update_details_user_attendance_label.setObjectName(u"update_details_user_attendance_label")

        self.horizontalLayout_29.addWidget(self.update_details_user_attendance_label)

        self.update_details_user_attendance_check_box = QCheckBox(self.update_details_tab)
        self.update_details_user_attendance_check_box.setObjectName(u"update_details_user_attendance_check_box")
        self.update_details_user_attendance_check_box.setEnabled(False)

        self.horizontalLayout_29.addWidget(self.update_details_user_attendance_check_box)


        self.verticalLayout_5.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_20)

        self.update_details_update_user_details_button = QPushButton(self.update_details_tab)
        self.update_details_update_user_details_button.setObjectName(u"update_details_update_user_details_button")
        self.update_details_update_user_details_button.setEnabled(False)

        self.horizontalLayout_27.addWidget(self.update_details_update_user_details_button)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_21)


        self.verticalLayout_5.addLayout(self.horizontalLayout_27)

        self.update_details_updated_user_details_display_label = QLabel(self.update_details_tab)
        self.update_details_updated_user_details_display_label.setObjectName(u"update_details_updated_user_details_display_label")

        self.verticalLayout_5.addWidget(self.update_details_updated_user_details_display_label)

        self.update_details_updated_user_details_tree = QTreeWidget(self.update_details_tab)
        __qtreewidgetitem2 = QTreeWidgetItem()
        __qtreewidgetitem2.setText(0, u"1");
        self.update_details_updated_user_details_tree.setHeaderItem(__qtreewidgetitem2)
        self.update_details_updated_user_details_tree.setObjectName(u"update_details_updated_user_details_tree")

        self.verticalLayout_5.addWidget(self.update_details_updated_user_details_tree)


        self.horizontalLayout_30.addLayout(self.verticalLayout_5)

        self.main_window_tabs.addTab(self.update_details_tab, "")

        self.verticalLayout.addWidget(self.main_window_tabs)


        self.verticalLayout_8.addWidget(self.main_widget)

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


        self.verticalLayout_8.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.main_window_tabs.setCurrentIndex(3)


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
        self.on_spot_registration_member_name_label_8.setText(QCoreApplication.translate("MainWindow", u"Member Name 8:", None))
        self.on_spot_registration_member_email_label_8.setText(QCoreApplication.translate("MainWindow", u"Member Email 8:", None))
        self.on_spot_registration_member_email_field_8.setText("")
        self.on_spot_registration_member_phone_label_8.setText(QCoreApplication.translate("MainWindow", u"Member Phone 8:", None))
        self.on_spot_registration_member_phone_field_8.setText("")
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
        self.on_spot_registration_member_phone_field_3.setText("")
        self.on_spot_registration_member_email_label_3.setText(QCoreApplication.translate("MainWindow", u"Member Email 3:", None))
        self.on_spot_registration_member_phone_label_3.setText(QCoreApplication.translate("MainWindow", u"Member Phone 3:", None))
        self.on_spot_registration_member_name_label_3.setText(QCoreApplication.translate("MainWindow", u"Member Name 3:", None))
        self.on_spot_registration_member_email_field_3.setText("")
        self.on_spot_registration_create_team_button.setText(QCoreApplication.translate("MainWindow", u"Create Team", None))
        self.main_window_tabs.setTabText(self.main_window_tabs.indexOf(self.on_spot_registration_tab), QCoreApplication.translate("MainWindow", u"On Spot Registration", None))
        self.event_member_details_event_label.setText(QCoreApplication.translate("MainWindow", u"Event:", None))
        self.event_member_details_refresh_button.setText(QCoreApplication.translate("MainWindow", u"Refresh Details", None))
        self.main_window_tabs.setTabText(self.main_window_tabs.indexOf(self.event_member_details_tab), QCoreApplication.translate("MainWindow", u"Event Member Details", None))
        self.update_details_team_id_label.setText(QCoreApplication.translate("MainWindow", u"Team ID:", None))
        self.update_details_load_team_details_button.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.update_details_team_name_label.setText(QCoreApplication.translate("MainWindow", u"Team Name:", None))
        self.update_details_team_school_label.setText(QCoreApplication.translate("MainWindow", u"Team School:", None))
        self.update_details_update_team_details_button.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.update_details_updated_team_details_display_label.setText(QCoreApplication.translate("MainWindow", u"Updated Team Details:", None))
        self.update_details_user_id_label.setText(QCoreApplication.translate("MainWindow", u"User ID:", None))
        self.update_details_load_user_details_button.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.update_details_user_name_label.setText(QCoreApplication.translate("MainWindow", u"User Name:", None))
        self.update_details_user_email_label.setText(QCoreApplication.translate("MainWindow", u"User Email:", None))
        self.update_details_user_phone_label.setText(QCoreApplication.translate("MainWindow", u"User Phone:", None))
        self.update_details_user_attendance_label.setText(QCoreApplication.translate("MainWindow", u"User Attendance:", None))
        self.update_details_user_attendance_check_box.setText("")
        self.update_details_update_user_details_button.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.update_details_updated_user_details_display_label.setText(QCoreApplication.translate("MainWindow", u"Updated User Details:", None))
        self.main_window_tabs.setTabText(self.main_window_tabs.indexOf(self.update_details_tab), QCoreApplication.translate("MainWindow", u"Update Details", None))
        self.api_key_label.setText(QCoreApplication.translate("MainWindow", u"API Key:", None))
        self.api_key_login_button.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.copyright_label.setText(QCoreApplication.translate("MainWindow", u"Copyright \u00a9 2023 National Public School Indiranagar. All rights reserved.", None))
    # retranslateUi

