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
    QPushButton, QRadioButton, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QStatusBar, QTabWidget,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1028, 614)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayoutWidget = QWidget(self.tab_3)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(380, 70, 191, 121))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.device = QComboBox(self.gridLayoutWidget)
        self.device.setObjectName(u"device")

        self.gridLayout.addWidget(self.device, 1, 0, 1, 1)

        self.midi_ac = QPushButton(self.gridLayoutWidget)
        self.midi_ac.setObjectName(u"midi_ac")

        self.gridLayout.addWidget(self.midi_ac, 2, 0, 1, 1)

        self.Refresh = QPushButton(self.gridLayoutWidget)
        self.Refresh.setObjectName(u"Refresh")

        self.gridLayout.addWidget(self.Refresh, 2, 1, 1, 1)

        self.connection = QPushButton(self.gridLayoutWidget)
        self.connection.setObjectName(u"connection")

        self.gridLayout.addWidget(self.connection, 1, 1, 1, 1)

        self.status = QLineEdit(self.gridLayoutWidget)
        self.status.setObjectName(u"status")

        self.gridLayout.addWidget(self.status, 4, 0, 1, 2)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayoutWidget_3 = QWidget(self.tab)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(320, 30, 331, 201))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_6 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setCursorPosition(16)
        self.lineEdit_6.setAlignment(Qt.AlignCenter)
        self.lineEdit_6.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_6, 0, 0, 1, 1)

        self.reset_dist = QPushButton(self.gridLayoutWidget_3)
        self.reset_dist.setObjectName(u"reset_dist")

        self.gridLayout_3.addWidget(self.reset_dist, 0, 1, 1, 1)

        self.fs_w = QSlider(self.gridLayoutWidget_3)
        self.fs_w.setObjectName(u"fs_w")
        self.fs_w.setMaximum(16)
        self.fs_w.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.fs_w, 6, 1, 1, 1)

        self.ham_mix = QSlider(self.gridLayoutWidget_3)
        self.ham_mix.setObjectName(u"ham_mix")
        self.ham_mix.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.ham_mix, 3, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_2, 2, 0, 1, 1)

        self.fs_c = QSlider(self.gridLayoutWidget_3)
        self.fs_c.setObjectName(u"fs_c")
        self.fs_c.setMaximum(16)
        self.fs_c.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.fs_c, 5, 1, 1, 1)

        self.e_fs_c = QSpinBox(self.gridLayoutWidget_3)
        self.e_fs_c.setObjectName(u"e_fs_c")
        self.e_fs_c.setMaximum(16)

        self.gridLayout_3.addWidget(self.e_fs_c, 5, 2, 1, 1)

        self.e_ham_mix = QSpinBox(self.gridLayoutWidget_3)
        self.e_ham_mix.setObjectName(u"e_ham_mix")

        self.gridLayout_3.addWidget(self.e_ham_mix, 3, 2, 1, 1)

        self.lineEdit_7 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_7, 6, 0, 1, 1)

        self.e_fs_w = QSpinBox(self.gridLayoutWidget_3)
        self.e_fs_w.setObjectName(u"e_fs_w")
        self.e_fs_w.setMaximum(16)

        self.gridLayout_3.addWidget(self.e_fs_w, 6, 2, 1, 1)

        self.lineEdit_5 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_5, 5, 0, 1, 1)

        self.oe = QSlider(self.gridLayoutWidget_3)
        self.oe.setObjectName(u"oe")
        self.oe.setMinimum(-50)
        self.oe.setMaximum(50)
        self.oe.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.oe, 2, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_4, 4, 0, 1, 1)

        self.expo = QSlider(self.gridLayoutWidget_3)
        self.expo.setObjectName(u"expo")
        self.expo.setValue(25)
        self.expo.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.expo, 1, 1, 1, 1)

        self.e_oe = QSpinBox(self.gridLayoutWidget_3)
        self.e_oe.setObjectName(u"e_oe")
        self.e_oe.setMinimum(-50)
        self.e_oe.setMaximum(50)

        self.gridLayout_3.addWidget(self.e_oe, 2, 2, 1, 1)

        self.e_randomness = QSpinBox(self.gridLayoutWidget_3)
        self.e_randomness.setObjectName(u"e_randomness")

        self.gridLayout_3.addWidget(self.e_randomness, 4, 2, 1, 1)

        self.lineEdit_3 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_3, 3, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_3.addWidget(self.lineEdit_8, 1, 0, 1, 1)

        self.randomness = QSlider(self.gridLayoutWidget_3)
        self.randomness.setObjectName(u"randomness")
        self.randomness.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.randomness, 4, 1, 1, 1)

        self.e_expo = QSpinBox(self.gridLayoutWidget_3)
        self.e_expo.setObjectName(u"e_expo")
        self.e_expo.setMaximum(99)
        self.e_expo.setValue(25)

        self.gridLayout_3.addWidget(self.e_expo, 1, 2, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 6)
        self.gridLayout_3.setColumnStretch(1, 4)
        self.gridLayout_3.setColumnStretch(2, 2)
        self.gridLayoutWidget_2 = QWidget(self.tab)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(690, 30, 301, 491))
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
        self.s5.setMaximum(100)
        self.s5.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s5, 5, 0, 1, 1)

        self.s14 = QSlider(self.gridLayoutWidget_2)
        self.s14.setObjectName(u"s14")
        self.s14.setMaximum(100)
        self.s14.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s14, 14, 0, 1, 1)

        self.s11 = QSlider(self.gridLayoutWidget_2)
        self.s11.setObjectName(u"s11")
        self.s11.setMaximum(100)
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
        self.s2.setMaximum(100)
        self.s2.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s2, 2, 0, 1, 1)

        self.s6 = QSlider(self.gridLayoutWidget_2)
        self.s6.setObjectName(u"s6")
        self.s6.setMaximum(100)
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
        self.s15.setMaximum(100)
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
        self.s16.setMaximum(100)
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
        self.s10.setMaximum(100)
        self.s10.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s10, 10, 0, 1, 1)

        self.s9 = QSlider(self.gridLayoutWidget_2)
        self.s9.setObjectName(u"s9")
        self.s9.setMaximum(100)
        self.s9.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s9, 9, 0, 1, 1)

        self.v16 = QSpinBox(self.gridLayoutWidget_2)
        self.v16.setObjectName(u"v16")
        self.v16.setMaximum(127)

        self.gridLayout_2.addWidget(self.v16, 16, 1, 1, 1)

        self.s8 = QSlider(self.gridLayoutWidget_2)
        self.s8.setObjectName(u"s8")
        self.s8.setMaximum(100)
        self.s8.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s8, 8, 0, 1, 1)

        self.s13 = QSlider(self.gridLayoutWidget_2)
        self.s13.setObjectName(u"s13")
        self.s13.setMaximum(100)
        self.s13.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s13, 13, 0, 1, 1)

        self.s3 = QSlider(self.gridLayoutWidget_2)
        self.s3.setObjectName(u"s3")
        self.s3.setMaximum(100)
        self.s3.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s3, 3, 0, 1, 1)

        self.s4 = QSlider(self.gridLayoutWidget_2)
        self.s4.setObjectName(u"s4")
        self.s4.setMaximum(100)
        self.s4.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s4, 4, 0, 1, 1)

        self.s7 = QSlider(self.gridLayoutWidget_2)
        self.s7.setObjectName(u"s7")
        self.s7.setMaximum(100)
        self.s7.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s7, 7, 0, 1, 1)

        self.v7 = QSpinBox(self.gridLayoutWidget_2)
        self.v7.setObjectName(u"v7")
        self.v7.setMaximum(127)

        self.gridLayout_2.addWidget(self.v7, 7, 1, 1, 1)

        self.s12 = QSlider(self.gridLayoutWidget_2)
        self.s12.setObjectName(u"s12")
        self.s12.setMaximum(100)
        self.s12.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s12, 12, 0, 1, 1)

        self.v3 = QSpinBox(self.gridLayoutWidget_2)
        self.v3.setObjectName(u"v3")
        self.v3.setMaximum(127)

        self.gridLayout_2.addWidget(self.v3, 3, 1, 1, 1)

        self.s1 = QSlider(self.gridLayoutWidget_2)
        self.s1.setObjectName(u"s1")
        self.s1.setMaximum(100)
        self.s1.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.s1, 1, 0, 1, 1)

        self.v9 = QSpinBox(self.gridLayoutWidget_2)
        self.v9.setObjectName(u"v9")
        self.v9.setMaximum(127)

        self.gridLayout_2.addWidget(self.v9, 9, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 10)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayoutWidget_5 = QWidget(self.tab)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(50, 30, 201, 121))
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

        self.gridLayoutWidget_7 = QWidget(self.tab)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(320, 240, 331, 266))
        self.gridLayout_7 = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_39 = QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_39.setObjectName(u"lineEdit_39")
        self.lineEdit_39.setReadOnly(True)

        self.gridLayout_7.addWidget(self.lineEdit_39, 8, 0, 1, 1)

        self.lineEdit_37 = QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_37.setObjectName(u"lineEdit_37")
        self.lineEdit_37.setReadOnly(True)

        self.gridLayout_7.addWidget(self.lineEdit_37, 2, 0, 1, 1)

        self.val_voice_timber = QSpinBox(self.gridLayoutWidget_7)
        self.val_voice_timber.setObjectName(u"val_voice_timber")

        self.gridLayout_7.addWidget(self.val_voice_timber, 9, 2, 1, 1)

        self.slide_rev_mix = QSlider(self.gridLayoutWidget_7)
        self.slide_rev_mix.setObjectName(u"slide_rev_mix")
        self.slide_rev_mix.setMaximum(70)
        self.slide_rev_mix.setSingleStep(10)
        self.slide_rev_mix.setOrientation(Qt.Horizontal)

        self.gridLayout_7.addWidget(self.slide_rev_mix, 4, 1, 1, 1)

        self.val_rev_damp = QSpinBox(self.gridLayoutWidget_7)
        self.val_rev_damp.setObjectName(u"val_rev_damp")

        self.gridLayout_7.addWidget(self.val_rev_damp, 3, 2, 1, 1)

        self.slide_voice_timber = QSlider(self.gridLayoutWidget_7)
        self.slide_voice_timber.setObjectName(u"slide_voice_timber")
        self.slide_voice_timber.setOrientation(Qt.Horizontal)

        self.gridLayout_7.addWidget(self.slide_voice_timber, 9, 1, 1, 1)

        self.lineEdit_35 = QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_35.setObjectName(u"lineEdit_35")
        self.lineEdit_35.setReadOnly(True)

        self.gridLayout_7.addWidget(self.lineEdit_35, 3, 0, 1, 1)

        self.val_voice_sustain = QSpinBox(self.gridLayoutWidget_7)
        self.val_voice_sustain.setObjectName(u"val_voice_sustain")
        self.val_voice_sustain.setMinimum(1)

        self.gridLayout_7.addWidget(self.val_voice_sustain, 8, 2, 1, 1)

        self.lineEdit_33 = QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_33.setObjectName(u"lineEdit_33")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.lineEdit_33.setFont(font2)
        self.lineEdit_33.setReadOnly(True)

        self.gridLayout_7.addWidget(self.lineEdit_33, 0, 0, 1, 1)

        self.val_rev_mix = QSpinBox(self.gridLayoutWidget_7)
        self.val_rev_mix.setObjectName(u"val_rev_mix")
        self.val_rev_mix.setMaximum(70)
        self.val_rev_mix.setSingleStep(10)

        self.gridLayout_7.addWidget(self.val_rev_mix, 4, 2, 1, 1)

        self.slide_voice_attack = QSlider(self.gridLayoutWidget_7)
        self.slide_voice_attack.setObjectName(u"slide_voice_attack")
        self.slide_voice_attack.setMinimum(1)
        self.slide_voice_attack.setOrientation(Qt.Horizontal)

        self.gridLayout_7.addWidget(self.slide_voice_attack, 7, 1, 1, 1)

        self.val_rev_feedback = QSpinBox(self.gridLayoutWidget_7)
        self.val_rev_feedback.setObjectName(u"val_rev_feedback")
        self.val_rev_feedback.setMaximum(98)

        self.gridLayout_7.addWidget(self.val_rev_feedback, 2, 2, 1, 1)

        self.lineEdit_36 = QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_36.setObjectName(u"lineEdit_36")
        self.lineEdit_36.setReadOnly(True)

        self.gridLayout_7.addWidget(self.lineEdit_36, 1, 0, 1, 1)

        self.lineEdit_34 = QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_34.setObjectName(u"lineEdit_34")
        self.lineEdit_34.setReadOnly(True)

        self.gridLayout_7.addWidget(self.lineEdit_34, 4, 0, 1, 1)

        self.lineEdit_41 = QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_41.setObjectName(u"lineEdit_41")
        self.lineEdit_41.setReadOnly(True)

        self.gridLayout_7.addWidget(self.lineEdit_41, 7, 0, 1, 1)

        self.val_voice_attack = QSpinBox(self.gridLayoutWidget_7)
        self.val_voice_attack.setObjectName(u"val_voice_attack")
        self.val_voice_attack.setMinimum(1)

        self.gridLayout_7.addWidget(self.val_voice_attack, 7, 2, 1, 1)

        self.slide_rev_feedback = QSlider(self.gridLayoutWidget_7)
        self.slide_rev_feedback.setObjectName(u"slide_rev_feedback")
        self.slide_rev_feedback.setMaximum(98)
        self.slide_rev_feedback.setOrientation(Qt.Horizontal)

        self.gridLayout_7.addWidget(self.slide_rev_feedback, 2, 1, 1, 1)

        self.lineEdit_40 = QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_40.setObjectName(u"lineEdit_40")
        self.lineEdit_40.setReadOnly(True)

        self.gridLayout_7.addWidget(self.lineEdit_40, 9, 0, 1, 1)

        self.lineEdit_38 = QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_38.setObjectName(u"lineEdit_38")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setItalic(False)
        self.lineEdit_38.setFont(font3)
        self.lineEdit_38.setReadOnly(True)

        self.gridLayout_7.addWidget(self.lineEdit_38, 6, 0, 1, 1)

        self.slide_rev_damp = QSlider(self.gridLayoutWidget_7)
        self.slide_rev_damp.setObjectName(u"slide_rev_damp")
        self.slide_rev_damp.setMaximum(90)
        self.slide_rev_damp.setOrientation(Qt.Horizontal)

        self.gridLayout_7.addWidget(self.slide_rev_damp, 3, 1, 1, 1)

        self.comb_voice_rev = QComboBox(self.gridLayoutWidget_7)
        self.comb_voice_rev.setObjectName(u"comb_voice_rev")

        self.gridLayout_7.addWidget(self.comb_voice_rev, 1, 1, 1, 1)

        self.slide_voice_sustain = QSlider(self.gridLayoutWidget_7)
        self.slide_voice_sustain.setObjectName(u"slide_voice_sustain")
        self.slide_voice_sustain.setMinimum(1)
        self.slide_voice_sustain.setOrientation(Qt.Horizontal)

        self.gridLayout_7.addWidget(self.slide_voice_sustain, 8, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_6, 5, 0, 1, 1)

        self.gridLayout_7.setColumnStretch(0, 6)
        self.gridLayout_7.setColumnStretch(1, 4)
        self.gridLayout_7.setColumnStretch(2, 2)
        self.tabWidget.addTab(self.tab, "")
        self.scale = QWidget()
        self.scale.setObjectName(u"scale")
        self.gridLayoutWidget_4 = QWidget(self.scale)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(60, 10, 541, 491))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.scale_sb8 = QSpinBox(self.gridLayoutWidget_4)
        self.scale_sb8.setObjectName(u"scale_sb8")
        self.scale_sb8.setMinimum(-50)
        self.scale_sb8.setMaximum(50)

        self.gridLayout_4.addWidget(self.scale_sb8, 9, 3, 1, 1)

        self.scale_sb1 = QSpinBox(self.gridLayoutWidget_4)
        self.scale_sb1.setObjectName(u"scale_sb1")
        self.scale_sb1.setMinimum(-50)
        self.scale_sb1.setMaximum(50)

        self.gridLayout_4.addWidget(self.scale_sb1, 16, 3, 1, 1)

        self.scale_r7 = QRadioButton(self.gridLayoutWidget_4)
        self.scale_r7.setObjectName(u"scale_r7")

        self.gridLayout_4.addWidget(self.scale_r7, 10, 2, 1, 1)

        self.scale_r5 = QRadioButton(self.gridLayoutWidget_4)
        self.scale_r5.setObjectName(u"scale_r5")

        self.gridLayout_4.addWidget(self.scale_r5, 12, 2, 1, 1)

        self.scale_sb6 = QSpinBox(self.gridLayoutWidget_4)
        self.scale_sb6.setObjectName(u"scale_sb6")
        self.scale_sb6.setMinimum(-50)
        self.scale_sb6.setMaximum(50)

        self.gridLayout_4.addWidget(self.scale_sb6, 11, 3, 1, 1)

        self.scale_r3 = QRadioButton(self.gridLayoutWidget_4)
        self.scale_r3.setObjectName(u"scale_r3")

        self.gridLayout_4.addWidget(self.scale_r3, 14, 2, 1, 1)

        self.scale_s1 = QSlider(self.gridLayoutWidget_4)
        self.scale_s1.setObjectName(u"scale_s1")
        self.scale_s1.setMinimum(-50)
        self.scale_s1.setMaximum(50)
        self.scale_s1.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.scale_s1, 16, 4, 1, 2)

        self.scale_r11 = QRadioButton(self.gridLayoutWidget_4)
        self.scale_r11.setObjectName(u"scale_r11")

        self.gridLayout_4.addWidget(self.scale_r11, 6, 2, 1, 1)

        self.scale_sb7 = QSpinBox(self.gridLayoutWidget_4)
        self.scale_sb7.setObjectName(u"scale_sb7")
        self.scale_sb7.setMinimum(-50)
        self.scale_sb7.setMaximum(50)

        self.gridLayout_4.addWidget(self.scale_sb7, 10, 3, 1, 1)

        self.scale_sb11 = QSpinBox(self.gridLayoutWidget_4)
        self.scale_sb11.setObjectName(u"scale_sb11")
        self.scale_sb11.setMinimum(-50)
        self.scale_sb11.setMaximum(50)

        self.gridLayout_4.addWidget(self.scale_sb11, 6, 3, 1, 1)

        self.scale_s11 = QSlider(self.gridLayoutWidget_4)
        self.scale_s11.setObjectName(u"scale_s11")
        self.scale_s11.setMinimum(-50)
        self.scale_s11.setMaximum(50)
        self.scale_s11.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.scale_s11, 6, 4, 1, 2)

        self.scale_sb12 = QSpinBox(self.gridLayoutWidget_4)
        self.scale_sb12.setObjectName(u"scale_sb12")
        self.scale_sb12.setMinimum(-50)
        self.scale_sb12.setMaximum(50)

        self.gridLayout_4.addWidget(self.scale_sb12, 5, 3, 1, 1)

        self.scale_b7 = QPushButton(self.gridLayoutWidget_4)
        self.scale_b7.setObjectName(u"scale_b7")

        self.gridLayout_4.addWidget(self.scale_b7, 10, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 17, 0, 1, 1)

        self.scale_r9 = QRadioButton(self.gridLayoutWidget_4)
        self.scale_r9.setObjectName(u"scale_r9")

        self.gridLayout_4.addWidget(self.scale_r9, 8, 2, 1, 1)

        self.scale_sb4 = QSpinBox(self.gridLayoutWidget_4)
        self.scale_sb4.setObjectName(u"scale_sb4")
        self.scale_sb4.setMinimum(-50)
        self.scale_sb4.setMaximum(50)

        self.gridLayout_4.addWidget(self.scale_sb4, 13, 3, 1, 1)

        self.scale_sb2 = QSpinBox(self.gridLayoutWidget_4)
        self.scale_sb2.setObjectName(u"scale_sb2")
        self.scale_sb2.setMinimum(-50)
        self.scale_sb2.setMaximum(50)

        self.gridLayout_4.addWidget(self.scale_sb2, 15, 3, 1, 1)

        self.scale_r4 = QRadioButton(self.gridLayoutWidget_4)
        self.scale_r4.setObjectName(u"scale_r4")

        self.gridLayout_4.addWidget(self.scale_r4, 13, 2, 1, 1)

        self.scale_s8 = QSlider(self.gridLayoutWidget_4)
        self.scale_s8.setObjectName(u"scale_s8")
        self.scale_s8.setMinimum(-50)
        self.scale_s8.setMaximum(50)
        self.scale_s8.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.scale_s8, 9, 4, 1, 2)

        self.scale_r6 = QRadioButton(self.gridLayoutWidget_4)
        self.scale_r6.setObjectName(u"scale_r6")

        self.gridLayout_4.addWidget(self.scale_r6, 11, 2, 1, 1)

        self.scale_r2 = QRadioButton(self.gridLayoutWidget_4)
        self.scale_r2.setObjectName(u"scale_r2")

        self.gridLayout_4.addWidget(self.scale_r2, 15, 2, 1, 1)

        self.scale_sb5 = QSpinBox(self.gridLayoutWidget_4)
        self.scale_sb5.setObjectName(u"scale_sb5")
        self.scale_sb5.setMinimum(-50)
        self.scale_sb5.setMaximum(50)

        self.gridLayout_4.addWidget(self.scale_sb5, 12, 3, 1, 1)

        self.scale_sb3 = QSpinBox(self.gridLayoutWidget_4)
        self.scale_sb3.setObjectName(u"scale_sb3")
        self.scale_sb3.setMinimum(-50)
        self.scale_sb3.setMaximum(50)

        self.gridLayout_4.addWidget(self.scale_sb3, 14, 3, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_5, 4, 0, 1, 1)

        self.scale_s3 = QSlider(self.gridLayoutWidget_4)
        self.scale_s3.setObjectName(u"scale_s3")
        self.scale_s3.setMinimum(-50)
        self.scale_s3.setMaximum(50)
        self.scale_s3.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.scale_s3, 14, 4, 1, 2)

        self.scale_s10 = QSlider(self.gridLayoutWidget_4)
        self.scale_s10.setObjectName(u"scale_s10")
        self.scale_s10.setMinimum(-50)
        self.scale_s10.setMaximum(50)
        self.scale_s10.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.scale_s10, 7, 4, 1, 2)

        self.scale_slot = QComboBox(self.gridLayoutWidget_4)
        self.scale_slot.setObjectName(u"scale_slot")

        self.gridLayout_4.addWidget(self.scale_slot, 1, 5, 1, 1)

        self.scale_s6 = QSlider(self.gridLayoutWidget_4)
        self.scale_s6.setObjectName(u"scale_s6")
        self.scale_s6.setMinimum(-50)
        self.scale_s6.setMaximum(50)
        self.scale_s6.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.scale_s6, 11, 4, 1, 2)

        self.scale_s9 = QSlider(self.gridLayoutWidget_4)
        self.scale_s9.setObjectName(u"scale_s9")
        self.scale_s9.setMinimum(-50)
        self.scale_s9.setMaximum(50)
        self.scale_s9.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.scale_s9, 8, 4, 1, 2)

        self.scale_sb10 = QSpinBox(self.gridLayoutWidget_4)
        self.scale_sb10.setObjectName(u"scale_sb10")
        self.scale_sb10.setMinimum(-50)
        self.scale_sb10.setMaximum(50)

        self.gridLayout_4.addWidget(self.scale_sb10, 7, 3, 1, 1)

        self.scale_s7 = QSlider(self.gridLayoutWidget_4)
        self.scale_s7.setObjectName(u"scale_s7")
        self.scale_s7.setMinimum(-50)
        self.scale_s7.setMaximum(50)
        self.scale_s7.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.scale_s7, 10, 4, 1, 2)

        self.scale_title_slot = QLineEdit(self.gridLayoutWidget_4)
        self.scale_title_slot.setObjectName(u"scale_title_slot")
        font4 = QFont()
        font4.setPointSize(9)
        font4.setBold(True)
        self.scale_title_slot.setFont(font4)
        self.scale_title_slot.setAlignment(Qt.AlignCenter)
        self.scale_title_slot.setReadOnly(True)

        self.gridLayout_4.addWidget(self.scale_title_slot, 0, 5, 1, 1)

        self.scale_s2 = QSlider(self.gridLayoutWidget_4)
        self.scale_s2.setObjectName(u"scale_s2")
        self.scale_s2.setMinimum(-50)
        self.scale_s2.setMaximum(50)
        self.scale_s2.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.scale_s2, 15, 4, 1, 2)

        self.scale_b9 = QPushButton(self.gridLayoutWidget_4)
        self.scale_b9.setObjectName(u"scale_b9")

        self.gridLayout_4.addWidget(self.scale_b9, 8, 0, 1, 1)

        self.scale_b4 = QPushButton(self.gridLayoutWidget_4)
        self.scale_b4.setObjectName(u"scale_b4")

        self.gridLayout_4.addWidget(self.scale_b4, 13, 0, 1, 1)

        self.scale_s12 = QSlider(self.gridLayoutWidget_4)
        self.scale_s12.setObjectName(u"scale_s12")
        self.scale_s12.setMinimum(-50)
        self.scale_s12.setMaximum(50)
        self.scale_s12.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.scale_s12, 5, 4, 1, 2)

        self.scale_s5 = QSlider(self.gridLayoutWidget_4)
        self.scale_s5.setObjectName(u"scale_s5")
        self.scale_s5.setMinimum(-50)
        self.scale_s5.setMaximum(50)
        self.scale_s5.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.scale_s5, 12, 4, 1, 2)

        self.scale_r8 = QRadioButton(self.gridLayoutWidget_4)
        self.scale_r8.setObjectName(u"scale_r8")

        self.gridLayout_4.addWidget(self.scale_r8, 9, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 2, 2, 1, 1)

        self.lineEdit_11 = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setFont(font1)
        self.lineEdit_11.setAlignment(Qt.AlignCenter)
        self.lineEdit_11.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineEdit_11, 3, 3, 1, 3)

        self.scale_r1 = QRadioButton(self.gridLayoutWidget_4)
        self.scale_r1.setObjectName(u"scale_r1")

        self.gridLayout_4.addWidget(self.scale_r1, 16, 2, 1, 1)

        self.scale_b2 = QPushButton(self.gridLayoutWidget_4)
        self.scale_b2.setObjectName(u"scale_b2")

        self.gridLayout_4.addWidget(self.scale_b2, 15, 0, 1, 1)

        self.scale_b11 = QPushButton(self.gridLayoutWidget_4)
        self.scale_b11.setObjectName(u"scale_b11")

        self.gridLayout_4.addWidget(self.scale_b11, 6, 0, 1, 1)

        self.scale_to_mruda = QPushButton(self.gridLayoutWidget_4)
        self.scale_to_mruda.setObjectName(u"scale_to_mruda")
        self.scale_to_mruda.setFont(font1)

        self.gridLayout_4.addWidget(self.scale_to_mruda, 18, 0, 1, 3)

        self.scale_r12 = QRadioButton(self.gridLayoutWidget_4)
        self.scale_r12.setObjectName(u"scale_r12")
        self.scale_r12.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_4.addWidget(self.scale_r12, 5, 2, 1, 1)

        self.scale_nat_ch = QComboBox(self.gridLayoutWidget_4)
        self.scale_nat_ch.setObjectName(u"scale_nat_ch")

        self.gridLayout_4.addWidget(self.scale_nat_ch, 1, 3, 1, 1)

        self.scale_r10 = QRadioButton(self.gridLayoutWidget_4)
        self.scale_r10.setObjectName(u"scale_r10")

        self.gridLayout_4.addWidget(self.scale_r10, 7, 2, 1, 1)

        self.scale_burn_mruda = QPushButton(self.gridLayoutWidget_4)
        self.scale_burn_mruda.setObjectName(u"scale_burn_mruda")
        self.scale_burn_mruda.setFont(font1)

        self.gridLayout_4.addWidget(self.scale_burn_mruda, 18, 4, 1, 2)

        self.scale_title_s_type = QLineEdit(self.gridLayoutWidget_4)
        self.scale_title_s_type.setObjectName(u"scale_title_s_type")
        self.scale_title_s_type.setFont(font4)
        self.scale_title_s_type.setAlignment(Qt.AlignCenter)
        self.scale_title_s_type.setReadOnly(True)

        self.gridLayout_4.addWidget(self.scale_title_s_type, 0, 3, 1, 1)

        self.scale_sb9 = QSpinBox(self.gridLayoutWidget_4)
        self.scale_sb9.setObjectName(u"scale_sb9")
        self.scale_sb9.setMinimum(-50)
        self.scale_sb9.setMaximum(50)

        self.gridLayout_4.addWidget(self.scale_sb9, 8, 3, 1, 1)

        self.scale_s4 = QSlider(self.gridLayoutWidget_4)
        self.scale_s4.setObjectName(u"scale_s4")
        self.scale_s4.setMinimum(-50)
        self.scale_s4.setMaximum(50)
        self.scale_s4.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.scale_s4, 13, 4, 1, 2)

        self.lineEdit_10 = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setFont(font1)
        self.lineEdit_10.setAlignment(Qt.AlignCenter)
        self.lineEdit_10.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineEdit_10, 3, 2, 1, 1)

        self.play_demo = QPushButton(self.gridLayoutWidget_4)
        self.play_demo.setObjectName(u"play_demo")
        self.play_demo.setFont(font1)

        self.gridLayout_4.addWidget(self.play_demo, 18, 3, 1, 1)

        self.scale_b1 = QPushButton(self.gridLayoutWidget_4)
        self.scale_b1.setObjectName(u"scale_b1")

        self.gridLayout_4.addWidget(self.scale_b1, 16, 0, 1, 2)

        self.scale_b3 = QPushButton(self.gridLayoutWidget_4)
        self.scale_b3.setObjectName(u"scale_b3")

        self.gridLayout_4.addWidget(self.scale_b3, 14, 0, 1, 2)

        self.scale_b5 = QPushButton(self.gridLayoutWidget_4)
        self.scale_b5.setObjectName(u"scale_b5")

        self.gridLayout_4.addWidget(self.scale_b5, 12, 0, 1, 2)

        self.scale_b6 = QPushButton(self.gridLayoutWidget_4)
        self.scale_b6.setObjectName(u"scale_b6")

        self.gridLayout_4.addWidget(self.scale_b6, 11, 0, 1, 2)

        self.scale_b8 = QPushButton(self.gridLayoutWidget_4)
        self.scale_b8.setObjectName(u"scale_b8")

        self.gridLayout_4.addWidget(self.scale_b8, 9, 0, 1, 2)

        self.scale_b10 = QPushButton(self.gridLayoutWidget_4)
        self.scale_b10.setObjectName(u"scale_b10")

        self.gridLayout_4.addWidget(self.scale_b10, 7, 0, 1, 2)

        self.scale_b12 = QPushButton(self.gridLayoutWidget_4)
        self.scale_b12.setObjectName(u"scale_b12")

        self.gridLayout_4.addWidget(self.scale_b12, 5, 0, 1, 2)

        self.lineEdit_9 = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setFont(font1)
        self.lineEdit_9.setAlignment(Qt.AlignCenter)
        self.lineEdit_9.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineEdit_9, 3, 0, 1, 2)

        self.type_w_i = QComboBox(self.gridLayoutWidget_4)
        self.type_w_i.setObjectName(u"type_w_i")

        self.gridLayout_4.addWidget(self.type_w_i, 1, 0, 1, 2)

        self.scale_title_type = QLineEdit(self.gridLayoutWidget_4)
        self.scale_title_type.setObjectName(u"scale_title_type")
        self.scale_title_type.setFont(font1)
        self.scale_title_type.setAlignment(Qt.AlignCenter)
        self.scale_title_type.setReadOnly(True)

        self.gridLayout_4.addWidget(self.scale_title_type, 0, 0, 1, 2)

        self.gridLayout_4.setColumnStretch(0, 5)
        self.gridLayout_4.setColumnStretch(1, 1)
        self.gridLayout_4.setColumnStretch(2, 2)
        self.gridLayout_4.setColumnStretch(3, 3)
        self.gridLayout_4.setColumnStretch(4, 3)
        self.gridLayout_4.setColumnStretch(5, 3)
        self.textEdit = QTextEdit(self.scale)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(630, 10, 331, 171))
        self.tabWidget.addTab(self.scale, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayoutWidget_6 = QWidget(self.tab_2)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(50, 20, 601, 401))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.lineEdit_20 = QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEdit_20, 10, 0, 1, 1)

        self.lineEdit_15 = QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEdit_15, 5, 0, 1, 1)

        self.d_tune = QSpinBox(self.gridLayoutWidget_6)
        self.d_tune.setObjectName(u"d_tune")
        self.d_tune.setMinimum(-50)
        self.d_tune.setMaximum(50)

        self.gridLayout_6.addWidget(self.d_tune, 5, 1, 1, 1)

        self.default_burn = QPushButton(self.gridLayoutWidget_6)
        self.default_burn.setObjectName(u"default_burn")
        self.default_burn.setFont(font1)

        self.gridLayout_6.addWidget(self.default_burn, 14, 2, 1, 2)

        self.d_voice_p1 = QComboBox(self.gridLayoutWidget_6)
        self.d_voice_p1.setObjectName(u"d_voice_p1")

        self.gridLayout_6.addWidget(self.d_voice_p1, 10, 1, 1, 1)

        self.comboBox_19 = QComboBox(self.gridLayoutWidget_6)
        self.comboBox_19.setObjectName(u"comboBox_19")

        self.gridLayout_6.addWidget(self.comboBox_19, 10, 3, 1, 1)

        self.d_voice_def = QComboBox(self.gridLayoutWidget_6)
        self.d_voice_def.setObjectName(u"d_voice_def")

        self.gridLayout_6.addWidget(self.d_voice_def, 9, 1, 1, 1)

        self.d_transpose = QComboBox(self.gridLayoutWidget_6)
        self.d_transpose.setObjectName(u"d_transpose")

        self.gridLayout_6.addWidget(self.d_transpose, 3, 1, 1, 1)

        self.d_sustain = QComboBox(self.gridLayoutWidget_6)
        self.d_sustain.setObjectName(u"d_sustain")

        self.gridLayout_6.addWidget(self.d_sustain, 8, 1, 1, 1)

        self.lineEdit_26 = QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEdit_26, 6, 2, 1, 1)

        self.lineEdit_21 = QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEdit_21, 11, 0, 1, 1)

        self.lineEdit_19 = QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEdit_19, 9, 0, 1, 1)

        self.lineEdit_13 = QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEdit_13, 3, 0, 1, 1)

        self.lineEdit_23 = QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEdit_23, 3, 2, 1, 1)

        self.d_tanpura_state = QComboBox(self.gridLayoutWidget_6)
        self.d_tanpura_state.setObjectName(u"d_tanpura_state")

        self.gridLayout_6.addWidget(self.d_tanpura_state, 6, 3, 1, 1)

        self.lineEdit_14 = QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEdit_14, 4, 0, 1, 1)

        self.lineEdit_25 = QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        self.lineEdit_25.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEdit_25, 5, 2, 1, 1)

        self.d_tanpura_sec = QComboBox(self.gridLayoutWidget_6)
        self.d_tanpura_sec.setObjectName(u"d_tanpura_sec")

        self.gridLayout_6.addWidget(self.d_tanpura_sec, 9, 3, 1, 1)

        self.lineEdit_12 = QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEdit_12, 2, 0, 1, 1)

        self.d_reverb = QComboBox(self.gridLayoutWidget_6)
        self.d_reverb.setObjectName(u"d_reverb")

        self.gridLayout_6.addWidget(self.d_reverb, 7, 1, 1, 1)

        self.lineEdit_17 = QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEdit_17, 7, 0, 1, 1)

        self.lineEdit_31 = QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_31.setObjectName(u"lineEdit_31")

        self.gridLayout_6.addWidget(self.lineEdit_31, 11, 2, 1, 1)

        self.d_tanpura_scale = QComboBox(self.gridLayoutWidget_6)
        self.d_tanpura_scale.setObjectName(u"d_tanpura_scale")

        self.gridLayout_6.addWidget(self.d_tanpura_scale, 7, 3, 1, 1)

        self.d_tanpura_vol = QComboBox(self.gridLayoutWidget_6)
        self.d_tanpura_vol.setObjectName(u"d_tanpura_vol")

        self.gridLayout_6.addWidget(self.d_tanpura_vol, 8, 3, 1, 1)

        self.d_octave = QComboBox(self.gridLayoutWidget_6)
        self.d_octave.setObjectName(u"d_octave")

        self.gridLayout_6.addWidget(self.d_octave, 4, 1, 1, 1)

        self.d_tsens = QComboBox(self.gridLayoutWidget_6)
        self.d_tsens.setObjectName(u"d_tsens")

        self.gridLayout_6.addWidget(self.d_tsens, 6, 1, 1, 1)

        self.d_midi = QComboBox(self.gridLayoutWidget_6)
        self.d_midi.setObjectName(u"d_midi")

        self.gridLayout_6.addWidget(self.d_midi, 2, 1, 1, 1)

        self.lineEdit_28 = QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_28.setObjectName(u"lineEdit_28")
        self.lineEdit_28.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEdit_28, 8, 2, 1, 1)

        self.d_voice_p2 = QComboBox(self.gridLayoutWidget_6)
        self.d_voice_p2.setObjectName(u"d_voice_p2")

        self.gridLayout_6.addWidget(self.d_voice_p2, 11, 1, 1, 1)

        self.d_auto_corr = QComboBox(self.gridLayoutWidget_6)
        self.d_auto_corr.setObjectName(u"d_auto_corr")

        self.gridLayout_6.addWidget(self.d_auto_corr, 2, 3, 1, 1)

        self.comboBox_20 = QComboBox(self.gridLayoutWidget_6)
        self.comboBox_20.setObjectName(u"comboBox_20")

        self.gridLayout_6.addWidget(self.comboBox_20, 11, 3, 1, 1)

        self.lineEdit_22 = QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEdit_22, 2, 2, 1, 1)

        self.lineEdit_30 = QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_30.setObjectName(u"lineEdit_30")

        self.gridLayout_6.addWidget(self.lineEdit_30, 10, 2, 1, 1)

        self.default_send = QPushButton(self.gridLayoutWidget_6)
        self.default_send.setObjectName(u"default_send")
        self.default_send.setFont(font1)

        self.gridLayout_6.addWidget(self.default_send, 14, 0, 1, 2)

        self.lineEdit_32 = QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_32.setObjectName(u"lineEdit_32")
        self.lineEdit_32.setFont(font)
        self.lineEdit_32.setAlignment(Qt.AlignCenter)
        self.lineEdit_32.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEdit_32, 0, 0, 1, 4)

        self.lineEdit_16 = QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEdit_16, 6, 0, 1, 1)

        self.lineEdit_29 = QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_29.setObjectName(u"lineEdit_29")
        self.lineEdit_29.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEdit_29, 9, 2, 1, 1)

        self.lineEdit_24 = QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEdit_24, 4, 2, 1, 1)

        self.lineEdit_27 = QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_27.setObjectName(u"lineEdit_27")
        self.lineEdit_27.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEdit_27, 7, 2, 1, 1)

        self.lineEdit_18 = QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEdit_18, 8, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_4, 12, 0, 1, 1)

        self.set_default = QPushButton(self.gridLayoutWidget_6)
        self.set_default.setObjectName(u"set_default")
        self.set_default.setFont(font1)

        self.gridLayout_6.addWidget(self.set_default, 13, 0, 1, 2)

        self.d_ac_boot = QComboBox(self.gridLayoutWidget_6)
        self.d_ac_boot.setObjectName(u"d_ac_boot")

        self.gridLayout_6.addWidget(self.d_ac_boot, 3, 3, 1, 1)

        self.d_ac_s1 = QComboBox(self.gridLayoutWidget_6)
        self.d_ac_s1.setObjectName(u"d_ac_s1")

        self.gridLayout_6.addWidget(self.d_ac_s1, 4, 3, 1, 1)

        self.d_ac_s2 = QComboBox(self.gridLayoutWidget_6)
        self.d_ac_s2.setObjectName(u"d_ac_s2")

        self.gridLayout_6.addWidget(self.d_ac_s2, 5, 3, 1, 1)

        self.gridLayout_6.setColumnStretch(0, 4)
        self.gridLayout_6.setColumnStretch(1, 1)
        self.gridLayout_6.setColumnStretch(2, 5)
        self.gridLayout_6.setColumnStretch(3, 3)
        self.textEdit_2 = QTextEdit(self.tab_2)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(700, 80, 281, 181))
        self.tabWidget.addTab(self.tab_2, "")
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
        font5 = QFont()
        font5.setPointSize(8)
        self.path.setFont(font5)
        self.path.setReadOnly(True)
        self.update_find = QPushButton(self.Update)
        self.update_find.setObjectName(u"update_find")
        self.update_find.setGeometry(QRect(170, 180, 351, 24))
        self.update_find.setFont(font1)
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
        self.menubar.setGeometry(QRect(0, 0, 1028, 22))
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
        self.midi_ac.setText(QCoreApplication.translate("MainWindow", u"AutoConnect", None))
        self.Refresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.connection.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Connection", None))
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"Harmonic Control", None))
        self.reset_dist.setText(QCoreApplication.translate("MainWindow", u"Reset All", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"Odd-even", None))
        self.lineEdit_7.setText(QCoreApplication.translate("MainWindow", u"Form Shape (w)", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"Form Shape (c)", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"Randomness", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"Harm. Mix", None))
        self.lineEdit_8.setText(QCoreApplication.translate("MainWindow", u"Expo", None))
        self.update.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.def_but.setText(QCoreApplication.translate("MainWindow", u"Set Defaults", None))
        self.flash.setText(QCoreApplication.translate("MainWindow", u"Burn Settings", None))
        self.send.setText(QCoreApplication.translate("MainWindow", u"Send to Mruda", None))
        self.lineEdit_39.setText(QCoreApplication.translate("MainWindow", u"Sustain", None))
        self.lineEdit_37.setText(QCoreApplication.translate("MainWindow", u"Feedback", None))
        self.lineEdit_35.setText(QCoreApplication.translate("MainWindow", u"Damping", None))
        self.lineEdit_33.setText(QCoreApplication.translate("MainWindow", u"Reverb Control", None))
        self.lineEdit_36.setText(QCoreApplication.translate("MainWindow", u"Presets", None))
        self.lineEdit_34.setText(QCoreApplication.translate("MainWindow", u"Mixing ratio", None))
        self.lineEdit_41.setText(QCoreApplication.translate("MainWindow", u"Attack", None))
        self.lineEdit_40.setText(QCoreApplication.translate("MainWindow", u"Timber pressure cont.", None))
        self.lineEdit_38.setText(QCoreApplication.translate("MainWindow", u"Other", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Voice Edit", None))
        self.scale_r7.setText("")
        self.scale_r5.setText("")
        self.scale_r3.setText("")
        self.scale_r11.setText("")
        self.scale_b7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.scale_r9.setText("")
        self.scale_r4.setText("")
        self.scale_r6.setText("")
        self.scale_r2.setText("")
        self.scale_title_slot.setText(QCoreApplication.translate("MainWindow", u"Slot", None))
        self.scale_b9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.scale_b4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.scale_r8.setText("")
        self.lineEdit_11.setText(QCoreApplication.translate("MainWindow", u"Tune", None))
        self.scale_r1.setText("")
        self.scale_b2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.scale_b11.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.scale_to_mruda.setText(QCoreApplication.translate("MainWindow", u"Send to Mruda", None))
        self.scale_r12.setText("")
        self.scale_r10.setText("")
        self.scale_burn_mruda.setText(QCoreApplication.translate("MainWindow", u"Burn to Mruda", None))
        self.scale_title_s_type.setText(QCoreApplication.translate("MainWindow", u"Scale Type", None))
        self.lineEdit_10.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.play_demo.setText(QCoreApplication.translate("MainWindow", u"Play Demo", None))
        self.scale_b1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.scale_b3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.scale_b5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.scale_b6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.scale_b8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.scale_b10.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.scale_b12.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.lineEdit_9.setText(QCoreApplication.translate("MainWindow", u"Keys", None))
        self.scale_title_type.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Custom scale setup for auto-correct:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A custom scale can be setup with required notes and microtonal adjustment. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent"
                        ":0px;\">Three available slots can be used to save custom scales. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Use &quot;send to Mruda&quot; button to test the scale, later press &quot;Burn to Mruda&quot; to store setting in permenant memory.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Important:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">This scale is only usable when auto-correct function is enabled. </span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scale), QCoreApplication.translate("MainWindow", u"Scale Set.", None))
        self.lineEdit_20.setText(QCoreApplication.translate("MainWindow", u"Voice (P1 key)", None))
        self.lineEdit_15.setText(QCoreApplication.translate("MainWindow", u"Tune", None))
        self.default_burn.setText(QCoreApplication.translate("MainWindow", u"Burn to Mruda", None))
        self.lineEdit_26.setText(QCoreApplication.translate("MainWindow", u"Tanpura Status", None))
        self.lineEdit_21.setText(QCoreApplication.translate("MainWindow", u"Voice (P2 key)", None))
        self.lineEdit_19.setText(QCoreApplication.translate("MainWindow", u"Voice (at start)", None))
        self.lineEdit_13.setText(QCoreApplication.translate("MainWindow", u"Transpose", None))
        self.lineEdit_23.setText(QCoreApplication.translate("MainWindow", u"Auto Correct scale (at start)", None))
        self.lineEdit_14.setText(QCoreApplication.translate("MainWindow", u"Octave", None))
        self.lineEdit_25.setText(QCoreApplication.translate("MainWindow", u"Auto Correct scale (S2 key)", None))
        self.lineEdit_12.setText(QCoreApplication.translate("MainWindow", u"Midi", None))
        self.lineEdit_17.setText(QCoreApplication.translate("MainWindow", u"Reverb", None))
        self.lineEdit_28.setText(QCoreApplication.translate("MainWindow", u"Tanpura Volume", None))
        self.lineEdit_22.setText(QCoreApplication.translate("MainWindow", u"Auto Correct", None))
        self.default_send.setText(QCoreApplication.translate("MainWindow", u"Send to Mruda", None))
        self.lineEdit_32.setText(QCoreApplication.translate("MainWindow", u"Default Settings", None))
        self.lineEdit_16.setText(QCoreApplication.translate("MainWindow", u"Touch Sensitivity", None))
        self.lineEdit_29.setText(QCoreApplication.translate("MainWindow", u"Tanpura secondary", None))
        self.lineEdit_24.setText(QCoreApplication.translate("MainWindow", u"Auto Correct scale (S1 key)", None))
        self.lineEdit_27.setText(QCoreApplication.translate("MainWindow", u"Tanpura Scale", None))
        self.lineEdit_18.setText(QCoreApplication.translate("MainWindow", u"Sustain", None))
        self.set_default.setText(QCoreApplication.translate("MainWindow", u"Set defaults", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Dustom configuration for System Default:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">These setting can be set as system default that are applied whenever device is started. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-inde"
                        "nt:0; text-indent:0px;\">To set it up press &quot;Burn to Mruda&quot;</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Default Setting", None))
        self.sel_file.setText(QCoreApplication.translate("MainWindow", u"Select file...", None))
        self.flash_mrida.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.update_find.setText(QCoreApplication.translate("MainWindow", u"Auto Connect", None))
        self.flash_connect.setText(QCoreApplication.translate("MainWindow", u"Connecct", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Update), QCoreApplication.translate("MainWindow", u"Update", None))
    # retranslateUi

