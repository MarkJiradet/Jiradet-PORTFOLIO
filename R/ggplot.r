#get working directory
getwd()

## ggplot2
## library tidyverse
library(tidyverse)

## First Plot
ggplot(data = mtcars, mapping = aes(x = hp, y = mpg)) +
  geom_point() +
  geom_smooth() +
  geom_rug()

ggplot(mtcars, aes(hp,mpg)) +
  geom_point(size = 3, col = "blue", alpha = 0.2)

ggplot(mtcars, aes(hp)) +
  geom_histogram(bins = 10, fill = "red", alpha = 0.7)

ggplot(mtcars, aes(hp)) +
  geom_boxplot()

p = ggplot(mtcars, aes(hp))
p + geom_histogram(bins = 10)
p + geom_density()
p + geom_boxplot()

## Box plot by groups
diamonds %>%
  count(cut)

ggplot(diamonds, aes(cut)) +
  geom_bar(fill = "#0366fc")

ggplot(diamonds, mapping = aes(cut,fill=cut)) +
  geom_bar()

ggplot(diamonds, mapping = aes(cut,fill=color)) +
  geom_bar()

ggplot(diamonds, mapping = aes(cut,fill=color)) +
  geom_bar(position = "dodge")

ggplot(diamonds, mapping = aes(cut,fill=color)) +
  geom_bar(position = "fill")

## SCATTER PLOT

#ถ้าอยากล็อคค่าที่สุ่มได้ไว้
set.seed(42)

small_diamonds = sample_n(diamonds, 5000)

ggplot(small_diamonds, aes(carat, price)) +
  geom_point()

#### FACET : SMALL MULTIPLES
ggplot(small_diamonds, aes(carat,price)) +
  geom_point() +
  geom_smooth(method = "lm", col="red") +
  facet_wrap(~color, ncol=2) +
  theme_minimal() +
  labs(title = "Relationship betweem carat and price by color",
       x = "Carat",
       y = "Price USD",
       caption = "Source: Diamonds from ggplot2 package")

#### Final Example
ggplot(small_diamonds, aes(carat,price, col=cut)) +
  geom_point(size = 3, alpha = 0.2) +
  facet_wrap(~color, ncol=2) +
  theme_minimal()