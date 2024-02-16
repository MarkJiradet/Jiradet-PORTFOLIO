# create our function

greeting = function(){
  print("Hello World!")
}

greeting_name = function(name){
  print(paste("Hello!",name))
}

# name , age => parameter
# "Toy" , 25 => argument
greeting_name = function(name = "Toy",age = 25){
  print(paste("Hello!",name))
  print(paste0("Age:",age))
}

func = function(){
  greeting()
  greeting_name("Mark")
}