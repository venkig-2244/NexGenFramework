from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

def main():
    print("NexGen Test starting..")

    driverService = Service('..//resources//chromedriver.exe')
    driver = webdriver.Chrome(service=driverService)
    driver.get("http://www.google.com")
    
    elem = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    
    print("Waiting... ")
    sleep(60)
    print("Before Quit function")
    driver.quit()
    
if __name__ == "__main__":
    main()

