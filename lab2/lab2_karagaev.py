
def get_all_information():
    # Вспомогательная функция, чтобы распределить всю информацию по категориям
    # Нужна , чтобы получить представление об информации в файле задания
    keys_dict = {}
    with open('steam.csv', encoding='utf-8') as f:
        keys = list(f.readline().split(','))
        for tag in keys:
            keys_dict[tag] = set()
        for line in f:
            line = list(line.split(','))
            game_dict = dict(zip(keys, line))
            for key in keys:
                keys_dict[key].add(game_dict[key])
    return keys_dict

def find_max_price():
    #Вспомогательная функция
    max_price = 0
    price = 0
    with open('steam.csv', encoding='utf-8') as f:
        for line in f:
            if 'appid'in line:
                continue
            line = list(line.split(','))
            price = float(str(line[-1]).replace('\n', ''))
            if price > max_price:
                max_price = price
    return max_price







print('Вводите несколько ответов через запятую\nЕсли это параметр не имеет значения, нажмите Enter\n')

user_platforms = input('На какую платформу искать игры (windows/mac/linux)\n').split(',')

try:
    user_age = int(input('Сколько вам лет?\n'))
except ValueError:
    user_age = int(input('Введите числовое значение'))

user_categories = input('Какаие категории игр вам интересны?\n').split(',')
user_genres = input('Какой жанр предпочитаете?\n').split(',')

rating = input('Важны ли вам оценки рользователей?\n если да, то поставьте +  ')
if rating == '+':
    rating = 1
else:
    rating = 0

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
                if (any(platform in line[6].split(';') for platform in user_platforms) or user_platforms == [''])\
                and (any(category in line[8].split(';') for category in user_categories) or user_categories == ['']) \
                and (any(genre in line[9].split(';') for genre in user_genres) or user_genres == ['']) \
                and (((rating > 0) and int(line[12]) > int(line[13])) or rating == 0 )\
                and (user_price[0] <= float(line[17]) <= user_price[1]):
                    result = f'{line[1]} Цена:{line[17]}  Жанр:{line[9]}\n'
                    result_file.write(result)







