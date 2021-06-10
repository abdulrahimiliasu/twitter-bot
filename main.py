from tweet import TwitterBot
from internetspeed import InternetSpeed

speed = InternetSpeed()

PINGS = speed.get_pings()
DWL_SPD = speed.get_download_speed()
UPL_SPD = speed.get_upload_speed()
print(PINGS, DWL_SPD, UPL_SPD)


tweet = TwitterBot(tweet=f'This Tweet is from a Python Bot\n Pings:{PINGS}, DOWN/{DWL_SPD}mbps, UP/{UPL_SPD}mbps',
                   username='', passowrd='')
