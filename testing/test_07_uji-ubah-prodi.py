import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

        link_mtk = driver.find_element(By.XPATH, '//a[@href="/prodi"]')
        link_mtk.click()
        time.sleep(2)

        tombol_ubah = driver.find_element(By.XPATH, "(//table[@class='table table-striped table-responsive table-hover text-center']//tr[position()=1]//a[text()='Ubah'])[1]")    
        tombol_ubah.click()
        time.sleep(3)

        nama_input = driver.find_element(By.NAME, "nama")
        kode_input = driver.find_element(By.NAME, "kode")

        nama_input.clear()
        time.sleep(2)
        nama_input.send_keys("pengujian 2")
        time.sleep(5)
        
        kode_input.clear()
        time.sleep(2)
        kode_input.send_keys("P10") 
        time.sleep(3)

        WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        ).click()

        assert "prodi" in driver.current_url and "pengujian 2" in driver.page_source
        print("Pengujian ubah program studi berhasil")

    except Exception as e:
        pytest.fail(f"Terjadi kesalahan: {e}")
