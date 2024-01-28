import sys
from typing import Optional
from PySide6.QtCore import Qt

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

from design import Ui_MainWindow

class PythonCPUBenchmark(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.ui.pushButton.clicked.connect(self.start_benchark)
        self.ui.checkBox.toggled.connect(self.chose_benchark_mode)
        self.ui.checkBox_2.toggled.connect(self.chose_benchark_mode)
        self.ui.horizontalSlider.valueChanged.connect(self.get_arrays_number)

        self.chosen_mods = set()

    def start_benchark(self):
        self.set_zero_into_table()
        print("Benchark started")
    
    def get_arrays_number(self):
        size = self.ui.horizontalSlider.value()
        self.ui.label_18.setText(str(size))
    
    def chose_benchark_mode(self, checked):
        sender = self.sender()
        if checked:
            self.chosen_mods.add(sender.text())
            if self.chosen_mods:
                self.ui.pushButton.setEnabled(True)
        else:
            self.chosen_mods.remove(sender.text())
            if not self.chosen_mods:
                self.ui.pushButton.setEnabled(False)
    
    def set_zero_into_table(self):
        self.ui.qtablewidgetitem6.setText("")
        self.ui.qtablewidgetitem7.setText("")
        self.ui.qtablewidgetitem8.setText("")
        self.ui.qtablewidgetitem9.setText("")
        self.ui.qtablewidgetitem10.setText("")
        self.ui.qtablewidgetitem11.setText("")
        self.ui.qtablewidgetitem12.setText("")
        self.ui.qtablewidgetitem13.setText("")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PythonCPUBenchmark()
    window.show()
    sys.exit(app.exec())