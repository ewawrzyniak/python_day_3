#create a print function that prints out hello world
# print("Hello, World")
#ask the user for the day of the week 
# dayofweek = input ("what day of the week is it?")
# print ("today is " + dayofweek)
#connection is when you add 2 strings together
#using a plus sign (+) 
# movies_this_week = input ("What movies are you watching this week")
# print ("I am watching " + movies_this_week + " this week")
# mood = input ("How are you feeling today?")
# print ("I am feeling " + mood )

#data types for variables in python 
#strings- text
#integers- whole numbers
#floats- decimal numbrs
#booleans- ture or false
# lists- a collection of items 

# name= "john" #this is a string 
# #whenever it is wrapped in quotation makes it is a string

# year= "2024" 
# #integers - whole numbers 
# year= 2024 
# #integer data type should NOT be wrapped in quotes
# yearfourfromnow = 2028 
# subtract = yearfourfromnow - year 
# print(subtract)

# pricebigmac= 3.99 #this is a float data type
# pricedoublepounder= 4.99
# totalprice= pricebigmac + pricedoublepounder
# print(totalprice)
# #needs to have a decimal point
# # booleans -true or false
# israining = False #this is a boolean data type 
# print (israining)

# #lists- a collection of items 
# groceries = ["apples", "bananas", "carots" ]
# print (groceries)


#challange 1
#you and your family are gpoing to a movie and dinner.
#you need a list of movies to choose from and the place of the restarunt
#time time of the movie ]
#the time of dinner
#the name of the movei 
#the price of the dinner
# the number of people going 
#print out the enttire output in one sentence 
#check to see if the movie is playing at that time

movies = ["beetlejuics beetlejuice", "deadpool and wolveriene", "Afraid",  ]
dinner= "Apple Bees" 
dinnertime= "8 pm"
movietime= "6 pm"
dinnerprice= "26.99"
movieprice= "20"
numberoffamily= "3"
isevning = True 
moviename= "Afraid"
peoplegoing= int(input("How Many people are going?"))
#type conversion concerting one data type to another 
print("we are going to see " + moviename + "at" + movietime + "and then eat dinner at" +dinner+ "at "+ dinnertime + " with " + peoplegoing + "people") 