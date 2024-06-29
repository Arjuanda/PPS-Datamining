import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_delete_first_student(setup):
    driver = setup
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

        # Temukan tombol hapus dari baris pertama
        tombol_hapus = driver.find_element(By.XPATH, "(//table[@class='table table-striped table-responsive table-hover text-center']//tr[position()=1]//a[text()='Hapus'])[1]")    
        tombol_hapus.click()
        time.sleep(3)

        # Menghadapi konfirmasi alert dan menyetujui (klik OK)
        alert = Alert(driver)
        alert.accept()
        time.sleep(3)

        assert "user" in driver.current_url and "123456" not in driver.page_source
        print("Pengujian hapus siswa sukses")

    except Exception as e:
        pytest.fail(f"Terjadi kesalahan: {e}")
