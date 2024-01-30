# -*- coding: utf-8 -*-

#####################################################################
# Form generated from reading UI file 'design.ui'
##
# Created by: Qt User Interface Compiler version 6.6.1
##
# WARNING! All changes made file will be lost when recompiling UI file!
#################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import (QFont,  QIcon)
from PySide6.QtWidgets import (QCheckBox, QComboBox, QFrame,
                               QHBoxLayout, QLabel, QMenuBar,
                               QPushButton, QSizePolicy, QSlider,
                               QStatusBar, QTableWidget, QTableWidgetItem,
                               QVBoxLayout, QWidget)
import my_res_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setFixedSize(618, 670)
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"font-family: Inter; background-color: #0b132b;")
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setWindowIcon(QIcon('images/logo.svg'))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 20, 601, 201))
        self.frame.setStyleSheet(u"background-color: #BD96BF;\n"
                                 "border-radius: 30px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 10, 321, 31))
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label.setFont(font1)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 40, 571, 154))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.layoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(
            "QLabel { margin-right: 50px; margin-left: 50px;}"
            )

        self.horizontalLayout.addWidget(self.label_14)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout.addWidget(self.label_5)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout_2.addWidget(self.label_8)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.verticalLayout_2.addWidget(self.label_9)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.verticalLayout_2.addWidget(self.label_10)

        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.verticalLayout_2.addWidget(self.label_11)

        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 240, 601, 101))
        self.frame_2.setStyleSheet(u"background-color: #F3DC77;\n"
                                   "border-radius: 30px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(130, 10, 331, 21))
        self.label_15.setFont(font1)
        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEnabled(True)
        self.comboBox.setGeometry(QRect(50, 40, 501, 40))
        self.comboBox.setMouseTracking(False)
        self.comboBox.setTabletTracking(False)
        self.comboBox.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox.setLayoutDirection(Qt.LeftToRight)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: #FFFFFF;")
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setFrame(True)
        self.comboBox.setFont(font1)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 360, 601, 100))
        self.frame_3.setStyleSheet(u"background-color: #EAA0A2;\n"
                                   "border-radius: 30px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalSlider = QSlider(self.frame_3)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(330, 40, 221, 22))
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setValue(4)
        self.horizontalSlider.setSliderPosition(4)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider.setTickInterval(0)
        self.label_18 = QLabel(self.frame_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(420, 70, 21, 16))
        self.label_18.setFont(font)
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 10, 81, 81))
        icon = QIcon()
        icon.addFile(
            u":/images/images/start.png",
            QSize(), QIcon.Normal, QIcon.Off
            )
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(75, 75))
        self.pushButton.setCheckable(True)
        self.layoutWidget1 = QWidget(self.frame_3)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(120, 10, 432, 22))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.layoutWidget1)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_16)

        self.label_17 = QLabel(self.layoutWidget1)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_17)

        self.layoutWidget2 = QWidget(self.frame_3)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(120, 40, 183, 48))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.layoutWidget2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFont(font)

        self.verticalLayout_3.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.layoutWidget2)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setFont(font)

        self.verticalLayout_3.addWidget(self.checkBox_2)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 480, 601, 121))
        self.frame_4.setStyleSheet(u"background-color: #F3DC77;\n"
                                   "border-radius: 30px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_19 = QLabel(self.frame_4)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(220, 10, 181, 21))
        self.label_19.setFont(font1)
        self.tableWidget = QTableWidget(self.frame_4)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 40, 571, 71))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tableWidget.sizePolicy().hasHeightForWidth()
            )
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QSize(571, 0))
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(45)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(207)
        self.tableWidget.horizontalHeader().setProperty(
            "showSortIndicator", False
            )
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(34)
        self.tableWidget.verticalHeader().setDefaultSectionSize(39)
        self.tableWidget.verticalHeader().setProperty(
            "showSortIndicator", False
            )
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.tableWidget.setStyleSheet(
            "QTableWidget { background-color: #FFFFFF; }"
            )
        self.tableWidget.setFont(font1)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(190, 620, 241, 31))
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 618, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate(
                "MainWindow", u"Python CPU Benchmark", None
                )
                )
        self.label.setText(
            QCoreApplication.translate(
                "MainWindow", u"\u0425\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 \u0432\u0430\u0448\u0435\u0433\u043e \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440\u0430:", None))
        self.label_14.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0438 \u043c\u0430\u0440\u043a\u0430 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440\u0430: ", None))
        self.label_2.setText("Название процессора:")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u043a\u0442\u043e\u0432\u0430\u044f \u0447\u0430\u0441\u0442\u043e\u0442\u0430, \u0413\u0446:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u044f\u0434\u0435\u0440, \u0448\u0442.", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u043e\u0442\u043e\u043a\u043e\u0432, \u0448\u0442:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c \u0434\u043b\u044f \u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0410\u043b\u0433\u043e\u0440\u0438\u0442\u043c \u043b\u0438\u043d\u0435\u0439\u043d\u043e\u0433\u043e \u043f\u043e\u0438\u0441\u043a\u0430", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0410\u043b\u0433\u043e\u0440\u0438\u0442\u043c \u0431\u0438\u043d\u0430\u0440\u043d\u043e\u0433\u043e \u043f\u043e\u0438\u0441\u043a\u0430", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0410\u043b\u0433\u043e\u0440\u0438\u0442\u043c \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438 \u0432\u0441\u0442\u0430\u0432\u043a\u0430\u043c\u0438", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0410\u043b\u0433\u043e\u0440\u0438\u0442\u043c \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438 \u0432\u044b\u0431\u043e\u0440\u043e\u043c", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\u0410\u043b\u0433\u043e\u0440\u0438\u0442\u043c \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438 \u043f\u0443\u0437\u044b\u0440\u044c\u043a\u043e\u043c", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"\u0410\u043b\u0433\u043e\u0440\u0438\u0442\u043c \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438 \u043f\u043e\u0434\u0441\u0447\u0435\u0442\u043e\u043c", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"\u0410\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u044b \u0431\u044b\u0441\u0442\u0440\u043e\u0439 \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"\u0410\u043b\u0433\u043e\u0440\u0438\u0442\u043c \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438 \u0441\u043b\u0438\u044f\u043d\u0438\u0435\u043c", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"\u0410\u043b\u0433\u043e\u0440\u0438\u0442\u043c \u0415\u0432\u043a\u043b\u0438\u0434\u0430 \u0440\u0435\u043a\u0443\u0440\u0441\u0438\u0432\u043d\u044b\u0439", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"\u0410\u043b\u0433\u043e\u0440\u0438\u0442\u043c \u0447\u0438\u0441\u0435\u043b \u0424\u0438\u0431\u043e\u043d\u0430\u0447\u0447\u0438 \u0440\u0435\u043a\u0443\u0440\u0441\u0438\u0432\u043d\u044b\u0439", None))

        self.label_18.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0436\u0438\u043c\u044b \u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0441\u043b\u043e \u043c\u0430\u0441\u0441\u0438\u0432\u043e\u0432 \u0434\u043b\u044f \u0442\u0435\u0441\u0442\u0430:", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0434\u043d\u043e\u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043d\u043e\u0441\u0442\u044c", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043d\u043e\u0433\u043e\u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043d\u043e\u0441\u0442\u044c", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0442 \u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f:", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0434\u043d\u043e\u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043d\u043e\u0441\u0442\u044c", None))
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043d\u043e\u0433\u043e\u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043d\u043e\u0441\u0442\u044c", None))
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u0440\u0430\u0431\u043e\u0442\u044b, \u0441:", None))

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.qtablewidgetitem3 = self.tableWidget.item(0, 0)
        self.qtablewidgetitem3.setText(
            QCoreApplication.translate("MainWindow", u"10", None)
            )
        self.qtablewidgetitem4 = self.tableWidget.item(0, 1)
        self.qtablewidgetitem4.setText(QCoreApplication.translate(
            "MainWindow", u"2", None
            )
            )
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_6.setText(QCoreApplication.translate(
            "MainWindow",
            u"github.com/IvanZaycev0717", None
            )
            )
        self.label_6.setStyleSheet("color: #eeeeee")