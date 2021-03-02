
"""
A time helper to get the current hours for a particular location
--> Modularized in case we want to webscrape the data in the future, instead of hard coding it
"""

# HOURS mappings from 
#   int Day --> [datetime startTime, datetime endTime]
#   the Day int is a dependency on the strftime('%w') interface
WEIGAND_HOURS = {
  '0': [], # SUN
  '1': [], 
  '2': [],
  '3': [], # WED
  '4': [],
  '5': [],
  '6': [] # SAT
}

# Returns a timestamp representing the current time
def getTodaysHours(locationToken, opening=True):
  today = datetime.date.today().strftime('%w')
  
  # if token == '':
  return 