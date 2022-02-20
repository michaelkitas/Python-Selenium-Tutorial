from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A11036071%2Cp_36%3A1253503011&dc&fs=true&qid=1635596580&rnid=16225007011&ref=sr_pg_1')

elem_list = browser.find_element(
    By.CSS_SELECTOR, "div.s-main-slot.s-result-list.s-search-results.sg-row")

items = elem_list.find_elements(
    By.XPATH, '//div[@data-component-type="s-search-result"]')

for item in items:
    title = item.find_element(By.TAG_NAME, 'h2').text
    price = "No Price Found"
    img = "No Image Found"
    link = item.find_element(By.CLASS_NAME, 'a-link-normal').get_attribute('href')

    try:
        price = item.find_element(By.CSS_SELECTOR, '.a-price').text.replace("\n", ".")
    except:
        pass

    try:
        img = item.find_element(By.CSS_SELECTOR, '.s-image').get_attribute("src")
    except:
        pass

    

    print("Title: " + title)
    print("Price: " + price)
    print("Image: " + img)
    print("Link: " + link + "\n")
