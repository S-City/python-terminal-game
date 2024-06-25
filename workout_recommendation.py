input_name = input("\nWhat is your name? ")
print(f"""\nHello {input_name.title()}! This is a gym recommendation
program designed to help you figure out what
exercises to do based on your desired group of muscles
you want to train. Lets begin shall we!""")

print(f"""\nWhat would you like to train today, please select from the
following options: \n- Chest\n- Back\n- Shoulders\n- Biceps\n- Triceps\n- Legs""")
muscle_group_options = ["chest", "back", "shoulders", "biceps", "triceps", "legs"]
input_training1 = input().lower()

if input_training1 in muscle_group_options:
    print(f"It seems you want to train {input_training1}!")
else:
    while input_training1 not in muscle_group_options:
        print("Option Invalid! Please ensure the spelling is correct and try again: ")
        input_training1 = input().lower()
    print(f"It seems you want to train {input_training1}!")

print(f"Please choose from the following options the exercises you want to do!")

exercises = {"chest":["Barbell Flat Bench Press", "Seated Chest Press Machine", "Cable Pulley High Chest Fly", 
                      "Barbell Incline Bench Press", "Pec Fly Machine", "Dumbbell Bench Press"], 
             "back":["Barbell Bent Over Row", "Lat Pulldown Machine", "Cable Pull Low Row", "Rear Dealt Machine",
                     "Assisted Pull", "Diverging Lat Pulldown", "Alternating Seated Row", "Cable Face Pull"], 
             "shoulders":["Dumbell Seated Shoulder Press", "Cable Pull Side Lateral Raise", "Cable Pull Rear Lateral Raise",
                          "Barbell Shoulder Press", "Seated Shoulder Press", "Dumbell Lateral Raises"], 
             "triceps":["Cable Pulley Overhead Rope Tricep Extension", "Cable Pulley One Arm Tricep Pushdown", "Cable Pulley Triceps Pull Down", 
                        "Triceps Extension Machine", "1 Dumbbell Overhead Tricep Extension", "Dumbbell Lying Tricep Extension"], 
             "biceps":["Cable Pull Bicep Curl", "Dumbell Bicep Curl", "Arm Curl Machine", "Pullups"], 
             "legs":["Calf Raise", "Squat Machine", "Leg Press Machine", "Hip thrust machine", "Leg Extension", "Hip Abduction", "Barbell Hip Thrust"]} 

exercise_counter = 0
exercises_list = []

if input_training1 != "legs":
    print("You may choose three different exercises:")

    for i in exercises[input_training1]:
        if exercise_counter < 3:
            choice = input(f"Would you like to add {i} to your regime? (Y = Yes | Anything else = NO)...\n")
            if choice.lower() == "y":
                exercises_list.append(i)
                exercise_counter += 1
                print(f"{i} has been add and you currently have {str(exercise_counter)} exercise in your regime.")

else:
    print("You may choose six different exercises:")
    for i in exercises[input_training1]:
        if exercise_counter < 6:
            choice = input(f"Would you like to add {i} to your regime? (Y = Yes | Anything else = NO)...\n")
            if choice.lower() == "y":
                exercises_list.append(i)
                exercise_counter += 1
                print(f"{i} has been add and you currently have {str(exercise_counter)} exercise in your regime.")

def choose_exercises(input_training, exercise_limit):
        exercise_counter_func = 0
        exercise_list_func = []
        print(f"You may choose {exercise_limit} different exercises:")
        for i in exercises[input_training]:
            if exercise_counter < exercise_limit:
                choice = input(f"Would you like to add {i} to your regime? (Y = Yes | Anything else = NO)...\n")
                if choice.lower() == "y":
                    exercise_list_func.append(i)
                    exercise_counter_func += 1
                    print(f"{i} has been add and you currently have {str(exercise_counter)} exercise in your regime.")
