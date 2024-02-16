url = "https://docs.google.com/spreadsheets/d/1MDw_4hubrrURYOONORBpJgCQhfHEVZNuy_-nZfeJ3dE"

#use it first before read_sheet
gs4_deauth()

df = read_sheet(url,sheet="student")
View(df)