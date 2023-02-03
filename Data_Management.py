# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 13:54:24 2019

@authors: Ingrid, Cristian, Marc - CITCEA
"""
# importing libraries
import datetime as dt
import re
import csv
import threading


# Writing the base class 'Thread'
class AsyncWrite(threading.Thread):

    def __init__(self, arduino):
        # calling superclass init
        threading.Thread.__init__(self)
        #self.out = out
        self.arduino = arduino

    def run(self):
        dataManagement(self.arduino)


def dataManagement(arduino):

    # creating communications object using Serial
    #arduino = serial.Serial('/dev/cu.usbserial-14330', 115200, timeout=3)
    #arduino = serial.Serial(str(HelperFunc.get_ESP32_port()), 115200, timeout=3)

    print("Starting!")

    # try-except-finally loop for data acquisition
    try:
        row = ["Timestemp", "Voltage"]
        with open('DataLogger.csv', 'w', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
            csvFile.close()

        while True:
            now = dt.datetime.now()
            # timeDiff = ((now - preTime).total_seconds()) # needed for Cost calculation

            # READ DATA
            # Check if there is new info from the Arduino and read it
            #print("start read")
            data_bytes = arduino.readline()
           # print(
              #  data_bytes
            #)
            #print("finish read")
            # Decoding the message into UTF-8
            data = data_bytes.decode("utf-8")

            # SAVE DATA
            # if data has been read, print and save it
            if data:
                # strip data string into 2, 3 or as many different values for each reading
                [voltage] = re.findall(pattern=r"[-+]?\d*\.\d+|[-+]?\d+",
                                      string=data)  # to understand pattern: https://regex101.com/

                # store date and readings (change them to float!) into a list
                row = [now,voltage]
                # save reading row into the csv file. File needs to be open with "a" (append) mode.
                with open('DataLogger.csv', 'a', newline='') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(row)
                    csvFile.close()
                    #print(row)
                with open('lastReading.csv', 'w', newline='') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(row)
                    csvFile.close()
            else:
                print('No data is being collected')

            preTime = now
    # handling KeyboardInterrupt by the end-user (CTRL+C)
    except KeyboardInterrupt:
        # closing communications port
        arduino.close()
        print('Communications closed')
