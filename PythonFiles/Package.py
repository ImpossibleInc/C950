from datetime import timedelta, datetime


class Package:

    def __init__(self, idNumber, deliveryAddress, deliveryCity, deliveryState, deliveryZipCode, deliveryDeadline, packageMass, specialNote, deliveryStatus):
        self.idNumber = idNumber
        self.deliveryAddress = deliveryAddress
        self.deliveryCity = deliveryCity
        self.deliveryState = deliveryState
        self.deliveryZipCode = deliveryZipCode
        self.deliveryDeadline = deliveryDeadline
        self.packageMass = packageMass
        self.specialNote = specialNote
        self.deliveryStatus = deliveryStatus
        self.whichTruck = None
        self.onTruck = False
        self.enRouteTimestamp = None
        self.deliveryTimestamp = None

    def isTruckChosen(self):
        if self.whichTruck is None:
            return False
        return True

    def getRequiredTruck(self):
        if "Can only be on truck" in self.specialNote:
            specifiedTruckId = [int(i) for i in self.specialNote.split() if i.isdigit()][0]
            return specifiedTruckId
        return None

    def getDelayedArrivalTime(self):
        if "Delayed on flight---will not arrive to depot until" in self.specialNote:
            tokenizedSpecialNotes = self.specialNote.split()
            for token in tokenizedSpecialNotes:
                try:
                    timestamp = datetime.strptime(token, "%H:%M")
                    delayedArrivalTime = timedelta(hours=timestamp.hour, minutes=timestamp.minute)
                    return delayedArrivalTime
                except:
                    pass

        if "Wrong address listed" in self.specialNote:
            delayedArrivalTime = timedelta(hours=10, minutes=20)
            return delayedArrivalTime
        return None

    def getDeliveryDeadline(self):
        tokenizedSpecialNotes = self.specialNote.split()
        for token in tokenizedSpecialNotes:
            try:
                timestamp = datetime.strptime(token, "%H:%M")
                deliveryDeadline = timedelta(hours=timestamp.hour, minutes=timestamp.minute)
                return deliveryDeadline
            except:
                pass