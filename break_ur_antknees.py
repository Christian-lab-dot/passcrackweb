from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from cracked import brute_u
from selenium.webdriver.common.keys import Keys
import random
import time

ser = Service("H://chromedriver.exe")
driver = webdriver.Chrome(service=ser)
f = open('passwords.txt', 'r')

driver.get("https://dummy.antknee.dev/Identity/Account/Register?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3DSimpleAuth.Web%26redirect_uri%3Dhttps%253A%252F%252Fdummy.antknee.dev%252Fauthentication%252Flogin-callback%26response_type%3Dcode%26scope%3DSimpleAuth.WebAPI%2520openid%2520profile%26state%3D4b426c5a76a34ec0a6b01a229b1cd606%26code_challenge%3DweYvcxi7J-SQOyB1Rwsm8335hBnZl1dVl0LVsEDCNVw%26code_challenge_method%3DS256%26response_mode%3Dquery")

act = ActionChains(driver)

email = ['@yahoo.com', '@gmail.com', '@hotmail.com', '@bigmac.com', '@whataburger.com', '@mail.com']

u_sub = driver.find_element(By.NAME, 'Input.Email')
p_sub = driver.find_element(By.NAME, 'Input.Password')
pc_sub = driver.find_element(By.NAME, 'Input.ConfirmPassword')

list = brute_u(3)
p_list = []
for p in f:
    p_list.append(p)


for w in list[1:]:
    rp = random.choice(p_list)
    act.click(on_element=u_sub).send_keys(w).send_keys(random.choice(email)).perform()
    act.click(on_element=p_sub).send_keys(rp).perform()
    act.click(on_element=pc_sub).send_keys(rp).perform()
    act.click(on_element=driver.find_element(By.ID, 'registerSubmit')).perform()
    time.sleep(3)
    act.reset_actions()
    act.click(on_element=driver.find_element(By.LINK_TEXT, 'Logout'))
    act.reset_actions()
    act.click(on_element=driver.find_element(By.LINK_TEXT, 'Register'))
    act.reset_actions()
