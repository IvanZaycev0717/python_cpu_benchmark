from asyncio import AbstractEventLoop
import platform
import psutil

from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import QSize

from design import Ui_MainWindow
from stress_test import CustomBenchamrk


class PythonCPUBenchmark(QMainWindow):
    """Class for GUI."""
    def __init__(self, loop: AbstractEventLoop) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.loop = loop
        self.ui.setupUi(self)
        self.set_zero_into_table()

        # flags
        self.is_benchmark_in_porgress: bool = False

        # Button images and setup
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

        # PyQt signals
        self.ui.pushButton.clicked.connect(self.start_benchmark)
        self.ui.checkBox.toggled.connect(self.chose_benchmark_mode)
        self.ui.checkBox_2.toggled.connect(self.chose_benchmark_mode)
        self.ui.horizontalSlider.valueChanged.connect(self.get_arrays_number)

        self.chosen_mods: set[str] = set()

    def get_cpu_information(self) -> None:
        """Inserts CPU info into widgets fields."""
        self.ui.label_8.setText(platform.processor()[:5])
        self.ui.label_9.setText(str(psutil.cpu_freq().max))
        self.ui.label_10.setText(str(psutil.cpu_count() // 2))
        self.ui.label_11.setText(str(psutil.cpu_count()))

    def start_benchmark(self) -> None:
        """Starts a custom benchmark."""
        if not self.is_benchmark_in_porgress:
            self.is_benchmark_in_porgress = True

            self.disable_mutable_widgets()

            self.set_zero_into_table()
            self.ui.pushButton.setIcon(self.stop_icon)
            self.output_results("Идет тестирование", "Идет тестирование")
            test = CustomBenchamrk(
                loop=self.loop,
                chosen_mods=self.chosen_mods,
                arrays_number=self.ui.horizontalSlider.value(),
                numbers_amount=self.ui.spinbox.value(),
                alghoritm=self.ui.comboBox.currentIndex(),
                output_results=self.output_results,
                activate_start_button=self.activate_start_button
            )
            test.start()
            self._load_test = test
        else:
            self._load_test.cancel()
            self._load_test = None
            self.ui.pushButton.setIcon(self.start_icon)
            self.is_benchmark_in_porgress = False
            self.enable_mutable_widgets()

    def activate_start_button(self) -> None:
        """Toggles start button to a ready condition."""
        self.ui.pushButton.setIcon(self.start_icon)
        self.is_benchmark_in_porgress = False
        self.enable_mutable_widgets()

    def disable_mutable_widgets(self) -> None:
        """Disables mutable all the widgets."""
        self.ui.horizontalSlider.setEnabled(False)
        self.ui.checkBox.setEnabled(False)
        self.ui.checkBox_2.setEnabled(False)
        self.ui.comboBox.setEnabled(False)
        self.ui.spinbox.setEnabled(False)

    def enable_mutable_widgets(self) -> None:
        """Enables mutable all the widgets."""
        self.ui.comboBox.setEnabled(True)
        self.ui.horizontalSlider.setEnabled(True)
        self.ui.checkBox.setEnabled(True)
        self.ui.checkBox_2.setEnabled(True)
        self.ui.spinbox.setEnabled(True)

    def get_arrays_number(self) -> None:
        size = self.ui.horizontalSlider.value()
        self.ui.label_18.setText(str(size))

    def chose_benchmark_mode(self, checked: bool) -> None:
        """Gets information which checkbox is activate."""
        sender = self.sender()
        if checked:
            self.chosen_mods.add(sender.text())
            if self.chosen_mods:
                self.ui.pushButton.setEnabled(True)
        else:
            self.chosen_mods.remove(sender.text())
            if not self.chosen_mods:
                self.ui.pushButton.setEnabled(False)

    def set_zero_into_table(self) -> None:
        """Clears test output fields in the table."""
        self.ui.qtablewidgetitem3.setText("")
        self.ui.qtablewidgetitem4.setText("")

    def output_results(self,
                       single_work_time: int,
                       multi_work_time: int) -> None:
        """Inserts the test results into the table."""
        self.ui.qtablewidgetitem3.setText(str(single_work_time))
        self.ui.qtablewidgetitem4.setText(str(multi_work_time))
