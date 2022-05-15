import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QApplication, 
    QMainWindow,
    QWidget,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout
    )

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        
        # ------------------------------------------------------- #
        # Main layout                                             #
        # ------------------------------------------------------- #
        main_layout = QVBoxLayout()

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)
        # -- Main Layout - End ---------------------------------- #

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()