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

# Static table
NOofrow=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr"))
NOofcol=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr/th"))
print("number of rows:",NOofrow,"number of columns:",NOofcol)

# Read the specific row data
RowData=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr").text
print(RowData)

driver.execute_script("window.scrollBy(0,1400)")

#Read all the rows and columns data
try:
    for Row in range(2,NOofrow+1):
        for Col in range(1,NOofcol+1):
            data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+ str(Row) +"]/td["+ str(Col) +"]").text
            print(data,end="  ")
        print()
except:
    print("unable to print")

# dynamic web table
header=driver.find_element(By.XPATH,"//table[@id='taskTable']/thead/tr").text
print(header)

row=len(driver.find_elements(By.XPATH,"//tbody[@id='rows']/tr"))
col=len(driver.find_elements(By.XPATH,"//tbody[@id='rows']/tr/td"))

try:
    for r in range(1,row+1):
        data = driver.find_element(By.XPATH, "//tbody[@id='rows']/tr[" + str(r) + "]").text
        print(data,print())
    print()
except:
    print("unable to print")
driver.quit()