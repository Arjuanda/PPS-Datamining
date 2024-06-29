import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_prodi(driver):
    try:
        login_url = 'http://127.0.0.1:9999/'
        driver.get(login_url)

        email_field = driver.find_element(By.XPATH, '//input[@name="email"]')
        password_field = driver.find_element(By.XPATH, '//input[@name="password"]')
        login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')

        email_field.send_keys('user@pps.local')
        time.sleep(2)
        password_field.send_keys('Password$1')
        time.sleep(2)
        login_button.click()
        time.sleep(2)

        link_mhs = driver.find_element(By.XPATH, '//a[@href="/card-prodi"]')
        link_mhs.click()
        time.sleep(2)

        tombol_lihat = driver.find_element(By.XPATH, "(//div[@class='card']//a)[2]")    
        tombol_lihat.click()
        time.sleep(3)


    except Exception as e:
        pytest.fail(f"Terjadi kesalahan: {e}")