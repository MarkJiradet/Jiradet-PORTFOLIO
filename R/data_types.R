# Data Types

# 1. numeric
age = 32
print(age)
class(age)

# 2. character
my_name = "Mark"
myname = 'Jiradet Nakham'
print(my_name)
print(myname)
class(my_name); class(myname)

# 3. logical
result = 1 + 1 == 2
print(result)
class(result)

# 4. factor
animals = c("Dog","Cat","Cat","Hippo")
class(animals)

animals = factor(animals)
class(animals)

# 5. date/time
time_now = Sys.time()
class(time_now)