# ask user to evaluate which data (id from database (table WMI))
# process fuzzy logic and show graph
# import Fuzzy
import DB_Data

# Structure:
# Ask user propmt DB id ---> DONE
# Perform select data using DB_Data , then return the data to us
# get data yg mandatory c(audio_dur, and audio_score)

player_id = input("Insert player ID to view: ")
data = DB_Data.fetch(player_id)
print("id | username | visual score | visual duration | auditory score | auditory duration | visual result | audio result | wmi result | date created ")
print(data)

#audio_dur = DB_Data.fetch()
#audio_scr = DB_Data.fetch() # ni kena fetch sql query ke from db_data??

#audio_fuzz = Fuzzy.calcAuditory(audio_dur, audio_scr, True)
#visual_fuzz = Fuzzy.calcVisual()
#wmi_fuzz = WMI.calcWMI(audio_fuzz, visual_fuzz, True)