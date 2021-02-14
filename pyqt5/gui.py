# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1603, 873)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(1260, 10, 321, 161))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.currentDate = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.currentDate.setFont(font)
        self.currentDate.setAlignment(QtCore.Qt.AlignCenter)
        self.currentDate.setObjectName("currentDate")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.currentDate)
        self.iPAddressLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.iPAddressLabel.setFont(font)
        self.iPAddressLabel.setObjectName("iPAddressLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.iPAddressLabel)
        self.iPAddressLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.iPAddressLineEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.iPAddressLineEdit.setFont(font)
        self.iPAddressLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.iPAddressLineEdit.setObjectName("iPAddressLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.iPAddressLineEdit)
        self.dateLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.dateLabel.setFont(font)
        self.dateLabel.setObjectName("dateLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.dateLabel)
        self.statusLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.statusLabel.setFont(font)
        self.statusLabel.setObjectName("statusLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.statusLabel)
        self.loginStatus = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.loginStatus.setFont(font)
        self.loginStatus.setObjectName("loginStatus")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.loginStatus)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 721, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.aPIIDLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.aPIIDLabel.setFont(font)
        self.aPIIDLabel.setObjectName("aPIIDLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.aPIIDLabel)
        self.aPIIDLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.aPIIDLineEdit.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.aPIIDLineEdit.setFont(font)
        self.aPIIDLineEdit.setAutoFillBackground(False)
        self.aPIIDLineEdit.setText("")
        self.aPIIDLineEdit.setFrame(True)
        self.aPIIDLineEdit.setReadOnly(False)
        self.aPIIDLineEdit.setClearButtonEnabled(False)
        self.aPIIDLineEdit.setObjectName("aPIIDLineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.aPIIDLineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonLogin = QtWidgets.QPushButton(self.layoutWidget)
        self.buttonLogin.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.buttonLogin.setFont(font)
        self.buttonLogin.setObjectName("buttonLogin")
        self.horizontalLayout.addWidget(self.buttonLogin)
        self.buttonLogout = QtWidgets.QPushButton(self.layoutWidget)
        self.buttonLogout.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.buttonLogout.setFont(font)
        self.buttonLogout.setObjectName("buttonLogout")
        self.horizontalLayout.addWidget(self.buttonLogout)
        self.buttonQuit = QtWidgets.QPushButton(self.layoutWidget)
        self.buttonQuit.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.buttonQuit.setFont(font)
        self.buttonQuit.setObjectName("buttonQuit")
        self.horizontalLayout.addWidget(self.buttonQuit)
        self.formLayout_2.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.dropletInfo = QtWidgets.QTableWidget(self.centralwidget)
        self.dropletInfo.setGeometry(QtCore.QRect(1250, 269, 331, 541))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dropletInfo.sizePolicy().hasHeightForWidth())
        self.dropletInfo.setSizePolicy(sizePolicy)
        self.dropletInfo.setWordWrap(False)
        self.dropletInfo.setObjectName("dropletInfo")
        self.dropletInfo.setColumnCount(3)
        self.dropletInfo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.dropletInfo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dropletInfo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dropletInfo.setHorizontalHeaderItem(2, item)
        self.aPIIDLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.aPIIDLabel_3.setGeometry(QtCore.QRect(1250, 209, 128, 29))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.aPIIDLabel_3.setFont(font)
        self.aPIIDLabel_3.setObjectName("aPIIDLabel_3")
        self.aPIIDLabel_4 = QtWidgets.QLabel(self.centralwidget)
        self.aPIIDLabel_4.setGeometry(QtCore.QRect(20, 210, 131, 29))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.aPIIDLabel_4.setFont(font)
        self.aPIIDLabel_4.setObjectName("aPIIDLabel_4")
        self.domainInfo = QtWidgets.QTableWidget(self.centralwidget)
        self.domainInfo.setGeometry(QtCore.QRect(20, 269, 131, 541))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.domainInfo.sizePolicy().hasHeightForWidth())
        self.domainInfo.setSizePolicy(sizePolicy)
        self.domainInfo.setWordWrap(False)
        self.domainInfo.setObjectName("domainInfo")
        self.domainInfo.setColumnCount(1)
        self.domainInfo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.domainInfo.setHorizontalHeaderItem(0, item)
        self.tabledomainRecords = QtWidgets.QTableWidget(self.centralwidget)
        self.tabledomainRecords.setGeometry(QtCore.QRect(190, 269, 1041, 541))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabledomainRecords.sizePolicy().hasHeightForWidth())
        self.tabledomainRecords.setSizePolicy(sizePolicy)
        self.tabledomainRecords.setWordWrap(False)
        self.tabledomainRecords.setObjectName("tabledomainRecords")
        self.tabledomainRecords.setColumnCount(10)
        self.tabledomainRecords.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabledomainRecords.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabledomainRecords.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabledomainRecords.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabledomainRecords.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabledomainRecords.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabledomainRecords.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabledomainRecords.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabledomainRecords.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabledomainRecords.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabledomainRecords.setHorizontalHeaderItem(9, item)
        self.labeldomainRecordsInfo = QtWidgets.QLabel(self.centralwidget)
        self.labeldomainRecordsInfo.setGeometry(QtCore.QRect(190, 210, 1011, 29))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.labeldomainRecordsInfo.setFont(font)
        self.labeldomainRecordsInfo.setObjectName("labeldomainRecordsInfo")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(750, 30, 501, 141))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.aPIIDLabel_2 = QtWidgets.QLabel(self.frame)
        self.aPIIDLabel_2.setGeometry(QtCore.QRect(160, 0, 134, 29))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.aPIIDLabel_2.setFont(font)
        self.aPIIDLabel_2.setObjectName("aPIIDLabel_2")
        self.accountInfo = QtWidgets.QTableWidget(self.frame)
        self.accountInfo.setGeometry(QtCore.QRect(110, 30, 241, 106))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accountInfo.sizePolicy().hasHeightForWidth())
        self.accountInfo.setSizePolicy(sizePolicy)
        self.accountInfo.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.accountInfo.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.accountInfo.setDragEnabled(True)
        self.accountInfo.setWordWrap(False)
        self.accountInfo.setObjectName("accountInfo")
        self.accountInfo.setColumnCount(0)
        self.accountInfo.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1603, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.domainInfo.currentCellChanged['int','int','int','int'].connect(self.tabledomainRecords.clear)
        self.buttonLogout.clicked.connect(self.domainInfo.clear)
        self.buttonLogout.clicked.connect(self.dropletInfo.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Digital Ocean Python with PyQt5"))
        self.currentDate.setText(_translate("MainWindow", "2021-02-13 22:51"))
        self.iPAddressLabel.setText(_translate("MainWindow", "IP Address"))
        self.iPAddressLineEdit.setText(_translate("MainWindow", "Public IP"))
        self.dateLabel.setText(_translate("MainWindow", "Date"))
        self.statusLabel.setText(_translate("MainWindow", "Status"))
        self.loginStatus.setText(_translate("MainWindow", "Logged Out"))
        self.aPIIDLabel.setText(_translate("MainWindow", "API ID"))
        self.aPIIDLineEdit.setPlaceholderText(_translate("MainWindow", "DigitalOcean API Key"))
        self.buttonLogin.setText(_translate("MainWindow", "Login"))
        self.buttonLogout.setText(_translate("MainWindow", "Logout"))
        self.buttonQuit.setText(_translate("MainWindow", "Quit"))
        item = self.dropletInfo.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.dropletInfo.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "id"))
        item = self.dropletInfo.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "networks"))
        self.aPIIDLabel_3.setText(_translate("MainWindow", "Droplet Info"))
        self.aPIIDLabel_4.setText(_translate("MainWindow", "Domain Info"))
        item = self.domainInfo.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Domain"))
        item = self.tabledomainRecords.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tabledomainRecords.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tabledomainRecords.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tabledomainRecords.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tabledomainRecords.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tabledomainRecords.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tabledomainRecords.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tabledomainRecords.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tabledomainRecords.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tabledomainRecords.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "New Column"))
        self.labeldomainRecordsInfo.setText(_translate("MainWindow", "Domain Records Info"))
        self.aPIIDLabel_2.setText(_translate("MainWindow", "Account Info"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionAbout.setText(_translate("MainWindow", "About"))