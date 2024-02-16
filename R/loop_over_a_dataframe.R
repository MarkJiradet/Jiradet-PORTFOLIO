# loop over a dataframe
data()
USArrests
class(USArrests)
View(USArrests)

# check row and column
nrow(USArrests)
ncol(USArrests)
head(USArrests)

#เขียนหาค่าเฉลี่ยแบบนี้เสียเวลา
mean(USArrests$Murder)
mean(USArrests$Assault)
mean(USArrests$UrbanPop)
mean(USArrests$Rape)

#เขียนได้แบบสั้นๆโดยการวนลูป
for(i in 1:ncol(USArrests)){
  print(names(USArrests[i]))
  print(mean(USArrests[[i]]))
}

names(USArrests)

# refactor our code for more readability
cal_mean_by_col = function(df) {
  col_names = names(df)
  
  for (i in 1:ncol(df)) {
    avg_col = mean(df[[i]]) 
    print(paste(col_names[i], ":", avg_col))
  }
}

# test our code with mtcars
cal_mean_by_col(mtcars)

USArrests$Murder
USArrests[["Murder"]]
USArrests[[4]]