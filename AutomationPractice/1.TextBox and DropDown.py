import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    ser_obj=Service("C:\Program Files\Drivers\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe")
    driver=webdriver.Chrome(service=ser_obj)
    return driver
def edge_setup():
    from selenium.webdriver.edge.service import Service
    ser_obj=Service("C:\Program Files\Drivers\edgedriver_win64 (1)\msedgedriver.exe")
    driver=webdriver.Edge(service=ser_obj)
    return driver
def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    ser_obj=Service("C:\Program Files\Drivers\geckodriver-v0.35.0-win64\geckodriver.exe")
    driver=webdriver.Firefox(service=ser_obj)
    return driver

driver=edge_setup()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)

# Identify the web elements and enter the value
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("jabez")
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("jabez16042000@gmail.com")
driver.find_element(By.XPATH,"//input[@id='phone']").send_keys("9972976889")
driver.find_element(By.XPATH,"//textarea[@id='textarea']").send_keys("kolar gold field")
driver.find_element(By.XPATH,"//label[@for='male']").click()

# Select multiple checkBox's
days=driver.find_elements(By.XPATH,"//*[@id='post-body-1307673142697428135']/div[4]/div")
for day in days:
    if day.text=="Sunday" or day.text=="Saturday":
        day.click()
    continue
driver.implicitly_wait(10)

# Select the country from the DropDown
countries=Select(driver.find_element(By.XPATH,"//select[@id='country']"))
countries.select_by_visible_text("India")
driver.implicitly_wait(10)

# Select the colour from the DropDown using for_loop
colours=driver.find_elements(By.XPATH,"//select[@id='colors']/option")
for colour in colours:
    if colour.text=="Blue":
        colour.click()
    continue
driver.implicitly_wait(10)

# Select an option from the dropdown using select_class
Animals=Select(driver.find_element(By.XPATH,"//select[@id='animals']"))
Animals.select_by_visible_text("Lion")
time.sleep(3)

# DatePicker using send_keys method
driver.find_element(By.ID, "datepicker").click()
time.sleep(1)

# Date picker
YEAR = "2023"
MONTH = "April"
Date = "16"
while True:
    month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    if month == MONTH and year == YEAR:
        break
    else:
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click()

date = driver.find_elements(By.XPATH, "//body[1]/div[5]/table[1]/tbody[1]/tr/td")
for D in date:
    if D.text == Date:
        D.click()
        break
time.sleep(5)
driver.quit()