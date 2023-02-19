import sys
from Adafruit_IO import MQTTClient
import time
import random
from TM_test import *
AIO_FEED_ID = "Button1"
AIO_USERNAME = "LamVinh"
AIO_KEY = "aio_ZIKb16NpOfu9Xwm16hN1KEB1BmAN"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_ID:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
# mỗi 10s gửi lệnh 1 lần
counter = 10
ai_detection = 5

ai_result = ""
prev_result = ""

while True:
    counter = counter - 1
    ai_detection = ai_detection - 1

    # cập nhật dữ liệu nhận dạng có người hay không mỗi 3 giây
    if ai_detection <= 0:
        ai_detection = 5
        prev_result = ai_result
        ai_result = simple_AI()
        if prev_result != ai_result:
            print("AI result",ai_result)
            client.publish('AI',ai_result)


    # cập nhật dữ liệu còn lại mỗi 10 giây
    if counter <= 0:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
        counter = 10
        #To do
        print("Dữ liệu đang cập nhật")
        temp = random.randint(15,35)
        client.publish('Temp_info',temp)    
        humi = random.randint(40,70)
        client.publish('Humi_info',humi)  
        light = random.randint(30,300)
        client.publish('light2',light)
    time.sleep(1)
    pass

