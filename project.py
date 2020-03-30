from PyQt5.QtCore    import * 
from PyQt5.QtWidgets import *
import os
import subprocess
class Page(QDialog): 
    def __init__(self, parent=None):             # __init__
        super(Page, self).__init__(parent)       # __init__

        self.my_label = QLineEdit("ls")
        button = QPushButton("OUTPUT")
        self.outputLabel = QLabel()
        
        self.layout   = QVBoxLayout()
        
        self.layout.addWidget(self.my_label)
        self.layout.addWidget(button)
        

        self.setLayout(self.layout)

        self.setLayout(self.layout)
        self.setWindowTitle("COMMAND PATH")
        button.clicked.connect(self.findCommand)

    def findCommand(self):
        stream = os.popen(self.my_label.text())
        p = subprocess.Popen(["whereis",self.my_label.text()], stdout=subprocess.PIPE) 
        directory_content = p.stdout.readlines()[0]
        length = len(directory_content)
        outputText = str(directory_content[0:length-1])
        self.outputLabel.setText(outputText  )
        self.layout.addWidget(self.outputLabel)
        
if __name__ == '__main__':                       
    import sys
    app = QApplication(sys.argv)
    window = Page()
    window.show()
    sys.exit(app.exec_())   