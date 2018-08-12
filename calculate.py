# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculate.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
ev=sqlite3.connect("FCleage.db")

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(610, 553)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 20, 291, 20))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 50, 511, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.c1 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.c1.setCurrentText("")
        self.c1.setObjectName("c1")
        
        self.horizontalLayout.addWidget(self.c1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.c2 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.c2.setMaxVisibleItems(9)
        self.c2.setObjectName("c2")
        self.horizontalLayout.addWidget(self.c2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(50, 140, 511, 331))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pl = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.pl.setObjectName("pl")
        self.horizontalLayout_2.addWidget(self.pl)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pp = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.pp.setObjectName("pp")
        self.horizontalLayout_2.addWidget(self.pp)
        self.cs = QtWidgets.QPushButton(self.centralwidget)
        self.cs.setGeometry(QtCore.QRect(250, 480, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cs.setFont(font)
        self.cs.setObjectName("cs")
        self.cs.clicked.connect(self.evaluate)
        self.c1.activated.connect(self.additem)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 110, 551, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 90, 71, 85))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(320, 90, 41, 85))
        self.label_4.setObjectName("label_4")
        self.points = QtWidgets.QLabel(self.centralwidget)
        self.points.setGeometry(QtCore.QRect(380, 90, 30, 85))
        self.points.setObjectName("points")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 610, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pl.setFont(font)
        self.pp.setFont(font)
        self.pl.setStyleSheet("color:rgb(0, 0, 255)")
        self.pp.setStyleSheet("color:#3bead6")
        self.points.setFont(font)
        self.points.setStyleSheet("color:#3bead6")

        self.retranslateUi(MainWindow)
        self.c2.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Evaluate Performance of your Fantasy Team</span></p></body></html>"))
        self.cs.setText(_translate("MainWindow", "Calculate Score"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Players</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Points</span></p></body></html>"))
        self.points.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#26ecec;\">0</span></p></body></html>"))

    def evaluate(self):
            self.cs.setEnabled(False)
            tm=ev.cursor()
            pt=0
            team=self.c1.currentText()
            tm.execute("select players from teams where name='"+team+"'")
            st=tm.fetchone()[0]
            x=""
            t=0
            for i in st:
                
                if(i != ' '):
                    x=x+i
                else: 
                   
                    k=ev.cursor()
                    k.execute("select * from match where player='"+x+"'")
                    bs=k.fetchall()[0]
                    bs=list(bs)
                    batscore=int(bs[1]/2)
                    
                    if batscore>=50:
                        batscore+=5
                    if batscore>=100: batscore+=10
                    if bs[1]>0:
                        sr=bs[1]*100/bs[2]
                        if sr>=80 and sr<100: batscore+=2
                        if sr>=100:batscore+=4
                    batscore=batscore+bs[3]
                    batscore=batscore+2*bs[4]+10*bs[9]+10*bs[10]+10*bs[11]
                    bowlscore=bs[8]*10
                    if bs[8]>=3: bowlscore=bowlscore+5
                    if bs[8]>=5: bowlscore=bowlscore=bowlscore+10
                    if bs[5]>0:
                      er=bs[7]/bs[5]
                      if er<=2: bowlscore=bowlscore+10
                      if er>2 and er<=3.5: bowlscore=bowlscore+7
                      if er>3.5 and er<=4.5: bowlscore=bowlscore+4
                    x=""
                    self.pp.addItem(str(batscore+bowlscore))
                    t=t+batscore+bowlscore
                self.points.setText(str(t))

                    
                
    def additem(self):
        self.cs.setEnabled(True)
        self.pl.clear()
        self.pp.clear()
        count=1
        self.points.setText("0")
        tm=ev.cursor()
        pt=0
        team=self.c1.currentText()
        tm.execute("select players from teams where name='"+team+"'")
        st=tm.fetchone()[0]
        x=""
        for i in st:
            if(i != ' '):
                x=x+i
            else: 
                self.pl.addItem(x)
                x=""
             


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

