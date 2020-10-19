
def get_all_information():
    keys_dict = {}
    with open('steam.csv', encoding='utf-8') as f:
        keys_list = list(f.readline().split(','))
        for tag in keys_list:
            keys_dict[tag] = set()
        for line_read in f:
            line_read = list(line_read.split(','))
            game_dict = dict(zip(keys_list, line_read))
            for key in keys_list:
                keys_dict[key].add(game_dict[key])
    return keys_dict


def find_max_price():
    max_price = 0
    price = 0
    with open('steam.csv', encoding='utf-8') as f:
        for line_read in f:
            if 'appid' in line_read:
                continue
            line_read = list(line_read.split(','))
            price = float(str(line_read[-1]).replace('\n', ''))
            if price > max_price:
                max_price = price
    return max_price


def check_platform():
    if any(platform in line[6].split(';') for platform in user_platforms) or user_platforms == ['']:
        return 1
    else:
        return 0


def check_category():
    if any(category in line[8].split(';') for category in user_categories) or user_categories == ['']:
        return 1
    else:
        return 0


def check_genre():
    if any(genre in line[9].split(';') for genre in user_genres) or user_genres == ['']:
        return 1
    else:
        return 0


def check_raiting():
    if line[12].isdigit() and line[13].isdigit():
        if ((user_rating > 0) and int(line[12]) > int(line[13])) or user_rating == 0:
            return 1
        else:
            return 0
    else:
        return 0


def check_price():
    if user_price[0] <= float(line[17]) <= user_price[1]:
        return 1
    else:
        return 0


def game_check():
    check = check_category() + check_raiting() + check_platform() + check_price() + check_genre()
    if check == 5:
        result = f'{line[1]} Цена:{line[17]}  Жанр:{line[9]}\n'
        return result
    else:
        return 0


instruction = '''Вводите несколько ответов через запятую\nЕсли это параметр не имеет значения, нажмите Enter\n'''
print(instruction)

user_platforms = input('На какую платформу искать игры (windows/mac/linux)\n').split(',')

try:
    user_age = int(input('Сколько вам лет?\n'))
except ValueError:
    user_age = int(input('Введите числовое значение'))

user_categories = input('Какаие категории игр вам интересны?\n').split(',')
user_genres = input('Какой жанр предпочитаете?\n').split(',')

user_rating = input('Важны ли вам оценки рользователей?\n если да, то поставьте +  ')
if user_rating == '+':
    user_rating = 1
else:
    user_rating = 0

user_price = [input('Co скольки долларов начинается стоимость игры?'), input('Максимальная стоимость игры')]
if user_price[0].isdigit():
    user_price[0] = int(user_price[0])
else:
    user_price[0] = 0
if user_price[1].isdigit():
    user_price[1] = int(user_price[1])
else:
    user_price[1] = find_max_price()


with open('steam.csv', encoding='utf-8') as f, open('result.txt', 'w', encoding='utf-8') as result_file:
    result_file.write('Вам подойдут слудующие игры:\n')
    keys = list(f.readline().split(','))
    for line in f:
        line = list(line.split(','))
        game_dict = dict(zip(keys, line))
        if line[7].isdigit():
            if user_age >= int(line[7]):
                if game_check() != 0:
                    result_file.write(game_check())








