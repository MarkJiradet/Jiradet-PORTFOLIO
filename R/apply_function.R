#apply function

#MARGIN = 2 , by column
apply(mtcars,MARGIN = 2,mean)

#MARGIN = 1 , by row
apply(mtcars,MARGIN = 1,mean)
avg_by_row_mtcars = apply(mtcars,MARGIN = 1,mean)

avg_by_row_mtcars[1:10]

#etc
apply(mtcars,MARGIN = 2,sum)
apply(mtcars,MARGIN = 2,sd)
apply(mtcars,MARGIN = 2,median)