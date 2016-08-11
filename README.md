# rpi_sensor_hat_with_bigobject_demo
a demo to collect data from sensor hat and then insert to the local bigobject server

collectData.py : 
collect current time, humidity, temperature, pressure, pitch, roll, yaw, accelerometer x,y,z

The "collect" table schema 

"CREATE TABLE collect ('time' DATETIME32, 'humidity' FLOAT, 'temperature' FLOAT, 'pressure' FLOAT, 'pitch' FLOAT, 'roll' FLOAT, 'yaw' FLOAT, 'acc_x' FLOAT, 'acc_y' FLOAT, 'acc_z' FLOAT)"


test.py : 
just a test about accelerometer, rotate the logo by accelerometer value


PS. you can add "python collectData.py &" in /etc/rc.local to perform the script when the raspberry pi boot.
