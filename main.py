# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import os
import sys
import subprocess
from selectfile import Select
import random

dir = os.getcwd() + '\\data\\'
_translate = QtCore.QCoreApplication.translate
ui = uic.loadUiType(dir+'main.ui')[0]

file = open(dir+'exefiles.dat', 'r')
lines = file.read()
exefile = lines.split('\n')
file.close()

class Form(QtWidgets.QMainWindow, ui):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1049,835)
        self.setupUi(self)
        self.codeindex = -1

        #self.listWidget.addItem('asdfghj')
        self.pushButton.clicked.connect(self.selectcode)
        self.pushButton_2.clicked.connect(self.runcode)
        self.pushButton_3.clicked.connect(self.close)

        self.show()

    def listadd(self, codename):
        self.listWidget.clear()
        file = open(dir+codename, 'r')
        self.lines = file.read()
        line = self.lines.split('\n')
        self.shuffleandadd(line)
        file.close()
    def shuffleandadd(self, lst):
        random.shuffle(lst)
        for i in lst:
            self.listWidget.addItem(i)

    
    def runcode(self):
        if self.codeindex == -1:
            QtWidgets.QMessageBox.critical(self,'코드 선택되지 않음','선택된 코드가 없습니다. \n코드를 실행하려면 우선 코드를 선택하십시오. ',QtWidgets.QMessageBox.Yes,QtWidgets.QMessageBox.Yes)
            return
        
        code = []
        originalCode = self.lines.split('\n')
        for i in range(self.listWidget.count()):
            code.append(self.listWidget.item(i).text())
        if originalCode == code:
            subprocess.run(dir+exefile[self.codeindex])
        else:
            QtWidgets.QMessageBox.information(self,'순서 잘못됨','코드의 순서가 잘못되었습니다. \n 다시 한 번 코드의 출력을 예상하며 각 코드의 위치를 바꾸어보세요. ',QtWidgets.QMessageBox.Yes,QtWidgets.QMessageBox.Yes)
        return
    
    def selectcode(self):
        select = Select()
        r = select.showModal()
        if r:
            codename=select.selecteditem
            self.codeindex = select.codeindex
            self.listadd(codename)
        return



if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    form = Form()
    sys.exit(app.exec_())