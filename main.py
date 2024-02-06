import asyncio
from asyncio import AbstractEventLoop
import sys
from threading import Thread


from ui import PythonCPUBenchmark
from PySide6.QtWidgets import QApplication


class ThreadedEventLoop(Thread):
    def __init__(self, loop: AbstractEventLoop):
        super().__init__()
        self._loop = loop
        self.daemon = True

    def run(self):
        self._loop.run_forever()


if __name__ == '__main__':
    loop = asyncio.new_event_loop()

    asyncio_thread = ThreadedEventLoop(loop)
    asyncio_thread.start()

    app = QApplication(sys.argv)
    window = PythonCPUBenchmark(loop)
    window.show()
    sys.exit(app.exec())