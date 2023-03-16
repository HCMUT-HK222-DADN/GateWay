import serial.tools.list_ports

def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        if "USB Serial Device" in strPort:
            splitPort = strPort.split(" ")
            commPort = (splitPort[0])
    return commPort
#Kết nối tích hợp yolobit

ser = serial.Serial(port = getPort () , baudrate =115200)

mess = ""
def processData(data,client):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)
    if splitData[1] == "temp":
        client.publish("Temp_info", splitData[2])
    if splitData[1] == "humi":
        client.publish("Humi_info", splitData[2])
    if splitData[1] == "light":
        client.publish("light2", splitData[2])

def readSerial(client):
    bytesToRead = ser.inWaiting()
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            processData(mess[start:end + 1],client)
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end+1:]
def writeData(data):
    ser.write(str(data).encode())