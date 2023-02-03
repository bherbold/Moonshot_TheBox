# importing libraries
import datetime as dt
import re
import csv
import serial
import HelperFunc

import Data_Management as DM
import Controller_main as CON_main
import Controller_Test as CON_test

arduino = serial.Serial(str(HelperFunc.get_ESP32_port()), 115200, timeout=3)

def Main():

    #background = DM.AsyncWrite(arduino)
    #background.start()

    #CON_main.Controller_main(arduino)
    CON_test.Controller_main(arduino)
    # wait till the background thread is done
    #background.join()
    print("Waited until thread was complete")

if __name__ == '__main__':
    Main()