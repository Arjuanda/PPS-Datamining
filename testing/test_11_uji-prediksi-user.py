import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

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

        link_prediksi = driver.find_element(By.XPATH, '//a[@href="/prediksi"]')
        link_prediksi.click()
        time.sleep(2)

        x1_input = driver.find_element(By.NAME, "feature1")
        x1_input.send_keys("90") 
        time.sleep(3)

        x2_input = driver.find_element(By.NAME, "feature2")
        x2_input.send_keys("88") 
        time.sleep(3)

        x3_input = driver.find_element(By.NAME, "feature3")
        x3_input.send_keys("90") 
        time.sleep(3)

        x4_input = driver.find_element(By.NAME, "feature4")
        x4_input.send_keys("80") 
        time.sleep(3)
        
        x5_input = driver.find_element(By.NAME, "feature5")
        x5_input.send_keys("80") 
        time.sleep(3)

        x6_input = driver.find_element(By.NAME, "feature6")
        x6_input.send_keys("85") 
        time.sleep(3)

        x7_input = driver.find_element(By.NAME, "feature7")
        x7_input.send_keys("88") 
        time.sleep(3)

        x8_input = driver.find_element(By.NAME, "feature8")
        x8_input.send_keys("90") 
        time.sleep(3)

        x9_input = driver.find_element(By.NAME, "feature9")
        x9_input.send_keys("90") 
        time.sleep(3)

        x10_input = driver.find_element(By.NAME, "feature10")
        x10_input.send_keys("86") 
        time.sleep(3)

        dropdown = Select(driver.find_element(By.NAME, "true-labels"))
        dropdown.select_by_visible_text("TEKNIK INFORMATIKA (IF)")
        time.sleep(3)

        tombol_tambah = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        tombol_tambah.click()
        time.sleep(3)

    except Exception as e:
        pytest.fail(f"Terjadi kesalahan: {e}")