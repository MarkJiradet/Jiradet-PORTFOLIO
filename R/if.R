# if
# =IF() in google sheets

score = 75

if(score >= 90){
  print("Passed")
}else if(score >= 50){
  print("Ok")
}else{
  print("Enroll again!")
}

# ifelse
ifelse(score >= 80,"Passed","Failed")

ifelse(score >= 90,"Passed",
       ifelse(score >= 50,"OK","Enroll Again!"))