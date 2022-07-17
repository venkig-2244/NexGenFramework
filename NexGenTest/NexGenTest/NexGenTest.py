from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from logging.handlers import TimedRotatingFileHandler
import logging
import ecs_logging
from influxdb import InfluxDBClient
from datetime import datetime
import random

def main():
    logfile_name = 'nexgen.json'
    #logger.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logger.INFO)
    
    #handler = TimedRotatingFileHandler(logfile_name,
    #                                   when="d",
    #                                   interval=1,
    #                                   backupCount=100)
    logger = logging.getLogger("nexgen")
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(logfile_name)
    handler.setFormatter(ecs_logging.StdlibFormatter())
    logger.addHandler(handler)
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}

    client = InfluxDBClient('20.219.137.165', 8086, 'admin', 'Password1', 'mydb')
    #print(client.create_database('mydb'))
    print(client.get_list_database())
    print(client.switch_database('mydb'))

    json_payload = []
    data = {
        "measurement": "stocks",
        "tags": {
            "ticker": "Infy" 
            },
        "time": datetime.now(),
        "fields": {
            'open': float(random.randint(2600, 2670)),
            'close': float(random.randint(2600, 2670))
        }
    }
    json_payload.append(data)


    #Send our payload
    client.write_points(json_payload)

    query = "select * from stocks;"
    print("Querying data: " + query)
    result = client.query(query)

    for measurement in result.get_points(measurement='stocks'):
        usage_system = measurement['ticker']
        open = measurement['open']
        close = measurement['close']
        print("{0}\t{1}\t{2}".format(usage_system, open, close))

    # while(1):
    #     logger.info("NexGen Test starting..")
    #     logger.info("Initializing Chromer driver..")
    #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    #     logger.info("Opening URL google.com")
    #     driver.get("http://www.google.com")
    
    #     elem = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
    #     elem.send_keys("pycon")
    #     elem.send_keys(Keys.RETURN)
    
    #     logger.info("Waiting... ")
    #     sleep(10)
    #     logger.warning("Test completed. Closing driver.")

    #     driver.quit()

    
if __name__ == "__main__":
    main()

