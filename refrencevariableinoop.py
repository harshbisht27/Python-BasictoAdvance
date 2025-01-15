class Person:
    def __init__(self):
        self.name = "Bappy"
        self.country = "india"
        
        
p = Person()
id(p)

q = p
id(q)


print(p.name)
print(q.name)

q.name = "Alex"
print(p.name)
print(q.name)