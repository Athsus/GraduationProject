# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Free.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Free(object):
    def setupUi(self, Free):
        Free.setObjectName("Free")
        Free.resize(564, 521)
        Free.setMinimumSize(QtCore.QSize(564, 521))
        self.label_2 = QtWidgets.QLabel(Free)
        self.label_2.setGeometry(QtCore.QRect(9, 489, 104, 23))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Free)
        self.label_3.setGeometry(QtCore.QRect(451, 489, 104, 23))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(Free)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 13, 541, 501))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.JUDGE = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.JUDGE.sizePolicy().hasHeightForWidth())
        self.JUDGE.setSizePolicy(sizePolicy)
        self.JUDGE.setObjectName("JUDGE")
        self.horizontalLayout.addWidget(self.JUDGE)
        self.PLAY = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PLAY.sizePolicy().hasHeightForWidth())
        self.PLAY.setSizePolicy(sizePolicy)
        self.PLAY.setObjectName("PLAY")
        self.horizontalLayout.addWidget(self.PLAY)
        self.BACK = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BACK.sizePolicy().hasHeightForWidth())
        self.BACK.setSizePolicy(sizePolicy)
        self.BACK.setObjectName("BACK")
        self.horizontalLayout.addWidget(self.BACK)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.START = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.START.sizePolicy().hasHeightForWidth())
        self.START.setSizePolicy(sizePolicy)
        self.START.setObjectName("START")
        self.horizontalLayout_2.addWidget(self.START)
        self.PAUSE = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PAUSE.sizePolicy().hasHeightForWidth())
        self.PAUSE.setSizePolicy(sizePolicy)
        self.PAUSE.setObjectName("PAUSE")
        self.horizontalLayout_2.addWidget(self.PAUSE)
        self.HALT = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HALT.sizePolicy().hasHeightForWidth())
        self.HALT.setSizePolicy(sizePolicy)
        self.HALT.setObjectName("HALT")
        self.horizontalLayout_2.addWidget(self.HALT)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Free)
        QtCore.QMetaObject.connectSlotsByName(Free)

    def retranslateUi(self, Free):
        _translate = QtCore.QCoreApplication.translate
        Free.setWindowTitle(_translate("Free", "Form"))
        self.label.setText(_translate("Free", "自由练习"))
        self.JUDGE.setText(_translate("Free", "评测"))
        self.PLAY.setText(_translate("Free", "播放"))
        self.BACK.setText(_translate("Free", "返回"))
        self.START.setText(_translate("Free", "开始"))
        self.PAUSE.setText(_translate("Free", "暂停"))
        self.HALT.setText(_translate("Free", "完成"))