class Musician:
    def __init__(self, name, instrument, genre):
        self.name = name
        self.instrument = instrument
        self.genre = genre
        self.age = 20

    def description(self):
        print "Hi my name is " + self.name + ". I play " + self.instrument

    def is_in_studio(self, recording):
        if recording == True:
            print self.name + (" is recording!")
        else:
            print self.name + (" is not recording")

jcole = Musician("j. cole", "voice", "rap")
beyonce = Musician("beyonce", "swag", "r&b")


#print jcole.name
#print beyonce.instrument
#jcole.description()
jcole.is_in_studio(True)
