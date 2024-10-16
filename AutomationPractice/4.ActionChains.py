import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    ser_obj=Service("C:\Windows\chromedriver.exe")
    driver=webdriver.Chrome(service=ser_obj)
    return driver
def edge_setup():
    from selenium.webdriver.edge.service import Service
    ser_obj=Service("C:\Windows\msedgedriver.exe")
    driver=webdriver.Edge(service=ser_obj)
    return driver
def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    ser_obj=Service("C:\Windows\geckodriver.exe")
    driver=webdriver.Firefox(service=ser_obj)
    return driver

driver=chrome_setup()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)

# # DoubleClick
doubleclick = driver.find_element(By.XPATH, "//button[normalize-space()='Copy Text']")
drag = driver.find_element(By.XPATH, "//div[@id='draggable']")
drop = driver.find_element(By.XPATH, "//div[@id='droppable']")

mouse = ActionChains(driver)
mouse.double_click(doubleclick).perform()
driver.implicitly_wait(10)
mouse.drag_and_drop(drag, drop).perform()
driver.implicitly_wait(10)

# scroll window
driver.execute_script("window.scrollBy(0,700)","")
driver.implicitly_wait(10)

# Slider
slid = driver.find_element(By.XPATH, "//div[@id='slider']")
mouse.drag_and_drop_by_offset(slid, 0, 50).perform()
driver.implicitly_wait(10)

# Resizable
initial_size=driver.find_element(By.XPATH,"//div[@id='resizable']")
print(initial_size.size)
resize_element=driver.find_element(By.XPATH,"//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
mouse.click_and_hold(resize_element).move_by_offset(150,150).release().perform()
resized=initial_size.size
print(resized)
driver.implicitly_wait(10)

driver.quit()