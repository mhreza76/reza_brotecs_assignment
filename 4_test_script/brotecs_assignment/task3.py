import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.selenium.dev/")
print(driver.title)
drop_down_about = driver.find_element(By.CSS_SELECTOR, ".nav-item span")
drop_down_about.click()
about = driver.find_element(By.XPATH, "//a[@href = '/about']")
about.click()
p_text = driver.find_element(By.CSS_SELECTOR, ".header-description p.body-large")
print(p_text.text)
actual_result = "Selenium is a suite of tools for automating web browsers."
if(p_text.text == actual_result):
    print("verifyd with actual result: its correct")
else:
    print("verifyd with actual result: its incorrect")
driver.back()
time.sleep(5)
driver.quit()
