from asyncio import AbstractEventLoop
import time


def count_test():
    start = time.time()
    remnant = 500_000_000
    while remnant:
        remnant -= 1
    end = time.time()
    return "done", end - start


class CustomBenchamrk:
    def __init__(self,
                 loop: AbstractEventLoop,
                 chosen_mods: set[str],
                 arrays_number: int,
                 alghoritm: str,
                 output_results):
        self._loop = loop
        self._chosen_mods = chosen_mods
        self._arrays_number = arrays_number
        self._alghoritm = alghoritm
        self._output_results = output_results
