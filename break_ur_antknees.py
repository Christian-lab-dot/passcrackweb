from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from cracked import brute_u
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

f = open('passwords.txt', 'r')
b_list = brute_u(3)
p_list = []
for p in f:
    p_list.append(p)

ser = Service("H://chromedriver.exe")
driver = webdriver.Chrome(service=ser)


driver.get("https://dummy.antknee.dev/")
act = ActionChains(driver)
url_reg = 'https://dummy.antknee.dev/Identity/Account/Register?returnUrl=/authentication/login'
url_freg = 'https://dummy.antknee.dev/Identity/Account/Register?returnUrl=%2Fauthentication%2Flogin'
url_fmreg = 'https://dummy.antknee.dev/Identity/Account/Register'
url_suc = 'https://dummy.antknee.dev/'

email = ['@yahoo.com', '@gmail.com', '@hotmail.com', '@bigmac.com', '@whataburger.com', '@mail.com']

regi = driver.find_element(By.LINK_TEXT, 'Register')
act.click(on_element=regi).perform()

for w in b_list[1:]:
    if driver.current_url == url_freg or driver.current_url == url_fmreg:
        act.reset_actions()
        u_sub = driver.find_element(By.NAME, 'Input.Email')
        p_sub = driver.find_element(By.NAME, 'Input.Password')
        pc_sub = driver.find_element(By.NAME, 'Input.ConfirmPassword')
        rp = random.choice(p_list)
        act.click(on_element=u_sub).key_down(Keys.CONTROL).send_keys(Keys.ARROW_RIGHT + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE).perform()
        act.reset_actions()
        act.click(on_element=u_sub).send_keys(w).send_keys(random.choice(email)).perform()
        act.reset_actions()
        act.click(on_element=p_sub).key_down(Keys.CONTROL).send_keys(Keys.ARROW_RIGHT + Keys.BACKSPACE).perform()
        act.reset_actions()
        act.click(on_element=p_sub).send_keys(rp).perform()
        act.reset_actions()
        act.click(on_element=pc_sub).key_down(Keys.CONTROL).send_keys(Keys.ARROW_RIGHT + Keys.BACKSPACE).perform()
        act.reset_actions()
        act.click(on_element=pc_sub).send_keys(rp).perform()
        act.reset_actions()
        # wait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'registerSubmit')))
        act.send_keys(Keys.ENTER).perform()
        act.reset_actions()
        # time.sleep(3)
        if driver.current_url == url_suc:
            act.reset_actions()
            log_i = driver.find_element(By.LINK_TEXT, 'Login')
            act.reset_actions()
            # wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//app-login-menu[@href='/authentication/logout']")))
            act.click(on_element=log_i).perform()
            act.reset_actions()
            time.sleep(2)
            log_o = driver.find_element(By.LINK_TEXT, 'Logout')
            act.click(on_element=log_o).perform()
            act.reset_actions()
            reg = driver.find_element(By.LINK_TEXT, 'Register')
            # wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//app-login-menu[@href='/authentication/register']")))
            act.click(on_element=reg).perform()
            act.reset_actions()
    elif driver.current_url == url_reg:
        act.reset_actions()
        u_sub = driver.find_element(By.NAME, 'Input.Email')
        p_sub = driver.find_element(By.NAME, 'Input.Password')
        pc_sub = driver.find_element(By.NAME, 'Input.ConfirmPassword')
        rp = random.choice(p_list)
        act.click(on_element=u_sub).key_down(Keys.CONTROL).send_keys(Keys.ARROW_RIGHT + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE).perform()
        act.reset_actions()
        act.click(on_element=u_sub).send_keys(w).send_keys(random.choice(email)).perform()
        act.reset_actions()
        act.click(on_element=p_sub).key_down(Keys.CONTROL).send_keys(Keys.ARROW_RIGHT + Keys.BACKSPACE).perform()
        act.reset_actions()
        act.click(on_element=p_sub).send_keys(rp).perform()
        act.reset_actions()
        act.click(on_element=pc_sub).key_down(Keys.CONTROL).send_keys(Keys.ARROW_RIGHT + Keys.BACKSPACE).perform()
        act.reset_actions()
        act.click(on_element=pc_sub).send_keys(rp).perform()
        act.reset_actions()
        #wait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'registerSubmit')))
        act.send_keys(Keys.ENTER).perform()
        act.reset_actions()
        if driver.current_url == url_suc:
            log_o = driver.find_element(By.LINK_TEXT, 'Logout')
            act.reset_actions()
            # wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//app-login-menu[@href='/authentication/logout']")))
            act.click(on_element=log_o).perform()
            act.reset_actions()
            reg = driver.find_element(By.LINK_TEXT, 'Register')
            # wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//app-login-menu[@href='/authentication/register']")))
            act.click(on_element=reg).perform()
            act.reset_actions()
        #time.sleep(3)
    # if not driver.find_element(By.NAME, 'Input.Email').is_displayed():
    #     act.reset_actions()
    #     log_o = driver.find_element(By.LINK_TEXT, 'Logout')
    #     act.reset_actions()
    #     #wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//app-login-menu[@href='/authentication/logout']")))
    #     act.click(on_element=log_o).perform()
    #     act.reset_actions()
    #     reg = driver.find_element(By.LINK_TEXT, 'Register')
    #     #wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//app-login-menu[@href='/authentication/register']")))
    #     act.click(on_element=reg).perform()
    #     act.reset_actions()
