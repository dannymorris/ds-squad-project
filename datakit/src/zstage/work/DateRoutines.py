from datetime import datetime, timedelta
import src.zstage.work.HandleFile as HandleFile
import src.zstage.main.config as config


class DateRoutines:
    def timestamp(self):
        self.currdate = datetime.now().strftime("%Y%m%d%H%M%S")
        return self.currdate

    def stringtoDate(self,string_val):
        for fmt in ('"%Y-%m-%dT%H:%M:%S.%f"', "%m/%d/%Y", "%Y-%m-%d'T'%H:%M:%S"):
            try :
                self.datetime = datetime.strptime(string_val, fmt)
                self.sql_format = datetime.strftime(self.datetime, "%Y-%m-%d %H:%M:%S")
                return self.sql_format

            except:
                pass
        HandleFile.HandleFile().logMessage("FAILED CONVERTING " + string_val + "TO   sql DATE format")
        raise ValueError('no valid date format found')

    def minusDays(self,Days):
        self.d = datetime.today() - timedelta(days=Days)
        return self.d

def main():
    config.setConfig("Crime")
    dateTime = "2021-03-03T0g0:26:00.000"
    sql = DateRoutines().stringtoDate(dateTime)
    print(sql)
if __name__ == "__main__":
    main()