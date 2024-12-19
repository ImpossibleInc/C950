class HashMap:
    def __init__(self, initialCapacity = 40):
        self.map = [None] * initialCapacity
        self.isFullTable = ["StartEmpty"] * initialCapacity

    def add(self, package):
        i = 0
        sectionsChecked = 0
        N = len(self.map)
        section = hash(package.idNumber)

        while sectionsChecked < N:
            if self.isFullTable[section] == "StartEmpty" or self.isFullTable[section] == "Removed":
                self.map[section] = package
                self.isFullTable[section] = "Filled"
                return True

            i += 1
            section = (hash(package.idNumber) + i ** 2) % N
            sectionsChecked += 1

        self.resize()
        self.insert(package)
        return True

    def search(self, key):
        i = 0
        sectionsChecked = 0
        N = len(self.map)
        section = hash(key) % N

        while (self.isFullTable[section] != "StartEmpty") and sectionsChecked < N:
            if (self.map[section] is not None) and (self.map[section].id_number == key):
                return self.map[section]

            i += 1
            section = (hash(key) + i ** 2) % N

            sectionsChecked += 1

        return None

    def resize(self):
        resizedMap = HashMap(initialCapacity = self.initialCapacity * 2)

        for package in self.map:
            resizedMap.add(package)

        self.initialCapacity = resizedMap.initialCapacity
        self.map = resizedMap.map
        self.isFullTable = resizedMap.isFullTable