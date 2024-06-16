from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = r"C:\Development\chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://ienabler.ug.edu.gh/pls/prodi41/w99pkg.mi_login")
driver.implicitly_wait(5)

id_number = 'YOUR ID NUMBER'
pin = 'YOUR PIN'


username = driver.find_element(By.NAME, "unum")
username.send_keys(id_number)

password = driver.find_element(By.NAME, "pin")
password.send_keys(pin)
password.send_keys(Keys.RETURN)


try:
    #
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
        (By.XPATH, '//*[@id="F1"]')))
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Student Enquiry'))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Academic Record (Local)"))
    )
    element.click()
except:
    print("An error occurred.")


