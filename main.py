import time
import requests
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def generate_mail():
    male_litery = "abcdefghijklmnoqprstuwxyz"
    wielkie_litery = "ABCDEFGHIJKLMNOQPRSTUWXYZ"
    liczby = "1234567890"

    wszystkie = male_litery + wielkie_litery + liczby
    result_str = ''.join((random.choice(wszystkie) for i in range(20)))
    return result_str
def generate_domains():
    url = "https://api.apilayer.com/temp_mail/domains"
    payload = {}
    headers = {
        "apikey": "fKZR5kWXCvScp7IgYzsvHYVDgSKYO6VF"
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    result = response.json()
    return result

def register_account(email):
    driver_path = "C:\\Users\\Lukas\\PycharmProjects\\accountBot\\chromedriver.exe"
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    registration_url = "https://www.adidas.se/account-register"
    driver.get(registration_url)

    #pliki cookie
    driver.find_element("css selector", "#glass-gdpr-default-consent-accept-button").click()

    #imie
    driver.find_element("css selector", "#registration-firstname-field").send_keys("Mirosław")

    #nazwisko
    driver.find_element("css selector", "#registration-lastname-field").send_keys("Inwalida")

    #płeć
    radio_buttons = driver.find_element("css selector", ".gl-radio-input__option")
    radio_buttons.click()

    #email
    driver.find_element("css selector", "#registration-email-field").send_keys(email)

    #hasło
    driver.find_element("css selector", "#registration-password-field").send_keys("AAAaaa123!!!")

    #dzień urodzenia
    driver.find_element("css selector", "#registration-dob-fields-day").send_keys("01")

    #miesiąć urodzenia
    driver.find_element("css selector", "#registration-dob-fields-month").send_keys("01")

    #rok urodzenia
    driver.find_element("css selector", "#registration-dob-fields-year").send_keys("2000")

    #chuj wei co
    driver.find_element("css selector", "#doc-mrkt-email-club").click()

    #zarejestruj
    driver.find_element("css selector", ".gl-cta__content").click()


while True:
    domeny = generate_domains()
    poczatek_maila = generate_mail()
    mail = poczatek_maila + random.choice(domeny)
    register_account(mail)

    with open("emails.txt", "a") as file:
        file.write(mail + "\n")

    time.sleep(5)