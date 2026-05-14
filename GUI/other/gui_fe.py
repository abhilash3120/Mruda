# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI_design.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSlider, QSpinBox, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(949, 641)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget_5 = QWidget(self.centralwidget)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(120, 210, 201, 121))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.update = QPushButton(self.gridLayoutWidget_5)
        self.update.setObjectName(u"update")

        self.gridLayout_5.addWidget(self.update, 0, 1, 1, 1)

        self.def_but = QPushButton(self.gridLayoutWidget_5)
        self.def_but.setObjectName(u"def_but")

        self.gridLayout_5.addWidget(self.def_but, 3, 0, 1, 2)

        self.slot_list = QComboBox(self.gridLayoutWidget_5)
        self.slot_list.setObjectName(u"slot_list")

        self.gridLayout_5.addWidget(self.slot_list, 0, 0, 1, 1)

        self.send = QPushButton(self.gridLayoutWidget_5)
        self.send.setObjectName(u"send")

        self.gridLayout_5.addWidget(self.send, 1, 0, 1, 2)

        self.flash = QPushButton(self.gridLayoutWidget_5)
        self.flash.setObjectName(u"flash")

        self.gridLayout_5.addWidget(self.flash, 2, 0, 1, 2)

        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(460, 30, 331, 551))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.v5 = QSpinBox(self.gridLayoutWidget_2)
        self.v5.setObjectName(u"v5")
        self.v5.setMaximum(127)

        self.gridLayout_2.addWidget(self.v5, 5, 1, 1, 1)

        self.v7 = QSpinBox(self.gridLayoutWidget_2)
        self.v7.setObjectName(u"v7")
        self.v7.setMaximum(127)

        self.gridLayout_2.addWidget(self.v7, 7, 1, 1, 1)

        self.s9 = QSlider(self.gridLayoutWidget_2)
        self.s9.setObjectName(u"s9")
        self.s9.setMaximum(127)
        self.s9.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s9, 9, 0, 1, 1)

        self.s6 = QSlider(self.gridLayoutWidget_2)
        self.s6.setObjectName(u"s6")
        self.s6.setMaximum(127)
        self.s6.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s6, 6, 0, 1, 1)

        self.v15 = QSpinBox(self.gridLayoutWidget_2)
        self.v15.setObjectName(u"v15")
        self.v15.setMaximum(127)

        self.gridLayout_2.addWidget(self.v15, 15, 1, 1, 1)

        self.s16 = QSlider(self.gridLayoutWidget_2)
        self.s16.setObjectName(u"s16")
        self.s16.setMaximum(127)
        self.s16.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s16, 16, 0, 1, 1)

        self.s15 = QSlider(self.gridLayoutWidget_2)
        self.s15.setObjectName(u"s15")
        self.s15.setMaximum(127)
        self.s15.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s15, 15, 0, 1, 1)

        self.s5 = QSlider(self.gridLayoutWidget_2)
        self.s5.setObjectName(u"s5")
        self.s5.setMaximum(127)
        self.s5.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s5, 5, 0, 1, 1)

        self.s3 = QSlider(self.gridLayoutWidget_2)
        self.s3.setObjectName(u"s3")
        self.s3.setMaximum(127)
        self.s3.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s3, 3, 0, 1, 1)

        self.s7 = QSlider(self.gridLayoutWidget_2)
        self.s7.setObjectName(u"s7")
        self.s7.setMaximum(127)
        self.s7.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s7, 7, 0, 1, 1)

        self.v1 = QSpinBox(self.gridLayoutWidget_2)
        self.v1.setObjectName(u"v1")
        self.v1.setMaximum(127)

        self.gridLayout_2.addWidget(self.v1, 1, 1, 1, 1)

        self.s12 = QSlider(self.gridLayoutWidget_2)
        self.s12.setObjectName(u"s12")
        self.s12.setMaximum(127)
        self.s12.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s12, 12, 0, 1, 1)

        self.v10 = QSpinBox(self.gridLayoutWidget_2)
        self.v10.setObjectName(u"v10")
        self.v10.setMaximum(127)

        self.gridLayout_2.addWidget(self.v10, 10, 1, 1, 1)

        self.v9 = QSpinBox(self.gridLayoutWidget_2)
        self.v9.setObjectName(u"v9")
        self.v9.setMaximum(127)

        self.gridLayout_2.addWidget(self.v9, 9, 1, 1, 1)

        self.v3 = QSpinBox(self.gridLayoutWidget_2)
        self.v3.setObjectName(u"v3")
        self.v3.setMaximum(127)

        self.gridLayout_2.addWidget(self.v3, 3, 1, 1, 1)

        self.v13 = QSpinBox(self.gridLayoutWidget_2)
        self.v13.setObjectName(u"v13")
        self.v13.setMaximum(127)

        self.gridLayout_2.addWidget(self.v13, 13, 1, 1, 1)

        self.s1 = QSlider(self.gridLayoutWidget_2)
        self.s1.setObjectName(u"s1")
        self.s1.setMaximum(127)
        self.s1.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s1, 1, 0, 1, 1)

        self.s4 = QSlider(self.gridLayoutWidget_2)
        self.s4.setObjectName(u"s4")
        self.s4.setMaximum(127)
        self.s4.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s4, 4, 0, 1, 1)

        self.v6 = QSpinBox(self.gridLayoutWidget_2)
        self.v6.setObjectName(u"v6")
        self.v6.setMaximum(127)

        self.gridLayout_2.addWidget(self.v6, 6, 1, 1, 1)

        self.s14 = QSlider(self.gridLayoutWidget_2)
        self.s14.setObjectName(u"s14")
        self.s14.setMaximum(127)
        self.s14.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s14, 14, 0, 1, 1)

        self.v16 = QSpinBox(self.gridLayoutWidget_2)
        self.v16.setObjectName(u"v16")
        self.v16.setMaximum(127)

        self.gridLayout_2.addWidget(self.v16, 16, 1, 1, 1)

        self.v4 = QSpinBox(self.gridLayoutWidget_2)
        self.v4.setObjectName(u"v4")
        self.v4.setMaximum(127)

        self.gridLayout_2.addWidget(self.v4, 4, 1, 1, 1)

        self.v12 = QSpinBox(self.gridLayoutWidget_2)
        self.v12.setObjectName(u"v12")
        self.v12.setMaximum(127)

        self.gridLayout_2.addWidget(self.v12, 12, 1, 1, 1)

        self.v11 = QSpinBox(self.gridLayoutWidget_2)
        self.v11.setObjectName(u"v11")
        self.v11.setMaximum(127)

        self.gridLayout_2.addWidget(self.v11, 11, 1, 1, 1)

        self.s13 = QSlider(self.gridLayoutWidget_2)
        self.s13.setObjectName(u"s13")
        self.s13.setMaximum(127)
        self.s13.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s13, 13, 0, 1, 1)

        self.v8 = QSpinBox(self.gridLayoutWidget_2)
        self.v8.setObjectName(u"v8")
        self.v8.setMaximum(127)

        self.gridLayout_2.addWidget(self.v8, 8, 1, 1, 1)

        self.s10 = QSlider(self.gridLayoutWidget_2)
        self.s10.setObjectName(u"s10")
        self.s10.setMaximum(127)
        self.s10.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s10, 10, 0, 1, 1)

        self.v2 = QSpinBox(self.gridLayoutWidget_2)
        self.v2.setObjectName(u"v2")
        self.v2.setMaximum(127)

        self.gridLayout_2.addWidget(self.v2, 2, 1, 1, 1)

        self.s2 = QSlider(self.gridLayoutWidget_2)
        self.s2.setObjectName(u"s2")
        self.s2.setMaximum(127)
        self.s2.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s2, 2, 0, 1, 1)

        self.s8 = QSlider(self.gridLayoutWidget_2)
        self.s8.setObjectName(u"s8")
        self.s8.setMaximum(127)
        self.s8.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s8, 8, 0, 1, 1)

        self.v14 = QSpinBox(self.gridLayoutWidget_2)
        self.v14.setObjectName(u"v14")
        self.v14.setMaximum(127)

        self.gridLayout_2.addWidget(self.v14, 14, 1, 1, 1)

        self.s11 = QSlider(self.gridLayoutWidget_2)
        self.s11.setObjectName(u"s11")
        self.s11.setMaximum(127)
        self.s11.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s11, 11, 0, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 10)
        self.gridLayout_2.setColumnStretch(1, 2)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(120, 30, 201, 160))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.connection = QPushButton(self.gridLayoutWidget)
        self.connection.setObjectName(u"connection")

        self.gridLayout.addWidget(self.connection, 1, 1, 1, 2)

        self.Refresh = QPushButton(self.gridLayoutWidget)
        self.Refresh.setObjectName(u"Refresh")

        self.gridLayout.addWidget(self.Refresh, 1, 0, 1, 1)

        self.device = QComboBox(self.gridLayoutWidget)
        self.device.setObjectName(u"device")

        self.gridLayout.addWidget(self.device, 0, 0, 1, 3)

        self.status = QLineEdit(self.gridLayoutWidget)
        self.status.setObjectName(u"status")

        self.gridLayout.addWidget(self.status, 2, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 949, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.update.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.def_but.setText(QCoreApplication.translate("MainWindow", u"Set Defaults", None))
        self.send.setText(QCoreApplication.translate("MainWindow", u"Send to Mruda", None))
        self.flash.setText(QCoreApplication.translate("MainWindow", u"Burn Settings", None))
        self.connection.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.Refresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
    # retranslateUi

