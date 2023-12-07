"""
Задание №5.
    Доработаем задачи 3 и 4. Создайте класс проекта, который
имеет следующие методы:
    - загрузка данных (функция из задания 4)
    - вход в систему - требует указать имя и id пользователя. Для
проверки наличия пользователя в множестве используйте
магический метод проверки на равенство пользователей.
Если такого пользователя нет, вызывайте исключение
доступа. А если пользователь есть, получите его уровень из
множества пользователей.
    - добавление пользователя. Если уровень пользователя
меньше, чем ваш уровень, вызывайте исключение уровня
доступа.
"""
import json


class BasedExcept(Exception):
    pass


class NameErr(BasedExcept):
    pass


class LevelErr(BasedExcept):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'Ошибка уровня'


class User:
    def __init__(self, name: str, user_id: str, level: str = '0') -> None:
        self.name = name
        self.user_id = user_id
        self.level = level


class CheckUserLogin:
    users = []

    def create_user(self, name, user_id, level):
        try:
            if level > 3:
                raise LevelErr(level)
        except LevelErr as e:
            print(e)
        else:
            self.users.append(User(name, user_id, level))

    def load_users(self):
        with open('user_data.json', 'r', encoding='UTF-8') as js_f:
            user_dict = json.load(js_f)
            for level, user_list in user_dict.items():
                for user_id, name in user_list.items():
                    self.users.append(User(name, user_id, level))

    def get_login_level(self, name):
        try:
            for el in self.users:
                if name == el.name:
                    return 'Пользователь найден'
                raise NameErr()
        except NameErr:
            return 'Пользователь не найден'


if __name__ == '__main__':
    user1 = CheckUserLogin()
    user1.load_users()
    print(len(user1.users))
    user1.create_user('Ivanov', '08', 2)
    print(user1.get_login_level('Новиков'))
