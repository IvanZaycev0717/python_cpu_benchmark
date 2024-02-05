import platform
import psutil

from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import QSize

from design import Ui_MainWindow
from stress_test import CustomBenchamrk


class PythonCPUBenchmark(QMainWindow):
    def __init__(self, loop):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.loop = loop
        self.ui.setupUi(self)
        self.set_zero_into_table()

        # flags
        self.is_benchmark_in_porgress = False

        # Button images
        self.start_icon, self.stop_icon = QIcon(), QIcon()
        self.start_icon.addFile(
            u":/images/images/start.png",
            QSize(), QIcon.Normal, QIcon.Off
            )
        self.stop_icon.addFile(
            u":/images/images/stop.png",
            QSize(), QIcon.Normal, QIcon.Off
            )
        self.ui.pushButton.setIcon(self.start_icon)
        self.ui.pushButton.setIconSize(QSize(75, 75))
        self.ui.pushButton.setEnabled(False)

        # processor images
        processor_type = platform.processor()
        if 'AMD' in processor_type:
            self.ui.label_14.setPixmap(QPixmap(u"images/amd.png"))
        else:
            self.ui.label_14.setPixmap(QPixmap(u"images/intel.png"))

        # processor information
        self.get_cpu_information()

        self.ui.pushButton.clicked.connect(self.start_benchark)
        self.ui.checkBox.toggled.connect(self.chose_benchark_mode)
        self.ui.checkBox_2.toggled.connect(self.chose_benchark_mode)
        self.ui.horizontalSlider.valueChanged.connect(self.get_arrays_number)

        self.chosen_mods = set()

    def get_cpu_information(self):
        self.ui.label_8.setText(platform.processor()[:5])
        self.ui.label_9.setText(str(psutil.cpu_freq().max))
        self.ui.label_10.setText(str(psutil.cpu_count() // 2))
        self.ui.label_11.setText(str(psutil.cpu_count()))

    def start_benchark(self):
        if not self.is_benchmark_in_porgress:
            self.is_benchmark_in_porgress = True

            self.disable_mutable_widgets()

            self.set_zero_into_table()
            self.ui.pushButton.setIcon(self.stop_icon)
            self.output_results("Идет тестирование", "Идет тестирование")
            test = CustomBenchamrk(self.loop, self.chosen_mods, self.ui.horizontalSlider.value(), self.ui.comboBox.currentIndex(), self.output_results, self.activate_start_button)
            test.start()
            self._load_test = test
        else:
            self._load_test.cancel()
            self._load_test = None
            self.ui.pushButton.setIcon(self.start_icon)
            self.is_benchmark_in_porgress = False
            self.enable_mutable_widgets()

    def activate_start_button(self):
        self.ui.pushButton.setIcon(self.start_icon)
        self.is_benchmark_in_porgress = False
        self.enable_mutable_widgets()

    def disable_mutable_widgets(self):
        self.ui.horizontalSlider.setEnabled(False)
        self.ui.checkBox.setEnabled(False)
        self.ui.checkBox_2.setEnabled(False)
        self.ui.comboBox.setEnabled(False)

    def enable_mutable_widgets(self):
        self.ui.comboBox.setEnabled(True)
        self.ui.horizontalSlider.setEnabled(True)
        self.ui.checkBox.setEnabled(True)
        self.ui.checkBox_2.setEnabled(True)

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
        self.ui.qtablewidgetitem3.setText("")
        self.ui.qtablewidgetitem4.setText("")

    def output_results(self,
                       single_work_time,
                       multi_work_time):
        self.ui.qtablewidgetitem3.setText(str(single_work_time))
        self.ui.qtablewidgetitem4.setText(str(multi_work_time))
