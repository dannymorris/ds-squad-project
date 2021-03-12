


import src.zstage.main.config as config
import src.zstage.work.db as db
import src.zstage.work.HandleFile as HandleFile
import src.zstage.work.DateRoutines as date


def main():
    db.DB().connect()
    status = config.setConfig("Crime")
    if "Crime" in config.jobDesc:
        Compile().compile_crime()
    if "Dates" in config.jobDesc:
        Compile().compile_dates()
    if "Weather" in config.jobDesc:
        Compile().compile_weather()
    if "All" in config.jobDesc:
        Compile().compile_crime()
        Compile().compile_dates()
        Compile().compile_weather()
    db.close()
    HandleFile.logger("Completed compile " + config.jobDesc+" " + status)


entityMap = {}
incidentTable = {268338: ['"0 Block MILLICENT AV"', '"21-0620021"', '"2021-03-03T00:26:00.000"', '"LARCENY/THEFT"', '"0 Block MILLICENT AV"', '"heh"'], 268339: ['"500 Block MINNESOTA AV"', '"21-0620037"', '"2021-03-03T00:05:51.000"', '"UUV"', '"500 Block MINNESOTA AV"', '"ehe"']}
addressTable ={20449: ['"0 Block MILLICENT AV"',  '"POINT (-78.81 42.935)"', '"UNIVERSITY"', '"District E"', '"Kensington-Bailey"', '"2"', '"ehe"'], 20450: ['"500 Block MINNESOTA AV"',  '"POINT (-78.808 42.946)"', '"UNIVERSITY"', '"District E"', '"Kensington-Bailey"', '"3"', '"eheh"']}
dateTable = {}
weatherTable = {}

class Compile :

    def compile_crime(self):
        HandleFile.HandleFile().getURI()
        #self.status = HandleFile.HandleFile().collectCrimeEntities()
        self.sql = self.generateAddressInsertStatement()
        if len(self.sql.split("VALUES")[1])>5:
            status = db.DB().insert(self.sql)
        self.sql = self.generateIncidentInsertStatement()
        if len(self.sql.split("VALUES")[1])>5:
            self.status =db.DB().insert(self.sql)
        return self.status

    def generateAddressInsertStatement(self):
        self.line = "INSERT into address (id,address1,location,council_district,police_district,neighborhood,zipcode) VALUES "
        HandleFile.HandleFile().logMessage("Adding " + str(len(incidentTable)) + " New rows to addresses")
        self.j=0
        for i in addressTable.keys():
            address1 = addressTable.get(i)[0]
            location = addressTable.get(i)[1]
            council_district = addressTable.get(i)[2]
            police_district = addressTable.get(i)[3]
            neighborhood = addressTable.get(i)[4]
            zipcode = addressTable.get(i)[6]
            if self.j==0:
                self.line = self.line + "(" + str(i) + ",'" + address1 + "','" + location + "," + council_district + "," + police_district + "," + neighborhood + "," + str(zipcode) + ")"
            else :
                self.line = self.line + ",(" + str(i) + ",'" + address1 + "','" + location + "," + council_district + "," + police_district + "," + neighborhood  + "," + zipcode + ")"
            self.j = self.j+1
        if self.line.endswith(','):
            self.line=self.line[:-1]
        print(self.line)
        return self.line

    def generateIncidentInsertStatement(self):
        self.line = "INSERT INTO incident (incident_id,incident_date,case_number,address_id,incident_type_id,location) VALUES "
        HandleFile.HandleFile().logMessage("Adding " + str(len(incidentTable)) + " New rows to incidents")
        self.j=0
        for i in incidentTable.keys():
            value = incidentTable.get(i)
            incident_id = str(i)
            if len(incident_id) < 2:
                incident_id="0"
            case_number = value[1]
            dateTime = value[2]
            mySQLDateTime = date.DateRoutines().stringtoDate(dateTime)
            incident_type = value[3]
            incident_type_id = db.DB().idWhere("incident_type", "incident_type='" + incident_type[1:-1] + "'")
            address1 = ""
            location = ""
            if len(value) > 4:
                address1=value[4]
            if len(value) > 5:
                location=value[5]
            address_id = db.DB().idWhere("address","address1='" + address1[1:-1] + "'")
            if self.j==0:
                self.line = self.line + "('" + str(incident_id) + "','" + mySQLDateTime + "','" + str(case_number) + "'," + str(address_id) + "," + str(incident_type_id) +","+location + ")"
            else :
                self.line = self.line + ",('" + str(incident_id) + "','" + mySQLDateTime + "','" + str(case_number) + "'," + str(address_id) + "," + str(incident_type_id) +","+location + ")"
            self.j=self.j+1
            print(self.line)
            if self.line.endswith(','):
                self.line = self.line[:-1]
                print(self.line)
                return self.line
        else :
            return self.line



    def compile_dates(self):
        return True

    def compile_weather(self):
        return True

def main():
    config.setConfig("Crime")
    #Compile().generateIncidentInsertStatement()
    #Compile().generateAddressInsertStatement()
    Compile().compile_crime()
if __name__ == "__main__":
    main()