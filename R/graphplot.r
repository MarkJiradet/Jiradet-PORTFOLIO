#get working directory
getwd()

## library tidyverse
library(tidyverse)

## basic plots (base R)

hist(mtcars$mpg)

# Analyzing horse power
## Histogram - One Quantitative variable
hist(mtcars$hp)
mean(mtcars$hp)
median(mtcars$hp)

str(mtcars)

# การทำให้ตัวเลขกลายเป็น string เพื่อที่จะได้ทำ bar plot
mtcars$am = factor(mtcars$am,
                   levels = c(0,1),
                   labels = c("Auto","Manual"))

## Bar Plot - One Qualitative Variable
barplot(table(mtcars$am))

## Box Plot 
boxplot(mtcars$hp)
fivenum(mtcars$hp)

max(mtcars$hp)
min(mtcars$hp)
quantile(mtcars$hp,probs = c(.25,.5,.75))

## Whisker calculation
Q3 = quantile(mtcars$hp, probs = .75)
Q1 = quantile(mtcars$hp, probs = .25)
IQR_hp = Q3 - Q1

Q3 + 1.5*IQR_hp
Q1 - 1.5*IQR_hp

boxplot.stats(mtcars$hp, coef = 1.5)

## filter out outliers
mtcars_no_out = mtcars %>%
  filter(hp < 335)

boxplot(mtcars_no_out$hp)

## Boxplot 2 Variables
## Qualitative x Quantitative
data(mtcars)
mtcars$am = factor(mtcars$am,
                   levels = c(0,1),
                   labels = c("Auto","Manual"))
boxplot(mpg ~ am, data = mtcars,
        col = c("gold","salmon"))

## scatter plot
## 2 x Quantitative
plot(mtcars$hp, mtcars$mpg , pch = 16, 
     col="blue",
     main = "My first scatter plot",
     xlab = "Horse Power",
     ylab = "Mile Per Gallon")
cor(mtcasr$hp, mtcars$mpg)
lm(mpg ~ hp, data = mtcars)