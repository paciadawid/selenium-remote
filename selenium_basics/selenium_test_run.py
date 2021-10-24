from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.implicitly_wait(10)

driver.get("http://automationpractice.com/index.php")

driver.find_element(By.CSS_SELECTOR, ".logo")
driver.find_element(By.CSS_SELECTOR, ".shopping_cart")
driver.find_element(By.CSS_SELECTOR, "#newsletter-input")
driver.find_element(By.CSS_SELECTOR, ".homefeatured[data-toggle='tab']")
driver.find_element(By.CSS_SELECTOR, ".twitter a")


driver.find_element(By.XPATH, "//div[@id='header_logo']//img")
driver.find_element(By.XPATH, "//div[@class='shopping_cart']")
driver.find_element(By.XPATH, "//input[@id='newsletter-input']")
driver.find_element(By.XPATH, "//a[@class='homefeatured']")
driver.find_element(By.XPATH, "//*[@class='twitter']/a")

driver.find_element(By.ID, "search_query_top").send_keys("test")
driver.find_element(By.NAME, "submit_search").click()

WebDriverWait(driver, 10).until(
    expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-warning")))

# driver.find_element(By.CSS_SELECTOR, ".alert.alert-warning")
