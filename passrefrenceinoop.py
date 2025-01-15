class Person:

  def __init__(self,name,gender):
    self.name = name
    self.gender = gender



#outside of class
def greeting(person):
  print(f"Hi My name is {person.name} and i am a {person.gender}")
  p1 = Person("Alex", "Male")
  return p1
p = Person("Harsh", "Male")
a = greeting(p)


a.name

a.gender
