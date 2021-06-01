# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'carsMenu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject, QThread

import game


def checkCarsInput(string):
    if string.isnumeric():
        value = int(string)
        return 0 < value <= 100
    else:
        return False


def checkMutationInput(string):
    if string.isnumeric():
        value = int(string)
        return 0 < value < 10
    else:
        return False


def checkMaxVelInput(string):
    if string.isnumeric():
        value = int(string)
        return 0 < value <= 25
    else:
        return False


def checkNeuronsInput(string):
    if string.isnumeric():
        return 0 < int(string) <= 100
    else:
        return False


class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def run(self, carsNum, neuronsNum):
        game.runGame(carsNum, neuronsNum)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(645, 519)
        Dialog.setStyleSheet("")
        self.startButton = QtWidgets.QPushButton(Dialog)
        self.startButton.setGeometry(QtCore.QRect(280, 470, 75, 23))
        self.startButton.setStyleSheet("")
        self.startButton.setIconSize(QtCore.QSize(41, 16))
        self.startButton.setObjectName("pushButton")
        self.startButton.clicked.connect(self.startClicked)

        self.heading = QtWidgets.QLabel(Dialog)
        self.heading.setGeometry(QtCore.QRect(180, 10, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.heading.setFont(font)
        self.heading.setObjectName("heading")

        self.carsNum = QtWidgets.QLabel(Dialog)
        self.carsNum.setGeometry(QtCore.QRect(20, 100, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.carsNum.setFont(font)
        self.carsNum.setObjectName("carsNum")

        self.carsNumT = QtWidgets.QLineEdit(Dialog)
        self.carsNumT.setGeometry(QtCore.QRect(170, 100, 113, 20))
        self.carsNumT.setObjectName("carsNumT")

        self.mutRate = QtWidgets.QLabel(Dialog)
        self.mutRate.setGeometry(QtCore.QRect(20, 140, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.mutRate.setFont(font)
        self.mutRate.setObjectName("mutRate")

        self.mutRateT = QtWidgets.QLineEdit(Dialog)
        self.mutRateT.setGeometry(QtCore.QRect(170, 140, 113, 20))
        self.mutRateT.setObjectName("mutRateT")

        self.MaxVel = QtWidgets.QLabel(Dialog)
        self.MaxVel.setGeometry(QtCore.QRect(20, 180, 151, 21))

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.MaxVel.setFont(font)
        self.MaxVel.setObjectName("MaxVel")
        self.maxVelT = QtWidgets.QLineEdit(Dialog)
        self.maxVelT.setGeometry(QtCore.QRect(170, 180, 113, 20))
        self.maxVelT.setObjectName("maxVelT")
        self.neuronsNum = QtWidgets.QLabel(Dialog)
        self.neuronsNum.setGeometry(QtCore.QRect(320, 100, 180, 21))

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.neuronsNum.setFont(font)
        self.neuronsNum.setObjectName("neuronsNum")
        self.neuronsNumT = QtWidgets.QLineEdit(Dialog)
        self.neuronsNumT.setGeometry(QtCore.QRect(500, 100, 113, 21))
        self.neuronsNumT.setObjectName("neuronsNumT")

        self.easy = QtWidgets.QLabel(Dialog)
        self.easy.setGeometry(QtCore.QRect(80, 390, 47, 13))
        self.easy.setAlignment(QtCore.Qt.AlignCenter)
        self.easy.setObjectName("easy")

        self.medium = QtWidgets.QLabel(Dialog)
        self.medium.setGeometry(QtCore.QRect(300, 390, 47, 13))
        self.medium.setAlignment(QtCore.Qt.AlignCenter)
        self.medium.setObjectName("medium")

        self.hard = QtWidgets.QLabel(Dialog)
        self.hard.setGeometry(QtCore.QRect(510, 390, 47, 13))
        self.hard.setAlignment(QtCore.Qt.AlignCenter)
        self.hard.setObjectName("hard")

        self.easyTrackB = QtWidgets.QPushButton(Dialog)
        self.easyTrackB.setGeometry(QtCore.QRect(20, 270, 181, 121))
        self.easyTrackB.setStyleSheet("")
        self.easyTrackB.setText("")
        self.easyTrackB.setStyleSheet("border :3px solid ;" "border-color : none; ")
        self.easyTrackB.clicked.connect(self.easyClicked)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/easyTrack.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.easyTrackB.setIcon(icon)
        self.easyTrackB.setIconSize(QtCore.QSize(171, 111))
        self.easyTrackB.setObjectName("easyTrackB")
        self.mediumTrackB = QtWidgets.QPushButton(Dialog)
        self.mediumTrackB.setGeometry(QtCore.QRect(230, 270, 181, 121))
        self.mediumTrackB.setAutoFillBackground(False)
        self.mediumTrackB.setStyleSheet("")
        self.mediumTrackB.setText("")
        self.mediumTrackB.setStyleSheet("border :3px solid ;" "border-color : none; ")
        self.mediumTrackB.clicked.connect(self.mediumClicked)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/mediumTrack.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mediumTrackB.setIcon(icon1)
        self.mediumTrackB.setIconSize(QtCore.QSize(171, 111))
        self.mediumTrackB.setObjectName("mediumTrackB")

        self.hardTrackB = QtWidgets.QPushButton(Dialog)
        self.hardTrackB.setGeometry(QtCore.QRect(450, 270, 180, 121))
        self.hardTrackB.setAutoFillBackground(False)
        self.hardTrackB.setStyleSheet("")
        self.hardTrackB.setText("")
        self.hardTrackB.setStyleSheet("border :3px solid ;" "border-color : none; ")
        self.hardTrackB.clicked.connect(self.hardClicked)

        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/hardTrack.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hardTrackB.setIcon(icon2)
        self.hardTrackB.setIconSize(QtCore.QSize(171, 111))
        self.hardTrackB.setObjectName("hardTrackB")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "AiCars"))
        self.startButton.setText(_translate("Dialog", "Start"))
        self.heading.setText(_translate("Dialog", "Choose prefered options"))
        self.carsNum.setText(_translate("Dialog", "Cars number (0 - 100]"))
        self.mutRate.setText(_translate("Dialog", "Mutation rate (0 - 10)"))
        self.MaxVel.setText(_translate("Dialog", "Max velocity (0 - 25]"))
        self.neuronsNum.setText(_translate("Dialog", "Hidden layer size (1 - 100]"))
        self.easy.setText(_translate("Dialog", "easy"))
        self.medium.setText(_translate("Dialog", "medium"))
        self.hard.setText(_translate("Dialog", "hard"))

    def easyClicked(self):
        self.mediumTrackB.setStyleSheet("border :3px solid ;" "border-color : none; ")
        self.hardTrackB.setStyleSheet("border :3px solid ;" "border-color : none; ")
        self.easyTrackB.setStyleSheet("border :3px solid ;" "border-color : green; ")
        game.MAP = "images/easyTrack.png"
        game.START_POS = (800, 150)

    def mediumClicked(self):
        self.mediumTrackB.setStyleSheet("border :3px solid ;" "border-color : green; ")
        self.hardTrackB.setStyleSheet("border :3px solid ;" "border-color : none; ")
        self.easyTrackB.setStyleSheet("border :3px solid ;" "border-color : none; ")
        game.MAP = "images/mediumTrack.png"
        game.START_POS = (800, 250)

    def hardClicked(self):
        self.mediumTrackB.setStyleSheet("border :3px solid ;" "border-color : none; ")
        self.hardTrackB.setStyleSheet("border :3px solid ;" "border-color : green; ")
        self.easyTrackB.setStyleSheet("border :3px solid ;" "border-color : none; ")
        game.MAP = "images/hardTrack.png"
        game.START_POS = (800, 150)

    def startClicked(self):
        notFilled = False
        carsNum = self.carsNumT.text()
        if checkCarsInput(carsNum):
            carsNum = int(carsNum)
            self.carsNumT.setStyleSheet("border :1px solid ;" "border-color : gray; ")
        else:
            self.carsNumT.setStyleSheet("border :1px solid ;" "border-color : red; ")
            notFilled = True

        mutRate = self.mutRateT.text()
        if checkMutationInput(mutRate):
            mutRate = int(mutRate)
            self.mutRateT.setStyleSheet("border :1px solid ;" "border-color : gray; ")
        else:
            self.mutRateT.setStyleSheet("border :1px solid ;" "border-color : red; ")
            notFilled = True

        maxVel = self.maxVelT.text()
        if checkMaxVelInput(maxVel):
            maxVel = int(maxVel)
            self.maxVelT.setStyleSheet("border :1px solid ;" "border-color : gray; ")
        else:
            self.maxVelT.setStyleSheet("border :1px solid ;" "border-color : red; ")
            notFilled = True

        neuronsNum = self.neuronsNumT.text()
        if checkNeuronsInput(neuronsNum):
            neuronsNum = int(neuronsNum)
            self.neuronsNumT.setStyleSheet("border :1px solid ;" "border-color : gray; ")
        else:
            self.neuronsNumT.setStyleSheet("border :1px solid ;" "border-color : red; ")
            notFilled = True

        if not notFilled:
            game.MAX_VEL = maxVel
            game.MUTATION_RATE = mutRate
            game.runGame(carsNum, neuronsNum)
            notFilled = False

    def startGame(self, carsNum, neuronsNum):
        self.thread = QThread()

        self.worker = Worker()

        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run(carsNum, neuronsNum))
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.reportProgress)

        self.thread.start()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
