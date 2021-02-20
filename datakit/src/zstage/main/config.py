import os
from datetime import datetime
from os.path import dirname

import src.zstage.work.date as date


jobDesc = ""
inputFile = ""
outputFile = ""
logFile = ""

# Note that we consider the csv files to be located dat datakit. We can change that as we want:
def setConfig(job):
        global inputFile
        global logFile
        global jobDesc
        jobDesc = job
        if "Crime" in job:
            inputFile = f"{dirname(dirname(dirname(os.getcwd())))}\\Crime_Incidents.csv"
            logFile = f"{dirname(dirname(dirname(os.getcwd())))}\\logs\\CompileCrime_{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.txt"

        elif "Date" in job:
            inputFile = f"{dirname(dirname(dirname(os.getcwd())))}\\Date.csv"
            logFile = f"{dirname(dirname(dirname(os.getcwd())))}\\logs\\CompileDate_{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.txt"
        return True

"""
Note that we cannot test file.logMessage in this file, it would work in any of the other files(This is because the 
file.py requires config.py and vice versa and there is a loop)
"""