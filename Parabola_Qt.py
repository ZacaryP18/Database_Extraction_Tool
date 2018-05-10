#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QDialog, QWidget, QApplication, QPushButton, QGridLayout, QLabel, QLineEdit, QComboBox, QFrame)
from PyQt5.QtGui import (QIcon, QFont, QPixmap)
from PyQt5 import QtCore

import os

""" Check how tabs work when selecting buttons """
class MassParabola(QDialog):

    def __init__(self):
        super().__init__()

        self.initUI()

        self.chemSymVar = ""
        self.A = ""
        self.T = "" 
 
    def initUI(self):

        pixmap = QPixmap('Output/gnuPlot/nuclearChart.gif')
        label = QLabel(self)
        label.setPixmap(pixmap)

        #Input Dialogs
        self.mass = QLineEdit(self)
        self.mass.setText("Mass #")
        self.mass.setMaximumWidth(260)
        self.mass.setStyleSheet("border: 1px solid #2B4570; border-radius:5px; width: 25px; height: 25px; margin: 0px 25px 0px 25px;")

        self.temp = QLineEdit(self)
        self.temp.setText("Temp (K)")
        self.temp.setMaximumWidth(260)
        self.temp.setStyleSheet("border: 1px solid #2B4570; border-radius:5px; width: 25px; height: 25px; margin: 0px 25px 0px 25px;")

        # Button defined below 

        submit = QPushButton("Submit", self)
        submit.clicked.connect(self.submitClicked)
        submit.setStyleSheet("background-color:#EBEEF2; border: 1px solid #2B4570; border-radius:5px; color: #2B4570; height:25px; margin: 0px 25px 0px 25px; padding: 0px 15px 0px 15px;")
        submit.installEventFilter(self) 


        full = QPushButton("Full", self)
        full.setStyleSheet("background-color:#EBEEF2; border: 1px solid #2B4570; border-radius:5px; color: #2B4570; height:25px; margin-left: 25px; margin-right: 25px;")      
        full.installEventFilter(self)      


        main = QPushButton("Main", self)
        main.clicked.connect(self.mainClicked)
        main.setStyleSheet("background-color:#EBEEF2; border: 1px solid #2B4570; border-radius:5px; color: #2B4570; height:25px; margin-left: 25px; margin-right: 25px;")                
        main.installEventFilter(self)      


        exit = QPushButton("Exit", self)
        exit.clicked.connect(QApplication.instance().quit)
        exit.setStyleSheet("background-color:#EBEEF2; border: 1px solid #2B4570; border-radius:5px; color: #2B4570; height:25px; margin-left: 25px; margin-right: 25px;")                
        exit.installEventFilter(self)      

 
       # GRID LAYOUT 

        grid = QGridLayout()
        self.setLayout(grid)

        topGrid = QGridLayout()

        line = QFrame()
        line.setFrameStyle(QFrame.HLine)
        line.setLineWidth(2)

        line2 = QFrame()
        line2.setFrameStyle(QFrame.HLine)
        line2.setLineWidth(2)


        innerinnerGrid = QGridLayout()
        topGrid.addWidget(full, 0, 4)
        topGrid.addWidget(main, 0, 5)
        topGrid.addWidget(exit, 0, 6)
        topGrid.setSpacing(40)

        botGrid = QGridLayout()
        botGrid.addWidget(self.mass, 0, 1)
        botGrid.addWidget(self.temp, 0, 3)
        botGrid.addWidget(submit, 0, 5)
        botGrid.setSpacing(40)    

        grid.addLayout(topGrid, 0, 0)
        grid.addWidget(line, 1, 0, 1, 6)
        grid.addWidget(label, 2, 0)
        grid.addWidget(line2, 3, 0, 1, 6)
        grid.addLayout(botGrid, 4, 0)

        self.setGeometry(300, 300, 500, 420) #x coord, y coord, width, height
        self.setWindowTitle('Mass Parabola Evaluation')
        self.setStyleSheet("background-color:white")

        #self.exec_()
    def eventFilter(self, object, event):
        if event.type() == QtCore.QEvent.HoverEnter:
            object.setStyleSheet("background-color:#1E555C; color:#EBEEF2; border:1px solid #1E555C; border-radius:5px; height:25px; margin: 0px 25px 0px 25px;padding: 0px 15px 0px 15px;")
            return True;
        if event.type() == QtCore.QEvent.HoverLeave:
            object.setStyleSheet("background-color:#EBEEF2; border: 1px solid #2B4570; border-radius:5px; color: #2B4570; height:25px; margin: 0px 25px 0px 25px;padding: 0px 15px 0px 15px;")
        return False;


    def submitClicked(self):
        """Send user input to nuclear structure sorting function"""
        self.A = self.mass.text()
        self.T = self.temp.text()
        self.accept()

    def mainClicked(self):
        #TODO: Resolve bug when exiting from main window
        self.chemSymVar = "Zn"
        self.A = 10
        self.spinVar = "0+"
        self.exitcount = 1
        self.close()
        os.system("python3 StartupQt.py")


#if __name__ == '__main__':

app = QApplication(sys.argv)
ex = MassParabola()
ex.exec_()
#sys.exit(app.exec_())
app.exec_()


#Need to define a class for the variables output by the gui (the user inputs), to be used in the other scripts

class parabolaoutputs:
#These are the Nuclear Structure (ENSDF inputs) variables
    periodicTable=open("ElementList.txt",'r')
    Z = periodicTable.readline()
    Z = Z.strip()
    A=ex.A
    J=""
    T=ex.T

    ##These if statements either kill the program or input preset values if the
    ##user leaves a section blank.
    if A == '' or A == "Mass #":
        print("Please choose a valid mass number.")
        sys.exit()
    if T == '' or T == "Temp (K)":
        T = 0

