#!/usr/bin/python3

class MyClass:
    def __init__(self):
        self.res = 0
        print ( "MyClass constructor ..." )

    def add(self,x,y):
        self.res = x + y

    def result(self):
        print ( self.res )

#Create an instance of MyClass
obj = MyClass()

#Invoke add method with parameters
obj.add( 10, 20)

#Invoke result method to print the result
obj.result()
