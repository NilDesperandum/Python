import sys
from PyQt5 import QtWidgets, uic
import random
import re
from MainWindow import Ui_MainWindow

words = ('gruszka','samolot','fabryka','szyba','nietoperz','czekolada','traktor','popcorn')
random_index = random.randint(0,len(words)-1)
word_to_guess = words[random_index]
hidden_text = ""
for i in range(len(word_to_guess)):
    hidden_text += "*"

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.hidden_text = hidden_text
        self.counter = 7
        self.setupUi(self)
        self.labelWord.setText(f"<html><head/><body><p align=\"center\">{hidden_text}</p></body></html>")
        self.wyjdzButton.clicked.connect(self.wyjdzButton_clicked)
        self.zgadujButton.clicked.connect(self.zgadujButton_clicked)
        self.lcdNumber.display(self.counter)
    
    def wyjdzButton_clicked(self):
        self.close()

    def check_input(self,word):
        print("tutej")
        pattern = r"^[a-zA-Z]$"
        if re.match(pattern,word):
            print('prawda')
            return True
        else:
            print('falsz')
            print(word)
            return False
    
    def check_win_lose_conditions(self):
        if self.counter == 0 or self.hidden_text == word_to_guess:
            self.zgadujButton.setEnabled(False)
            self.lineEdit.setEnabled(False)
            if self.hidden_text == word_to_guess:
                self.lineEdit.setText("Wygrałeś!!!")


    def findall(self,p, s):
        i = s.find(p)
        while i != -1:
            yield i
            i = s.find(p, i+1)

    def check_guess(self,word):
        indexes = [i for i in self.findall(word, word_to_guess)]
        print(len(indexes))
        if(len(indexes) != 0):
            for i in indexes:
                self.hidden_text = self.hidden_text[:i] + word_to_guess[i] + self.hidden_text[i+1 :]
        else:
            self.counter = self.counter - 1
        
        


    def zgadujButton_clicked(self):
        if(self.check_input(self.lineEdit.text())):
            self.check_guess(self.lineEdit.text())
            print('tu')
            self.labelWord.setText(f"<html><head/><body><p align=\"center\">{self.hidden_text}</p></body></html>")
            self.lcdNumber.display(self.counter)
        self.lineEdit.setText("")
        self.check_win_lose_conditions()

        


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()