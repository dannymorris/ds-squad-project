import mysql.connector
import traceback

import src.zstage.work.HandleFile as HandleFile
import src.zstage.main.config as config



class DB:
    def __init__(self):
        self.con = None
        self.mycursor = None
        self.user = 'caskey5_melvinSebastian'
        self.password = 'dsSquad12'
        self.host = '192.249.124.190'
        self.database = 'caskey5_buffaloCrime_test'

    def connect(self):
        try:
            self.con = mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=
                                               self.database)

            self.mycursor = self.con.cursor()
            return self.mycursor
        except Exception as e:
            traceback.print_exc()
            HandleFile.HandleFile().logMessage(e)
            return None

    def close(self):
        try:
            self.con.close()
            return True
        except Exception as e:
            traceback.print_exc()
            HandleFile.HandleFile().logMessage(e)
            return False

    def insert(self, *args):
        self.mycursor = self.connect()
        if len(args) == 2:
            try:
                print("INSERT INTO " + args[0] + " VALUES " + args[1])
                self.mycursor.execute("INSERT INTO " + args[0] + " VALUES " + args[1])
                #self.mycursor.commit()
                return True
            except Exception as e:
                traceback.print_exc()
                HandleFile.HandleFile().logMessage(e)
                return False
        elif len(args) == 1:
            try:
                self.mycursor.execute(args[0])
                return True
            except Exception as e:
                traceback.print_exc()
                HandleFile.HandleFile().logMessage(e)
                return False

    def tableSize(self, table):
        self.mycursor = self.connect()
        size = 0
        try:
            self.mycursor.execute("SELECT COUNT(*) FROM " + table)
            size = self.mycursor.fetchall()
            return size[0][0]

        except Exception as e:
            traceback.print_exc()
            HandleFile.HandleFile().logMessage(e)
            return size

    def exists(self, table, where):
        self.mycursor = self.connect()
        exists = False
        if len(where) < 1:
            return exists
        try:
            self.mycursor.execute("SELECT COUNT(*) FROM " + table + " WHERE " + where)
            rs = self.mycursor.fetchall()
            size = rs
            if size[0][0] > 0:
                exists = True
            return exists
        except Exception as e:
            traceback.print_exc()
            HandleFile.HandleFile().logMessage(e)
            return exists

    def idWhere(self, table, where):
        self.mycursor = self.connect()
        try:
            id=0
            self.mycursor.execute("SELECT id FROM " + table + " WHERE " + where)
            rs = self.mycursor.fetchall()
            for i in rs:
                id = i[0]
            # Check with Eric
            if id==0 and len(where.split("=")[0].replace("'","")) >0:
                self.mycursor.execute("SELECT * FROM "+ table + " LIMIT 1")
                rs = self.mycursor.fetchall()
                column_count = len(rs[0])
                if column_count == 2:
                    tableKey = self.tableSize(table) + 1
                    value = where.split("=")[1].replace("'", "")
                    if len(value)>0:
                        print(table)
                        print(value)
                        self.insert(table, "(" + str(tableKey) + ",'" + str(value) + "')")
                        self.con.close()
                        return id
            else:
                return id

        except Exception as e:
            traceback.print_exc()
            HandleFile.HandleFile().logMessage(e)
            return None

    def selectStatement(self, select):
        self.mycursor = self.connect()
        results = {}
        try:
            self.mycursor.execute(select)
            rs = self.mycursor.fetchall()
            print("Returned dataset")
            column_count = len(rs[0])
            j = 0
            for i in rs:
                j = j + 1
                c = 1
                line = ""
                while c <= column_count:
                    if c == 1:
                        line = "" + str(i[c - 1])
                        c = c + 1
                    else:
                        line = line + "," + str(i[c - 1])
                        c = c + 1
                results[len(results) + 1] = line
            return results
        except Exception as e:
            #traceback.print_exc()
            HandleFile.HandleFile().logMessage(e)
            return results


def main():
    #sql = "select * from address limit 1000"
    #print(sql)
    #connection = DB()
    #connection.connect()
    config.setConfig("Crime")
    address = "'0 Block MARTHA AV'"
    results = DB().selectStatement(f"select location from address where address1 = {address} limit 1")
    print(results[1])
    #connection.close()
    #print(size)
    #for i in maps.keys():
    #    HandleFile.HandleFile().writeFileName("results.csv", maps.get(i))

if __name__ == "__main__":
    main()
