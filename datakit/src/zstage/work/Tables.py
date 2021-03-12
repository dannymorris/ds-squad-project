

import src.zstage.work.db as db
import src.zstage.work.HandleFile as HandleFile
import src.zstage.main.config as config

entityMap = {}
incidentTable = {}
addressTable = {}
dateTable = {}
weatherTable = {}

incidentParentTypeTable = {}
weatherTypeTable = {}
incidentTypeTable = {}
dateTypeTable = {}


def main():
    results = db.DB().selectStatement("SELECT * FROM incident_type_parent")
    for i in results.keys():
        if len(results.get(i).split(",")) > 1:
            key = results.get(i).split(",")[1]
            incidentParentTypeTable[key] = int(results.get(i).split(",")[0])
        else:
            incidentParentTypeTable[""] = 0

    results = db.DB().selectStatement("SELECT * FROM incident_type")
    for i in results.keys():
        if len(results.get(i).split(",")) > 1:
            key = results.get(i).split(",")[1]
            incidentTypeTable[key] = int(results.get(i).split(",")[0])
        else:
            incidentTypeTable[""] = 0

    results = db.DB().selectStatement("SELECT * FROM date_type")
    for i in results.keys():
        if len(results.get(i).split(",")) > 1:
            key = results.get(i).split(",")[1]
            dateTypeTable[key] = int(results.get(i).split(",")[0])
        else:
            dateTypeTable[""] = 0

    results = db.DB().selectStatement("SELECT * FROM incident")
    for i in results.keys():
        row = results.get(i).split(",")
        incidentTable[int(results.get(i).split(",")[0])] = row

    HandleFile.HandleFile().logMessage(" Imported  Tables  ")
    HandleFile.HandleFile().logMessage("address : " + str(len(addressTable)))
    HandleFile.HandleFile().logMessage("incident : " + str(len(addressTable)))
    HandleFile.HandleFile().logMessage("incident_type : " + str(len(incidentTypeTable)))
    HandleFile.HandleFile().logMessage("incident_type_parent : " + str(len(incidentParentTypeTable)))
    HandleFile.HandleFile().logMessage("date : " + str(len(dateTable)))



if __name__ == "__main__":
    config.setConfig("Crime")
    main()
