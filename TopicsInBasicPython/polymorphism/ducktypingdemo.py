class Duck:
    def Talk(self):
        print('Quack Quack')

class Human:
    def Talk(self):
        print('Hello')

def callTalk(obj):
    obj.Talk()

d=Duck()
callTalk(d)

h=Human()
callTalk(h)
