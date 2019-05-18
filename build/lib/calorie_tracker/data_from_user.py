def get_gender():
    """
    :return: False if gender is not correct, else: gender
    """
    gender = str(input('\033[1;23;1mWoman or Man: '))
    gender = gender.strip()
    if gender not in ['woman','Woman', 'WOMAN', 'MAN', 'man', 'Man']:
        return False

    elif gender in ['woman', 'Woman', 'WOMAN', 'MAN', 'man', 'Man']:
        return gender.lower()



def get_physical_activity():
    """

    :return: False if activity level is not correct, else: activity level
    """
    activity = str(input("\033[1;23;1mChoose your activity level: minimum, weak, medium, high, extra-high: "))
    activity = activity.lower().strip()
    if activity not in ['minimum', 'weak', 'medium', 'high', 'extra-high']:
        return False
    return activity


def get_weight():
    """
    :return: False if weight is not correct, else: weight
    """
    try:
        weight = int(input("\033[1;23;1mEnter your weight: "))
    except ValueError:
        return False
    return weight

def get_height():
    """

    :return: False if height is not correct, else: height
    """
    try:
        height = int(input("\033[1;23;1mEnter your height in cm: "))
    except ValueError:
        return False
    return height


def get_age():
    """

    :return: False if age is not correct, else: age
    """

    try:
        age = int(input("\033[1;23;1mEnter your age: "))
    except ValueError:
        return False
    return age

def get_name():
    """

    :return: name
    """
    name = str(input(("\033[1;23;1mEnter your name: ")))
    return name.strip()

def get_grams():
    """

    :return: False if grams is not correct, else: grams
    """
    try:
        grams = int(input("\033[1;23;1mEnter grams: "))
    except ValueError:
        print("\033[1;32;1m enter grams correctly!")
        return False
    return grams

