**Призначення та коротка характеристика програми** 

Ця програма призначена для підрахунку денної норми калорій, води і додавання певних продуктів для підрахунку вжитку.

Вхідні та вихідні дані програми 
Вхідні дані: 
Користувач вводить своє ім’я, стать, зріст, вагу, рівень щоденної активності. Користувач вводить назву страви чи продукту, користувач обирає із запропонованих варіантів та вводить кількість грамів.
Вихідні дані:
Користувач отримує інформацію про денну норму калорій та води,
Користувач отримує інформацію про кількість калорій, білків, жирів, вуглеводів що містяться в обраній страві/продукті на введену кількість грамів. 

**-Структура програми з коротким описом модулів, функцій,  класів та методів.:** 
Пакет calorie_tracker

 Модуль user.py -- В цьому модулі знаходиться клас User, що представляє користувача програми.
Атрибути класу:  name - ім’я , gender - стать, weight - вага  , height - зріст,  age - вік, physical -рівень щоденної активності.
Методи класу: __ str__ -  повертає інформацію про норму калорій і води; get_Calories - визначає норму калорій, get_Water() - визначає норму води;.

Модуль data_from_user.py :
Цей модуль охоплює функції, що відповідають за вхідні дані від користувача, перевірку правильності та обробку винятків.
get_gender() - повертає стать
get_physical_activity() - повертає рівень активності
get_weight() - повертає вагу
get_height() - повертає зріст
get_age() - повертає вік
get_name() - повертає ім’я
get_grams() - повертає грами
Всі функції, окрім get_name() повертають False, якщо дані введено невірно. 

Модуль workwithjson.py
Цей модуль об’єднує функції, що відповідають за виклик API, обробку json файлу, що був отриманим в результаті виклику.

api_call(product) - виклик API(пошук продукту), запис отриманих даних в файл.

check_existing(file) - повертає True, якщо продукт було знайдено, інакше - False

get_product_names(json_f) - повертає назви продуктів/страв, що були знайдено, внаслідок виклику.

search_by_name(name_food) - повертає частину josn файлу, що містить інформацію про nutrition продукту/страви.

nutrition_product(lst_nutr) - повертає кількість білків, жирів, вуглеводів, калорій продукту/страви на 100 грам.

count_nutrition(grams, product_dict) - підраховує кількість білків, жирів, вуглеводів на введену кількість грамів.

product_search_count() - функція, в якій задіяні всі попередні для пошуку продукту, вибору з запропонованих, введення грамів, підрахунку.

data_for_user(file) - читає файл, в який раніше було записано доданий продукт/страву, інформацію про кількість вжитих білків, жирів, вуглеводів, калорій.


Модуль ADT.py

Цей модуль містить абстрактний клас DynamicArray.
Цей масив зручно використовувати, адже можна динамічно змінювати розмір. Методи: __len__ - повертає довжину масиву, add - додає елемент в кінець масиву, _сhangesize - змінює розмір, delete_item -видаляє елемент, __str__ - виводить інформацію про елементи масиву.

Модуль PROGRAM_EXECUTING.py
В цьому модулі відбувається зчитування даних від користувача і обробка інформації, проведення обчислень. Це головний модуль проекту

**Коротка інструкція по користуванню програмою** 

Ввести свої дані: ім’я,  стать, зріст, вагу, рівень щоденної активності.
Отримати інформацію про норму калорій, води.
Вибрати команду add, щоб додати продукт/страву. Отримати отримані результати пошуку. Обрати продукт/страву з запропонованих. Ввести кількість грамів. Отримати інформацію про кількість білків, жирів, вуглеводів, калорій в введеній кількості продукту/страви.
Команда norma, щоб дізнатись норму калорій. 
Команда stop - завершення роботи і виведення результатів
**Опи тестових прикладів для первірки працездатності  програми.** 
````
WELCOME TO CALORIE TRACK PROGRAM!
Enter your name: Anna
Woman or Man: woman
Choose your activity level: minimum, weak, medium, high, extra-high: high
Enter your age: 46
Enter your height in cm: 180
Enter your weight: 70
 Anna you should consume 2474 calories, 2100 ml of water
>>> add
Enter product: orange
The products found: 

All Natural 100% Orange Juice
Biscotti, Orange
All Natural &amp; Vegetarian Couscous Salad With Orange Dressing
Duerr&#039;s Marmelade Morceaux Fins Orange
Marmelade classique a l&#039;orange
Emojeez, Fruit Flavored Gummies, Green Apple, Orange, Fruit Punch, Lemon, Cherry Blue Raspberry
Confiture de bleuet sauvages  l&#039;orange
Bill Knapp&#039;s, Iced Toaster Bread, Cranberry-Orange
Excel Intense Orange Chocolate
Mummy Mints, Orange


Enter which product to add: Excel Intense Orange Chocolate
Enter grams: 78
Current track : carbohydrates: 49 , fat: 29, protein: 9, calories: 2075
RESULTS: 2075/2474
>>> norma
 Anna you should consume 2474 calories, 2100 ml of water
>>> stop
		 carbohydrates, protein, fat, calories
Excel Intense Orange Chocolate [39, 5, 25, 1707]