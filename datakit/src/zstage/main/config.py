import os
from datetime import datetime
from os.path import dirname
import src.zstage.work.DateRoutines as date

jobDesc = ""
inputFile = ""
outputFile = ""
logFile = ""
inputURL = ""
today = datetime.now()
pastDate = None
# Note that we consider the csv files to be located in datakit. We can change that as we want:


def setConfig(job):
    global inputFile
    global logFile
    global jobDesc
    global inputURL
    jobDesc = job
    if "Crime" in job:
        pastDate = date.DateRoutines().minusDays(1)
        inputFile = f"{dirname(dirname(dirname(os.getcwd())))}\\Crime_Incidents.csv"
        logFile = f"{dirname(dirname(dirname(os.getcwd())))}\\logs\\CompileCrime_" \
                  f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.txt"
        yyyymmdd = pastDate.strftime("%Y-%m-%d")
        inputURL = "https://data.buffalony.gov/resource/d6g9-xbgu.csv?$where=created_at%20%3E%20%27" + yyyymmdd + \
                   "T00:00:00%27"

    elif "Date" in job:
        inputFile = f"{dirname(dirname(dirname(os.getcwd())))}\\Date.csv"
        logFile = f"{dirname(dirname(dirname(os.getcwd())))}\\logs\\CompileDate_{datetime.now().strftime('%Y_%m_%d')}.txt"
    return True


"""
Note that we cannot test file.logMessage in this file, it would work in any of the other files(This is because the 
file.py requires config.py and vice versa and there is a loop)
"""
