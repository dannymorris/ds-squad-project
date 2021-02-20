import logging
import traceback
import os
import datetime
from os.path import dirname

import src.zstage.main.config as config
import src.zstage.main.compile as compile
import src.zstage.work.db as db


# Note that the log file created from errors in the file python file will be stored as 'file_log'. Can be changed as needed
# Create and configure logger :
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(filename=f"{dirname(dirname(dirname(os.getcwd())))}/logs/file_log.log",
                    format='\n%(asctime)s   %(message)s',
                    filemode='a', level=logging.DEBUG)
logger = logging.getLogger()

"""
 Note that fileName will need to have the full address as input which can be changed if 
I know where the file normally originates from:
"""
class File:

    def getSQL(self, fileName):
        self.sql = ""
        try:
            self.br = open(fileName, "r")
            for line in self.br.read().splitlines():
                self.sql = self.sql + " " + line
            self.br.close()
            return self.sql
        except Exception as ex:
            traceback.print_exc()
            logger.exception("Exception occurred")
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
        except Exception as ex:
            traceback.print_exc()
            logger.exception("Exception occurred")

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
            logger.exception("Exception occurred")

    def collectCrimeEntities(self):
        try:
            self.br = open(config.inputFile, "r")
            for line in self.br.read().splitlines()[1:]:
                self.row = line.split(',')
                if len(self.row) > 6 and not db.exists("addresses",
                                                       "address1='" + self.row[6] + "' AND address2='" + self.row[
                                                           7] + "';"):
                    self.value = []
                    self.value.append(self.row[6])
                    self.value.append(self.row[7])
                    self.value.append(self.row[16])
                    self.value.append(self.row[25])
                    self.value.append(self.row[24])
                    self.value.append(self.row[23])
                    self.value.append(self.row[22])
                    self.value.append(self.row[11])
                    compile.addressTable.put(compile.addressTable.size() + db.tableSize("address") + 1, self.value)

                if len(self.row) > 6 and not db.exists("incidents",
                                                       "case_number='" + self.row[1] + "' AND address2='" + self.row[
                                                           0] + "';"):
                    self.value = []
                    self.value.append(self.row[6])
                    self.value.append(self.row[1])
                    self.value.append(self.row[2])
                    self.value.append(self.row[3])
                    self.value.append(self.row[6])
                    self.value.append(self.row[7])
                    compile.incidentTable.put(compile.incidentTable.size() + db.tableSize("incident") + 1, self.value)
            return True
        except Exception as ex:
            traceback.print_exc()
            logger.exception("Exception occurred")
            return False

