import os
import datetime

import src.zstage.work.date as date
import src.zstage.work.file as file

jobDesc = ""
inputFile = ""
outputFile = ""
logFile = ""

def setConfig(job):
        jobDesc = job
        global inputFile
        global logFile
        if "Crime" in job:
            inputFile = "Crime_Incidents.csv"
            logFile = f"logs/CompileCrime_{datetime.datetime.now()}.txt"

        elif "Date" in job:
            inputFile = f"Date.csv"
            logFile = f"logs/CompileDate_{datetime.datetime.now()}.txt"
        return True



def main():
    setConfig("Crime")
    file.File().logMessage("Test")

if __name__ == "__main__":
    main()
