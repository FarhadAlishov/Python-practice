"""
Change vowels in string to lowercase
and consonants to Uppercase
"""
def changecase(given_string):

    new_string = ""
    vowels = "AEOIU"
    consonants = "qwrtypsdfghjklzxcvbnm"

    for item in given_string:
        if item in vowels:
            item = item.lower()
        elif item in consonants:
            item = item.upper()
        new_string += item

    print(new_string)


changecase("alphabet")
changecase("yesterday")

"""
Shuffle random numbers
from 1 to n
"""

import random


def Shuffle(n):

    r = list(range(1, int(n)+1))
    random.shuffle(r)
    print(r)


Shuffle(10)

"""
Implementing Class Inheritance
System and letting user
adding and deleting members 
"""

x = 1


class Folder:
    def __init__(self, folname, child=None):
        self.name = folname

        if child is None:
            self.childname = []
        else:
            self.childname = child

    def add(self, child):
        if child not in self.childname:
            self.childname.append(child)

    def remove(self, child):
        if child in self.childname:
            self.childname.remove(child)

    def display(self):
        global x
        if x == 1:
            print(self.name)
            x = 0
        for child in self.childname:
            print(child.name)
            if isinstance(child, File):
                continue
            child.display()


class File:
    def __init__(self, filename, content=None):
        self.name = filename

        if content is None:
            self.contentstring = "None"
        else:
            self.contentstring = content

    def content(self, contentstr):
        self.contentstring = contentstr

    def display(self):
        print(self.contentstring)








Grandparent = Folder("Grandparent")
Parent = Folder("Parent")
ChildA = File("ChildA")
ChildA.content("This is the content for Child A")
ChildB = File("ChildB")
ChildC = Folder("ChildC")
Grandchild = File("Grandchild")

ChildC.add(Grandchild)
Parent.add(ChildA)
Parent.add(ChildB)
Parent.add(ChildC)
Grandparent.add(Parent)
Grandparent.display()
ChildA.display()
