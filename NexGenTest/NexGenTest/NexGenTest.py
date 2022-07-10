from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def main():
    print("NexGen Test starting..")

  #  driverService = Service(ChromeDriverManager().install())
    #driver = webdriver.Chrome(executable_path='../resources/chromedriver')

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    driver.get("http://www.google.com")
    
    elem = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    
    file = open("logs.txt")
    file.write("Hello world")
    file.close()

    print("Waiting... ")
    sleep(60)
    print("Before Quit function")
    driver.quit()
    
if __name__ == "__main__":
    main()

