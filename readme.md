***после ввода команды жми enter***

### Подготовительные работы
1. Установить python https://www.python.org/
или прямая [ссылка на загрузку](https://www.python.org/ftp/python/3.8.5/python-3.8.5-amd64.exe)

[Видео о том как устанавливать](https://www.youtube.com/watch?v=HbBJGue1km4)

2. Создать рабочую директорию для скрипта и разархивировать туда [архив](https://github.com/repen/4bet_parser/archive/master.zip). Например `С:\bet_scripts` .

3. Необходимо открыть командную строку в windows. Как открыть командную строку есть в видео в пункте 1.

4. перейти в рабочию директорию скрипта командой `cd С:\bet_scripts`

5. Выполнить команду `python install.py`

6. Если не установлен браузер Chrome то установить браузер Chrome.

### Запуск скрипта
При первом запуске потребует доступ. нужно нажать разрешить.

1. Необходимо открыть командную строку в windows. Как открыть командную строку есть в видео в пункте 1.

2. перейти в рабочию директорию скрипта командой `cd С:\bet_scripts`

3. Старт. `python main.py`

4. Остановка. `Ctrl + C`

### Информация

В файле s.conf находится конфигурация скрипта. Там нужно указать ссылки на нужные матчи и все, остальное желательно не трогать.

headless=1 - безголовый браузер работает все в фоне, что очень удобно

headless=0 - видно браузер, браузер работает в интерактивном режиме постоянно перключает вкладки , что не очень удобно.

Данные сохраняются в папку data.

Для последующих запусков выполнять только пункт **Запуск скрипта**