***после ввода команды жми enter***

### Подготовительные работы
1. Установить python https://www.python.org/

Для проверки правельности установки необходимо открыть командную строку в windows см. пункт 3 и выполнить команду `python`. Далее должен открытся интерактивный режим ![img](https://programfiles.info/wp-content/uploads/2019/03/windows-python-shell.png)

Версия должна быть 3.6 или выше.

Выйти из интерактивного режима командой `exit()`

2. Создать рабочую директорию для скрипта и разархивировать туда архив. Например `С:\bet_scripts` .

3. Необходимо открыть командную строку в windows. [ссылка](https://remontcompa.ru/windows/windows-81/477-kak-otkryt-komandnuyu-stroku-windows-8.html) 4 способ

4. перейти в рабочию директорию скрипта командой `cd С:\bet_scripts`

5. Выполнить команду `python install.py`

### Работа скрипта

Старт.
`python main.py`

Остановка.
`Ctrl + C`

### Информация

В файле s.conf находится конфигурация скрипта. Там нужно указать ссылки на нужные матчи и все, остальное желательно не трогать.

headless=1 - безголовый браузер работает все в фоне, что очень удобно

headless=0 - видно браузер, браузер работает в интерактивном режиме постоянно перключает вкладки , что не очень удобно.

Данные сохраняются в папку data.

Для последующих запусков подготовительный пункт не нужно выполнять, а достаточно:
- открыть командную строку
- перйти в рабочую дерикторию скрипта командой `cd С:\bet_scripts`
- `python main.py`