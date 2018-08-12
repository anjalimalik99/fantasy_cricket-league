# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finalModule.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import *
from calculate import Ui_MainWindow2
import ctypes
import sqlite3
ckt=sqlite3.connect('FCleage.db')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 557)
        MainWindow.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 40, 641, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayoutWidget.setStyleSheet("background-color:#dfdfdf;border:0px 1px 1px solid black")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 20, 0, 16)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        
        self.bt = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.bt.setAlignment(QtCore.Qt.AlignCenter)
        self.bt.setObjectName("bt")
        self.bt.setText("")
        self.horizontalLayout.addWidget(self.bt)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        
        self.bow = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.bow.setAlignment(QtCore.Qt.AlignCenter)
        self.bow.setObjectName("bow")
        self.bow.setText("")
        self.horizontalLayout.addWidget(self.bow)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        
        self.ar = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.ar.setAlignment(QtCore.Qt.AlignCenter)
        self.ar.setObjectName("ar")
        self.ar.setText("")
        self.horizontalLayout.addWidget(self.ar)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        
        self.wk = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.wk.setAlignment(QtCore.Qt.AlignCenter)
        self.wk.setObjectName("wk")
        self.wk.setText("")
        self.horizontalLayout.addWidget(self.wk)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(80,40, 91, 16))
        self.label_10.setObjectName("label_10")
        self.label_10.setStyleSheet("background-color:#dfdfdf;font-size:8px;border:1px 0px 1px  1px solid black")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(130, 140, 251, 21))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.rbBat = QtWidgets.QRadioButton(self.layoutWidget)
        self.rbBat.setObjectName("rbBat")
        self.horizontalLayout_6.addWidget(self.rbBat)
        self.rbBow = QtWidgets.QRadioButton(self.layoutWidget)
        self.rbBow.setObjectName("rbBow")
        self.horizontalLayout_6.addWidget(self.rbBow)
        self.rbAR = QtWidgets.QRadioButton(self.layoutWidget)
        self.rbAR.setObjectName("rbAR")
        self.horizontalLayout_6.addWidget(self.rbAR)
        self.rbWK = QtWidgets.QRadioButton(self.layoutWidget)
        self.rbWK.setObjectName("rbWK")
        self.horizontalLayout_6.addWidget(self.rbWK)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(114, 120, 231, 21))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        
        self.pa = QtWidgets.QLabel(self.layoutWidget1)
        self.pa.setMaximumSize(QtCore.QSize(16777215, 14))
        self.pa.setObjectName("pa")
        self.pa.setText("")
        self.horizontalLayout_2.addWidget(self.pa)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(400, 120, 211, 21))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        
        self.pu = QtWidgets.QLabel(self.layoutWidget2)
        self.pu.setObjectName("pu")
        self.pu.setText("")
        self.horizontalLayout_3.addWidget(self.pu)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(400, 140, 291, 21))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.team = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.team.setText("")
        self.team.setObjectName("team")
        self.horizontalLayout_4.addWidget(self.team)

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(65)
        self.l1 = QtWidgets.QListWidget(self.centralwidget)
        self.l1.setGeometry(QtCore.QRect(130, 160, 251, 331))
        self.l1.setObjectName("l1")
        self.l1.setFont(font)
        self.l1.setStyleSheet("color:rgb(0, 0, 255);font-size:10pt")
        self.l2 = QtWidgets.QListWidget(self.centralwidget)
        self.l2.setGeometry(QtCore.QRect(430, 160, 251, 331))
        self.l2.setObjectName("l2")
        self.l2.setFont(font)
        self.l2.setStyleSheet("color:rgb(0, 0, 255);font-size:10pt")
        self.l2_2 = QtWidgets.QListWidget(self.centralwidget)
        self.l2_2.setGeometry(QtCore.QRect(130, 160, 251, 331))
        self.l2_2.setObjectName("l2_2")
        self.l2_2.setFont(font)
        self.l2_2.setStyleSheet("color:rgb(0, 0, 255);font-size:10pt")
        self.l3 = QtWidgets.QListWidget(self.centralwidget)
        self.l3.setGeometry(QtCore.QRect(130, 160, 251, 331))
        self.l3.setObjectName("l3")
        self.l3.setFont(font)
        self.l3.setStyleSheet("color:rgb(0, 0, 255);font-size:10pt")
        self.l4 = QtWidgets.QListWidget(self.centralwidget) 
        self.l4.setGeometry(QtCore.QRect(130, 160, 251, 331))
        self.l4.setObjectName("l4")
        self.l4.setFont(font)
        self.l4.setStyleSheet("color:rgb(0, 0, 255);font-size:10pt")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        self.menubar.setStyleSheet("background-color:#b3b4b5")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.new1 = QtWidgets.QAction(MainWindow)
        self.new1.setObjectName("new1")
        self.save = QtWidgets.QAction(MainWindow)
        self.save.setObjectName("save")
        self.open = QtWidgets.QAction(MainWindow)
        self.open.setObjectName("open")
        self.evaluate = QtWidgets.QAction(MainWindow)
        self.evaluate.setObjectName("evaluate")
        self.menuManage_Teams.addAction(self.new1)
        self.menuManage_Teams.addAction(self.save)
        self.menuManage_Teams.addAction(self.open)
        self.menuManage_Teams.addAction(self.evaluate)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.menubar.addAction(self.menuManage_Teams.menuAction())
        self.rbBat.setCheckable(True)
        self.rbBow.setCheckable(True)
        self.rbAR.setCheckable(True)
        self.rbWK.setCheckable(True)
        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.menufunction)
        self.rbBat.toggled.connect(self.rb1)
        self.rbBow.toggled.connect(self.rb2)
        self.rbAR.toggled.connect(self.rb3)
        self.rbWK.toggled.connect(self.rb4)

        self.bt.setFont(font)
        self.bt.setStyleSheet("color:#3bead6;font-size:10pt")
        self.bow.setFont(font)
        self.bow.setStyleSheet("color:#3bead6;font-size:10pt")
        self.ar.setFont(font)
        self.ar.setStyleSheet("color:#3bead6;font-size:10pt")
        self.wk.setFont(font)
        self.wk.setStyleSheet("color:#3bead6;font-size:10pt")
        self.pa.setFont(font)
        self.pa.setStyleSheet("color:#3bead6;font-size:10pt")
        self.pu.setFont(font)
        self.pu.setStyleSheet("color:#3bead6;font-size:10pt")
        self.team.setFont(font)
        self.team.setStyleSheet("color:#3bead6;font-size:10pt")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;height:30px\">Batsman(BAT)</span></p></body></html>"))
        self.bt.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#3bead6;\">0</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;height:30px\">Bowler(BOW)</span></p></body></html>"))
        self.bow.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#3bead6;\">0</span></p></body></html>"))
        self.ar.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#3bead6;\">0</span></p></body></html>"))
        self.wk.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#3bead6;\">0</span></p></body></html>"))
        self.pa.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#3bead6;\">0</span></p></body></html>"))
        self.pu.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#3bead6;\">0</span></p></body></html>"))

        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;height:30px\">All Rounder(AR)</span></p></body></html>"))
        self.ar.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#3bead6;\">0</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#000000;\">Wicket Keeper(WK)</span></p></body></html>"))
        self.wk.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#3bead6; ;margin-left:2px\">0</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Your Selection</span></p></body></html>"))
        self.rbBat.setText(_translate("MainWindow", "BAT"))
        self.rbBow.setText(_translate("MainWindow", "BOW"))
        self.rbAR.setText(_translate("MainWindow", "AR"))
        self.rbWK.setText(_translate("MainWindow", "WK"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#000000;\">Points Available</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Points Used</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Team Name </span>"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage_Teams"))
        self.new1.setText(_translate("MainWindow", "New_Team"))
        self.save.setText(_translate("MainWindow", "Save_Team"))
        self.open.setText(_translate("MainWindow", "Open_Team"))
        self.evaluate.setText(_translate("MainWindow", "Evaluate_Team"))
        self.l1.itemDoubleClicked.connect(self.select)
        self.l2_2.itemDoubleClicked.connect(self.select)
        self.l3.itemDoubleClicked.connect(self.select)
        self.l4.itemDoubleClicked.connect(self.select)
        self.l2.itemDoubleClicked.connect(self.remove)
               
    def remove(self, item): 
        if(self.l2.count() > 0):
            p=item.text()
            b2=ckt.cursor()
            b2.execute("select value from stats  where player='"+p+"'")
            x=b2.fetchone()
            u=int(self.pu.text())
            a=int(self.pa.text())
            u=u-x[0]
            a=a+x[0]
                
            self.pa.setText(str(a))
            self.pu.setText(str(u))
            
            b2.execute("select ctg from stats  where player='"+p+"'")
            ctg=list(b2.fetchone())

            
            if ctg[0] == "BAT":
                    self.l2.takeItem(self.l2.row(item))
                    self.l1.addItem(item.text())
                    t=int(self.bt.text())-1
                    self.bt.setText(str(t))
                
            elif(ctg[0]=="BWL"):
                    self.l2.takeItem(self.l2.row(item))
                    self.l2_2.addItem(item.text())
                    self.bow.setText(str(int(self.bow.text())-1))
        
            elif(ctg[0]=="AR"):
                    self.l2.takeItem(self.l2.row(item))
                    self.l3.addItem(item.text())
                    self.ar.setText(str(int(self.ar.text())-1))
                    
            elif(ctg[0]=="WK"):
                    self.l2.takeItem(self.l2.row(item))
                    self.l4.addItem(item.text())
                    self.wk.setText(str(int(self.wk.text())-1))
                                            
        
    def select(self,item):
        if(self.l2.count() < 11):
            p=item.text()    
            b2=ckt.cursor()
            b2.execute("select value from stats  where player='"+p+"'")
            if int(self.bt.text())+int(self.bow.text())+int(self.ar.text()) == 10:
                ctypes.windll.user32.MessageBoxW(0,"You have selected 10 players,there must be 1 wicket keeper in team","Error",0)
               
            if(self.rbBat.isChecked()==True and int(self.bt.text())+int(self.bow.text())+int(self.ar.text())<10 ):
                if self.bt.text() <='5':
                    self.l1.takeItem(self.l1.row(item))
                    self.l2.addItem(item.text())
                    x=b2.fetchone()
                    u=int(self.pu.text())
                    a=int(self.pa.text())
                    u=u+x[0]
                    a=a-x[0]    
                    self.pa.setText(str(a))
                    self.pu.setText(str(u))
                    t=int(self.bt.text())+1
                    self.bt.setText(str(t))
                else:
                    ctypes.windll.user32.MessageBoxW(0,"More than 6 Batsman are  not allowed in a team","Error",0)                       
              
                    
            elif(self.rbBow.isChecked()==True and int(self.bt.text())+int(self.bow.text())+int(self.ar.text())<10):
                if self.bow.text() <='4':
                    self.l2_2.takeItem(self.l2_2.row(item))
                    self.l2.addItem(item.text())
                    x=b2.fetchone()
                    u=int(self.pu.text())
                    a=int(self.pa.text())
                    u=u+x[0]
                    a=a-x[0]    
                    self.pa.setText(str(a))
                    self.pu.setText(str(u))
                    self.bow.setText(str(int(self.bow.text())+1))
                else:
                    ctypes.windll.user32.MessageBoxW(0,"More than 5 Bowlers are  not allowed in a team","Error",0)                       
              
            
            elif(self.rbAR.isChecked()==True and int(self.bt.text())+int(self.bow.text())+int(self.ar.text())<10 ):
                if self.ar.text() <'2':
                    self.l3.takeItem(self.l3.row(item))
                    self.l2.addItem(item.text())
                    x=b2.fetchone()
                    u=int(self.pu.text())
                    a=int(self.pa.text())
                    u=u+x[0]
                    a=a-x[0]    
                    self.pa.setText(str(a))
                    self.pu.setText(str(u))
                    self.ar.setText(str(int(self.ar.text())+1))
                else:
                    ctypes.windll.user32.MessageBoxW(0,"More than 2 all rounders  are not allowed in a team","Error",0)                       
              
                
            elif(self.rbWK.isChecked()==True):
                if self.wk.text() =='0':
                    self.l4.takeItem(self.l4.row(item))
                    self.l2.addItem(item.text())     
                    x=b2.fetchone()
                    u=int(self.pu.text())
                    a=int(self.pa.text())
                    u=u+x[0]
                    a=a-x[0]    
                    self.pa.setText(str(a))
                    self.pu.setText(str(u))
                    self.wk.setText(str(int(self.wk.text())+1))
            
                elif self.wk.text() =='1':
                             ctypes.windll.user32.MessageBoxW(0,"More than 1 Wicket Keeper is not allowed in a team","Error",0)                       
                  
                        
            
            
        else:
            ctypes.windll.user32.MessageBoxW(0,"More than 11 Players  are not allowed in a team","Error",0)
            
            

    def rb1(self):
            self.l1.show()
            self.l2_2.hide()
            self.l3.hide()
            self.l4.hide()
            choice=ckt.cursor()
            choice.execute("select choice from stats where ctg='BAT'")
            if choice.fetchone()[0]==1:
                choice.execute("update stats set choice=0 where ctg='BAT'")
                bat=ckt.cursor()
                bat.execute("select player from stats where ctg='BAT'")
                data=bat.fetchall()
                for x in data:
                    self.l1.addItem(x[0])
                bat.execute("select value from stats where ctg='BAT'")
                data=bat.fetchall()
                val=int(self.pa.text())
                for x in data:
                    val=val + x[0]
                self.pa.setText(str(val))
               
    def rb2(self):
            self.l2_2.show()
            self.l1.hide()
            self.l3.hide()
            self.l4.hide()
            choice2=ckt.cursor()
            choice2.execute("select choice from stats where ctg='BWL'")
            if choice2.fetchone()[0]==1:
                choice2.execute("update stats set choice=0 where ctg='BWL'")
                bwl=ckt.cursor()
                bwl.execute("select player from stats where ctg='BWL'")
                data=bwl.fetchall()
                for x in data:
                    self.l2_2.addItem(x[0])
                bwl.execute("select value from stats where ctg='BWL'")
                data=bwl.fetchall()
                val=int(self.pa.text())
                for x in data:
                    val=val + x[0]
                self.pa.setText(str(val))

    def rb3(self):
            self.l3.show()
            self.l2_2.hide()
            self.l1.hide()
            self.l4.hide()
            choice3=ckt.cursor()
            choice3.execute("select choice from stats where ctg='AR'")
            if choice3.fetchone()[0]==1:
                choice3.execute("update stats set choice=0 where ctg='AR'")
                ckt.commit()
                ar=ckt.cursor()
                ar.execute("select player from stats where ctg='AR'")
                data=ar.fetchall()
                for row in data:
                  self.l3.addItem(row[0])
                ar.execute("select value from stats where ctg='AR'")
                data=ar.fetchall()
                val=int(self.pa.text())
                for x in data:
                  val=val + x[0]
                self.pa.setText(str(val))

    def rb4(self):
            self.l4.show()
            self.l2_2.hide()
            self.l3.hide()
            self.l1.hide()
            choice4=ckt.cursor()
            choice4.execute("select choice from stats where ctg='WK'")
            if choice4.fetchone()[0]==1:
                choice4.execute("update stats set choice=0 where ctg='WK'")              
                wk=ckt.cursor()
                wk.execute("select player from stats where ctg='WK'")
                data=wk.fetchall()
                for row in data:
                  self.l4.addItem(row[0])
                wk.execute("select value from stats where ctg='WK'")
                data=wk.fetchall()
                val=int(self.pa.text())
                for x in data:
                  val=val + x[0]
                self.pa.setText(str(val))

    def menufunction(self,action):
        txt=action.text()       
        if(txt == "New_Team"):
            self.pa.setText("0")
            self.pu.setText("0")
            self.bt.setText("0")
            self.bow.setText("0")
            self.ar.setText("0")
            self.wk.setText("0")
            self.l1.clear()
            self.l2_2.clear()
            self.l3.clear()
            self.l4.clear()
            self.l2.clear()
            
            choice5=ckt.cursor()
            choice5.execute("update stats set choice=1")
        elif txt=="Save_Team":
            
            self.master=Tk()
            self.master.title("Team Name")
            self.master.geometry("300x200+550+300")
            self.tm=StringVar()
            Label(self.master,text="Team Name").pack()
            self.myentry = Entry(self.master,textvariable=self.tm).pack()
            self.saveButton=Button(self.master,text="Save",command=self.ins).pack()
            self.master.mainloop()
            
        elif txt=="Evaluate_Team":
            self.window=QtWidgets.QMainWindow()
            self.ui=Ui_MainWindow2()
            self.ui.setupUi(self.window)
            self.window.show()
            ev=ckt.cursor()
            ev.execute("select name from teams")
            x=ev.fetchall()
            for i in tuple(x):
                   self.ui.c1.addItem(i[0])

        elif txt=="Open_Team":
            self.master=Tk()
            self.master.title("Team Name")
            self.master.geometry("300x200+550+300")
            self.op=StringVar()
            Label(self.master,text="Team Name").pack()
            self.myentry = Entry(self.master,textvariable=self.op).pack()
            self.openButton=Button(self.master,text="Open",command=self.opn).pack()
            self.master.mainloop()

    def opn(self):
        self.master.destroy()
        tn=self.op.get()
        o=ckt.cursor()
        o.execute("select players from teams where name='"+tn+"'")
        self.team.setText(tn)
        st=o.fetchone()[0]
        self.l2.clear()
        x=""
        nbat=0
        nbow=0
        nwk=0
        nar=0
        pt=0
        for i in st:
            if(i != ' '):
                x=x+i
            else:
                self.l2.addItem(x)
                k=ckt.cursor()
                k.execute("select ctg from stats where player='"+x+"'")
                ctg=list(k.fetchone())
                if( ctg[0] =="BAT"):
                    nbat=nbat+1
                elif(ctg[0]=="BWL"):
                    nbow=nbow+1
                elif(ctg[0]=="AR"):
                    nar=nar+1
                elif (ctg[0]=="WK"):
                    nwk=nwk+1
                
                k.execute("select value from stats where player='"+x+"'")
                pt=pt+k.fetchone()[0]
                x=""
        self.bt.setText(str(nbat))
        self.bow.setText(str(nbow))
        self.ar.setText(str(nar))
        self.wk.setText(str(nwk))
        self.pu.setText(str(pt))
        self.pa.setText(str(0))
        self.l1.clear()
        self.l2_2.clear()
        self.l3.clear()
        self.l4.clear()     
            
    def ins(self):
        it=""
        for indx in range(self.l2.count()):
            it=it + self.l2.item(indx).text() +" "
        n=self.tm.get()
        self.master.destroy()
        self.team.setText(n)
        i=ckt.cursor()
        i.execute("insert into teams(name,players) values ('"+n+"','"+it+"')")
        ckt.commit()
 

    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

