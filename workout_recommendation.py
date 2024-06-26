input_name = input("\nWhat is your name? ")
print(f"""\nHello {input_name.title()}! This is a gym recommendation
program designed to help you figure out what
exercises to do based on your desired group of muscles
you want to train. Lets begin shall we!""")

print(f"""\nWhat would you like to train today, please select from the
following options: \n- Chest\n- Back\n- Shoulders\n- Biceps\n- Triceps\n- Legs""")
muscle_group_options = ["chest", "back", "shoulders", "biceps", "triceps", "legs"]


def choose_muscle_group(choosen_muscle):
    choosen_muscle.lower()
    while choosen_muscle not in muscle_group_options:
        print("Option Invalid! Please ensure the spelling is correct and try again: ")
        choosen_muscle = input().lower()
    return choosen_muscle

input_muscle_option1 = choose_muscle_group(input())
print(f"It seems like you want to train {input_muscle_option1}!\n")

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


exercises_list = []


def choose_exercises(muscle, exercise_limit):
    exercise_counter_func = 0
    exercise_list_func = []
    print(f"You may choose {exercise_limit} different exercises: (Select Y = Yes | Anything else = NO)...")

    while len(exercise_list_func) < exercise_limit:
        for i in exercises[muscle]:
            if i not in exercise_list_func and exercise_counter_func < exercise_limit:
                choice = input(f"Would you like to add {i}?\n")
                if choice.lower() == "y":
                    exercise_list_func.append(i)
                    exercise_counter_func += 1
                    print(f"{i} has been added and you currently have {str(exercise_counter_func + len(exercises_list))} exercise in your regime.")
        if exercise_counter_func < exercise_limit:
            print(f"You still need to choose {exercise_limit - len(exercise_list_func)} more exercises...")
    for i in exercise_list_func:
        exercises_list.append(i)
    
def train_two_muscle_groups():
    global input_muscle_option2
    choose_exercises(input_muscle_option1, 3)
    input_muscle_option2 = choose_muscle_group(input("Please select the second group of muscles you want to train: "))
    while input_muscle_option2 == input_muscle_option1 or input_muscle_option2 == "legs":
        if input_muscle_option2 == input_muscle_option1:
             print(f"You have already selected {input_muscle_option2} as your first muscle group.")
        else:
            print(f"You cannot choose {input_muscle_option2} as a second muscle group due to the number of exercises it requires for an effecient workout.\nIt is best to dedicate a day to train them by itself!")
        input_muscle_option2 = choose_muscle_group(input(f"Please pick another muscle group to train: "))
    choose_exercises(input_muscle_option2, 3)
    return input_muscle_option2

if input_muscle_option1 != "legs":
    train_two_muscle_groups()
    print(f"\nHere is your exercise plan for today:\nFor {input_muscle_option1.title()}: {exercises_list[0]}, {exercises_list[1]}, {exercises_list[2]}\nFor {input_muscle_option2.title()}: {exercises_list[3]}, {exercises_list[4]}, {exercises_list[5]}\n")
else:
    choose_exercises(input_muscle_option1, 6)
    print(f"\nHere is your exercise plan for today:\nFor {input_muscle_option1.title()}: {exercises_list[0]}, {exercises_list[1]}, {exercises_list[2]}, {exercises_list[3]}, {exercises_list[4]}, {exercises_list[5]}\n")