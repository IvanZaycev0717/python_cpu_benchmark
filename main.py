import asyncio
from asyncio import AbstractEventLoop
import sys
from threading import Thread

from PySide6.QtWidgets import QApplication

from ui import PythonCPUBenchmark


class ThreadedEventLoop(Thread):
    """Class for async event loop."""
    def __init__(self, loop: AbstractEventLoop) -> None:
        super().__init__()
        self._loop = loop
        self.daemon: bool = True

    def run(self) -> None:
        self._loop.run_forever()


if __name__ == '__main__':
    loop = asyncio.new_event_loop()

    asyncio_thread = ThreadedEventLoop(loop)
    asyncio_thread.start()

    app = QApplication(sys.argv)
    window = PythonCPUBenchmark(loop)
    window.show()
    sys.exit(app.exec())
