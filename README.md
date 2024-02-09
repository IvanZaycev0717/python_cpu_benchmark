# :deciduous_tree: Python CPU Benchmark

![pcbgif](https://github.com/IvanZaycev0717/python_cpu_benchmark/assets/111955306/368cfdbd-3288-456e-bd7e-8f6425e4df23)

**Python CPU Benchmark** - это desktop-приложение для тестирования процессора компьютера с помощью нагрузочных тестов, которые являются классическими алгоритмами сортировки массива из книги Дональда Кнута "Искусство программирования".

## :palm_tree: Технологии
- :zap: **Python 3.12**
- :zap: **PySide6 (PyQt6)**
- :zap: **asyncio**
- :zap: **threading**
- :zap: **concurrent.futures**
- :zap: **psutil**

## :evergreen_tree: Демонстрация работы приложения
На своём YouTube канале я записал видео, которое содержит всю необходимую теорию для понимания работы приложения, а также сами тесты с выводами. Также сущуствует текстовая версия данного видео - статья на сайте Хабр.
Сайт        | Ссылка           |Описание|
| ------------- |:-------------:|:--------:|
|![AID](https://github.com/IvanZaycev0717/the_mystery_of_the_mansion/assets/111955306/138cf8d1-a6f8-4835-9e54-93a48df815d3)|[Ссылка](https://youtu.be/eud7mDUjJ3E)|Демонстрация работы приложения|
|![habr](https://github.com/IvanZaycev0717/the_mystery_of_the_mansion/assets/111955306/772e1cac-b1e7-49c3-b87f-5f8fb2bdfbc8)|[Ссылка](https://habr.com/ru/articles/779624/)|Статья о создании приложения|

## :sunflower: Техническое описание
![scheme](https://github.com/IvanZaycev0717/python_cpu_benchmark/assets/111955306/1e3bcfb6-fc7e-4a00-95d2-adec8539507b)  

В приложении реализовано разделение выполнения кода на потоки: в главном потоке выполняется код графического интерфейса (GUI) с его сигналами и слотами (фреймворк Qt); на дополнительном потоке выполняется асинхронный цикл событий. В зависимости от выбранного режима тестирования в асинхронном цикле событий инициалицируется многопроцессный пул подключений, который выполняет поставленные задачи на разных логических ядрах процессора. В приложении возможно измерение скорости выполнения кода в синхронном режиме (на одном логическом ядре) и в многопроцессности (на нескольких логических ядрах). После тестирования в GUI возвращаются результаты тестирования для сравнения.

## :cactus: Установка
:leaves: **для Windows**

1) Скопируйте репозиторий к себе на компьютер по SSH-ключу `git@github.com:IvanZaycev0717/python_cpu_benchmark.git`

2) Установите виртуальное окружение `python -m venv venv`

3) Активируйте виртуальное окружение `source venv/Scripts/activate`

4) Установите внешние библиотеки, выполнив: `pip install -r requirements.txt`

5) Запустите файл main.py

:fallen_leaf: **для Linux**

1) Скопируйте репозиторий к себе на компьютер по SSH-ключу `git@github.com:IvanZaycev0717/python_cpu_benchmark.git`

2) Установите виртуальное окружение `python3 -m venv venv`

3) Активируйте виртуальное окружение `. venv/bin/activate`

4) Установите внешние библиотеки, выполнив: `pip3 install -r requirements.txt`

5) Запустите файл main.py

## :herb: Автор
Иван Зайцев (IvanZaycev0717)  
2024






