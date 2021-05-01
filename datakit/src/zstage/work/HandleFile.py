import traceback
import os
import datetime
import requests

import src.zstage.main.config as config
import src.zstage.main.compile as compile
import src.zstage.work.db as db


# Note that the log file created from errors in the file python file will be stored as 'file_log'.
# Can be changed as needed


"""
 Note that fileName will need to have the full address as input which can be changed if 
I know where the file normally originates from:
"""


class HandleFile:

    def getSQL(self, fileName):
        self.sql = ""
        try:
            self.br = open(fileName, "r")
            for line in self.br.read().splitlines():
                self.sql = self.sql + " " + line
            self.br.close()
            return self.sql
        except Exception as e:
            traceback.print_exc()
            HandleFile().logMessage(e)
            self.br.close()
            return self.sql

    def writeFileName(self, fileName, line):
        try:
            self.bw = open(fileName, "a")
            if os.path.getsize(fileName) == 0:
                self.bw.write(line)
                self.bw.close()
            else:
                self.bw.write(f'\n{line}')
                self.bw.close()
        except Exception as e:
            traceback.print_exc()
            HandleFile().logMessage(e)

    def logMessage(self, line):
        print(line)
        self.bw = open(config.logFile, "a")
        try:
            if os.path.getsize(config.logFile) == 0:
                self.bw.write(f"{datetime.datetime.now()} :: {line}")
                self.bw.close()
            else:
                self.bw.write(f'\n{datetime.datetime.now()} :: {line}')
                self.bw.close()
        except Exception as ex:
            traceback.print_exc()

    def collectCrimeEntities(self):
        self.addresstable = compile.addressTable
        self.incidenttable = compile.incidentTable
        try:
            self.br = open(config.inputFile, "r")
            for line in self.br.read().splitlines()[1:]:
                self.row = line.split(',')
                if len(self.row) > 6 and not db.DB().exists("incident",
                                                       "case_number='" + self.row[1][1:-1]  + "';"):
                    self.value = []
                    self.value.append(self.row[6][1:-1])
                    #self.value.append(self.row[7])
                    self.value.append(self.row[16][1:-1])
                    #self.value.append(self.row[25])
                    self.value.append(self.row[25][1:-1])
                    self.value.append(self.row[24][1:-1])
                    self.value.append(self.row[23][1:-1])
                    self.value.append(self.row[10][1:-1])
                    compile.addressTable[len(compile.addressTable) + db.DB().tableSize("address") + 1]= self.value
                    self.addresstable = compile.addressTable
                    print(self.addresstable)
                if len(self.row) > 6 and not db.DB().exists("incident",
                                                       "case_number='" + self.row[1][1:-1]  + "';"):
                    self.value = []
                    self.value.append(self.row[0])
                    self.value.append(self.row[1])
                    self.value.append(self.row[2])
                    self.value.append(self.row[3])
                    self.value.append(self.row[6])
                    self.value.append(self.row[7])
                    self.value.append(self.row[16])
                    compile.incidentTable[len(compile.incidentTable) + db.DB().tableSize("incident") + 1] = self.value
                    self.incidenttable = compile.incidentTable
                    print(self.incidenttable)
            return (self.addresstable, self.incidenttable)
        except Exception as e:
            traceback.print_exc()
            HandleFile().logMessage(e)
            return (self.addresstable, self.incidenttable)

    @staticmethod
    def getURI():
        try:
            url = config.inputURL
            r = requests.get(url, allow_redirects=True)
            open(config.inputFile, 'wb').write(r.content)
            return True
        except Exception as ex:
            traceback.print_exc()
            HandleFile().logMessage("Exception occurred" + "  " + config.inputURL)

def main():
    config.setConfig("Crime")
    HandleFile().collectCrimeEntities()
if __name__ == "__main__":
    main()


