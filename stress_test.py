import asyncio
from asyncio import AbstractEventLoop
from concurrent.futures import ProcessPoolExecutor
import time
from functools import partial
from random import randint
import random
from typing import Callable

from algorithms import (insert_sort, selection_sort,
                        bubble_sort, count_sort,
                        quick_sort, merge_sort)


random.seed(1)


class CustomBenchamrk:
    """Class for CPU benchmark by means of a stress test."""
    def __init__(self,
                 loop: AbstractEventLoop,
                 chosen_mods: set[str],
                 arrays_number: int,
                 numbers_amount: int,
                 alghoritm: str,
                 output_results: Callable,
                 activate_start_button: Callable) -> None:

        self._load_test_future = None
        self._loop = loop
        self._chosen_mods = chosen_mods
        self._arrays_number = arrays_number
        self._alghoritm = alghoritm
        self._output_results = output_results
        self._numbers_amount = numbers_amount
        self._activate_start_button = activate_start_button

        # Local data
        self._func_choice: dict[int, Callable] = {
            0: insert_sort,
            1: selection_sort,
            2: bubble_sort,
            3: count_sort,
            4: quick_sort,
            5: merge_sort
        }
        self.single_time: float = None
        self.multi_time: float = None

    def start(self) -> None:
        future = asyncio.run_coroutine_threadsafe(self._test_1(), self._loop)
        self._load_test_future = future

    def cancel(self) -> None:
        if self._load_test_future:
            self._loop.call_soon_threadsafe(self._load_test_future.cancel)
        self._output_results("Отмена", "Отмена")

    async def _test_1(self) -> None:
        self.nums = [
            [
                randint(1, 1000) for n in range(self._numbers_amount)
                ] for _ in range(10)
            ][:self._arrays_number]

        # testing single-processing
        if "Однопроцессность" in self._chosen_mods:
            start = time.time()
            for num in self.nums:
                self._func_choice[self._alghoritm](num)
            end = time.time()
            self.single_time = end - start

        # testing multi-processing
        if "Многопроцессность" in self._chosen_mods:
            start = time.time()
            with ProcessPoolExecutor() as process_pool:
                calls = [
                    partial(self._func_choice[self._alghoritm], num)
                    for num in self.nums
                    ]
                call_coros = []
                for call in calls:
                    call_coros.append(
                        self._loop.run_in_executor(process_pool, call)
                        )

                await asyncio.gather(*call_coros)

            end = time.time()
            self.multi_time = end - start

        # output result data into GUI
        self._output_results(self.single_time, self.multi_time)
        self._activate_start_button()
