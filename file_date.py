import os
import datetime

def show_file_date(filename):
  
  file = open(filename, "w")
  timestamp = os.path.getmtime(filename)
  time = str(datetime.datetime.fromtimestamp(timestamp))

  file.close()

  return ("{}".format(time[:10]))

print(show_file_date("test_file.txt")) 
# Should be today's date in the format of yyyy-mm-dd