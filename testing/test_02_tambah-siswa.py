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

        link_mhs = driver.find_element(By.XPATH, '//a[@href="/user"]')
        link_mhs.click()
        time.sleep(2)

        link_add_mhs = driver.find_element(By.XPATH, '//a[@href="/siswa/tambah"]')
        link_add_mhs.click()
        time.sleep(2)

        nisn_input = driver.find_element(By.NAME, "nisn")
        nisn_input.send_keys("123456") 
        time.sleep(3)

        nama_input = driver.find_element(By.NAME, "nama")
        nama_input.send_keys("Pengguna Baru")  
        time.sleep(3)

        email_input = driver.find_element(By.NAME, "email")
        email_input.send_keys("pengguna@1.tes") 
        time.sleep(3)

        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys("percobaan1")  
        time.sleep(3)

        tempat_lahir_input = driver.find_element(By.NAME, "tempat_lahir")
        tempat_lahir_input.send_keys("Batam") 
        time.sleep(3)

        tanggal_lahir_input = driver.find_element(By.NAME, "tanggal_lahir")
        tanggal_lahir_input.send_keys("01/01/2024")  
        time.sleep(3)

        jenis_kelamin_input = driver.find_element(By.ID, "Laki-Laki")
        jenis_kelamin_input.click()
        time.sleep(3)

        sekolah_input = driver.find_element(By.NAME, "sekolah_asal")
        sekolah_input.send_keys("SMA Bengkong")  
        time.sleep(3)

        dropdown = Select(driver.find_element(By.NAME, "jurusan"))
        dropdown.select_by_visible_text("IPA")
        time.sleep(3)

        kontak_input = driver.find_element(By.NAME, "kontak")
        kontak_input.send_keys("081234556")  
        time.sleep(3)

        alamat_input = driver.find_element(By.NAME, "alamat")
        alamat_input.send_keys("Bengkong")  
        time.sleep(5)
        
        tombol_tambah = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        tombol_tambah.click()
        time.sleep(3)

        # Assert halaman ke dashboard dan 123456 tersimpan ke Database
        assert "user" in driver.current_url
        assert "123456" in driver.page_source
        print("Pengujian tambah data siswa sukses.")

    except Exception as e:
        pytest.fail(f"Terjadi kesalahan: {e}")