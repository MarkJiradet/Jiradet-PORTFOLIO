def main():
    welcome()
    gender = get_gender()
    height = get_height()
    weight = get_weight()
    age = get_age() 
    calculate_calorie(weight,height,age,gender)
    calculate_bmi(weight,height)
   
def welcome():
    print("================================================================================")
    print("========================= Welcome to health calculator =========================")
    print("================================================================================")
    
def get_gender():
    gender_list = ["Male","Female","male","female","M","F","m","f"]
    while True:
        try:
            sex = str(input("Please enter your gender (Male or Female): "))
            if sex not in gender_list:
                print("Invalid input! Please fill in male or female only.")
            else:
                print("================================================================================")
                return sex
        except:
            print("Invalid input! Please fill in male or female only.")
            
def get_weight():
    while True:
        try:
            weight = float(input("Please enter you weight(kg): "))
            if weight <= 0:
                print("Invalid input! You enter a weight value equal to 0 or less.")
            else:
                print("================================================================================")
                return weight
        except:
            print("Invalid input! Please enter only numbers.")
            
def get_height():
    while True:
        try:
            height = float(input("Please enter you height(cm): "))
            if height <= 0:
                print("Invalid input! You enter a height value equal to 0 or less.")
            else:
                print("================================================================================")
                return height
        except:
            print("Invalid input! Please enter only numbers.")
            
def get_age():
    while True:
        try:
            age = int(input("Please enter you age in years: "))
            if age <= 0:
                print("Invalid input! You enter a age value equal to 0 or less.")
            else:
                print("================================================================================")
                return age
        except:
            print("Invalid input! Please enter only integer numbers.")
            
def calculate_calorie(weight,height,age,gender):
    male = ["male", "M" , "m", "Male"]
    female = ["female", "F", "f", "Female"]
    bmr = 0
    if gender in male:
        bmr = 66+(13.7*weight)+(5*height)-(6.8*age)
    else:
        bmr = 665+(9.6*weight)+(1.8*height)-(4.7*age)
    
    tdee = 0
    print("============================== Exercise behavior ===============================")
    print("1.Didn't exercise at all.")
    print("2.Get some exercise or play a sport 1-3 days a week.")
    print("3.Get some exercise or play a sport 3-5 days a week.")
    print("4.Get some exercise or play a sport 6-7 days a week.")
    print("5.Exercising or playing sports every day, morning and evening\n")
    eb_list = [1,2,3,4,5]
    while True:
        try:
            eb = int(input("Please enter your exercise habits(1-5): "))
            if eb not in eb_list:
                print("Invalid input! Please enter only numbers 1 to 5.")
            else:
                break
        except:
            print("Invalid input! Please enter only numbers 1 to 5.")
    if eb == 1:
        tdee = bmr*1.2
    elif eb == 2:
        tdee = bmr*1.375
    elif eb == 3:
        tdee = bmr*1.55
    elif eb == 4:
        tdee = bmr*1.725
    elif eb == 5:
        tdee = bmr*1.9
    
    print("\n================================================================================")
    print("============================= Show your information ============================")
    print("================================================================================")
    print("BMR (Basal Metabolic Rate) is the basic energy needed to live :",int(bmr),"kilocalorie")
    print("TDEE (Total Daily Energy Expenditure) The energy you use each day :",int(tdee),"kilocalorie")
                
def calculate_bmi(weight,height):
    height = height/100
    bmi = weight/(height*height)
    print("Your Body Mass Index (BMI) = ",round(bmi,2))
    if bmi >= 40:
        print("Extreme obesity")
    elif bmi >= 35 and bmi < 40:
        print("Obesity grade 2 You are at risk for diseases that come with obesity.")
        print("If you have a waist circumference greater than the norm,")
        print("you are at high risk of developing the disease. You have to control your diet. and exercise vigorously.")
    elif bmi >= 28.5 and bmi < 35:
        print("Obesity grade 1 And if you have a waist circumference of more than 90 cm (men) 80 cm (women),")
        print("you will have a chance of high blood pressure, diabetes, need to control diet. and exercise.")
    elif bmi >= 23.5 and bmi < 28.5:
        print("Overweight If you have a genetic predisposition to diabetes or hyperlipidemia,")
        print("try to lose weight with a body mass index below 23.")
    elif bmi >= 18.5 and bmi < 23.5:
        print("Normal weight and fat content within the normal range I rarely have a bad disease.")
        print("Incidence of diabetes Lower blood pressure than those who are obese.")
    else:
        print("Underweight This may be caused by athletes who exercise a lot.")
        print("and not getting enough nutrients The solution is to eat quality food.")
        print("and has sufficient energy and exercise appropriately")
    print("================================================================================")
        
if __name__ == '__main__':
    main()