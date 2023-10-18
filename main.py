import unreal
import sys

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget


def say_hello():
    print('Hello!!')

if __name__ == '__main__':
    
    class MainWindow(QMainWindow):
        
        def __init__(self):
            super().__init__(parent=None)

            self.window = QMainWindow()
            self.window.setWindowTitle("Simple PySide2 GUI")

            self.button = QPushButton("Click Me")
            self.button.clicked.connect(self.callFunction)

            self.layout = QVBoxLayout()
            self.layout.addWidget(self.button)

            widget = QWidget()
            widget.setLayout(self.layout)
            self.setCentralWidget(widget)
            
        def callFunction(self):
            say_hello()

    if not QApplication.instance():
        myApp = QApplication()
    else:
        myApp = QApplication.instance()
        
    window = MainWindow()
    window.show()
    unreal.parent_external_window_to_slate(window.winId())
    # sys.exit(myApp.exec_())


