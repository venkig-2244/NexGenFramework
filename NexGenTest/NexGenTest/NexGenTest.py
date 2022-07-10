from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from logging.handlers import TimedRotatingFileHandler
import logging as logger

def main():
    logfile_name = 'nexgen.log'
    logger.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logger.INFO)
    
    handler = TimedRotatingFileHandler("nxtgen.log",
                                       when="d",
                                       interval=1,
                                       backupCount=100)

    logger.getLogger().addHandler(handler)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}

    for i in range(0, 5):
        logger.info("NexGen Test starting..")
        logger.info("Initializing Chromer driver..")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        logger.info("Opening URL google.com")
        driver.get("http://www.google.com")
    
        elem = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
    
        logger.info("Waiting... ")
        sleep(60)
        logger.warning("Test completed. Closing driver.")

        driver.quit()
    
if __name__ == "__main__":
    main()

