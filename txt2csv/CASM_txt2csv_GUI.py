# *-* coding: utf-8 *-*

import sys, os
from bs4 import BeautifulSoup
import csv
from PyQt5.QtWidgets import QLabel,QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot




class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Simple TXT to CSV converter for CASM'
        self.left = 10
        self.top = 40
        self.width = 400
        self.height = 300
        self.initUI()
        self.txtfileName = ''
        self.csvfileName = ''
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        button1 = QPushButton('Load txt file', self)
        button1.setToolTip('Choose a CASM marked-up text file.')
        button1.move(self.width/4,70)
        button1.clicked.connect(self.openFileNameDialog)


        button2 = QPushButton('Output csv file', self)
        button2.setToolTip('Insert your output csv file.')
        button2.move(self.width/2,70)
        button2.clicked.connect(self.saveFileDialog)


        button3 = QPushButton('CONVERT', self)
        button3.setToolTip('convert file')
        button3.move(self.width/4,100)
        button3.resize(190,50)
        button3.clicked.connect(self.txt2csv)

        self.show()
    
    @pyqtSlot() 
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.txtfileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","txt Files(*.txt);;All Files (*)", options=options)
        if self.txtfileName:
            print("Your text file:" + self.txtfileName)
    
    @pyqtSlot()
    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.csvfileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","csv Files (*.csv);;All Files (*)", options=options)
        if self.csvfileName:
            self.csvfileName += ".csv"
            print("Your csv file:" + self.csvfileName)
          

    def txt2csv(self):
        CASM_tags_lst = ["e", "sb", "st", "s","act"]
        try:
            INPUT_txt = self.txtfileName
            OUTPUT_csv = self.csvfileName
            with open(OUTPUT_csv,'w',newline='',encoding='UTF-8') as csv_file,  open(INPUT_txt,'r',encoding='UTF-8') as open_f:
                soup = BeautifulSoup(open_f.read(), "html.parser")
                writer = csv.writer(csv_file)  
                for CASM_tags in soup.find_all(CASM_tags_lst):
                    first, second = CASM_tags.name, CASM_tags.get_text()
                    #print(first,second)
                    res = self.markup_check(first, second)
                    if res != None:
                        writer.writerow(res)
                self.file_exists(OUTPUT_csv)
            
        except Exception as e:
            print('Detected Error: ', getattr(e, 'message', repr(e)))

    def markup_check(self,f,s):
        if (f and s) != '':
            if len(s) > 100:
                msg = 'Line \"('+f+') '+s[:20]+'... \" is over <b>100</b> characters. Proceed anyway?'
                buttonReply = QMessageBox.question(self, 'Possible Mark-up Error', msg, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    return [f,s]
                else:
                    return None
            else:
                return [f,s]
    
    def file_exists(self,o_f):
        f_exits =os.path.isfile(o_f)
        #f_size = os.path.getsize(o_f)
        #print(f_exits)
        #print(f_size)
        if f_exits: 
            #if f_size > 0:
            print ('Your csv file has been successfully created.')
            #else:
                #print ('Detected Error: Empty File.')
        else:
            print('Detected Error: File was not created.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())