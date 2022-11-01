#functions printing and returning
#print something in a fuction, its only for displaying some data, you aren't doing anything with the data

#when you return in a function, you are going to use it to another part of your program

apples = int(input("How many apples?"))
oranges = int(input("How many oranges?"))


from addfruit import add_fruit
from subtractfruit import subtract_fruit
from dividefruit import divide_fruit
from displayfruit import display_fruit


# add fruit
fruitAdded = add_fruit(apples,oranges) 
print(fruitAdded) #whenever you you return items, you must put the returned value inside of a variable
#subtract fruit
subtractedFruits = subtract_fruit(apples,oranges)
print(subtractedFruits)
# divide fruit
dividedFruit = divide_fruit(apples,oranges)
print(dividedFruit)
# display the added fruit, subtracted fruit, and divided fruit
display_fruit(fruitAdded,subtractedFruits,dividedFruit)
