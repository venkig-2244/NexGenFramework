from influxdb import InfluxDBClient
from datetime import datetime
import yfinance as yf
# from influxdb_client import InfluxDBClient, Point, WritePrecision
# from influxdb_client.client.write_api import SYNCHRONOUS

token = "mySuP3rS3cr3tT0keN"
# #Setup database
client = InfluxDBClient('20.219.137.165', 8086, username=None, password=None, headers={"Authorization": token})
client.create_database('mydb')
print(client.get_list_database())
client.switch_database('mydb')


# data = yf.download("MSFT", start='2022-07-01')
# data = data.to_csv()

# print(data)
# #Setup Payload
json_payload = []
index = 0
while(index <= 100):
    data = {
        "measurement": "stocks",
        "tags": {
            "ticker": "Infy" 
            },
        "time": datetime.now(),
        "fields": {
            'open': 1688.37,
            'close': 1667.93
        }
    }
    json_payload.append(data)
    index += 1

    # #Send our payload
    client.write_points(json_payload)

# url = "http://20.219.137.165:8086"
# org = "myorg"
# bucket = "mybucket"



# client = InfluxDBClient(url=url, token=token, bucket=bucket)

# write_api = client.write_api(SYNCHRONOUS)
# write_api.write(bucket, org, data, write_precision='s')

