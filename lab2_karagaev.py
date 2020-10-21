
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
    if any(platform in game_dict['platforms'].split(';') for platform in user_platforms) or user_platforms == ['']:
        return True
    else:
        return False


def check_category():
    if any(category in game_dict['categories'].split(';') for category in user_categories) or user_categories == ['']:
        return True
    else:
        return False


def check_genre():
    if any(genre in game_dict['genres'].split(';') for genre in user_genres) or user_genres == ['']:
        return True
    else:
        return False


def check_raiting():
    if game_dict['positive_ratings'].isdigit() and game_dict['negative_ratings'].isdigit():
        if ((user_rating > 0) and int(game_dict['positive_ratings']) > int(game_dict['negative_ratings'])) or user_rating == 0:
            return True
        else:
            return False
    else:
        return False


def check_price():
    if user_price_low <= float(game_dict['price\n']) <= user_price_max:
        return True
    else:
        return False


def game_check():
    check = check_category() and check_raiting() and check_platform() and check_price() and check_genre()
    if check:
        result = '{} Цена:{}  Жанр:{}\n'.format(game_dict['name'], game_dict['price\n'], game_dict['genres'])
        return result
    else:
        return False


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

user_price_low = input('Co скольки долларов начинается стоимость игры?')
user_price_max = input('Максимальная стоимость игры')
if user_price_low.isdigit():
    user_price_low = int(user_price_low)
else:
    user_price_low = 0
if user_price_max.isdigit():
    user_price_max = int(user_price_max)
else:
    user_price_max = find_max_price()


with open('steam.csv', encoding='utf-8') as f, open('result.txt', 'w', encoding='utf-8') as result_file:
    result_file.write('Вам подойдут слудующие игры:\n')
    keys = list(f.readline().split(','))
    for line in f:
        line = list(line.split(','))
        game_dict = dict(zip(keys, line))
        if game_dict['required_age'].isdigit():
            if user_age >= int(game_dict['required_age']):
                if game_check():
                    result_file.write(game_check())





