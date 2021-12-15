import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get("https://suninjuly.github.io/explicit_wait2.html")
    wait = WebDriverWait(driver, 12)
    el = wait.until(EC.text_to_be_present_in_element((By.ID, 'price'), "$100"))
    assert el is not None, 'price is not equal $100'

    # Click on the "Book" button
    driver.find_element(By.ID, 'book').click()

    # считать x and running function
    # x = driver.find_element(By.ID, 'input_value').text
    # Ввести ответ в текстовое поле.
    driver.find_element(By.ID, 'answer').send_keys(calc(driver.find_element(By.ID, 'input_value').text))
    # click button "Submit"
    driver.find_element(By.ID, "solve").click()

    a = driver.switch_to.alert
    a_list = a.text.split()
    a.accept()

    time.sleep(5)
    url = "https://stepik.org/catalog"
    url1 = "https://stepik.org/lesson/181384/step/8?unit=156009"

    driver.execute_script("window.open();") # откроем новое окно
    driver.switch_to.window(driver.window_handles[1]) # переключим область действия драйвера на новую вкладку
    driver.get(url)
    driver.find_element(By.CSS_SELECTOR, '.navbar__auth_login').click()
    driver.find_element(By.ID, 'id_login_email').send_keys("sahaling@ya.ru")
    driver.find_element(By.ID, 'id_login_password').send_keys('7EIvfh0G')
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login_form .button_with-loader")))
    driver.find_element(By.CSS_SELECTOR, '#login_form .button_with-loader').click()

    driver.execute_script("window.open();")  # откроем новое окно
    driver.switch_to.window(driver.window_handles[2])  # переключим область действия драйвера на новую вкладку
    driver.get(url1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.textarea')))
    driver.find_element(By.CSS_SELECTOR, '.textarea').send_keys(a_list[len(a_list)-1])
    driver.find_element(By.CLASS_NAME, 'submit-submission').click()

finally:
    # time.sleep(10)
    driver.quit()
