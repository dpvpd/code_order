from PyQt5 import QtCore, QtGui, QtWidgets, uic
import os

dir = os.getcwd() + '\\data\\'

file = open(dir+'codefiles.dat', 'r')
lines = file.read()
codefile = lines.split('\n')
file.close()

subui = uic.loadUiType(dir+'selectcode.ui')[0]

class Select(QtWidgets.QDialog, subui):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.setFixedSize(221,219)
        self.setupUi(self)
        for i in codefile:
            self.listWidget.addItem(i)
        self.pushButton.clicked.connect(self.accept)
        self.pushButton_2.clicked.connect(self.reject)
        self.listWidget.itemClicked.connect(self.selectionChanged)
        
    def selectionChanged(self, item):
        self.selecteditem = item.text()
        self.codeindex = -1
        for i in range(len(codefile)):
            if codefile[i] == item.text():
                self.codeindex = i


    def showModal(self):
        return super().exec_()