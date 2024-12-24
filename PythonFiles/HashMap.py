class HashMap:
    def __init__(self, initialCapacity = 40):
        self.map = [None] * initialCapacity
        self.isFullTable = ["StartEmpty"] * initialCapacity

    def insert(self, key, package):
        section = hash(key) % len(self.list)
        sectionList = self.list[section]

        for kv in sectionList:
            if kv[0] == key:
                kv[1] = package
                return True

        keyValue = [key, package]
        sectionList.append(keyValue)
        return True

    def search(self, key):
        section = hash(key) % len(self.list)
        sectionList = self.list[section]
        for pair in sectionList:
            if key == pair[0]:
                return pair[1]
        return None

    def resize(self):
            resizedMap = HashMap(initialCapacity = self.initialCapacity * 2)

            for package in self.map:
                resizedMap.insert(package)

            self.initialCapacity = resizedMap.initialCapacity
            self.map = resizedMap.map
            self.isFullTable = resizedMap.isFullTable

    def remove(self, key):
        slot = hash(key) % len(self.list)
        destination = self.list[slot]

        if key in destination:
            destination.remove(key)