import requests
import random

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

domeny = generate_domains()
poczatek_maila = generate_mail()
mail = poczatek_maila + random.choice(domeny)
print(mail)