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

def test_add_new_student(driver):
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

        link_add_mtk = driver.find_element(By.XPATH, '//a[@href="/prodi/tambah"]')
        link_add_mtk.click()
        time.sleep(2)

        nama_prodi_input = driver.find_element(By.NAME, "nama")
        nama_prodi_input.send_keys("Percobaan 2") 
        time.sleep(3)

        kode_input = driver.find_element(By.NAME, "kode")
        kode_input.send_keys("P2")  
        time.sleep(3)

        link_input = driver.find_element(By.NAME, "link")
        link_input.send_keys("percobaan2.com")
        time.sleep(3)

        tombol_tambah = driver.find_element(By.XPATH, "//button[text()='Simpan']")
        tombol_tambah.click()
        time.sleep(3)

        # Assert halaman ke dashboard dan pengantar aja tersimpan ke Database
        assert "prodi" in driver.current_url
        assert "Percobaan 2" in driver.page_source
        print("Pengujian tambah data program studi sukses.")

    except Exception as e:
        pytest.fail(f"Terjadi kesalahan: {e}")

