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
python yota_selenium -h
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