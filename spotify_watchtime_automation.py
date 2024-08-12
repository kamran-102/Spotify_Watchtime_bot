from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
import chromedriver_autoinstaller
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
import random 
import string
from faker import Faker
import threading 

url = "https://open.spotify.com/album/0a183xiCHiC1GQd8ou7WXO"

def selenium_task():
    # Initialize the WebDriver
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options = chrome_options)
    driver.maximize_window()

    # Your Selenium automation code here
    driver.get(url)
    driver.implicitly_wait(15)
    # signup button
    driver.find_element(By.XPATH, """//*[@id="main"]/div/div[2]/div[3]/header/div[2]/div[3]/div[1]/button[1]""").click()
    time.sleep(4)

    data =  []
    # Random email generation
    chars = 'abcdefghijklmnopqrstuvwxyz'
    length = 7
    local_part = ''.join(random.choice(chars) for _ in range(length))
    dig_length = 3
    characters = string.digits
    local_part_2 = ''.join(random.choice(characters) for _ in range(dig_length))
    email = f"{local_part}{local_part_2}@gmail.com"

    # random password generation

    pswrd_length = 10
    characters = string.ascii_letters + string.digits
    pswrd = ''.join(random.choice(characters) for _ in range(pswrd_length))
    password = f"{pswrd}1"
    data.append({"Email": email,
                "Password": password})
    record = pd.DataFrame(data)
    record

    # Entering email id 
    email_input = driver.find_element(By.XPATH, """//*[@id="username"]""")
    email_input.send_keys(email)
    time.sleep(3)
    email_input.send_keys(Keys.ENTER)
    driver.implicitly_wait(10)

    # Entering id password 
    pswrd_input = driver.find_element(By.XPATH, """//*[@id="new-password"]""")
    pswrd_input.send_keys(password)
    time.sleep(3)
    pswrd_input.send_keys(Keys.ENTER)
    time.sleep(2)

    # Entering name
    fake = Faker()
    name = fake.name()
    nme = driver.find_element(By.XPATH, """//*[@id="displayName"]""")
    nme.send_keys(name)
    nme.send_keys(Keys.ENTER)
    time.sleep(1)

    # Entering date of birth
    date = driver.find_element(By.XPATH, """//*[@id="day"]""")
    rnd_date = random.randint(1,30)
    date.send_keys(rnd_date)

    month = Select(driver.find_element(By.XPATH, """//*[@id="month"]"""))
    rnd_month = random.randint(1,12)
    month.options[rnd_month].click()

    year = driver.find_element(By.XPATH, """//*[@id="year"]""")
    rnd_year = random.randint(1970, 2010)
    year.send_keys(rnd_year)
    time.sleep(1)
    m_x = """//*[@id="__next"]/main/main/section/div/form/div[1]/div[2]/div/section/div[3]/fieldset/div/div/div[1]/label"""
    f_x = """//*[@id="__next"]/main/main/section/div/form/div[1]/div[2]/div/section/div[3]/fieldset/div/div/div[2]"""
    n_x = """//*[@id="__next"]/main/main/section/div/form/div[1]/div[2]/div/section/div[3]/fieldset/div/div/div[3]"""
    sex = [m_x, f_x, n_x]
    rnd_gender = random.choice(sex)
    gender = driver.find_element(By.XPATH, rnd_gender)
    gender.click()
    driver.switch_to.active_element.send_keys(Keys.ENTER)
    click1 = driver.find_element(By.XPATH, """//*[@id="__next"]/main/main/section/div/form/div[1]/div[2]/div/section/div[4]/div[1]/div/div/label""")
    click1.click()
    click2 = driver.find_element(By.XPATH, """//*[@id="__next"]/main/main/section/div/form/div[1]/div[2]/div/section/div[4]/div[2]/div/label""")
    click2.click()
    sign_button = driver.find_element(By.XPATH, """//*[@id="__next"]/main/main/section/div/form/div[2]/button""")
    sign_button.click()
    driver.implicitly_wait(30)
    start_button = driver.find_element(By.XPATH, """//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/main/section/div[3]/div[2]/div/div/div[1]/button/span""")
    start_button.click()
    # Time
    time.sleep(185)
    # Close the WebDriver
    driver.close()

if __name__=='__main__':
    iter_input = int(input("Enter the number of iterations to be made: "))
    windows_input = int(input("Enter the number of windows to be opened: "))
    for i in range(iter_input):
        # Create multiple threads
        threads = []
        for _ in range(windows_input):  # You can adjust the number of threads as per your requirement
            thread = threading.Thread(target=selenium_task)
            threads.append(thread)

        # Start all threads
        for thread in threads:
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()