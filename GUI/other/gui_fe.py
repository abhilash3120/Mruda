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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QLineEdit, QMainWindow, QMenuBar, QProgressBar,
    QPushButton, QSizePolicy, QSlider, QSpinBox,
    QStatusBar, QTabWidget, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1032, 624)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayoutWidget_3 = QWidget(self.tab)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(80, 200, 411, 306))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.fs_c = QSlider(self.gridLayoutWidget_3)
        self.fs_c.setObjectName(u"fs_c")
        self.fs_c.setMaximum(16)
        self.fs_c.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.fs_c, 6, 1, 1, 1)

        self.fs_w = QSlider(self.gridLayoutWidget_3)
        self.fs_w.setObjectName(u"fs_w")
        self.fs_w.setMaximum(16)
        self.fs_w.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.fs_w, 7, 1, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.e_randomness = QSpinBox(self.gridLayoutWidget_3)
        self.e_randomness.setObjectName(u"e_randomness")

        self.gridLayout_3.addWidget(self.e_randomness, 5, 2, 1, 1)

        self.randomness = QSlider(self.gridLayoutWidget_3)
        self.randomness.setObjectName(u"randomness")
        self.randomness.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.randomness, 5, 1, 1, 1)

        self.lineEdit_7 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_7, 7, 0, 1, 1)

        self.e_tilt = QSpinBox(self.gridLayoutWidget_3)
        self.e_tilt.setObjectName(u"e_tilt")

        self.gridLayout_3.addWidget(self.e_tilt, 1, 2, 1, 1)

        self.expo = QSlider(self.gridLayoutWidget_3)
        self.expo.setObjectName(u"expo")
        self.expo.setValue(25)
        self.expo.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.expo, 2, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_4, 5, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_5, 6, 0, 1, 1)

        self.oe = QSlider(self.gridLayoutWidget_3)
        self.oe.setObjectName(u"oe")
        self.oe.setMinimum(-50)
        self.oe.setMaximum(50)
        self.oe.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.oe, 3, 1, 1, 1)

        self.ham_mix = QSlider(self.gridLayoutWidget_3)
        self.ham_mix.setObjectName(u"ham_mix")
        self.ham_mix.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.ham_mix, 4, 1, 1, 1)

        self.tilt = QSlider(self.gridLayoutWidget_3)
        self.tilt.setObjectName(u"tilt")
        self.tilt.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.tilt, 1, 1, 1, 1)

        self.lineEdit_6 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setCursorPosition(15)
        self.lineEdit_6.setAlignment(Qt.AlignCenter)
        self.lineEdit_6.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_6, 0, 0, 1, 3)

        self.reset_dist = QPushButton(self.gridLayoutWidget_3)
        self.reset_dist.setObjectName(u"reset_dist")

        self.gridLayout_3.addWidget(self.reset_dist, 8, 1, 1, 1)

        self.e_expo = QSpinBox(self.gridLayoutWidget_3)
        self.e_expo.setObjectName(u"e_expo")
        self.e_expo.setMaximum(99)
        self.e_expo.setValue(25)

        self.gridLayout_3.addWidget(self.e_expo, 2, 2, 1, 1)

        self.lineEdit_8 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_3.addWidget(self.lineEdit_8, 2, 0, 1, 1)

        self.e_ham_mix = QSpinBox(self.gridLayoutWidget_3)
        self.e_ham_mix.setObjectName(u"e_ham_mix")

        self.gridLayout_3.addWidget(self.e_ham_mix, 4, 2, 1, 1)

        self.e_fs_c = QSpinBox(self.gridLayoutWidget_3)
        self.e_fs_c.setObjectName(u"e_fs_c")
        self.e_fs_c.setMaximum(16)

        self.gridLayout_3.addWidget(self.e_fs_c, 6, 2, 1, 1)

        self.lineEdit_3 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_3, 4, 0, 1, 1)

        self.e_oe = QSpinBox(self.gridLayoutWidget_3)
        self.e_oe.setObjectName(u"e_oe")
        self.e_oe.setMinimum(-50)
        self.e_oe.setMaximum(50)

        self.gridLayout_3.addWidget(self.e_oe, 3, 2, 1, 1)

        self.e_fs_w = QSpinBox(self.gridLayoutWidget_3)
        self.e_fs_w.setObjectName(u"e_fs_w")
        self.e_fs_w.setMaximum(16)

        self.gridLayout_3.addWidget(self.e_fs_w, 7, 2, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_2, 3, 0, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 3)
        self.gridLayoutWidget_2 = QWidget(self.tab)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(590, 30, 331, 501))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.v5 = QSpinBox(self.gridLayoutWidget_2)
        self.v5.setObjectName(u"v5")
        self.v5.setMaximum(127)

        self.gridLayout_2.addWidget(self.v5, 5, 1, 1, 1)

        self.v14 = QSpinBox(self.gridLayoutWidget_2)
        self.v14.setObjectName(u"v14")
        self.v14.setMaximum(127)

        self.gridLayout_2.addWidget(self.v14, 14, 1, 1, 1)

        self.s5 = QSlider(self.gridLayoutWidget_2)
        self.s5.setObjectName(u"s5")
        self.s5.setMaximum(127)
        self.s5.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s5, 5, 0, 1, 1)

        self.s14 = QSlider(self.gridLayoutWidget_2)
        self.s14.setObjectName(u"s14")
        self.s14.setMaximum(127)
        self.s14.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s14, 14, 0, 1, 1)

        self.s11 = QSlider(self.gridLayoutWidget_2)
        self.s11.setObjectName(u"s11")
        self.s11.setMaximum(127)
        self.s11.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s11, 11, 0, 1, 1)

        self.v1 = QSpinBox(self.gridLayoutWidget_2)
        self.v1.setObjectName(u"v1")
        self.v1.setMaximum(127)

        self.gridLayout_2.addWidget(self.v1, 1, 1, 1, 1)

        self.v10 = QSpinBox(self.gridLayoutWidget_2)
        self.v10.setObjectName(u"v10")
        self.v10.setMaximum(127)

        self.gridLayout_2.addWidget(self.v10, 10, 1, 1, 1)

        self.s2 = QSlider(self.gridLayoutWidget_2)
        self.s2.setObjectName(u"s2")
        self.s2.setMaximum(127)
        self.s2.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s2, 2, 0, 1, 1)

        self.s6 = QSlider(self.gridLayoutWidget_2)
        self.s6.setObjectName(u"s6")
        self.s6.setMaximum(127)
        self.s6.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s6, 6, 0, 1, 1)

        self.v13 = QSpinBox(self.gridLayoutWidget_2)
        self.v13.setObjectName(u"v13")
        self.v13.setMaximum(127)

        self.gridLayout_2.addWidget(self.v13, 13, 1, 1, 1)

        self.v2 = QSpinBox(self.gridLayoutWidget_2)
        self.v2.setObjectName(u"v2")
        self.v2.setMaximum(127)

        self.gridLayout_2.addWidget(self.v2, 2, 1, 1, 1)

        self.v6 = QSpinBox(self.gridLayoutWidget_2)
        self.v6.setObjectName(u"v6")
        self.v6.setMaximum(127)

        self.gridLayout_2.addWidget(self.v6, 6, 1, 1, 1)

        self.v8 = QSpinBox(self.gridLayoutWidget_2)
        self.v8.setObjectName(u"v8")
        self.v8.setMaximum(127)

        self.gridLayout_2.addWidget(self.v8, 8, 1, 1, 1)

        self.s15 = QSlider(self.gridLayoutWidget_2)
        self.s15.setObjectName(u"s15")
        self.s15.setMaximum(127)
        self.s15.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s15, 15, 0, 1, 1)

        self.v4 = QSpinBox(self.gridLayoutWidget_2)
        self.v4.setObjectName(u"v4")
        self.v4.setMaximum(127)

        self.gridLayout_2.addWidget(self.v4, 4, 1, 1, 1)

        self.v11 = QSpinBox(self.gridLayoutWidget_2)
        self.v11.setObjectName(u"v11")
        self.v11.setMaximum(127)

        self.gridLayout_2.addWidget(self.v11, 11, 1, 1, 1)

        self.s16 = QSlider(self.gridLayoutWidget_2)
        self.s16.setObjectName(u"s16")
        self.s16.setMaximum(127)
        self.s16.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s16, 16, 0, 1, 1)

        self.v15 = QSpinBox(self.gridLayoutWidget_2)
        self.v15.setObjectName(u"v15")
        self.v15.setMaximum(127)

        self.gridLayout_2.addWidget(self.v15, 15, 1, 1, 1)

        self.v12 = QSpinBox(self.gridLayoutWidget_2)
        self.v12.setObjectName(u"v12")
        self.v12.setMaximum(127)

        self.gridLayout_2.addWidget(self.v12, 12, 1, 1, 1)

        self.s10 = QSlider(self.gridLayoutWidget_2)
        self.s10.setObjectName(u"s10")
        self.s10.setMaximum(127)
        self.s10.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s10, 10, 0, 1, 1)

        self.s9 = QSlider(self.gridLayoutWidget_2)
        self.s9.setObjectName(u"s9")
        self.s9.setMaximum(127)
        self.s9.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s9, 9, 0, 1, 1)

        self.v16 = QSpinBox(self.gridLayoutWidget_2)
        self.v16.setObjectName(u"v16")
        self.v16.setMaximum(127)

        self.gridLayout_2.addWidget(self.v16, 16, 1, 1, 1)

        self.s8 = QSlider(self.gridLayoutWidget_2)
        self.s8.setObjectName(u"s8")
        self.s8.setMaximum(127)
        self.s8.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s8, 8, 0, 1, 1)

        self.s13 = QSlider(self.gridLayoutWidget_2)
        self.s13.setObjectName(u"s13")
        self.s13.setMaximum(127)
        self.s13.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s13, 13, 0, 1, 1)

        self.s3 = QSlider(self.gridLayoutWidget_2)
        self.s3.setObjectName(u"s3")
        self.s3.setMaximum(127)
        self.s3.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s3, 3, 0, 1, 1)

        self.s4 = QSlider(self.gridLayoutWidget_2)
        self.s4.setObjectName(u"s4")
        self.s4.setMaximum(127)
        self.s4.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s4, 4, 0, 1, 1)

        self.s7 = QSlider(self.gridLayoutWidget_2)
        self.s7.setObjectName(u"s7")
        self.s7.setMaximum(127)
        self.s7.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s7, 7, 0, 1, 1)

        self.v7 = QSpinBox(self.gridLayoutWidget_2)
        self.v7.setObjectName(u"v7")
        self.v7.setMaximum(127)

        self.gridLayout_2.addWidget(self.v7, 7, 1, 1, 1)

        self.s12 = QSlider(self.gridLayoutWidget_2)
        self.s12.setObjectName(u"s12")
        self.s12.setMaximum(127)
        self.s12.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s12, 12, 0, 1, 1)

        self.v3 = QSpinBox(self.gridLayoutWidget_2)
        self.v3.setObjectName(u"v3")
        self.v3.setMaximum(127)

        self.gridLayout_2.addWidget(self.v3, 3, 1, 1, 1)

        self.s1 = QSlider(self.gridLayoutWidget_2)
        self.s1.setObjectName(u"s1")
        self.s1.setMaximum(127)
        self.s1.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s1, 1, 0, 1, 1)

        self.v9 = QSpinBox(self.gridLayoutWidget_2)
        self.v9.setObjectName(u"v9")
        self.v9.setMaximum(127)

        self.gridLayout_2.addWidget(self.v9, 9, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 10)
        self.gridLayoutWidget = QWidget(self.tab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(80, 60, 161, 121))
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

        self.gridLayoutWidget_5 = QWidget(self.tab)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(290, 60, 201, 121))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.slot_list = QComboBox(self.gridLayoutWidget_5)
        self.slot_list.setObjectName(u"slot_list")

        self.gridLayout_5.addWidget(self.slot_list, 0, 0, 1, 1)

        self.update = QPushButton(self.gridLayoutWidget_5)
        self.update.setObjectName(u"update")

        self.gridLayout_5.addWidget(self.update, 0, 1, 1, 1)

        self.def_but = QPushButton(self.gridLayoutWidget_5)
        self.def_but.setObjectName(u"def_but")

        self.gridLayout_5.addWidget(self.def_but, 5, 0, 1, 1)

        self.flash = QPushButton(self.gridLayoutWidget_5)
        self.flash.setObjectName(u"flash")

        self.gridLayout_5.addWidget(self.flash, 5, 1, 1, 1)

        self.send = QPushButton(self.gridLayoutWidget_5)
        self.send.setObjectName(u"send")
        font1 = QFont()
        font1.setBold(True)
        self.send.setFont(font1)

        self.gridLayout_5.addWidget(self.send, 4, 0, 1, 2)

        self.tabWidget.addTab(self.tab, "")
        self.Update = QWidget()
        self.Update.setObjectName(u"Update")
        self.sel_file = QPushButton(self.Update)
        self.sel_file.setObjectName(u"sel_file")
        self.sel_file.setGeometry(QRect(170, 220, 121, 24))
        self.flash_mrida = QPushButton(self.Update)
        self.flash_mrida.setObjectName(u"flash_mrida")
        self.flash_mrida.setGeometry(QRect(170, 260, 121, 24))
        self.progressBar = QProgressBar(self.Update)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(300, 260, 231, 23))
        self.progressBar.setValue(0)
        self.text_log = QTextEdit(self.Update)
        self.text_log.setObjectName(u"text_log")
        self.text_log.setGeometry(QRect(170, 300, 361, 221))
        self.path = QLineEdit(self.Update)
        self.path.setObjectName(u"path")
        self.path.setGeometry(QRect(300, 220, 231, 22))
        self.path.setReadOnly(True)
        self.update_find = QPushButton(self.Update)
        self.update_find.setObjectName(u"update_find")
        self.update_find.setGeometry(QRect(170, 180, 351, 24))
        self.com_list = QComboBox(self.Update)
        self.com_list.setObjectName(u"com_list")
        self.com_list.setGeometry(QRect(170, 140, 181, 22))
        self.flash_connect = QPushButton(self.Update)
        self.flash_connect.setObjectName(u"flash_connect")
        self.flash_connect.setGeometry(QRect(380, 140, 131, 24))
        self.tabWidget.addTab(self.Update, "")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1032, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Mruda Editor", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"TIlt", None))
        self.lineEdit_7.setText(QCoreApplication.translate("MainWindow", u"Form Shape (w)", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"Randomness", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"Form Shape (c)", None))
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"Overall Control", None))
        self.reset_dist.setText(QCoreApplication.translate("MainWindow", u"Reset All", None))
        self.lineEdit_8.setText(QCoreApplication.translate("MainWindow", u"Expo", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"Harm. Mix", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"Odd-even", None))
        self.connection.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.Refresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.update.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.def_but.setText(QCoreApplication.translate("MainWindow", u"Set Defaults", None))
        self.flash.setText(QCoreApplication.translate("MainWindow", u"Burn Settings", None))
        self.send.setText(QCoreApplication.translate("MainWindow", u"Send to Mruda", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Voice Edit", None))
        self.sel_file.setText(QCoreApplication.translate("MainWindow", u"Select file...", None))
        self.flash_mrida.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.update_find.setText(QCoreApplication.translate("MainWindow", u"Find and Connect", None))
        self.flash_connect.setText(QCoreApplication.translate("MainWindow", u"Connecct", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Update), QCoreApplication.translate("MainWindow", u"Update", None))
    # retranslateUi

