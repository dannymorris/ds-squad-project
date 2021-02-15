import os
import datetime

import src.zstage.work.date as date
import src.zstage.work.file as file

class config:

    def setConfig(self, job):
        self.jobDesc = job
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
    config().setConfig("Crime")
    file.File().logMessage("Test")

if __name__ == "__main__":
    main()
