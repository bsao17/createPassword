# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_password.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
                               QFrame, QHBoxLayout, QLabel, QLineEdit,
                               QRadioButton, QSizePolicy, QSpacerItem, QSpinBox,
                               QTextBrowser, QVBoxLayout, QWidget)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(500, 450)
        Dialog.setMinimumSize(QSize(500, 450))
        Dialog.setMaximumSize(QSize(500, 450))
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 481, 431))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.line_3 = QFrame(self.verticalLayoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.input_char_label = QLabel(self.verticalLayoutWidget)
        self.input_char_label.setObjectName(u"input_char_label")
        self.input_char_label.setScaledContents(False)
        self.input_char_label.setAlignment(Qt.AlignBottom | Qt.AlignJustify)

        self.verticalLayout_2.addWidget(self.input_char_label)

        self.input_char = QLineEdit(self.verticalLayoutWidget)
        self.input_char.setObjectName(u"input_char")

        self.verticalLayout_2.addWidget(self.input_char)

        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.default_radio = QRadioButton(self.verticalLayoutWidget)
        self.default_radio.setObjectName(u"default_radio")
        self.default_radio.setCursor(QCursor(Qt.CrossCursor))
        self.default_radio.setFocusPolicy(Qt.StrongFocus)
        self.default_radio.setAcceptDrops(False)
        self.default_radio.setAutoFillBackground(False)
        self.default_radio.setChecked(True)

        self.verticalLayout_5.addWidget(self.default_radio)

        self.char_radio = QRadioButton(self.verticalLayoutWidget)
        self.char_radio.setObjectName(u"char_radio")
        self.char_radio.setEnabled(True)
        self.char_radio.setCursor(QCursor(Qt.CrossCursor))

        self.verticalLayout_5.addWidget(self.char_radio)

        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.char_size_label = QLabel(self.verticalLayoutWidget)
        self.char_size_label.setObjectName(u"char_size_label")
        self.char_size_label.setAlignment(Qt.AlignBottom | Qt.AlignJustify)

        self.verticalLayout_3.addWidget(self.char_size_label)

        self.char_size = QSpinBox(self.verticalLayoutWidget)
        self.char_size.setObjectName(u"char_size")
        self.char_size.setCursor(QCursor(Qt.ArrowCursor))
        self.char_size.setMouseTracking(False)

        self.verticalLayout_3.addWidget(self.char_size)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_3)

        self.line = QFrame(self.verticalLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.password_display_label = QLabel(self.verticalLayoutWidget)
        self.password_display_label.setObjectName(u"password_display_label")
        self.password_display_label.setTextFormat(Qt.AutoText)
        self.password_display_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.password_display_label)

        self.password_display = QTextBrowser(self.verticalLayoutWidget)
        self.password_display.setObjectName(u"password_display")

        self.verticalLayout.addWidget(self.password_display)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_2)

        self.buttons = QDialogButtonBox(self.verticalLayoutWidget)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setOrientation(Qt.Horizontal)
        self.buttons.setStandardButtons(QDialogButtonBox.Apply | QDialogButtonBox.Reset | QDialogButtonBox.Save)
        self.buttons.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttons)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_4)

        self.line_2 = QFrame(self.verticalLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.retranslateUi(Dialog)
        self.buttons.accepted.connect(Dialog.accept)
        self.buttons.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.input_char_label.setText(
            QCoreApplication.translate("Dialog", u"Entrer les caract\u00e8res qui composeront votre mot de passe",
                                       None))
        self.default_radio.setText(QCoreApplication.translate("Dialog", u"Utiliser les valeurs par d\u00e9faut", None))
        self.char_radio.setText(QCoreApplication.translate("Dialog", u"Utiliser mes caract\u00e8res", None))
        self.char_size_label.setText(QCoreApplication.translate("Dialog", u"Taille du mot de passe", None))
        self.password_display_label.setText(
            QCoreApplication.translate("Dialog", u"Voici votre nouveau mot de passe complexe", None))
    # retranslateUi