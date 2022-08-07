from tokenize import Single
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

class DBConnection(object):
    
    _connectionToken = "mySuP3rS3cr3tT0keN"
    _dbConnection = "InfluxDB"

    def __init__(self, ipAddress):
        """virtual private constructor"""
        if DBConnection._dbConnection != 'InfluxDB':
            raise Exception("This class is a singleton class !")
        else:
            DBConnection._dbConnection = self

        self.client = InfluxDBClient(ipAddress, 8086, username=None, password=None, headers={"Authorization": self._connectionToken})            
        self.client.create_database('mydb')
        print(self.client.get_list_database())
        self.client.switch_database('mydb')        

    @staticmethod
    def getInstance():
        """Static Access Method"""
        if DBConnection._dbConnection == 'InfluxDB':
            DBConnection()

        return DBConnection._dbConnection


    def writeDataToDB(self, jsonPayload):
        # Send our payload
        self.client.write_points(jsonPayload)

class WriteResponseTimeToDB(object):
    
    dbConnection = DBConnection('20.219.137.165')
    def __init__(self):
        pass    

    def WriteResponseTimeToDB(self, json_payload):
        DBConnection.getInstance().writeDataToDB(json_payload)

class ResponseTimeForLogin(WriteResponseTimeToDB):
    def __init__(self):
        self.measurementName = "ResponseTime"
        WriteResponseTimeToDB.__init__(self)

    def WriteResponseTime(self, responseTime):
        json_payload = []    
        data = {
            "measurement": self.measurementName,
            "tags": {
                "ticker": "LoginRT" 
                },
            "fields": {
                'responsetime': responseTime
            }
        }

        json_payload.append(data)
        return super().WriteResponseTimeToDB(json_payload)

class ResponseTimeSearch(WriteResponseTimeToDB):
    def __init__(self):
        self.measurementName = "ResponseTime"
        WriteResponseTimeToDB.__init__(self)

    def WriteResponseTime(self, responseTime):
        json_payload = []    
        data = {
            "measurement": self.measurementName,
            "tags": {
                "ticker": "SearchRT" 
                },
            "fields": {
                'responsetime': responseTime
            }
        }

        json_payload.append(data)
        return super().WriteResponseTimeToDB(json_payload)

class TransactionsPerSecond(WriteResponseTimeToDB):
    def __init__(self):
        self.measurementName = "Transactions"
        WriteResponseTimeToDB.__init__(self)

    def WriteTransactionTime(self, txPerSecond):
        json_payload = []    
        data = {
            "measurement": self.measurementName,
            "tags": {
                "ticker": "TxPerSecond" 
                },
            "fields": {
                'txTime': txPerSecond
            }
        }

        json_payload.append(data)
        return super().WriteResponseTimeToDB(json_payload)

class CpuUsage(WriteResponseTimeToDB):
    def __init__(self):
        self.measurementName = "ResourceUsage"
        WriteResponseTimeToDB.__init__(self)

    def WriteUsagePercentage(self, cpuUsage):
        json_payload = []    
        data = {
            "measurement": self.measurementName,
            "tags": {
                "ticker": "CPU" 
                },
            "fields": {
                'usage': cpuUsage
            }
        }

        json_payload.append(data)
        return super().WriteResponseTimeToDB(json_payload)

class MemoryUsage(WriteResponseTimeToDB):
    def __init__(self):
        self.measurementName = "ResourceUsage"
        WriteResponseTimeToDB.__init__(self)

    def WriteUsagePercentage(self, memUsage):
        json_payload = []    
        data = {
            "measurement": self.measurementName,
            "tags": {
                "ticker": "Memory" 
                },
            "fields": {
                'usage': memUsage
            }
        }

        json_payload.append(data)
        return super().WriteResponseTimeToDB(json_payload)

class DiskUsage(WriteResponseTimeToDB):
    def __init__(self):
        self.measurementName = "ResourceUsage"
        WriteResponseTimeToDB.__init__(self)

    def WriteUsagePercentage(self, diskUsage):
        json_payload = []    
        data = {
            "measurement": self.measurementName,
            "tags": {
                "ticker": "Disk" 
                },
            "fields": {
                'usage': diskUsage
            }
        }

        json_payload.append(data)
        return super().WriteResponseTimeToDB(json_payload)

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
    
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_prefs = {}
    # chrome_options.experimental_options["prefs"] = chrome_prefs
    # chrome_prefs["profile.default_content_settings"] = {"images": 2}

    index = 0
    loginResponse = ResponseTimeForLogin()
    searchResponse = ResponseTimeSearch()
    txPerSec = TransactionsPerSecond()
    cpuUsage = CpuUsage()
    diskUsage = DiskUsage()
    memUsage = MemoryUsage()

    
    while(index <= 100):
        # json_payload = []    
        # data = {
        #     "measurement": "ResponseTime",
        #     # "tags": {
        #     #     "ticker": "Response" 
        #     #     },
        #     "time": datetime.now(),
        #     "fields": {
        #         'rtime': float(random.randint(2600, 3000))
        #     }
        # }

        # json_payload.append(data)
        loginResponse.WriteResponseTime(random.randint(5000, 5300))
        searchResponse.WriteResponseTime(random.randint(1000,1200))
        txPerSec.WriteTransactionTime(random.randint(1000,2000))
        cpuUsage.WriteUsagePercentage(random.randint(90,99))
        memUsage.WriteUsagePercentage(random.randint(50,80))
        diskUsage.WriteUsagePercentage(random.randint(20,50))

        index += 1

    #Send our payload
#    client.write_points(json_payload)

    # query = "select * from ResponseTime;"
    # print("Querying data: " + query)
    # result = client.query(query)

    # for measurement in result.get_points(measurement='ResponseTime'):
    #     curtime = measurement['time']
    #     timeval = measurement['rtime']
    #     print("{0}\t{1}".format(curtime, timeval))

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

