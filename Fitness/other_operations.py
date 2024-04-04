def calculate_nutrition(client):
    # Unpack client data
    name = client.name
    age = client.age
    sex = client.sex.upper() == 'M'
    weight = client.weight
    height = client.height
    waist = client.waist
    hip = client.hip
    activity_index = client.activity_index
    goal = client.goal

    # Calculate BMI
    BMI = weight / ((0.01 * height) ** 2)
    
    # Calculate WHR
    WHR = waist / hip
    
    # Calculate BFP based on sex
    if sex:
        BFP = (1.2 * BMI) + (0.23 * age) - 16.2  # men
    else:
        BFP = (1.2 * BMI) + (0.23 * age) - 5.4  # women
    
    # Calculate BMR
    if sex:
        BMR = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        BMR = (10 * weight) + (6.25 * height) - (5 * age) - 161
    
    # Calculate TDEE
    TDEE = activity_index * BMR
    
    # Calculate daily calories based on goal
    if goal == 'lose':
        daily_calory = TDEE - 500
    elif goal == 'gain':
        daily_calory = TDEE + 500
    else:
        daily_calory = TDEE
    
    # Calculate macronutrients
    proteins = daily_calory * 0.2 / 4
    carbs = daily_calory * 0.5 / 4
    fat = daily_calory * 0.3 / 9
    
    # Print nutrition plan
    print()
    print()
    print(f"Daily Calory for {name},")
    print(f"Age: {age}, Weight: {weight}:")
    print("-----------------------------------------------------------")
    print("-----------------------------------------------------------")
    print("TDEE: ", TDEE)
    print("Daily Calories: ", daily_calory)
    print("-----------------------------------------------------------")
    print(f"Nutrition plan:")
    print("------------------------------------------------------------")
    print("Proteins = {:.2f} g".format(proteins))
    print("Carbs = {:.2f} g".format(carbs))
    print("Fat = {:.2f} g".format(fat))
    print("------------------------------------------------------------")
    print("Meal Plan:")
    print("------------------------------------------------------------")
    print("Meal\t\tProtein (g)\tCarbs (g)\tFat (g)")
    print("------------------------------------------------------------")
    print("Breakfast\t{:.2f}\t\t{:.2f}\t\t{:.2f}".format(proteins * 0.2, carbs * 0.2, fat * 0.2))
    print("Snack1\t\t{:.2f}\t\t{:.2f}\t\t{:.2f}".format(proteins * 0.05, carbs * 0.05, fat * 0.05))
    print("Lunch\t\t{:.2f}\t\t{:.2f}\t\t{:.2f}".format(proteins * 0.3, carbs * 0.3, fat * 0.3))
    print("Snack2\t\t{:.2f}\t\t{:.2f}\t\t{:.2f}".format(proteins * 0.1, carbs * 0.1, fat * 0.1))
    print("Dinner\t\t{:.2f}\t\t{:.2f}\t\t{:.2f}".format(proteins * 0.3, carbs * 0.3, fat * 0.3))
    print("Snack3\t\t{:.2f}\t\t{:.2f}\t\t{:.2f}".format(proteins * 0.05, carbs * 0.05, fat * 0.05))
    print("------------------------------------------------------------")
    print("-----------------------------------------------------------")
