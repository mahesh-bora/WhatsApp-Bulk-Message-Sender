from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
import time


with open('message.txt', 'r') as file:
    message = file.read()
message = (quote(message))

numbers = []
with open('numbers.txt', 'r') as file:
    for num in file.readlines():
        numbers.append(num.rstrip)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

link  = 'https://web.whatsapp.com'

driver.get(link)

time.sleep(60)

link2 = f'https://web.whatsapp.com/send/?phone=91{numbers[0]}&text={message}'

driver.get(link2)
time.sleep(15)

for num in numbers: 
    link2 = f'https://web.whatsapp.com/send/?phone=91{num}&text={message}'
    driver.get(link2)
    time.sleep(15)
    action = ActionChains(driver)
    action.send_keys(Keys.ENTER)
    action.perform()
time.sleep(5000)
