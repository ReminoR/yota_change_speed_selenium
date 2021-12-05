# Консольная утилита для изменения тарифов интернета Yota.

### Для использования необходимы:
- python 3+
- selenium ([Инструкция по установке](https://selenium-python.com/install-chromedriver-chrome))
- driver for chrome (https://sites.google.com/chromium.org/driver/). Необходимо разместить в корневой директории библиотеки, либо указать путь.

### Устанавливаем необходимые библиотеки:
```
pip install -r requirements.txt
```

### Создаем файл .env в корневой директории и заполняем его: 
```
LOGIN=your_login_from_yota
PASSWORD=your_password
PATH_TO_DRIVER=chromedriver.exe (Windows) / chromedriver (Linux)
```

### Для вызовы справки запускаем:
```
python yota_selenium.py -h
```

### Параметры:
```
usage: yota_selenium.py [-h] [-u USERNAME] [-p PASSWORD] -t TARIFF_NUMBER
                        [-f FILEPATH] [-s SLEEP] [-g]

The application changes yota speed

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        Email / Phone / Account number from Yota
  -p PASSWORD, --password PASSWORD
                        your password
  -t TARIFF_NUMBER, --tariff_number TARIFF_NUMBER
                        tariff. range from 2 (min speed) to 15 (max speed)
  -f FILEPATH, --filepath FILEPATH
                        Path to chrome driver file
  -s SLEEP, --sleep SLEEP
                        Pause before changing tariff
  -g, --gui             Using GUI Browser
```

### Автоматический запуск скрипта при старте и выключении ПК (Windows 7, 8, 10)

1. Создаем .bat скрипт с запуском скрипта Yota.
```
С: # указываем локальный диск
cd \Path\to\Script\yota_change_speed_selenium & venv\Scripts\activate.bat & python yota_selenium.py arguments
# В одной команде указываем путь к окружению python, активируем виртуальное окружение и запускаем скрипт
```
2. Заходим в групповые политики Windows  
`Выполнить > gpedit.msc > Конфигурация пользователя > Конфигурация Windows > Сценарии (вход/выход из системы) > Выход из системы > Показать файлы. Копируем скрипт в папку и добавляем сценарий в список` 
3. Чтобы скрипт сработал при запуске Windows, можно добавить в автозагрузку, либо использовать групповые политики на «Вход в систему».
4. Обновляем групповые политики через терминал: `gpupdate /force`

## Улучшения

- Добавить информацию об установленном тарифе.
- Не запускать скрипт, если выбранный и установленный тарифы совпадают


