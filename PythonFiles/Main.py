import csv
from datetime import datetime, timedelta
from builtins import ValueError

from HashMap import *
from Package import *
from Truck import *



with open("/Users/isaiah/Documents/GitHub/C950/WGUFiles/CSVFiles/Distance.csv",encoding='utf-8-sig') as csvfile1:
    CSVDistance = csv.reader(csvfile1)
    CSVDistance = list(CSVDistance)

with open("/Users/isaiah/Documents/GitHub/C950/WGUFiles/CSVFiles/Address.csv", encoding='utf-8-sig') as csvfile2:
    CSVAddress = csv.reader(csvfile2)
    CSVAddress = list(CSVAddress)

with open("/Users/isaiah/Documents/GitHub/C950/WGUFiles/CSVFiles/PackageFiles.csv", encoding='utf-8-sig') as csvfile3:
    CSVPackage = csv.reader(csvfile3)
    CSVPackage = list(CSVPackage)

def loadPackageData(filename, packageHashTable):
    with open(filename, mode='r', encoding='utf-8-sig') as packageInfo:
        packageData = csv.reader(packageInfo)
        for package in packageData:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZipcode = package[4]
            pDeadline_time = package[5]
            pWeight = package[6]
            pStatus = "At Hub"

            p = Package(pID, pAddress, pCity, pState, pZipcode, pDeadline_time, pWeight, pStatus)

            HashMap.insert(pID, p)
def distanceBetween(x, y):
    distance = CSVDistance[x][y]
    if distance == '':
        distance = CSVDistance[y][x]

    return float(distance)

def getAddress(address):
    for row in CSVAddress:
        if address in row[2]:
            return int(row[0])

truck1 = Truck(16, 18, None, [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East",
                     timedelta(hours=8))

truck2 = Truck(16, 18, None, [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 0.0,
                     "4001 South 700 East", timedelta(hours=8))

truck3 = Truck(16, 18, None, [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], 0.0, "4001 South 700 East",
                     timedelta(hours=9, minutes=5))

packageTable = HashMap()

loadPackageData("/Users/isaiah/Documents/GitHub/C950/WGUFiles/CSVFiles/PackageFiles.csv", packageTable )
