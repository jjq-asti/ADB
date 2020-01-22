import subprocess
import re

def getRawGpsCoordinates():
    process = subprocess.Popen(['adb', 'shell', 'dumpsys', 'location', '|', 'grep', 'Longitude'],stdout=subprocess.PIPE, stderr= subprocess.PIPE)
    stdout,stderr = process.communicate()
    return stdout,stderr

def parseGpsCoordinates(raw_gps_coordinates):
    data = raw_gps_coordinates
    data = data[0].decode().split(',')
    data = data[0:2]
    data = "".join(data)
    values = re.findall('\d+\.\d+',data)
    if not values:
        return None
    return values
    

if __name__ == "__main__":
    raw_data = getRawGpsCoordinates()
    data = parseGpsCoordinates(raw_data)
    print(data)
