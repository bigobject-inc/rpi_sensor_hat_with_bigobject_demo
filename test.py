from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.low_light = True
sense.set_rotation(180)
sense.load_image("logo8.png")
sleep(2)
sense.clear()
humidity = round(sense.get_humidity(),1)
msg = "Humidity:" + str(humidity)
temp = round(sense.get_temperature(),1)
#temp2 = round(sense.get_temperature_from_humidity(),1)
#temp3 = round(sense.get_temperature_from_pressure(),1)
#msg = msg + " Temperatue:" + str(temp) + "|" + str(temp2) + "|" + str(temp3)
msg = msg + " Temperatue:" + str(temp)

pressure = round(sense.get_pressure(),1)
msg = msg + " Pressure:" + str(pressure)
print(msg)
sense.show_message("GO!!",scroll_speed=0.05)
sense.load_image("logo8.png")

sense.set_imu_config(True, True, True)
#for index in range(30):
while True:
        orientation = sense.get_orientation_degrees()
        print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))
        #orientation_rad = sense.get_orientation_radians()
        #print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation_rad))
        #gyro_only = sense.get_gyroscope()
        #print("p: {pitch}, r: {roll}, y: {yaw}".format(**gyro_only))
        #raw = sense.get_gyroscope_raw()
        #print("x: {x}, y: {y}, z: {z}".format(**raw))

        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']

        x = round(x, 0)
        y = round(y, 0)

        if x == -1:
                sense.set_rotation(90)
        elif y == 1:
                sense.set_rotation(0)
        elif y == -1:
                sense.set_rotation(180)
        else:
                sense.set_rotation(270)
        sleep(0.5)


#sense.set_rotation(180)
#sense.show_message("Done.",scroll_speed=0.05)
#sense.show_message(msg, text_colour=[100, 255, 100], scroll_speed=0.05)
