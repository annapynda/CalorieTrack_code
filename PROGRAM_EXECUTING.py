from data_from_user import get_physical_activity, get_gender, get_age, get_height, get_weight, get_name
from user import User
from workwithjson import product_search_count

print("\033[1;32;1m WELCOME TO CALORIE TRACK PROGRAM!")

name = get_name()
gender = get_gender()
if not gender:
    print('\033[1;32;1m enter gender correctly')
    while not gender:
        gender = get_gender()

activity = get_physical_activity()
if not activity:
    print('\033[1;32;1m enter activity correctly')
    while not activity:
        activity = get_physical_activity()

age = get_age()
if not age:
    print('\033[1;32;1m enter age correctly')
    while not age:
        age = get_age()

height = get_height()
if not height:
    print('\033[1;32;1m enter height correctly')
    while not height:
        height = get_height()

weight = get_weight()
if not weight:
    print('\033[1;32;1m enter weight correctly')
    while not weight:
        weight = get_weight()

user = User(name, gender, weight, height, age, activity)

print(user)

global COUNTER_fat, COUNTER_protein, COUNTER_carbs, COUNTER_ccal
COUNTER_ccal = 0
COUNTER_carbs = 0
COUNTER_fat = 0
COUNTER_protein = 0

executing = True
while True:
    command = input(">>> ")
    command.strip().lower()
    if command == 'add':
        lst = []
        lst_2 = []
        result = product_search_count()
        for i in range(len(result)):
            lst.append(result[i])
        COUNTER_ccal += lst[-1]
        COUNTER_carbs += lst[0]
        COUNTER_fat += lst[2]
        COUNTER_protein += lst[1]
        print('\033[1;32;1mCurrent track : carbohydrates: ' + str(COUNTER_carbs) , ', fat: ' + str(COUNTER_fat)  + ', protein: ' + str(COUNTER_protein) + ', calories: ' + str(COUNTER_ccal))
        norma = user.get_Calories()
        print('\033[1;34;1m' + 'RESULTS: '+ str(COUNTER_ccal) + '/' + str(norma))
        with open('file_user.txt', 'r') as f:
            f = f.read()
            f = f.split('\n')
            for i in f:
                lst_2.append(i)






    elif command == 'norma':
        print(user)

    elif command == 'stop':
        for i in lst_2:
            print('**Product\tnutrition information(carbohydrates, fat, protein, calories)**')
            print(i)
        executing = False






