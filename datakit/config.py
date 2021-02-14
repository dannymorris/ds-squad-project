from os.path import dirname
import os
import datetime

import work.date
import work.file


class config:
    def __init__(self):
        self.jobDesc = ""
        self.inputFile = ""
        self.outputFile = ""
        self.logFile = ""

    def setConfig(self, job):
        self.jobDesc = job
        if "Crime" in job:
            self.inputFile = f"{dirname(os.getcwd())}Crime_Incidents.csv"
            self.logFile = f"{dirname(os.getcwd())}CompileCrime_{datetime.datetime.now()}.txt"

        elif "Date" in job:
            self.inputFile = f"{dirname(os.getcwd())}Date.csv"
            self.logFile = f"{dirname(os.getcwd())}CompileDate_{datetime.datetime.now()}.txt"
        return True


def main():
    config.setConfig("Crime")
    file.logMessage("Test")

if __name__ == "__main__":
    main()