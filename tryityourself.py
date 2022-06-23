#%%
# 3-1
names = ['isabella', 'sarah', 'stuart', 'tommy']
print(names[0])
print(names[1])
print(names[2])
print(names[-1])
message = f"Hello {names[0].title()}, hope you are having a great day today!"
message = f"Hello {names[1].title()}, hope ya'll enjoy your time here in Mississippi."
message = f"Hello {names[2].title()}, time to party tonight."
message = f"Hello {names[3].title()}, hope things are going well in TN."
print(message)
transportation = ['car', 'truck', 'motorcycle', 'h1 hummer']
message = f"One day I would like to own an {transportation[3].title()} to go off-roading with."
print(message)
# %%
# 3-4
names = ['Isabella', 'Andrew', 'Brandon', 'Evan']
message = f"Hello {names} I would like to invite you over for dinner tonight."
print(message)
#%%
print('Evan')
names.pop(3)
print(names)
names.append('Josh')
print(names)
message = f"Hello {names}, hoping you can still join me for dinner."
print(message)
#%%
    msg = """Dear Terry,,
    You must cut down the mightiest
    tree in the forest with...
    a herring!"""
# %%
name = input('What is your name?: ')
age = input('What is your age?: ')
print('Hello ' + name + '! You are ' + age + ' years old')
# %%
num1 = input('Enter a digit: ')
num2 = input('Enter a second number: ')
answer = float(num1) + float(num2)
print(answer)
# %%
first_name = input('Enter your first name: ')
distance_km = input('Enter distance in km: ')
distance_mi = float(distance_km)/1.609
print(f'Hello {name.title()}! {distance_km}km is equivalent to {round(distance_mi, 1)} miles.')
# %%
sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales_w2.insert(6, 16)
sales = sales_w1 + sales_w2
print('On the first week our best day was ' + float(sales_w1[2]) * float(1.5))
# %%
sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []
new_day = input('Enter #of lemonades for new day: ')
sales_w2.append(int(new_day))
#sales.extend(sales_w1)
#sales.extend(sales_w2)
sales = sales_w1 + sales_w2
#sales.sort()
worst_day_prof = min(sales) * 1.5 #The min(sales) will take the smallest number from the list
best_day_prof = max(sales) * 1.5 #The max(sales) will take the biggest number from the list
print(f'Worst day profit:$ {worst_day_prof}')
print(f'Best day profit:$ {best_day_prof}')
print(f'Combined profit:$ {worst_day_prof + best_day_prof}')
#%%
#Sets - blazingly fast unordered Lists 
friends = ['John','Michael','Terry','Eric','Graham']
friends_tuple = ('John','Michael','Terry','Eric','Graham')
friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']

print(friends_set.intersection(my_friends_set)) 
# intersection prints what is the same in both. Uses the & (friends & my_friends)
# difference prints what is different from each. Uses - minus sign (friends - my_friends)
# union will combine all the items with no duplicates. Also uses the | (friends | my_friends)
# symmetric_difference "Show only the names who only appear in one of the lists" (my_friends ^ friends)
cars_no_dupl = set(cars) #To turn back into a list do =list(set(cars))
print(cars_no_dupl)
# %%
# def or defined is used to start your function
def greeting():     #Always put a : at the end
    print("Hello Friend")   #Anything after or below must be indented to be included 
    
greeting()
# %%
def greeting(name):     #Name is an parameter that you want to pass. Similar to a variable
    print("Hello " + name + "!")
    
greeting("Brian")   #Brian is the argument that we pass through for name
# %%
def greeting(name, age=28):
    print("Hello " + name + ", you are " + str(age) + "!")
    print(f"Hello {name}, you are {age}!")
    
name = input("Enter your name: ")
age = input("Enter your age: ")
greeting(name, age)
greeting("Judith") #We didn't add her age here so the default is 28
# %%
def greeting(name, age=28, color="red"):
    #Greets user with 'name' from 'input box' and 'age', if available, default age is used
    #print('Hello '  + name.capitalize() + ', you will be ' + str(age + 1) +' on your next birthday!')
    print(f'Hello {name.capitalize()}, you will be {age + 1} on your next birthday!')
    print(f"We hear you like the color {color.lower()}")

name = input('Enter your name: ')
age = input('Enter your age: ')
color = input("Enter your favorite color: ")
greeting(name, int(age), color)
# 1. Add new print statement - on a new line
#    which says 'We hear you like the color xxx! xxx is a string with color 
# 2. extend the function with another  input parameter 'color', that defaults to 'red'
# 3. Capture the color via an input box as variable:color 
# 4. Change the 'You are xx!' text to say 'you will be xx+1 years old next birthday 
#  adding 1 to the age
# 5. Capitalize first letter of the 'name', and rest are small caps 
# 6. Favorite color should be in lowercase
# %%
#Return statements
def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    #return f"{amount}, {tax}, {total_amount}" #Returns a string
    #return amount, tax, total_amount #Returns a tuple
    #return [amount, tax, total_amount] #Returns a list. Can also print certain index so price[1] returns amount
    #return {amount, tax, total_amount} #Returns a set which is unordered so you can't do price[1]
    
price = value_added_tax(100)    
print(price, type(price))