#Якщо метод підкласу має те саме ім'я, яке оголошено в методі суперкласу, тоді це називається Методом перевизначення
#Щоб досягти перевизначення методу, ми повинні використовувати успадкування.
class A:
    def sayHi(self):
        print(“I am in A”)

class B(A):
    def sayHi(self):
        print(“I am in B”)

ob = B()
ob.sayHi()
