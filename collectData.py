#!/usr/bin/python
import requests
import json
import sys
from sense_hat import SenseHat
from time import sleep
from time import gmtime, strftime

def cmd2JSON(cmd):
        return json.dumps({'Stmt':cmd,'Workspace':"",'Opts':{}})

def getData(server,cmdStr):
        r = requests.post(server,data=cmd2JSON(cmdStr) , stream=True)
        for content in json_stream(r.raw):
                return (json.dumps(content))

def json_stream(fp):
        for line in fp:
                yield json.loads(line)
                
if __name__ == "__main__":
        sense = SenseHat()
        sense.set_rotation(180)
        sense.low_light = True
        sense.load_image("logo8.png")
        sleep(1)

        #sense.clear()
        #humidity = round(sense.get_humidity(),2)
        #temp = round(sense.get_temperature(),2)
        #pressure = round(sense.get_pressure(),2)

        sense.show_message("Data collection starting.",scroll_speed=0.05)
        sense.load_image("logo8.png")
        sense.set_imu_config(True, True, True)
        count = 0
        while True:
                sleep(1)
                count = count + 1
                if count%60 == 0:
                        count=0
                        #sense.show_message("*",scroll_speed=0.05)
                        tmp_res = json.loads(getData("http://localhost:9090/cmd,"select count(*) from collect"))
                        now_count = str(tmp_res['Content']['content'])
                        sense.show_message( now_count[2:-2] + " rows", scroll_speed=0.05)
                        sense.load_image("logo8.png")

                sense.set_pixel(7, 6, 20*(count%10)+50, 110, 20*(count%10)+50)
                sense.set_pixel(7, 7, 20*(count%10)+50, 110, 20*(count%10)+50)
                sense.set_pixel(6, 6, 20*(count%10)+50, 110, 20*(count%10)+50)
                sense.set_pixel(6, 7, 20*(count%10)+50, 110, 20*(count%10)+50)

                humidity = sense.get_humidity()
                temp = sense.get_temperature()
                pressure = sense.get_pressure()

                orientation = sense.get_orientation_degrees()
                pitch = orientation['pitch']
                roll = orientation['roll']
                yaw = orientation['yaw']
                acceleration = sense.get_accelerometer_raw()
                acc_x = acceleration['x']
                acc_y = acceleration['y']
                acc_z = acceleration['z']
                
                now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                stmt = "insert into collect values('" + now + "','"
                stmt = stmt + str(humidity) + "','"  + str(temp) + "','" + str(pressure) + "','" + str(pitch)
                stmt = stmt + "','" + str(roll) + "','" + str(yaw) + "','" + str(acc_x)
                stmt = stmt + "','" + str(acc_y) + "','" + str(acc_z) + "')"

                #print now, humidity, temp, pressure, pitch, roll, yaw, acc_x, $
                #print stmt
                getData("http://localhost:9090/cmd", stmt)

