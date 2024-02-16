#convert data types

# main functions

x = 100
class(x)

# as.character()
char_x = as.character(x)
class(char_x)

# as.numeric()
num_x = as.numeric(char_x)
class(num_x)

# as.logical() :TRUE / FALSE
as.logical(0)
as.logical(1)
as.numeric(TRUE)
as.numeric(FALSE)