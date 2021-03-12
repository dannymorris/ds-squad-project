from datetime import datetime, timedelta
import logging
import os
from os.path import dirname

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(filename=f"{dirname(dirname(dirname(os.getcwd())))}/logs/date_log.log",
                    format='\n%(asctime)s   %(message)s',
                    filemode='a', level=logging.DEBUG)
logger = logging.getLogger()


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
        logger.warning('no valid date format found')
        raise ValueError('no valid date format found')

    def minusDays(self,Days):
        self.d = datetime.today() - timedelta(days=Days)
        return self.d

def main():
    dateTime = "2021-03-03T00:26:00.000"
    sql = DateRoutines().stringtoDate(dateTime)
    print(sql)
if __name__ == "__main__":
    main()