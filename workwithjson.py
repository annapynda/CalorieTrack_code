import json
import http.client
from ADT import DynamicArray
from data_from_user import get_grams

def api_call(product):
    """
    Calls Api and loads data to the json file
    :param product: name of product that is searched
    """
    conn = http.client.HTTPSConnection("chompthis.com")
    A = "/api/product-search.php?token=2smoc9ANRJyKpzL1ZvY&name="
    C = A + product
    conn.request("GET", C)
    res = conn.getresponse()
    global data
    data = res.read()
    data = data.decode("utf-8")
    data = json.loads(data)
    with open("d.json", 'w') as f:
        json.dump(data, f)



def check_existing(file):
    """
    :param file: file with json dict
    :return: if product which is searched exsist: True, else: False
    """
    with open(file, 'r') as main_file:
        data = json.load(main_file)
        if data['chomp']['response']['products_found'] == 0:
            return False
        return True


def get_product_names(json_f):
    """
    :param json_f: the file with json dict
    :return: names of products found
    """
    D = DynamicArray()
    with open(json_f, 'r') as main_file:
        data = json.load(main_file)
    for i in data['products']:
        for el in data['products'][i]:
            if el == 'name':
                D.add(data['products'][i][el])
    return D


def search_by_name(name_food):
    """
    :param name_food: the name of chosen product
    :return: the nutrition information of the product
    """
    with open("d.json", 'r') as f:
        data = json.load(f)
    D = DynamicArray()
    for i in data['products']:
        for el in data['products'][i]:
            if el == 'name':
                if data['products'][i][el] == name_food:
                    D.add(data['products'][i])
    D2 = DynamicArray()
    for i in range(len(D)):
        for j in D[i]:
            if j == 'details':
                D2.add(D[i][j])
    nutr = DynamicArray()
    for i in range(len(D2)):
        for j in D2[i]:
            if j == 'nutrition_label':
                nutr.add(D2[i][j])
    return nutr

def nutrition_product(lst_nutr):
    """
    :param lst_nutr: the nutrition json dict
    :return: the information of carbohydrates, calories, fat, proteins
    """
    D = DynamicArray()
    dct_nutrition = dict()
    for i in range(len(lst_nutr)):
        for j in lst_nutr[i]:
            if j == 'carbohydrates':
                dct_nutrition[j] = lst_nutr[i][j]
            if j == 'calories':
                dct_nutrition[j] = lst_nutr[i][j]

            if j == 'fat':
                dct_nutrition[j] = lst_nutr[i][j]

            if j == 'proteins':
                dct_nutrition[j] = lst_nutr[i][j]


    for i in dct_nutrition:
        del dct_nutrition[i]['name']
        del dct_nutrition[i]['measurement']
        del dct_nutrition[i]['per_serving']
    D.add(dct_nutrition)
    return D




def check_if_one_result(file):
    """
    :param data: the json file
    :return: True if only one product was founded, else: False
    """
    with open(file, 'r') as main_file:
        data = json.load(main_file)
        if data['chomp']['response']['products_found'] == 1:
            return True
        return False





def count_nutrition(grams, product_dict):
    """
    :param grams: grams consumed
    :param product_dict: the json dict of the product
    :return: product name, number of: carbohydrates, fat, protein, calories
    """
    D = DynamicArray()
    lst = []
    # D.add(choose_which)
    # print(product_dict)
    grams_consumed = grams/100
    # print(grams_consumed)
    carbs = 0
    fat = 0
    protein = 0
    calories = 0
    try:
        if product_dict['carbohydrates']:
            carb_100g = product_dict['carbohydrates']['per_100g']
            carbs = carb_100g * grams_consumed
            carbs = round(carbs)
            # D.add(carbs)
            lst.append(carbs)
    except KeyError:
        # D.add(0)
        lst.append(0)

    try:
        if product_dict['proteins']:
            protein_100g = product_dict['proteins']['per_100g']
            protein = protein_100g * grams_consumed
            protein = round(protein)
            # D.add(protein)
            lst.append(protein)
    except KeyError:
        # D.add(0)
        lst.append(0)

    try:
        if product_dict['fat']:
            fat_100g = product_dict['fat']['per_100g']
            fat = fat_100g * grams_consumed
            fat = round(fat)
            # D.add(fat)
            lst.append(fat)
    except KeyError:
        # D.add(0)
        lst.append(0)

    try:
        if product_dict['calories']:
            calories_100g = product_dict['calories']['per_100g']
            calories = calories_100g * grams_consumed
            calories = round(calories)
            # D.add(calories)
            lst.append(calories)
    except KeyError:
        lst.append(0)


    return lst


def product_search_count():
    """

    :return: the counted nutriton of chosen product
    """

    product = str(input("Enter product: "))
    if len(product) < 5:
        product = str(input("Enter product: "))
    api_call(product)

    if check_existing('d.json') != False:
        print("\033[1;35;1mThe products found: ")
        print('\n')
        a = get_product_names('d.json')
        for i in range(len(a)):
            print(a[i])
        print('\n')
        choose_which = str(input("Enter which product to add or enter NO if nothing mathces: "))
        choose_which = choose_which.strip()
        if choose_which != 'NO':
            nutrition = search_by_name(choose_which)
            inf_product = nutrition_product(nutrition)
            grams = get_grams()
            while not grams:
                grams = get_grams()
            nutrition_pr = count_nutrition(grams, inf_product[0])
            with open('file_user.txt', 'a') as new_f:
                new_f.write(str(choose_which) + ' ' + str(nutrition_pr) + '\n')
    else:
        return "nothing found"
    return nutrition_pr



# def data_for_user(file):
#     with open(file, 'r') as new_file:
#         data = new_file.read()
#         data = data.strip('\n')
#     return data

