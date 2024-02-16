#basic calculation
1+1
2-2
3*3
4/2
5%%2 #mod
5**2 #power
log(5) #log
exp(2) #expo
abs(-10) #absolute

## Basic knowledge programming
# 1.variable
# 2. data types
# 3. data structures
# 4. control flow
# 5. function

## Variable
# create variable
income = 28000
expense = 19500
saving = income - expense
saving

# remove variable
rm(saving)
rm(income)
rm(expense)

## Data Types
# numeric,character(text)
# date,logical(TRUE,FALSE)
my_age = 20
my_name = "Mark"
movie_lover = TRUE

# check class
class(my_age)
class(my_name)
class(movie_lover)

is.numeric(my_age) #TRUE
is.character(my_age) #FALSE
is.logical(movie_lover) #TRUE

# Convert to date
# YYYY-MM-DD
wantee = "2023-02-04"
wantee = as.Date(wantee)
class(wantee)

## Data Structures
# 1. vector
# 2. matrix
# 3. list
# 4. dataframe

# Vector
friends = c("Mark","Posh","Moshi","Best","Josh")
friends[1]  #Mark
friends[2]  #Posh
friends[3]  #Moshi
friends[4]  #Best
friends[5]  #Josh
friends[1:2] #Mark Posh
friends[3:5] #Moshi Best Josh
friends[c(1,3,5)] #Mark Moshi Josh

# change value
friends[2] = "ditto"
friends[2]
friends[1:2] = c("A","B")

which(friends == "Best") #4
friends[4] #Best

# Matrix
# matrix, vector 2 dimension
# R case sensitive
m = matrix(1:10) # 1 column
m = matrix(1:10,ncol=2) # 2 column
m = matrix(1:10,ncol=2,byrow=TRUE) #จะเรียงตามแถว
m2 = matrix(1:20,ncol=5)

m = matrix(c(5,10,2,4),ncol=2)
x = m*2
y = 1:100 * 2/3

m1 = matrix(c(5,10,2,4),ncol=2)
m2 = matrix(c(1,2,5,5),ncol=2)
m1*m2
m1 %*% m2

y = 1:6
dim(y) = c(3,2)

# List
# can collect multiple data types/objects
#key = value
my_playlist = list(
  fav_movie = "The Dark Knight",
  fav_song = "OMG",
  fav_artist = "NewJeans"
)
# ดึงข้อมูล
my_playlist$fav_movie #"The Dark Knight"
my_playlist$fav_song #"OMG"
my_playlist$fav_artist #"NewJeans"

my_playlist[1] #มันจะดึงชื่อตัวแปรและค่า
my_playlist[[1]] #มันจะดึงแค่ค่าของข้อมูล

mylist = list(
  movies = c("The Dark Knight","Marvel"),
  songs = c("OMG","Ditto","Attention"),
  artists = c("NewJeans"),
  year = 2000,
  movie_lover = TRUE,
  my_fav_matrix = matrix(1:100, ncol=50)
)

mylist$songs[2] # "Ditto"
mylist$movies[1] # "The Dark Knight"
mylist[[2]] # "OMG" "Ditto" "Attention"
mylist[[2]][3] # "Attention"

## customer database for our company
customer_01 = list(
  name = "Toy",
  location = "BKK",
  age = 34,
  movies = c("John Wick","Dark Knight")
)
customer_02 = list(
  name = "John",
  lname = "Wick",
  age = 42,
  movies = "John Wick 4",
  fav_weapon = "A pencil"
)

customer_db = list(
  toy = customer_01,
  john = customer_02
)

customer_db$toy$name
customer_db$toy$movies
customer_db$toy$movies[2]

customer_db$john$age = 45

#check key
names(customer_db)
names(customer_db$toy)

#dataframe
data()
mtcars #build-in df

#create a new dataframe
friends = c("Toy","Jisoo","Lisa","Rose","Jenny")
ages = c(34,25,27,26,28)
movie_lover = c(F,F,T,F,T)

df = data.frame(id = 1:5,
           friend = friends,
           age = ages,
           movie_love = movie_lover)
View(df)

#alterative approach to create dataframe in R
customers = list(
  friends = c("John","David","Anna"),
  ages = c(25,20,19),
  movie = c(T,T,F)
)

df2 = data.frame(customers)
View(df2)

customers = list(
  friends = c("John","David",NA),
  ages = c(25,20,19),
  movie = c(T,T,F)
)

## Function
add_two_numbers = function(v1,v2){
  return(v1+v2)
}
add_two_numbers(10,20) #30
add_two_numbers(30,40) #70

# short function
cube = function(x) x**3
cube(4)

my_power = function(base,pow) base**pow
my_power(base=5,pow=2) #25
my_power(pow=2,base=5) #25 สามารถสลับที่ได้

#default argument
mypow = function(base,pow=3) base**pow

greeting_bot = function(){
  username = readline("What is your name: ")
  print(paste("Hello!",username))
  
  your_age = readline("How old are you: ")
  your_age = as.numeric(your_age)
  print(paste("You are",your_age,"years old."))
}

## Control Flow
#if , for , while

# if, else if, else
score = 65
if(score >= 80){
  print("Passed")
}else if(score >= 50){
  print("Just OK")
}else{
  print("Failed")
}

# while

count = 0
while(count<5){
  print("Hello")
  count = count + 1
}

new_chatbot = function(){
  print("How to exit program , type 'exit'")
  while(TRUE){
    text = readline("What's your name: ")
    if(text=="exit"){
      break
    }else{
      print(paste("Hello!",text))
    }
  }
}

new_chatbot()

# for loop

friends = c("Mark","Jane","Tiger")

for (i in friends){
  print(paste("Hi",i))
}

# Vectorization
paste("Hi",friends)

## Regular Expression
state.name
grep("^K",state.name)
state.name[c(16,17)]

city_contain_new = grep("new",state.name,ignore.case = TRUE)
state.name[city_contain_new]