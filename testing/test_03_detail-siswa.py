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

def test_update_student_info(driver):
    try:
        login_url = 'http://127.0.0.1:9999/'
        driver.get(login_url)

        email_field = driver.find_element(By.XPATH, '//input[@name="email"]')
        password_field = driver.find_element(By.XPATH, '//input[@name="password"]')
        login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')

        email_field.send_keys('admin@pps.local')
        time.sleep(2)
        password_field.send_keys('Password$2')
        time.sleep(2)
        login_button.click()
        time.sleep(2)

        link_mhs = driver.find_element(By.XPATH, '//a[@href="/user"]')
        link_mhs.click()
        time.sleep(2)

        tombol_detail = driver.find_element(By.XPATH, "(//table[@class='table table-striped table-responsive table-hover text-center']//tr[position()=1]//a[text()='Detail'])[1]")    
        tombol_detail.click()
        time.sleep(10)

    except Exception as e:
        pytest.fail(f"Terjadi kesalahan: {e}")
