read_excel("students.xlsx",sheet=1)
read_excel("students.xlsx",sheet=2)
read_excel("students.xlsx",sheet=3)

read_excel("students.xlsx",sheet="Data")
read_excel("students.xlsx",sheet="Economics")
read_excel("students.xlsx",sheet="Business")

econ_student = read_excel("students.xlsx",sheet="Economics")
View(econ_student)

result = list()
for(i in 1:3){
  result[[i]] = read_excel("students.xlsx",sheet=i)
}

result