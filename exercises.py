 #1

# class Bank_Account():
#     def __init__(self, Account_name , Balance = 0) -> None:
#         self.__Account_name = Account_name
#         self.__Balance = Balance

#     def Getter(self):
#         return self.__Account_name
    
#     def Setter(self,value):
#         self.__Account_name+= value

#     def Deposit(self,Deposit) -> str:
#         self.Deposit = Deposit
#         self.__Balance += self.Deposit
#         return f"თანხის შეტანა შესრულებულია. ამჟამად თქვენ ანგარიშზე გაქვთ {self.__Balance}: ლარი"
    
#     def withdraw(self,withdraw) -> str:
#         self.withdraw =withdraw
#         self.__Balance -= self.withdraw
#         return f"თანხის გამოტანა შესრულებულია. ამჟამად თქვენ ანგარიშზე გაქვთ {self.__Balance}: ლარი"
#     x = property(Getter,Setter)
# luka = Bank_Account("Luka karzhalovi" , 200)
# print(luka.withdraw(100))
# print(luka.x)
# luka.x = "1234"
# print(luka.x)


#2


# class Fraction():
#     def __init__(self,top, bottom ,) -> None:
#         self.top = top
#         self.bottom = bottom
    
#     def __str__(self) -> str:
#         return f"{self.top}/{self.bottom}"

#     def __add__ (self,other):
#         if isinstance(other,Fraction):
#             if self.bottom == other.bottom:
#                 return Fraction(self.top + other.top, self.bottom)
#             else:
#                 return Fraction (self.top+(self.bottom*other.bottom), self.bottom *other.bottom)
#     def inverse(self) -> str:
#         return f"{self.bottom}/{self.top}" 


# a1 = Fraction(15,6)
# f1 = Fraction(5,6)
# j1 = Fraction(5,6)
# V3 = a1 + f1
# print(V3)
# print(V3.inverse())

#3

# class Contacts():
#     def __init__(self,name= None, phone=None) -> None:
#         self.name = name
#         self.phone = phone
        

# class MailSender():
#     def sent_mail():
#         return f"თქვენი ემაილი გაგზავნილია"

# class Friends(Contacts,MailSender):
#     def __init__(self, name, phone,email) -> None:
#         super().__init__(name, phone)
#         self.email = email

# class Family(Contacts, MailSender):
#     def __init__(self, name, phone,email,birthday) -> None:
#         super().__init__(name, phone)
#         self.email , self.birthday = email ,birthday

 #4

# class Currency():
#     def __init__(self,value , unit = "GEL") -> None:
#         self.value = value
#         self.unit - unit
#     def __str__(self) -> str:
#         return f"{self.value}.00 {self.unit}"
    
#     def ChangeTo(self,valute):
#         mylist = ["GEL","USD","EUR"]
#         return self.value
#     def __add__(self,other):
#         if isinstance(other,Currency):
#             if self.unit != other.unit:


