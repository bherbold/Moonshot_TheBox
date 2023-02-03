# -*- coding: utf-8 -*-
"""
Created on Friday 6th January 2023

@authors: José Luz, Bendiks Herbold
"""
# importing libraries
import csv
import time


def Controller_main(arduino):
    try:
        print("enter Controller")
        # SEND MESSAGE
        arduino.write('L'.encode())
        preSteam = 0
        preTemp = 0
        pre_water_temp = 0
        t_pre = 0
        time.sleep(1)

        with open('lastReading.csv', 'r') as file:
            # Create a CSV reader
            reader = csv.reader(file)

            # Iterate over the rows of the CSV
            for row in reader:
                # Get the value from the second column (index 1)
                voltage = row[1]
        
        while(True):
            time.sleep(1)
            # Open the CSV file
            with open('../Control_Automation/Data_Management/lastReading.csv', 'r') as file:
                # Create a CSV reader
                reader = csv.reader(file)

                # Iterate over the rows of the CSV
                for row in reader:
                    # Get the value from the second column (index 1)
                    sauna_temp = row[4]
                    steam = row[6]
                    onOff = row[1]
                    water_temp = row[7]
            if float(water_temp) <= 40 and float(sauna_temp) <= 27 :
                # cold start
                coldStart.coldStart(arduino, 52, 20)
                arduino.write('H'.encode())
                print('Plug Off (Startup)')
                time.sleep(10)

            else:
                # Start PID controller
                PID.PID(arduino, 4)

            # set pre-Values
            preSteam = steam
            preTemp = sauna_temp
            pre_water_temp = water_temp

    # handling KeyboardInterrupt by the end-user (CTRL+C)
    except KeyboardInterrupt:
        # closing communications port
        arduino.close()
        print('Communications closed')