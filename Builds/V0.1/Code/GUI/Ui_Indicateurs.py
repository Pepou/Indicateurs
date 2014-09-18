# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Travail\EFS\Travail accreditation\SQ\Temperature\Logiciel Saisie des Etalonnages\Indicateurs\Builds\V0.1\Code\GUI\Indicateurs.ui'
#
# Created: Thu Sep 11 16:09:16 2014
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(900, 543)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.dateEdit = QtGui.QDateEdit(self.centralWidget)
        self.dateEdit.setDate(QtCore.QDate(2014, 1, 1))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.verticalLayout.addWidget(self.dateEdit)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.dateEdit_2 = QtGui.QDateEdit(self.centralWidget)
        self.dateEdit_2.setDate(QtCore.QDate(2014, 1, 1))
        self.dateEdit_2.setObjectName(_fromUtf8("dateEdit_2"))
        self.verticalLayout_2.addWidget(self.dateEdit_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.comboBox = QtGui.QComboBox(self.centralWidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.verticalLayout_3.addWidget(self.comboBox)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.tableWidget = QtGui.QTableWidget(self.centralWidget)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.verticalLayout_4.addWidget(self.tableWidget)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Indicateurs", None))
        self.label.setText(_translate("MainWindow", "Date debut", None))
        self.label_2.setText(_translate("MainWindow", "Date de fin", None))
        self.label_3.setText(_translate("MainWindow", "Domaine", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "Composition Parc", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "Temperature", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "Volumes", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "Cartographie", None))
        self.comboBox.setItemText(4, _translate("MainWindow", "Afficheurs", None))
        self.comboBox.setItemText(5, _translate("MainWindow", "Masses/Temps", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Items", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Resultats", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

