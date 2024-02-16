# for loop
friends = c("Toy","John","Mary","Anna")
nums = c(5,10,12,20,25)

for (friend in friends){
  print(paste("Hi!",friend))
}

for (i in seq(1,length(nums))){
  nums[i] = nums[i] + 2
}

#vectorization

paste("Hi!",friends)

(nums = nums + 2)

# while loop
count = 0

while(count < 5){
  print("Hi")
  count = count + 1
}