# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Editor.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(678, 535)
        Form.setMinimumSize(QtCore.QSize(620, 535))
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 340, 511))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.BACK = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.BACK.setObjectName("BACK")
        self.gridLayout.addWidget(self.BACK, 2, 3, 1, 1)
        self.LOAD = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.LOAD.setObjectName("LOAD")
        self.gridLayout.addWidget(self.LOAD, 0, 3, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 4)
        self.SAVE = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.SAVE.setObjectName("SAVE")
        self.gridLayout.addWidget(self.SAVE, 0, 2, 1, 1)
        self.IS_ZD = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.IS_ZD.setObjectName("IS_ZD")
        self.gridLayout.addWidget(self.IS_ZD, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.ADD_PPT = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ADD_PPT.setObjectName("ADD_PPT")
        self.gridLayout.addWidget(self.ADD_PPT, 2, 2, 1, 1)
        self.EXPORT = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.EXPORT.setObjectName("EXPORT")
        self.gridLayout.addWidget(self.EXPORT, 0, 1, 1, 1)
        self.TEXT_CORRECTION = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.TEXT_CORRECTION.setObjectName("TEXT_CORRECTION")
        self.gridLayout.addWidget(self.TEXT_CORRECTION, 2, 1, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(350, 10, 321, 511))
        self.scrollArea.setMinimumSize(QtCore.QSize(281, 231))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 302, 4000))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 4000))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.layoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 301, 791))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.BACK.setText(_translate("Form", "返回"))
        self.LOAD.setText(_translate("Form", "加载"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.SAVE.setText(_translate("Form", "保存"))
        self.IS_ZD.setText(_translate("Form", "是否为照读稿"))
        self.label.setText(_translate("Form", "编辑栏"))
        self.ADD_PPT.setText(_translate("Form", "添加PPT"))
        self.EXPORT.setText(_translate("Form", "导出"))
        self.TEXT_CORRECTION.setText(_translate("Form", "语法纠错"))
