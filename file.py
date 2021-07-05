num1 = 42 #variable declaration
num2 = 2.3 #variable declaration
boolean = True #Primitive, Boolean
string = 'Hello World' #Primitive, String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # List
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # Dir
fruit = ('blueberry', 'strawberry', 'banana') #Tuple
print(type(fruit)) #Tuple, initialize
print(pizza_toppings[1]) #List, access value
pizza_toppings.append('Mushrooms') # List, add value
print(person['name']) # Dir, access value
person['name'] = 'George' # Dir, change value
person['eye_color'] = 'blue' # Dir, add value
print(fruit[2]) # Tuple, access value

if num1 > 45: # If, else
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5: #If, else if, else
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): # For loop
    print(x)
for x in range(2,5): # For loop
    print(x) # For loop
for x in range(2,10,3): # For loop
    print(x)
x = 0 # While loop start
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop() # List delete value
pizza_toppings.pop(1) # List delete value

print(person)
person.pop('eye_color') # Dir delete value
print(person)

for topping in pizza_toppings: # For loop
    if topping == 'Pepperoni': # If
        continue
    print('After 1st if statement')
    if topping == 'Olives':  # If
        break # End

def print_hello_ten_times(): #function
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x): #Function
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10): #Function
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)