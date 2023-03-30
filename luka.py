#მემკვიდრეობა 

# class Shape:
#     def __init__(self, color) -> None:
#         self.color = color

#     def hello (self) -> str:
#         return (f"Hello, I'm geometric figure with {self.color} color.")
    

# class Quadrangle(Shape):
#     def __init__(self, color,a,b,c=None,d=None):
#         super().__init__(color)
#         self.a, self.b, self.c, self.d = a,b,c,d
    
#     def perimeter(self):
#         return self.a + self.b + self.c + self.d
    

# class Rectangle(Quadrangle):
#     def area(self):
#         return self.a*self.b

# r1 = Rectangle('green', 2, 5)
# print(r1.area())
# print(r1.hello())

#პოლიმორფიზმი

# class Shape:
#     def __init__(self, color):
#         self.color = color

#     def hello (self):
#         return (f"Hello, I'm geometric figure with {self.color} color.")
    

# class Quadrangle(Shape):
#     def __init__(self, color,a,b=None,c=None,d=None):
#         super().__init__(color)
#         self.a, self.b, self.c, self.d = a,b,c,d
    
#     def perimeter(self):
#         if self.b and self.c and self.d:
#             return self.a + self.b + self.c + self.d
#         elif self.b:
#             return (self.a + self.b) * 2
#         else:
#             return self.a * 4
    

# class Rectangle(Quadrangle):
#     def area(self):
#         return self.a*self.b
    

# r1 = Rectangle('green', 6, 4)
# print(r1.area())
# print(r1.perimeter())

#პოლიმორფული კლასები

# class Chiken:
#     def speak(self):
#         print('Cock A Doodle Doo')

# class Dog:
#     def speak(self):
#         print('Woof Woof')

# class Cat:
#     def speak(self):
#         print('Meow Meow')


# a1 = Chiken()
# b1 = Dog()
# c1 = Cat()

# a1.speak()
# b1.speak()
# c1.speak()


# def talk(obj):
#     obj.speak()

# talk(a1)
# talk(b1)
# talk(c1)

# def talk(obj):
#     try:
#         obj.speak()
#     except AttributeError as msg:
#         print(msg)

# talk(127)

# ოპერატორების გადატვირთვა

class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other,
                        self.y * other,
                        self.z * other)
        elif isinstance(other, Vector):
            return Vector(self.x * other.x,
                        self.y * other.y,
                        self.z * other.z)
        
    def __str__(self):
        return f'{str(self.x), str(self.y), str(self.z)}'
        

v1 = Vector(1,2,3)  
v2 = Vector(4,5,6)  
v3 = v1 * v2
v4 = v1 * 7
print(v3)
print(v4)



# არითმეტიკული ოპერატორები

# class Calc():

#     def __init__(self, x):
#         self.x = x

#     def __add__(self, other):
#         n = self.x + other.x
#         return Calc(n)

#     def __sub__(self, other):
#         n = self.x - other.x
#         return Calc(n)

#     def __repr__(self):
#         return str(self.x)

# t1 = Calc(12)
# t2 = Calc(5)
# t3 = Calc(7)
# c = t1 + t2 - t3
# print(c)

#ინფორმაციის დამალვა

# class Hiding:
#     def public(self):
#         print("This is public method!")
        
#     def _protected(self):      
#         print("This is protected method!")

#     def __private(self):      
#         print("This is private method!")

# a = Hiding()
# a.public()
# a._protected()
# a.__private()


#hasattr, getattr, setattr, getter, setter, deleter

# class Rectangle:
#     def __init__(self, color, x, y):
#         self.color = color
#         self.__x = x
#         self.__y = y

#     def get_x(self):
#         return self.__x
    
#     def set_x(self, value):
#         self.__x += value

#     def del_x(self):
#         del self.__x

#     x = property(get_x, set_x, del_x)

# a1 = Rectangle('red', 5, 4)

# print(hasattr(a1, '__x'))
# print(hasattr(a1, 'color'))
# print(getattr(a1, 'color', 'ar moidzebna'))
# print(getattr(a1, 'area', 'ar moidzebna'))
# setattr(a1, 'color', 'black')
# print(getattr(a1, 'color', 'ar moidzebna'))

# print(a1.get_x())
# a1.set_x(7)
# print(a1.get_x())
# a1.del_x()
# print(a1.get_x())

# print(a1.x)
# a1.x = 3
# print(a1.x)
# del a1.x
# print(a1.x)

# getter, setter, deleter დეკორატორების გამოყენებით 
# class Employee:
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last

#     @property
#     def email(self):
#         return f'{self.first}{self.last}@btu.edu.ge'
    
#     @property
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
    
#     @fullname.setter
#     def fullname(self, name):
#         first, last = name.split(' ')
#         self.first = first
#         self.last = last

#     @fullname.deleter
#     def fullname(self):
#         print('Delete Name!')
#         self.first = None
#         self.last = None
    
# a1 = Employee('Nikoloz', 'Kvizhinadze')

# print(a1.email)
# print(a1.fullname)

# a1.fullname = 'Harry Potter'
# print(a1.fullname)

# del a1.fullname
# print(a1.fullname)
# def Fraction_Sum (self,top1,bottom1,) -> str :
#         self.top1 = top1
#         self.bottom1 = bottom1
#         self.fr_Sum = 0 
#         if (self.bottom // self.bottom1) == 1: 
#             self.fr_Sum = f"{self.top + self .top1} / {self.bottom}"
#         else:
#             self.fr_Sum= f"{(self.top * self.bottom1) + self.top1 * self.bottom1} / {self.bottom * self.bottom1}"
#         return self.fr_Sum

    
# def inverse(self) -> str:
#     return f"{self.bottom} / {self.top}"
    