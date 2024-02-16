library(dplyr)
library(readxl)

#read excel file
econ = read_excel("students.xlsx",sheet=1)
business = read_excel("students.xlsx",sheet=2)
data = read_excel("students.xlsx",sheet=3)

#bind_rows == SQL UNION ALL
bind_rows(econ,business,data)

#if most sheets
list_df = list(econ,business,data)
bind_rows(list_df)