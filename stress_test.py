import asyncio
from asyncio import AbstractEventLoop
from concurrent.futures import ProcessPoolExecutor
import time
from functools import partial


def count(count_to):
    counter = 0
    while counter < count_to:
        counter = counter + 1
    return counter


class CustomBenchamrk:
    def __init__(self,
                 loop: AbstractEventLoop,
                 chosen_mods: set[str],
                 arrays_number: int,
                 alghoritm: str,
                 output_results,
                 activate_start_button):
        self._load_test_future = None
        self._loop = loop
        self._chosen_mods = chosen_mods
        self._arrays_number = arrays_number
        self._alghoritm = alghoritm
        self._output_results = output_results
        self._activate_start_button = activate_start_button

        self.single_time = None
        self.multi_time = None


    def start(self):
        future = asyncio.run_coroutine_threadsafe(self._test_1(), self._loop)
        self._load_test_future = future
    
    def cancel(self):
        if self._load_test_future:
            self._loop.call_soon_threadsafe(self._load_test_future.cancel)
        self._output_results("Отмена", "Отмена")
    
    async def _test_1(self):
        nums = [100000000, 100000000, 100000000, 100000000, 100000000, 100000000]

        if "Однопроцессность" in self._chosen_mods:
            start = time.time()
            for num in nums:
                count(num)
            end = time.time()
            self.single_time = end - start
        
        if "Многопроцессность" in self._chosen_mods:
            start = time.time()
            with ProcessPoolExecutor() as process_pool:
                calls = [partial(count, num) for num in nums]
                call_coros = []
                for call in calls:
                    call_coros.append(self._loop.run_in_executor(process_pool, call))

                await asyncio.gather(*call_coros)

            end = time.time()
            self.multi_time = end - start
        self._output_results(self.single_time, self.multi_time)
        self._activate_start_button()


