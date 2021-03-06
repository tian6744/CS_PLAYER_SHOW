import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import QApplication, QMainWindow, QAbstractItemView, QTableWidgetItem


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1050, 800)
        MainWindow.setStyleSheet("#MainWindow{background-image:url(../resources/gun.png)}")
        MainWindow.setWindowIcon(QIcon("G:/ProJect/resources/开心果.png"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 0, 191, 731))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.widget)
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 0, 0, 1, 1)

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(240, 10, 900, 731))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(0, -10, 811, 741))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(17)
        self.tableWidget.setRowCount(807)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置数据只读

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, item)
        self.frame.hide()

        self.frame2 = QtWidgets.QFrame(self.centralwidget)
        self.frame2.setGeometry(QtCore.QRect(330, 0, 631, 731))
        self.frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2.setObjectName("frame")
        self.tableWidget2 = QtWidgets.QTableWidget(self.frame2)
        self.tableWidget2.setGeometry(QtCore.QRect(0, 400, 651, 81))
        self.tableWidget2.setColumnCount(16)
        self.tableWidget2.setRowCount(1)
        self.tableWidget2.setObjectName("tableWidget2")
        self.tableWidget2.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置数据只读

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(15, item)

        self.pushButton2 = QtWidgets.QPushButton(self.frame2)
        self.pushButton2.setGeometry(QtCore.QRect(260, 310, 121, 41))
        self.pushButton2.setObjectName("pushButton")
        self.lineEdit21 = QtWidgets.QLineEdit(self.frame2)
        self.lineEdit21.setGeometry(QtCore.QRect(130, 200, 391, 81))
        self.lineEdit21.setText("")
        self.lineEdit21.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.frame2)
        self.label.setGeometry(QtCore.QRect(200, 120, 261, 71))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame2.hide()

        self.frame3 = QtWidgets.QFrame(self.centralwidget)
        self.frame3.setGeometry(QtCore.QRect(300, 0, 651, 721))
        self.frame3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame3.setObjectName("frame")
        self.label3 = QtWidgets.QLabel(self.frame3)
        self.label3.setGeometry(QtCore.QRect(240, 100, 200, 30))
        self.label3.setObjectName("label")
        self.gridLayoutWidget3 = QtWidgets.QWidget(self.frame3)
        self.gridLayoutWidget3.setGeometry(QtCore.QRect(60, 140, 571, 321))
        self.gridLayoutWidget3.setObjectName("gridLayoutWidget")
        self.gridLayout3 = QtWidgets.QGridLayout(self.gridLayoutWidget3)
        self.gridLayout3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout3.setObjectName("gridLayout")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget3)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout3.addWidget(self.lineEdit_4, 3, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget3)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout3.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout3.addWidget(self.lineEdit_2, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget3)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout3.addWidget(self.lineEdit_3, 2, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget3)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout3.addWidget(self.lineEdit_5, 4, 0, 1, 1)
        self.pushButton31 = QtWidgets.QPushButton(self.frame3)
        self.pushButton31.setGeometry(QtCore.QRect(60, 510, 131, 61))
        self.pushButton31.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.frame3)
        self.label_2.setGeometry(QtCore.QRect(370, 510, 231, 61))
        self.label_2.setObjectName("label_2")
        self.frame3.hide()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "数据显示模块"))
        self.pushButton_2.setText(_translate("MainWindow", "数据查询"))
        self.pushButton_3.setText(_translate("MainWindow", "数据预测"))
        self.pushButton_1.setText(_translate("MainWindow", "数据展示"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "选手"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "参与率"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "影响力"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "生涯Rating"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "生涯总击杀"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "爆头率"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "生涯总死亡"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "击杀死亡比"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "平均每回合伤害"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "平均每回合道具造成伤害"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "生涯比赛场数"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "生涯比赛回合数"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "平均每回合击杀"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "平均每回合助攻"))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "平均每回合死亡"))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "平均每回合队友存活"))
        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "平均每回合存活"))

        item = self.tableWidget2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "参与率"))
        item = self.tableWidget2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "影响力"))
        item = self.tableWidget2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "生涯Rating"))
        item = self.tableWidget2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "生涯总击杀"))
        item = self.tableWidget2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "爆头率"))
        item = self.tableWidget2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "生涯总死亡"))
        item = self.tableWidget2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "击杀死亡比"))
        item = self.tableWidget2.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "平均每回合伤害"))
        item = self.tableWidget2.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "平均每回合道具造成伤害"))
        item = self.tableWidget2.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "生涯比赛场数"))
        item = self.tableWidget2.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "生涯比赛回合数"))
        item = self.tableWidget2.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "平均每回合击杀"))
        item = self.tableWidget2.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "平均每回合助攻"))
        item = self.tableWidget2.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "平均每回合死亡"))
        item = self.tableWidget2.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "平均每回合队友存活"))
        item = self.tableWidget2.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "平均每回合存活"))

        self.pushButton2.setText(_translate("MainWindow", "查询"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">输入选手的名称</span></p></body></html>"))

        self.label3.setText(_translate("MainWindow",
                                       "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">输入数据(小数)</span></p></body></html>"))

        self.lineEdit.setPlaceholderText('参与率')
        self.lineEdit_2.setPlaceholderText('每回合击杀数')
        self.lineEdit_3.setPlaceholderText('每回合死亡数')
        self.lineEdit_4.setPlaceholderText('每回合平均造成伤害')
        self.lineEdit_5.setPlaceholderText('影响力')
        self.pushButton31.setText(_translate("MainWindow", "预测"))
        self.label_2.setText(_translate("MainWindow", "显示rating"))



