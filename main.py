from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtUiTools import *
import math

class Calc(QMainWindow):
    def __init__(self):
        super().__init__()


        loader = QUiLoader()
        self.ui = loader.load("design.ui")
        self.ui.show()
        self.ui.jam.clicked.connect(self.jam)
        self.ui.mosavi.clicked.connect(self.mosavi)
        self.ui.tafrigh.clicked.connect(self.tafrigh)
        self.ui.zarb.clicked.connect(self.zarb)
        self.ui.taghsim.clicked.connect(self.taghsim)
        self.ui.tavan.clicked.connect(self.tavan)
        self.ui.jazr.clicked.connect(self.jazr)
        self.ui.baghimande.clicked.connect(self.baghimande)
        self.ui.sin.clicked.connect(self.sin)
        self.ui.cos.clicked.connect(self.cos)
        self.ui.tan.clicked.connect(self.tan)
        self.ui.cot.clicked.connect(self.cot)


    def tafrigh(self):
        self.amalgar = "tafrigh"
        self.num1 = int(self.ui.tb.toPlainText())
        self.ui.tb.setText("")
  
    def jam(self) :
        self.amalgar = "jam"
        self.num1 = int(self.ui.tb.toPlainText())
        self.ui.tb.setText("")

    def zarb(self) :
        self.amalgar = "zarb"
        self.num1 = int(self.ui.tb.toPlainText())
        self.ui.tb.setText("")
    
    def taghsim(self) :
        self.amalgar = "taghsim"
        self.num1 = int(self.ui.tb.toPlainText())
        self.ui.tb.setText("")
        
    def tavan(self) :
        self.amalgar = "tavan"
        self.num1 = int(self.ui.tb.toPlainText())
        self.ui.tb.setText("")

    def baghimande(self) :
        self.amalgar = "baghimande"
        self.num1 = int(self.ui.tb.toPlainText())
        self.ui.tb.setText("")

    def sin(self) :
        self.amalgar = "sin"
        self.num1 = int(self.ui.tb.toPlainText())
        self.ui.tb.setText("")

    def cos(self) :
        self.amalgar = "cos"
        self.num1 = int(self.ui.tb.toPlainText())
        self.ui.tb.setText("")

    def jazr(self) :
        self.amalgar = "jazr"
        self.num1 = int(self.ui.tb.toPlainText())
        self.ui.tb.setText("")

    def tan(self) :
        self.amalgar = "tan"
        self.num1 = int(self.ui.tb.toPlainText())
        self.ui.tb.setText("")
    
    def cot(self) :
        self.amalgar = "cot"
        self.num1 = int(self.ui.tb.toPlainText())
        self.ui.tb.setText("")

    def mosavi(self):
        if self.amalgar == "sin" :
            self.result = math.sinh(self.num1)   
        elif self.amalgar == "cos" :
            self.result = math.cosh(self.num1)
        elif self.amalgar == "jazr" :
            self.result = self.num1 ** 0.5
        elif self.amalgar == "tan":
            self.result = math.tanh(self.num1)
        elif self.amalgar == "cot":
            self.result = (1 / math.tan(self.num1))
        else : 
            self.num2 = int(self.ui.tb.toPlainText())
            if self.amalgar == "jam" :
                self.result = self.num1 + self.num2
            elif self.amalgar == "tafrigh" :
                self.result = self.num1 - self.num2
            elif self.amalgar == "zarb" :
                self.result = self.num1 * self.num2
            elif self.amalgar == "taghsim" :
                self.result = self.num1 / self.num2
            elif self.amalgar == "tavan" :
                self.result = self.num1 ** self.num2
            elif self.amalgar == "baghimande" :
                self.result = self.num1 % self.num2
        self.ui.tb.setText(str(self.result))


my_app = QApplication()
main_window = Calc()
my_app.exec()





