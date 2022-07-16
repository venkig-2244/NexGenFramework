from influxdb import InfluxDBClient
from datetime import datetime

#Setup database
client = InfluxDBClient('localhost', 8086, 'admin', 'Password1', 'mydb')
client.create_database('mydb')
client.get_list_database()
client.switch_database('mydb')


#Setup Payload
json_payload = []
data = {
    "measurement": "stocks",
    "tags": {
        "ticker": "TCS" 
        },
    "time": datetime.now(),
    "fields": {
        'open': 1688.37,
        'close': 1667.93
    }
}
json_payload.append(data)


#Send our payload
client.write_points(json_payload)
