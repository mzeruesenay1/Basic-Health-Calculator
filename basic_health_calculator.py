#program that calculates BMI, body fat percentage, daily caloric needs
def calc_bmi(height, weight):
    bmi = weight/(height**2) * 703
    bmi = round(bmi, 1)

    if bmi < 18.5:
        print("BMI: " + str(bmi) + ", Category: Underweight")

    elif 18.5 <= bmi < 25:
        print("BMI: " + str(bmi) + ", Category: Normal Weight")

    elif 25 <= bmi < 30:
        print("BMI: " + str(bmi) + ", Category: Overweight")
       
    else:
        print("BMI: " + str(bmi) + ", Category: Obese")


def calc_body_fat(sex, height, weight, age):
    if sex == "M":
        bmi = weight/(height**2) * 703
        body_fat = str((1.2 * bmi) + (0.23 * age) - 16.2)
        print(body_fat + "%")
    
    elif sex == "F":
        bmi = weight/(height**2) * 703
        body_fat = str((1.2 * bmi) + (0.23 * age) - 5.4)
        print(body_fat + "%")


def calc_cal_intake(sex, activity, weight, height, age):
    if activity == 1:
        activity_factor = 1.2

    elif activity == 2:
        activity_factor = 1.375

    elif activity == 3:
        activity_factor = 1.55

    elif activity == 4:
        activity_factor = 1.725
    
    elif activity == 5:
        activity_factor = 1.9
    
    else:
        print("Invalid Option")
        return

    if sex == "M":
        calorie = (66 + (6.23 * weight) + (12.7 * height) - (6.8 * age)) * activity_factor
        print(int(calorie))

    elif sex == "F":
        calorie = (655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)) * activity_factor
        print(int(calorie) + "calories")

    else:
        print("Invalid Entry")


while True: 

    print("Choose a calculation:")
    print("A) BMI")
    print("B) Body Fat Percentage")
    print("C) Daily Caloric Intake")

    choice = input("Enter a choice (A,B,C): ")

    if choice == "A":
        height = float(input("Enter height(in): "))
        weight = float(input("Enter weight(lbs): "))
        calc_bmi(height, weight)
    

    elif choice == "B":
        sex = str(input("Enter sex (M/F): "))
        age = int(input("Enter age: "))
        height = float(input("Enter height(in): "))
        weight = float(input("Enter weight(lbs): "))
        calc_body_fat(sex, height, weight, age)
    
    elif choice == "C":
        sex = input("Enter sex (M/F): ")
        age = int(input("Enter age: "))
        height = float(input("Enter height(in): "))
        weight = float(input("Enter weight(lbs): "))
        print("1. Sedentary (little/no exercise)")
        print("2. Lightly Active (1-3 days/week)")
        print("3. Moderately Active (3-5 days/week)")
        print("4. Very Active (6-7 days/week)")
        print("5. Super Active (athlete, physical job)")
        activity = int(input("Enter activity level: "))
        calc_cal_intake(sex, activity, weight, height, age)


    else:
        print("Please enter A, B, or C")

    again = input("Would you like to perform another calculation? (Y/N): ")
    if again == "N":
        print("Goodbye!")
        break