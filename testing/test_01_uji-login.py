import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_and_logout(driver):
    login_url = 'http://127.0.0.1:9999/'
    email = 'admin@pps.local'
    password = 'Password$2'

    driver.get(login_url)

    email_field = driver.find_element(By.XPATH, '//input[@name="email"]')
    password_field = driver.find_element(By.XPATH, '//input[@name="password"]')
    login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')

    email_field.send_keys(email)
    time.sleep(2)
    password_field.send_keys(password)
    time.sleep(2)
    login_button.click()

    time.sleep(2)

    current_url = driver.current_url

    if '/dashboard' in current_url:
        assert True, "Login berhasil"
        
        time.sleep(3)
        logout = driver.find_element(By.XPATH, "//a[@href='/logout']")
        logout.click()

        assert '/' in driver.current_url, "Logout berhasil"
    elif '/' in current_url:
        assert False, "Login gagal karena autentikasi"
    else:
        assert False, "Login gagal karena kesalahan tidak dikenal"
