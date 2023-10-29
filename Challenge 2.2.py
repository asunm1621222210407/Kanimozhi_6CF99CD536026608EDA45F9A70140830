#Implement a class called Player that represents a cricket player. The Player class should have a method called play() which prints "The player is playing cricket. Derive two classes, Batsman and Bowler, from the Player class. Override the play() method in each derived class to print "The batsman is batting" and "The bowler is bowling", respectively. Write a program to create objects of both the Batsman and Bowler classes and call the play() method for each object.
class Batsman:
  def __init__(self, name):
      self.name = name

  def play(self):
      print(f"{self.name} is a batsman. They are ready to bat!")

class Bowler:
  def __init__(self, name):
      self.name = name

  def play(self):
      print(f"{self.name} is a bowler. They are ready to bowl!")

batsman1 = Batsman("Virat Kohli")
bowler1 = Bowler("Jasprit Bumrah")

batsman1.play()
bowler1.play()