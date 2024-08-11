import csv
import readline
import code

class Area:
    def __init__(self,name,hectares,coordinates):
        self.name = name
        self.hectares = hectares
        self.coordinates = coordinates
        self.notices = []
        self.animalSeasons = []
    
    def addNotice(self,expiry,body):
        self.notices.append(Notice(expiry,body))

    def getNotices(self):
        return self.notices

    def addAnimalSeason(self,animalSeason):
        self.animalSeasons.append(animalSeason)
    
    def getAnimalSeasons(self):
        return self.animalSeasons

    def __str__(self):
        return "Area Object: " + self.name
    
    def dump(self):
        for a in self.animalSeasons:
            print("    ",a)

class Animal:
    def __init__(self,comName,sciName):
        self.sciName = sciName
        self.comName = comName
    
    def __str__(self):
        return "Animal Object: " + self.comName

class Map:
    def __init__(self):
        self.animals = {}
        self.areas = {}
    
    def addAnimal(self,animal):
        self.animals[animal.comName] = animal

    def addArea(self,area):
        self.areas[area.name] = area

    def getAreaByName(self,name):
        return self.areas[name]

    def buildAnimals(self,filename):
        with open(filename,newline='') as csvFile:
            reader = csv.reader(csvFile,delimiter=',',quotechar='"')
            for row in reader:
                self.addAnimal(Animal(row[0],row[1]))
    
    def buildAreas(self,filename):
        with open(filename,newline='') as csvFile:
            reader = csv.reader(csvFile,delimiter=',',quotechar='"')
            for row in reader:
                self.addArea(Area(row[0],row[2],row[1]))
    
    def buildAbundances(self,filename):
        with open(filename,newline='') as csvFile:
            reader = csv.reader(csvFile,delimiter=',',quotechar='"')
            for row in reader:
                area = self.areas[row[0]]
                animal = self.animals[row[1]]
                animalSeason = AnimalSeason(animal,area,row[2],row[3],row[4])
                area.addAnimalSeason(animalSeason)
    
    def dump(self):
        for a in self.areas.items():
            print(a[1])
            a[1].dump()

class Notice:
    def __init__(self,expiry,body):
        self.expiry = expiry
        self.body = body
    
    def __str__(self):
        return "Notice Object: " + self.body

class AnimalSeason:
    def __init__(self,animal,area,seasonStart,seasonEnd,abundance):
        self.animal = animal
        self.area = area
        self.seasonStart = seasonStart
        self.seasonEnd = seasonEnd
        self.abundance = abundance
    
    def __str__(self):
        return "Animal-Season Assoc Object: " + self.animal.comName + " in " + self.area.name

map = Map()

map.buildAnimals('animals.csv')
map.buildAreas('areas_hec.csv')
map.buildAbundances('abundances.csv')

map.dump()

#variables = globals().copy()
#variables.update(locals())
#shell = code.InteractiveConsole(variables)
#shell.interact()

#for area in map.areas:
#    print(area)
#    for animal in map.areas[area].animalSeasons:
#        print("    " + animal.animal.comName + " " + animal.abundance)
