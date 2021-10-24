from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.implicitly_wait(10)

driver.get("http://automationpractice.com/index.php")


driver.find_element(By.CLASS_NAME, "login").click()

driver.find_element(By.ID, "email").send_keys("seleniumremote@gmail.com")
driver.find_element(By.ID, "passwd").send_keys("test123")
driver.find_element(By.ID, "SubmitLogin").click()

driver.find_element(By.XPATH, "//a[@title='Addresses']").click()
driver.find_element(By.CSS_SELECTOR, ".bloc_adresses div")
driver.back()
driver.find_element(By.XPATH, "//a[@title='Credit slips']").click()

WebDriverWait(driver, 10).until(
    expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-warning")))