from selenium import webdriver
from selenium.webdriver.common.by import By

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

driver=edge_setup()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)

# Simple Alert
driver.find_element(By.XPATH,"//button[@id='alertBtn']").click()
driver.switch_to.alert.accept()
driver.implicitly_wait(10)

# Conformation Alert
driver.find_element(By.XPATH,"//button[@id='confirmBtn']").click()
driver.switch_to.alert.accept()
driver.implicitly_wait(10)

# Prompt Alert
driver.find_element(By.XPATH,"//button[@id='promptBtn']").click()
text=driver.switch_to.alert
text.send_keys("Jabez")
text.accept()
driver.implicitly_wait(10)

# Popup window / multiple window
driver.find_element(By.XPATH,"//button[@id='PopUp']").click()
windowID=driver.window_handles
parentwindow=windowID[0]
child1window=windowID[1]
child2window=windowID[2]

driver.switch_to.window(child1window)
print("child1window",driver.title)
driver.switch_to.window(child2window)
print("child2window",driver.title)
driver.switch_to.window(parentwindow)
print("parentwindow",driver.title)
driver.implicitly_wait(10)

driver.quit()