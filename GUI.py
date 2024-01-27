# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\GUI\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(358, 305)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 311, 251))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_tool = QtWidgets.QWidget()
        self.tab_tool.setObjectName("tab_tool")
        self.btn_start = QtWidgets.QPushButton(self.tab_tool)
        self.btn_start.setGeometry(QtCore.QRect(30, 40, 251, 51))
        self.btn_start.setObjectName("btn_start")
        self.btn_stop = QtWidgets.QPushButton(self.tab_tool)
        self.btn_stop.setGeometry(QtCore.QRect(30, 100, 251, 61))
        self.btn_stop.setObjectName("btn_stop")
        self.tabWidget.addTab(self.tab_tool, "")
        self.tab_config = QtWidgets.QWidget()
        self.tab_config.setObjectName("tab_config")
        self.comboBox = QtWidgets.QComboBox(self.tab_config)
        self.comboBox.setGeometry(QtCore.QRect(10, 20, 181, 41))
        self.comboBox.setObjectName("comboBox")
        self.btn_select = QtWidgets.QPushButton(self.tab_config)
        self.btn_select.setGeometry(QtCore.QRect(200, 20, 81, 41))
        self.btn_select.setObjectName("btn_select")
        self.tabWidget.addTab(self.tab_config, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 358, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_start.setText(_translate("MainWindow", "Start"))
        self.btn_stop.setText(_translate("MainWindow", "Stop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_tool), _translate("MainWindow", "Tool"))
        self.btn_select.setText(_translate("MainWindow", "Select"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_config), _translate("MainWindow", "Config"))

