#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Make a calculator using Python with addition , subtraction ,multiplication ,division and power.
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
        else:
        print("Invalid Input")


# In[8]:


#Write a program to check if there is any numeric value in list using for loop.
numbers = ["Usman",9,0,8,7]
for i in numbers:
    if type(i) == int:
        print("numeric value")
    else:
        print("no numeric value")


# In[1]:


a = {
    "name" : "usman",
    "resident of" : "karachi",
    "customer no" : 1678
}
a["age"] = 20
print(a)


# In[2]:


a = {
    "a" : 1,
    "b" : 2,
    "c" : 3
}
print(sum(a.values()))


# In[4]:


x = [1,2,3,1,3,2,4]
y = []
for i in x:
    if i not in y:
        y.append(i)
    else:
        print(i,"is duplicate")


# In[8]:





# In[16]:





# In[15]:


#
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)
is_key_present(1)


# In[ ]:




