'''
Created on Jan 13, 2016
author: belalballout
'''
import sys
from PySide import QtGui,QtCore
import re

class FileDialog(QtGui.QFileDialog):
    
    def __init__(self,objectName = 'fileDialog',parent = None):
        super(FileDialog,self).__init__(parent)
        self.initUI()
        
    def initUI(self):
        pass

class CentralWidget(QtGui.QWidget):
    
    def __init__(self,objectName = 'centralWidget',parent = None):
        super(CentralWidget,self).__init__(parent)
        self.initUI()
        
    def initUI(self):
        self.mainLayout = QtGui.QVBoxLayout(objectName = 'mainLayout')
        self.setLayout(self.mainLayout)
        
        self.textEditWidget = QtGui.QWidget()
        self.textEditLayout = QtGui.QVBoxLayout()
        self.matchFromTextField = QtGui.QLineEdit()
        self.matchToTextField = QtGui.QLineEdit()
        self.textEditLayout.addWidget(self.matchFromTextField)
        self.textEditLayout.addWidget(self.matchToTextField)
        self.textEditWidget.setLayout(self.textEditLayout)
       
        self.outText = QtGui.QTextEdit()
        self.outText.setEnabled(False)
                
        self.mainLayout.addWidget(self.textEditWidget)
        self.mainLayout.addWidget(self.outText)

        self.matchFromTextField.textChanged.connect(self.matchFunc)
        self.matchToTextField.textChanged.connect(self.matchFunc)
        
    def matchFunc(self):
        textFrom = self.matchFromTextField.text()
        textTo = self.matchToTextField.text()
        
        matchedText = []
        
        for match in  re.findall(textFrom, textTo):
            matchedText.append(match)
            
        matchedStr = ''.join(matchedText)
        self.outText.setText(matchedStr)

class TestUI(QtGui.QMainWindow):

    def __init__(self,objectName = 'testWin',parent = None):
        super(TestUI,self).__init__(parent)
        self.initUI()
        
    def initUI(self):
        centralWidget = CentralWidget(parent = self)
        self.setCentralWidget(centralWidget)
        
def main():
        app = QtGui.QApplication(sys.argv)
        #=======================================================================
        # window = TestUI()
        # window.show()
        #=======================================================================
        fileD = FileDialog()
        fileD.show()
        sys.exit(app.exec_())      

if __name__ == '__main__':
    main()
        