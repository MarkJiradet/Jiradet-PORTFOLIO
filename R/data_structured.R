# Data Structures
# 1.Vector 2.Matrix 3.List 4.DataFrame

#---------------------------------
# Vector
1:10
16:25

# sequence generation
seq(from = 1,to = 100, by = 5)
seq(1,100,5)
seq(1,20)
# seq(1,100,5) เหมือน range() ใน Python

# function c เก็บได้แค่ 1 ประเภทเท่านั้น
friends = c("David","Marry","Anna",
            "John","William")
age = c(30,31,25,29,32)
is_male = c(TRUE,FALSE,FALSE,TRUE,TRUE)

# help function
help("seq")

#-----------------------------------
# Matrix
x = 1:25
length(x)
dim(x) = c(5,5)  #dim = dimension row , column

m1 = matrix(1:25, ncol=5)
m2 = matrix(1:6, ncol=3, nrow=2, byrow=TRUE)

# element wise computation
m2 + 100
m2 * 4

#------------------------------------
# List
my_name = "Mark"
my_friends = c("Wan","Toy","Zue")
m1 = matrix(1:25,ncol=5)
r_is_cool = TRUE

my_list = list(item1 = my_name,
               item2 = my_friends,
               item3 = m1,
               item4 = r_is_cool)

my_list$item2
my_list[2]

#---------------------------------------
# DataFrame

friends = c("Wan","Ink","Aan",
            "Bee","Top")

ages = c(26,27,32,31,28)

locations = c("New York","London",
              "London","Tokyo",
              "Manchester")

movie_lover = c(TRUE,TRUE,FALSE,
                TRUE,TRUE)

df = data.frame(friends,
           ages,
           locations,
           movie_lover)

View(df)

#create dataframe from list
my_list = list(friend = friends,
               age = ages,
               location = locations,
               movie = movie_lover)

df2 = data.frame(my_list)
View(df2)
