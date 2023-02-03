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
        arduino.write('X'.encode())
        time.sleep(1)

        with open('lastReading.csv', 'r') as file:
            # Create a CSV reader
            reader = csv.reader(file)

            # Iterate over the rows of the CSV
            for row in reader:
                # Get the value from the second column (index 1)
                voltage = row[1]
        
        while(True):
            time.sleep(0.2)

            #print("Charge 1, Discharge 2, disconnect 3")

            UserOption = input("Charge 1, Discharge 2, disconnect 3, CLoud 4")

            if UserOption == '1':
                arduino.write('C'.encode())
                print("Charge")
            elif UserOption == '2':
                arduino.write('D'.encode())
                print("Discharge")
            elif UserOption == '3':
                arduino.write('X'.encode())
                print("Disconnect Battery")
            elif UserOption == '4':
                arduino.write('D'.encode())
                time.sleep(0.5)
                arduino.write('X'.encode())
                print("Disconnect Battery")

            else:
                print("No Valid Input")


    # handling KeyboardInterrupt by the end-user (CTRL+C)
    except KeyboardInterrupt:
        # closing communications port
        arduino.close()
        print('Communications closed')

