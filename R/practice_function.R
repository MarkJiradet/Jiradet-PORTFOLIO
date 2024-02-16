# add_two_nums() function
add_two_nums = function(val1,val2){
  return(val1 + val2)
}
add_two_nums(10,25)

# cube() function
cube = function(base,power=3){
  return(base ** power)
}
cube(5)
cube(5,4) #overide ค่า power
cube(power=4 ,base=5) #สลับที่parameterได้

# count_ball() function
balls = c("red","green","blue","yellow",
               "red","pink","green","blue")
               
count_ball = function(balls,color){
  sum(balls == color)
}

count_ball(balls,"green")