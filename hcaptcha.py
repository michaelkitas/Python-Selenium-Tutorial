import os
from twocaptcha import TwoCaptcha
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def solvehCaptcha():
    api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')

    solver = TwoCaptcha(api_key)

    try:
        result = solver.hcaptcha(
            sitekey='3ceb8624-1970-4e6b-91d5-70317b70b651',
            url='https://2captcha.com/demo/hcaptcha',
        )

    except Exception as e:
        print(e)
        return False

    else:
        return result


browser = webdriver.Chrome()
browser.get('https://2captcha.com/demo/hcaptcha')

# wait for iframe
WebDriverWait(browser, 10).until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, '#root > div > main > div > section > form > div > div > div > iframe')))

result = solvehCaptcha()

if result:
    code = result['code']

    browser.execute_script(
        "document.querySelector(" + "'" + '[name="h-captcha-response"]' + "'" + ").innerHTML = " + "'" + code + "'")

    browser.find_element(
        By.CSS_SELECTOR, "#root > div > main > div > section > form > button._2iYm2u0v9LWjjsuiyfKsv4._1z3RdCK9ek3YQYwshGZNjf._3zBeuZ3zVV-s2YdppESngy._28oc7jlCOdc1KAtktSUZvQ").click()
