import src.zstage.main.config as config
import src.zstage.work.db as db
import src.zstage.work.HandleFile as HandleFile
import src.zstage.work.DateRoutines as date
import src.zstage.work.fill_data as filldata


entityMap = {}
incidentTable = {}
addressTable ={}
dateTable = {}
weatherTable = {}

class Compile :

    def compile_crime(self):
        HandleFile.HandleFile().getURI()
        filldata.filldata()
        self.tuple = HandleFile.HandleFile().collectCrimeEntities()
        self.addresstable=self.tuple[0]
        self.incidenttable = self.tuple[1]
        self.sql = self.generateAddressInsertStatement()
        print(self.sql)
        if len(self.sql.split("VALUES")[1])>5:
            status = db.DB().insert(self.sql)
        self.sql = self.generateIncidentInsertStatement()
        print(self.sql)
        if len(self.sql.split("VALUES")[1])>5:
            self.status =db.DB().insert(self.sql)
        return True

    def generateAddressInsertStatement(self):
        self.line = "INSERT into address (id,address1,location,council_district,police_district,neighborhood,zipcode) VALUES "
        HandleFile.HandleFile().logMessage("Adding " + str(len(self.addresstable)) + " New rows to addresses")
        self.j=0
        for i in self.addresstable.keys():
            rs =db.DB().selectStatement(f"select location from address where address1 = '{self.addresstable.get(i)[0]}' limit 1")
            if len(rs)==0:
                address1 = self.addresstable.get(i)[0]
                location = self.addresstable.get(i)[1]
                council_district = self.addresstable.get(i)[2]
                police_district = self.addresstable.get(i)[3]
                neighborhood = self.addresstable.get(i)[4]
                zipcode = self.addresstable.get(i)[5]
                if self.j == 0:
                    self.line = self.line + "(" + str(
                        i) + ",'" + address1 + "','" + location + "','" + council_district + "','" + police_district + "','" + neighborhood + "','" + zipcode + "')"
                else:
                    self.line = self.line + ",(" + str(
                        i) + ",'" + address1 + "','" + location + "','" + council_district + "','" + police_district + "','" + neighborhood + "','" + zipcode + "')"


            else:
                location = self.addresstable.get(i)[1]
                new_loc =  str(rs[1]) + f",{location[8:-2]}"
                print(new_loc)
                db.DB().insert(f"update address set location = '{new_loc}' where address1 = '{self.addresstable.get(i)[0]}'")
            self.j = self.j+1
        if self.line.endswith(','):
            self.line=self.line[:-1]
        return self.line

    def generateIncidentInsertStatement(self):
        self.line = "INSERT INTO incident (incident_id,incident_date,case_number,address_id,incident_type_id,location) VALUES "
        HandleFile.HandleFile().logMessage("Adding " + str(len(self.incidenttable)) + " New rows to incidents")
        self.j=0
        for i in self.incidenttable.keys():
            value = self.incidenttable.get(i)
            print(value)
            incident_id = value[0][1:-1]
            if len(incident_id) < 2:
                incident_id='0'
            case_number = value[1][1:-1]
            dateTime = value[2]
            mySQLDateTime = date.DateRoutines().stringtoDate(dateTime)
            incident_type = value[3]
            incident_type_id = db.DB().idWhere("incident_type", "incident_type='" + incident_type[1:-1] + "'")
            address1 = ""
            location = ""
            if len(value) > 4:
                address1=value[4][1:-1]
            if len(value) > 6:
                location=value[6][8:-2]

            address_id = db.DB().idWhere("address","address1='" + address1 + "'")
            if self.j==0:
                self.line = self.line + "('" + str(incident_id) + "','" + mySQLDateTime + "','" + str(case_number) + "'," + str(address_id) + "," + str(incident_type_id) +",'"+location + "')"
            else :
                self.line = self.line + ",('" + str(incident_id) + "','" + mySQLDateTime + "','" + str(case_number) + "'," + str(address_id) + "," + str(incident_type_id) +",'"+location + "')"
            self.j=self.j+1
            if self.line.endswith(','):
                self.line = self.line[:-1]
                return self.line
        else :
            return self.line



    def compile_dates(self):
        return True

    def compile_weather(self):
        return True

def main():
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
    HandleFile.HandleFile().logMessage("Completed compile " + config.jobDesc+" " + status)


if __name__ == "__main__":
    main()
