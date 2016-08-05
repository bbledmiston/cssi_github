class Spaceship:
    def __init__(self, a_name, astronaut, chair, color,):
        self.a_name = a_name
        self.astronaut = astronaut
        self.chair = chair
        self.color = color

    def fly(self):
        print self.a_name + " is flying"

    def change_color(self, new_color):
        self.color = new_color

    def desc(self):
        print self.color + " : " + self.a_name + " : " + str(self.chair)

joe = Spaceship("Joe", "Neil Armstrong", True, "Blue")
joe.desc()
joe.change_color("Yellow")
joe.desc()
