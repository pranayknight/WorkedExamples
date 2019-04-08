#creating getter and setter methods
class programmer:

    def setName(self,n):
        self.name=n
    def getName(self):
        return self.name

    def setSalary(self,s):
        self.salary=s
    def getSalary(self):
        return self.salary

    def setTechnologies(self,t):
        self.technologies=t
    def getTechnologies(self):
        return self.technologies

p1=programmer()
p1.setName("John Johny")
p1.setSalary(10000)
p1.setTechnologies(["Java","Hibernate","Spring","Python"])

print(p1.getName())
print(p1.getSalary())
print(p1.getTechnologies())

