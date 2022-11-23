#!/usr/bin/env python
# coding: utf-8

# In[9]:


#control statements excerise3
#1
def print_temp(temperature):
    if temperature < 0:
        print("Below freezing")
    elif temperature < 10:
        print("Very cold")
    elif temperature < 20:
        print('Chilly')
    elif temperature < 30:
        print("Warm")
    elif temperature < 40:
        print("Hot")
    else:
        print("Too hot")

print_temp(29)                        


# In[14]:


#2
student_number = input("Please enter your student number: ")
student_tutorial = float(input("Please enter your student tutorial mark: "))
student_test = float(input("Please enter your student test mark: "))

if (student_test + student_tutorial)/2 < 40:
    print("Your final grade is F")
else:
    examination_mark = float(input("Please enter your examination mark: "))
    final_grade = 0.25*student_tutorial + 0.25*student_test + 0.5*examination_mark
    if final_grade < 50:
        print("Your final grade is E")
    elif final_grade < 60:
        print("Your final grade is D")
    elif final_grade < 70:
        print("Your final grade is C")
    elif final_grade < 80:
        print("Your final grade is B") 
    else:
        print("Your final grade is A")


# In[27]:


#collections excerise1
a = [1,3,5]
b = [2,4,6]

c = a + b
print(c)

d = sorted(c)
print(d)


d = list(reversed(d))
print(d)

c[3] = 42
print(c)

d.append(10)
print(d)

c = c + [7,8,9]
print(c)

print(c[:3])

print(d[-1])

print(len(d))


# In[37]:


#tuples

a = (4,3,2,1)
b = (5,6,7,8)

c = a + b
print(c)

d = tuple(sorted(c))
print(d)

print(d[2])
print(d[-3:])
print(len(d))


# In[41]:


#set

a = {1,2,3,4}

b = {1,3,5,7}

c = a | b
print(c)

d = a - b
print(d)


e = b - a
print(e)

f = b & a
print(f)

g = b ^ a
print(g)

print(len(c))


# In[47]:


#ranges

print(list(range(0,20)))
print(list(range(3,13)))
print(list(range(2,51,3)))


# In[50]:


# Dictionaries

directory = {'Jane Doe': '+27 555 5367', 'John Smith':'+27 555 6254', 'Bob Stone':'+27 555 5689'}

directory['Jane Doe'] = '+27 555 1024'
print(directory)

directory['Anna Cooper'] = '+27 555 3237'
print(directory)

print(directory['Bob Stone'])
print(directory.get("Bob Stone", None))
print(directory.keys())
print(directory.values())


# In[56]:


#Converting between collection types

a = [1,1,2,3,3]

a = tuple(a)

b = list(a)
print(len(b))

c = set(b)
print(len(c))

d = list(c)
print(len(d))

e = list(range(1,11))
print(e)

directory = {'Jane Doe': '+27 555 5367', 'John Smith':'+27 555 6254', 'Bob Stone':'+27 555 5689'}

t = [tup for tup in directory.items()]
print(t)

v = [tup for tup in directory.values()]
print(v)

k = [tup for tup in directory.keys()]
print(k)

s = "antidisestablishmentarianism"

s = sorted(s)
print(s)

s2 = "".join(s)
print(s2)

w = "the quick brown fox jumped over the lazy dog".split(" ")
print(w)


# In[67]:


#Two-dimensional sequences

a = [(1),(1,2),(1,2,3)]
print(a[1][1])

b = [list(range(4)),list(range(4,8)),list(range(8,12)), list(range(12,16))]
print(b)

print(b[0][-2:])


# In[71]:


#loops excerise4
#1.
months = ('January','February','March','April','May','June','July','August','September','October','November','December')
days_in_months = (31,28,31,30,31,30,31,31,30,31,30,31)

d = {months[i]:days_in_months[i] for i in range(len(months))}
print(d)

#2

d = dict(zip(months, days_in_months))
print(d)


# In[ ]:


# errors and exceptions excerise2
#1
person = {}

properties = [
    ("name", str, "string"),
    ("surname", str, "string"),
    ("age", int, "number"),
    ("height", float, "number"),
    ("weight", float, "number"),
]

for prop, p_type, print_type in properties:
    value_type = None
    while value_type is None:
        try:
            person[prop] = p_type(input("Please enter your %s: " % prop))
            value_type = type(person[prop])
        except ValueError:
            print("please enter %s" % print_type)


# In[1]:


#2
def print_list_element(thelist, index):
    try:
        print(thelist[index])
    except IndexError:
        print("index out of range")
        
print_list_element([1,2,3], 4)        


# In[17]:


#3
def add_to_list_in_dict(thedict, listname, element):
    try:
        l = thedict[listname]
    except KeyError:
        thedict[listname] = []
        print("Created %s." % listname)
    else:
        print("%s already has %d elements." % (listname, len(l)))
    finally:
        thedict[listname].append(element)
        print("Added %s to %s." % (element, listname))
        
add_to_list_in_dict({'a':[1,2,3], 'b':[4,5,6]}, 'c', 5)        


# In[97]:


#functions ex7
#1

import numpy as np

p = lambda x: x**0.5

print(p(10))

p2 = lambda x,y: (x**0.5 + y**0.5)**0.5

print(p2(10,15))

c = lambda *args: sum(args)/len(args)

print(c(1,2,3))

p4 = lambda s: set(s)

print(p4("nfdsnjkdnf"))


# In[98]:


#2

def p(x):
    print(x**0.5)
      
def p2(x,y):
    print((x**0.5 + y**0.5)**0.5)

def p3(*args):
    print(sum(args)/len(args)) 
    
def p4(s):
    print(set(s))    
    
p(10)
p2(10,15)
p3(1,2,3)
p4("nfdsnjkdnf")


# In[94]:


#Classes ex1


#1. Class
# 2. instance of the class Person
# 3. surname passed as a variable to the class
# 4. self is a parameter passed into each instance method of the class
# 5. age is a method of the Person class
# 6. local variable inside age method
# 7. variable in the object
# 8. person instance is referred to by the variable name person



# In[ ]:


#2
import datetime # we will use this for date objects

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

        self.address = address
        self.telephone = telephone
        self.email = email
        self._age = None
        self._age_last_recalculated = None

        self._recalculate_age()

    def _recalculate_age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        self._age = age
        self._age_last_recalculated = today

    def age(self):
        if (datetime.date.today() > self._age_last_recalculated):
            self._recalculate_age()

person = Person(
    "Jane",
    "Doe",
    datetime.date(1992, 3, 12), # year, month, day
    "No. 12 Short Street, Greenville",
    "555 456 0987",
    "jane.doe@example.com"
)

print(person.name)
print(person.email)
print(person.age())


# In[ ]:


#3

# profession and surname are class attributes, However, proffesion when called in the initializer then is set to
# default None, but if passed to the initializer a variable for profession it set to be the variable. surname will Smith for
# all instances.

# name will be set as what given to the initializer


# In[ ]:


#4

class Numbers:
    MULTIPLIER = 4
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def add(self):
        return self.x + self.y
    
    @classmethod
    def multiply(cls, a):
        return a * cls.MULTIPLIER
    
    @staticmethod
    def subtract(b, c):
        return b - c
    
    @property
    def value(self):
        return (self.x, self.y)
    
    @value.setter
    def value(self, x, y):
        self.x = x
        self.y = y

    @value.deleter
    def value(self):
        del self.x
        del self.y
    
    
        


# In[115]:


#5
import datetime # we will use this for date objects

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

        self.address = address
        self.telephone = telephone
        self.email = email
        self._age = None
        self._age_last_recalculated = None

        self._recalculate_age()

    def _recalculate_age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        self._age = age
        self._age_last_recalculated = today

    def age(self):
        if (datetime.date.today() > self._age_last_recalculated):
            self._recalculate_age()
            

person = Person(
    "Jane",
    "Doe",
    datetime.date(1992, 3, 12), # year, month, day
    "No. 12 Short Street, Greenville",
    "555 456 0987",
    "jane.doe@example.com"
)

print(dir(person))
print(dir(Person))

print(person.__str__())
print(str(person))

print(type(person))
print(type(Person))

def print_object_attrs(obj):
    for k, v in obj.__dict__.items():
        print("%s: %s" % (k, v))
        
print_object_attrs(person)       


# In[127]:


#6
class Something:
    
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        
    def __str__(self):
        attrs = ["%s=%s" % (k, v) for (k, v) in self.__dict__.items()]
        return "%s: %s" % (self.__class__.__name__, " ".join(attrs))
        
a = Something(name="Jane", surname="Doe")

print(a.__str__())

