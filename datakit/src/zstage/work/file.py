import main.config
import main.compile
import main.db

import logging
import traceback
import os
import datetime

# Create and configure logger
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(filename="newfile.log",
                    format='\n%(asctime)s   %(message)s',
                    filemode='a', level=logging.DEBUG)
logger = logging.getLogger()


class File:

    def getSQL(self, fileName):
        self.sql = ""
        try:
            br = open(fileName, "r")
            self.line = ""
            while self.line != None:
                self.line = br.readline()
                self.sql = self.sql + " " + self.line
            return self.sql
        except Exception as ex:
            traceback.print_exc()
            # logging.exception('Something awful happened!')
            logger.exception("Something awful happened")
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
        except:
            traceback.print_exc()
            logger.exception("Something awful happened")

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
        except:
            traceback.print_exc()
            logger.exception("Something awful happened")

    def collectCrimeEntities(self):
        try:
            self.br = open(config.inputFile, "r")
            for line in self.br:
                self.row = line.split(',')
                if len(self.row) > 6 and not db.exists("addresses",
                                                       "address1='" + self.row[6] + "' AND address2='" + self.row[
                                                           7] + "';"):
                    self.value = []
                    self.value[0] = self.row[6]
                    self.value[1] = self.row[7]
                    self.value[2] = self.row[16]
                    self.value[3] = self.row[25]
                    self.value[4] = self.row[24]
                    self.value[5] = self.row[23]
                    self.value[6] = self.row[22]
                    self.value[7] = self.row[11]
                    compile.addressTable.put(compile.addressTable.size() + db.tableSize("address") + 1, self.value)

                if len(self.row) > 6 and not db.exists("incidents",
                                                       "case_number='" + self.row[1] + "' AND address2='" + self.row[
                                                           0] + "';"):
                    self.value = []
                    self.value[0] = self.row[6]
                    self.value[1] = self.row[1]
                    self.value[2] = self.row[2]
                    self.value[3] = self.row[3]
                    self.value[4] = self.row[6]
                    self.value[5] = self.row[7]
                    compile.incidentTable.put(compile.incidentTable.size() + db.tableSize("incident") + 1, self.value)
            return True
        except:
            traceback.print_exc()
            logger.exception("Something awful happened")
            return False
