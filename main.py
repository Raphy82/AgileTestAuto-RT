
"""Input and Print"""
#print("Hello Raphy , what is the side of your rectangle")
#Omk = input()
#Omkrets = 4 * float(Omk)
#print("Din omkrets är " + str(Omkrets))

"""Input and Print"""
#First = int(input("what is your first nr: "))
#Second = int(input("What is your second nr: "))
#Sum = First + Second
#print("your total is: " + str(Sum))

"""If loop"""
#Weight = float(input("what is your weight: "))
#Value = (input("is your value Kg or Lbs: "))
#if Value.upper() == "K":
#    print("your weight is KG " + str(Weight))
#else:
#    print("your weight is Lbs " + str(Weight))

"""While loop"""
#i = 1
#while i <= 5:
#    print(i)
#    i = i + 1

"""List []"""
#list = ["Ett", "Två", "Tre", "Fyra"]
#l = "Ett, Två, Tre, Fyra"
#print(list) #skriver ut hela listan
#print(list[0:2]) #skriver ut första till andra plats i listan
#list.insert(0, "Noll")  #lägger till i första plats plats noll
#print(list) #skriver ut hela listan
#print(l[0:l.index(',')]) #skrive ut från noll position till , = Ett

"""For Loop"""
#Lista = [1, 2, 3, 4, 5, 6]
#for item in Lista:
#    print(item)

"""range"""
#Number = range(5) #0-4
#Number2 = range(1,6) #1-5
#Number3 = range(1,6,2) #1-5 but print every second nr 1,3,5.
#for number in Number2:
#    print(number) # will print 012345.

"""Parametrize - loop through list of data for your one test"""
#import pytest
#@pytest.mark.parametrize("username,password", [("kalle","password1"),("Anka","password2"),])
#def test_login(username,password):
    #print(username)
    #print(password)

"""Fixture - before and after each test run do this..."""
#import pytest
#@pytest.fixture
#def setup():
#    print("start browser")
#    yield
#    print("close browser")
#
#def test_test1(setup):
#    print("test 1 executed")
#
#def test_test2(setup):
#    print("test 2 executed")

