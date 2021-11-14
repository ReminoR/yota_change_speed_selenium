from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import argparse
import getpass
import time
import os


load_dotenv()
opts = Options()


def createParser():
    parser = argparse.ArgumentParser(description='The application changes yota speed')
    parser.add_argument('-u', '--username', default=os.getenv("LOGIN"), help='Email / Phone / Account number from Yota')
    parser.add_argument('-p', '--password', default=os.getenv("PASSWORD"), help='your password')
    parser.add_argument('-t', '--tariff_number', required=True, type=int, help='tariff. range from 2 (min speed) to 15 (max speed)')
    parser.add_argument('-f', '--filepath', default=os.getenv('PATH_TO_DRIVER'), help='Path to chrome driver file')
    parser.add_argument('-s', '--sleep', default=5, type=int, help='Pause before changing tariff')
    parser.add_argument('-g', '--gui', action='store_true', help='Using GUI Browser')

    return parser


def auth(driver, login, password, pause):
    driver.get("https://my.yota.ru")
    assert "Yota" in driver.title
    time.sleep(pause)

    driver.find_element_by_css_selector('input#y-input-0').send_keys(login)
    driver.find_element_by_css_selector('input#y-input-1').send_keys(password)
    driver.find_element_by_css_selector('.form-login-page form').submit()


def change_tariff(driver, tariff_number):
    slider = driver.find_element_by_css_selector('.ticks div:nth-child(' + str(tariff_number) + ')')
    slider.click()
    time.sleep(1)

    change_tariff_button = driver.find_element_by_css_selector('.conditions .y-button')
    change_tariff_button.click()


def main():
    parser = createParser()
    namespace = parser.parse_args()

    if not namespace.gui:
        opts.set_headless()
        assert opts.headless

    if namespace.tariff_number < 2 or namespace.tariff_number > 15:
        print("Неверно указан тариф. Используйте цифру от 2 (минимальная скорость) до 15 (максимальная скорость)")
        return

    driver = webdriver.Chrome(namespace.filepath, options=opts)

    auth(driver, namespace.username, namespace.password, namespace.sleep)
    time.sleep(namespace.sleep)
    change_tariff(driver, namespace.tariff_number)
    time.sleep(namespace.sleep)


if __name__ == '__main__':
    main()