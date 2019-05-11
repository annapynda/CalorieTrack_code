class User:
    """
    class representing user
    """
    def __init__(self, name, gender, weight, height, age, physical):
        """
        :param name: name of user
        :param gender: gender of user
        :param weight: weight of user
        :param height: height of user
        :param age: age of user
        :param physical: level of physical activity of user
        """
        self.name = name
        self.gender = gender
        self.weight = weight
        self.height = height
        self.age = age
        self.physical = physical
        if self.physical == 'minimum':
            self.physical = 1.2

        elif self.physical == 'weak':
            self.physical = 1.375

        elif self.physical == 'medium':
            self.physical = 1.55

        elif self.physical == 'high':
            self.physical = 1.725

        elif self.physical == 'extra-high':
            self.physical = 1.9


    def get_Calories(self):
        """
        :return: the calorie norma of user
        """
        if self.gender == 'man':
            calories = (10 * self.weight + 6.25 * self.height - 5 * self.age + 5) * self.physical
        elif self.gender == 'woman':
            calories = (10 * self.weight + 6.25 * self.height - 5 * self.age - 161) * self.physical
        calories = round(calories)
        return calories

    def get_Water(self):
        """
        :return: norma of water of user
        """
        water = self.weight * 30
        return water

    def __str__(self):
        """
        :return: the information about calories and water
        """
        return '\033[1;34;1m {} you should consume {} calories, {} ml of water'.format(self.name, self.get_Calories(), self.get_Water())


u1 = User('Marie', 'woman', 56, 177, 26, 'medium')
a = u1.get_Water()
print(a)
